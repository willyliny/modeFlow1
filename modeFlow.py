from taskflow import engines
from taskflow.patterns import linear_flow
import TaskPool
from FlowPool import IntergrationFlow

class Mode1Flow():
    def __init__(self, shadowModel):
        self.shadowModel = shadowModel
        self.mode1Flow = linear_flow.Flow(self.__class__.__name__)
        self.intergrationFlow = IntergrationFlow(self.__class__.__name__, 'frame').buildFlow()
       
    def buildFlow(self): 
        self.mode1Flow.add(
            TaskPool.frameTask(self.__class__.__name__ + '_frameTask',provides = 'frame'),
            TaskPool.yoloTask(self.__class__.__name__+'yoloTask', requires = 'frame', provides = 'frame'),
            TaskPool.wholeTask(self.__class__.__name__+'wholeTask', requires = 'frame', provides = 'frame'),
            self.intergrationFlow              
        )
        result = engines.load(self.mode1Flow, store={'shadowModel':self.shadowModel}, engine = "parallel")
        result.run()

def runFlow(shadowModel):
	Mode1Flow(shadowModel).buildFlow()
