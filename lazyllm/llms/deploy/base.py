import json
import time
import requests
from ..core import LLMBase
import lazyllm
from lazyllm import launchers, flows
import random


class LazyLLMDeployBase(LLMBase):

    def __init__(self, *, launcher=launchers.slurm()):
        super().__init__(launcher=launcher)


class DummyDeploy(LazyLLMDeployBase, flows.NamedPipeline):
    input_key_name = None
    default_headers = {'Content-Type': 'application/json'}
    message_format = None
    
    def __init__(self, launcher=launchers.slurm(sync=False), *, stream=False, **kw):
        super().__init__(launcher=launcher)
        def func():
            def impl(x):
                print(f'input is {x}')
                return f'reply for {x}'
            def impl_stream(x):
                for i in range(10):
                    yield f'reply-{i} for {x}'
                    time.sleep(0.2)
            return impl_stream if stream else impl
        flows.Pipeline.__init__(self, func,
            deploy.RelayServer(port=random.randint(30000, 40000), launcher=launcher))

    def __call__(self, *args):
        url = flows.NamedPipeline.__call__(self)
        print(f'dummy deploy url is : {url}')
        return url

    def __repr__(self):
        return flows.NamedPipeline.__repr__(self)


def verify_fastapi_func(job):
    while True:
        line = job.queue.get()
        if line.startswith('ERROR:'):
            print("Capture error message: ", line, "\n\n")
            return False
        elif 'Uvicorn running on' in line:
            print("Capture startup message:   ",line)
            break
        if job.status == lazyllm.launchers.status.Failed:
            print("Service Startup Failed.")
            return False
    return True
