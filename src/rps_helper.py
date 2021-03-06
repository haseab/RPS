import numpy as np
import random


class RPSHelper:

    @staticmethod
    def distribution():
        a, c, d, k = 0.370, 0.497, 805.0, 0.022
        x = np.linspace(0, 1000, 1001)
        y = a * np.arctan(k * (x - d)) + c
        y = np.array([i if i > 0 else 0 for i in y])
        rewards_probabilities = np.concatenate([y[:758], np.linspace(0.2002, 1, 1000 - 758)])
        punishment_probabilities = np.array(list(y[600:]) + [1] * 600)
        return np.round(rewards_probabilities, 3), punishment_probabilities

    @staticmethod
    def generate_efficiency_results(distribution):
        x = np.linspace(1, 1000, 1000)/10
        y = [1 if i > random.random() else 0 for i in distribution]
        return dict(zip(x, y))