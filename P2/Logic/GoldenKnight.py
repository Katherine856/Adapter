# Concret Builder
from P2.Logic.Knight import *
from P2.Logic.Actions import *


class GoldenKnight(Knight):

    '''
    Concrete Factory Golden Knight
    '''

    def iddle(self):
        super().iddle()
        i = GKFactory()
        return i.createIddleAction()

    def walk(self):
        super().walk()
        w = GKFactory()
        return w.createWalkAction()

    def jump(self):
        super().jump()
        j = GKFactory()
        return j.createJumpAction()
