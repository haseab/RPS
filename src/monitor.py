import time
from datetime import datetime, timedelta
from helper import Helper
import matplotlib.pyplot as plt

class Monitor:
    def __init__(self):
        self.dates = []
        self.efficiencies = []
        self.inefficiencies = []

    def check_reward_status(self, reward_sys, goal_efficiency, actual_efficiency, r_level, end_datetime):
        current_datetime = datetime.now()

        self.dates.append(current_datetime)
        self.efficiencies.append(actual_efficiency)

        if actual_efficiency > goal_efficiency and current_datetime > end_datetime:
            string = f"""Congratulations!! Choose one of the following: \n"""
            for reward in reward_sys.rewards[r_level]:
                string += f" --->  {reward} \n"

            plt.scatter(self.dates, self.efficiencies)
            plt.show()
            return True
        return False

    def check_punishment_status(self, punish_sys, goal_inefficiency, actual_inefficiency,p_type, p_amount, end_datetime):
        current_datetime = datetime.now()

        self.dates.append(current_datetime)
        self.efficiencies.append(actual_inefficiency)

        if actual_inefficiency > goal_inefficiency and current_datetime > end_datetime:
            string = f"""
Damn!! You just lost! Here's your punishment:
{p_type} for {p_amount}
"""

            plt.scatter(self.dates, self.inefficiencies)
            plt.show()
            return True
        return False

    def monitor_rps(self, reward_sys, punish_sys, loader, analyzer):
        while True:
            # Setting all random parameters
            goal_efficiency, r_level, r_period, r_start_date, r_end_date = reward_sys.samplepick(debug=True)
            goal_inefficiency, p_type, p_amount, p_period, p_start_date, p_end_date = punish_sys.samplepick(debug=True)
            a, b = False

            # Calculating date-times for rps period
            r_end_datetime = datetime.now() + timedelta(r_period)
            p_end_datetime = datetime.now() + timedelta(p_period)

            while not a and not b:
                time.sleep(5)
                efficiencies = Helper.get_actual_efficiency(loader, analyzer, r_start_date, r_end_date)
                actual_efficiency = efficiencies[0]
                actual_inefficiency = efficiencies[1]

                # Checking Rewards
                a = self.check_reward_status(reward_sys, goal_efficiency, actual_efficiency, r_level, r_end_datetime)

                # Checking punishments
                b = self.check_punishment_status(punish_sys, goal_inefficiency, actual_inefficiency, p_type, p_amount, p_end_datetime)

        return None
