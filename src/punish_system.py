import random
import numpy as np
from datetime import datetime, timedelta
from rps_helper import RPSHelper


class PunishSystem:

    def __init__(self):
        self.probabilities = RPSHelper.distribution()[1]
        self.amount = {"Money Lost": ["$50", "$100", "$150"],
                       "No Access to Comp": ["8 hours", "16 hours", "24 hours"],
                       "Sleep on Floor": ["1 night", "2 nights"]
                       }
        self.type = list(self.amount.keys())
        self.period = np.linspace(0.5, 2, 100)

    def sample_pick(self, debug=False):
        start_date = str(datetime.now())[:10]

        x = np.linspace(1, 1000, 1000)/10
        # Converting probability into a random number generator
        y = [1 if i > random.random() else 0 for i in self.probabilities]

        pick_probabilities = dict(zip(x, y))

        pick_type = random.choice(self.type)
        pick_amount = random.choice(self.amount[pick_type])
        pick_period = int(random.choice(self.period)*7)
        end_date = str(datetime.now() + timedelta(pick_period-1))[:10]

        string = f"""
        If you don't, you will get be punished by {pick_type} for {pick_amount} 
        Effective from {start_date} to {end_date}
        """
        if debug:
            print(string)
        return [pick_probabilities, pick_type,pick_amount, pick_period, start_date, end_date]

