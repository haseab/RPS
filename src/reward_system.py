import random
import numpy as np
from datetime import datetime, timedelta
from rps_helper import RPSHelper

class RewardSystem:

    def __init__(self):
        self.probabilities = RPSHelper.distribution()[0]
        self.level = ["Level 1", "Level 2", "Level 3"]
        # Refactor -> db
        self.rewards = {"Level 1": ["1 Pizza", "2 Burgers", "1 Osmows", "2 Chips"],
                        "Level 2": ["2 Pizzas", "4 Burgers", "2 Osmows", "4 Chips"],
                        "Level 3": ["3 Pizzas", "6 Burgers", "3 Osmows", "6 Chips"]}
        self.period = np.linspace(0.5, 2, 100)

    def sample_pick(self, debug=False):
        start_date = str(datetime.now())[:10]

        pick_probabilities = RPSHelper.generate_efficiency_results(self.probabilities)
        pick_level = random.choice(self.level)
        pick_period = int(random.choice(self.period) * 7)

        end_date = str(datetime.now() + timedelta(pick_period-1))[:10]

        string = f"""
        If you win, you will get a {pick_level} Reward
        Effective from {start_date} to {end_date}
        """
        if debug:
            print(string)
        return [pick_probabilities, pick_level, pick_period, start_date, end_date]

    def __repr__(self):
        return "Reward System"
