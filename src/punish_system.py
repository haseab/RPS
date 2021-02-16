import random
import numpy as np
from datetime import datetime, timedelta


class PunishSystem():

    def __init__(self):
        self.wasted_range = np.linspace (0.20,0.35,100)
        self.amount = {"Money Lost": ["$50", "$100", "$150"],
                       "No Access to Comp": ["8 hours", "16 hours", "24 hours"],
                       "Sleep on Floor": ["1 night", "2 nights"]
                       }
        self.type = list(self.amount.keys())
        self.period = np.linspace(0.5, 2, 100)


    def samplepick(self, debug= False):
        start_date = str(datetime.now())[:10]
        pick_wasted_range = round(random.choice(self.wasted_range), 2)
        pick_type = random.choice(self.type)
        pick_amount = random.choice(self.amount[pick_type])
        pick_period = int(random.choice(self.period)*7)
        end_date = str(datetime.now() + timedelta(pick_period))[:10]

        string = f"""
        Goal is to be below {pick_wasted_range*100}% wasted
        If you don't, you will get be punished by {pick_type} for {pick_amount} 
        Effective from {start_date} to {end_date}
        """
        if debug:
            print(string)
        return [pick_wasted_range, pick_type,pick_amount, pick_period, start_date, end_date]

