import random
import numpy as np
from datetime import datetime, timedelta


class RewardSystem:

    def __init__(self):
        self.efficiency_range = np.linspace(0.80,0.95,100)
        self.level = ["Level 1", "Level 2", "Level 3"]
        self.rewards = {"Level 1": ["1 Pizza", "2 Burgers", "1 Osmows", "2 Chips"],
                        "Level 2" : ["2 Pizzas", "4 Burgers", "2 Osmows", "4 Chips"],
                        "Level 3" : ["3 Pizzas", "6 Burgers", "3 Osmows", "6 Chips"]}
        self.period = np.linspace(0.5, 2, 100)


    def samplepick(self, debug = False):
        start_date = str(datetime.now())[:10]
        pick_efficiency_range = round(random.choice(self.efficiency_range), 2)
        pick_level = random.choice(self.level)
        pick_period = int(random.choice(self.period)*7)
        end_date = str(datetime.now() + timedelta(pick_period))[:10]

        string = f"""
        Goal is to be {pick_efficiency_range*100}% productive
        If you do, you will get a {pick_level} Reward
        Effective from {start_date} to {end_date}
        """
        if debug == True:
            print(string)
        return [pick_efficiency_range, pick_level, pick_period, start_date, end_date]

