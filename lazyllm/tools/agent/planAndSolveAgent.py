import re
from lazyllm.module import ModuleBase
from lazyllm.components import ChatPrompter
from lazyllm import loop, pipeline, _0, package, bind, LOG
from .functionCall import FunctionCallAgent
from typing import List, Union

PLANNER_PROMPT = (
    "Let's first understand the problem and devise a plan to solve the problem."
    " Please output the plan starting with the header 'Plan:' "
    "and then followed by a numbered list of steps. "
    "Please make the plan the minimum number of steps required "
    "to accurately complete the task. If the task is a question, "
    "the final step should almost always be 'Given the above steps taken, "
    "please respond to the users original question'. "
    "At the end of your plan, say '<END_OF_PLAN>'"
)

SOLVER_PROMPT = (
    "Objective: {objective}\n\n"
    "Previos steps: {previous_steps}\n\n"
    "Current objective: {current_step}"
)

class PlanAndSolveAgent(ModuleBase):
    def __init__(self, llm, tools: List[str], *, plan_llm: Union[ModuleBase, None] = None,
                 solve_llm: Union[ModuleBase, None] = None, max_retries: int = 5, return_trace: bool = False):
        super().__init__(return_trace=return_trace)
        self._max_retries = max_retries
        assert sum(x is not None for x in [llm, plan_llm, solve_llm]) <= 2, \
               "llm and plan_llm, solve_llm cannot be set at the same time."
        assert tools, "tools cannot be empty."
        if plan_llm is None and solve_llm is None and llm is not None:
            self._plan_llm = llm.share(prompt=ChatPrompter(instruction=PLANNER_PROMPT))
            self._solve_llm = llm.share()
        elif plan_llm is None and solve_llm is not None and llm is not None:
            self._plan_llm = llm.share(prompt=ChatPrompter(instruction=PLANNER_PROMPT))
            self._solve_llm = solve_llm.share()
        elif solve_llm is None and plan_llm is not None and llm is not None:
            self._plan_llm = plan_llm.share(prompt=ChatPrompter(instruction=PLANNER_PROMPT))
            self._solve_llm = llm.share()
        elif plan_llm is not None and solve_llm is not None and llm is None:
            self._plan_llm = plan_llm.share(prompt=ChatPrompter(instruction=PLANNER_PROMPT))
            self._solve_llm = solve_llm.share()
        else:
            raise ValueError("Either set llm, or set plan_llm and solve_llm, or set llm and one of [plan_llm, "
                             f"solve_llm]. Other situations are not supported. llm: {llm}, plan_llm: {plan_llm}, "
                             f"solve_llm: {solve_llm}")
        self._tools = tools
        with pipeline() as self._agent:
            self._agent.plan = self._plan_llm
            self._agent.parse = (lambda text, query: package([], '', [v for v in re.split("\n\\s*\\d+\\. ", text)[1:]],
                                 query)) | bind(query=self._agent.input)
            with loop(stop_condition=lambda pre, res, steps, query: len(steps) == 0) as self._agent.lp:
                self._agent.lp.pre_action = lambda pre_steps, response, steps, query: \
                    package(SOLVER_PROMPT.format(previous_steps="\n".join(pre_steps), current_step=steps[0],
                            objective=query) + "input: " + response + "\n" + steps[0], [])
                self._agent.lp.solve = FunctionCallAgent(self._solve_llm, tools=self._tools)
                self._agent.lp.post_action = self._post_action | bind(self._agent.lp.input[0][0], _0,
                                                                      self._agent.lp.input[0][2],
                                                                      self._agent.lp.input[0][3])

            self._agent.post_action = lambda pre, res, steps, query: res

    def _post_action(self, pre_steps: List[str], response: str, steps: List[str], query: str):
        LOG.info(f"current step: {steps[0]}, response: {response}")
        pre_steps.append(steps.pop(0))
        return package(pre_steps, response, steps, query)

    def forward(self, query: str):
        ans = self._agent(query)
        return ans