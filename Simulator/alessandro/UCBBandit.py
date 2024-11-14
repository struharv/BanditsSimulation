from random import random

import numpy as np

from engine.Simulator import Simulator
from engine.bandits.Orchestrator import Orchestrator

def simple_max(Q, N, t):
    return np.random.choice(np.flatnonzero(Q == Q.max())) # breaking ties randomly

class UCBBandit(Orchestrator):
    def __init__(self):
        print("UCBBandit.__init__")

    def init(self):
        self.An = []
        self.bn = []

    def tick(self, time_s: int):
        if time_s % 30 != 0:
            return

        context = []
        ()



        print("UCBBANDIT tick!", time_s)


