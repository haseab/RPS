import time
from datetime import datetime, timedelta
from tiba_helper import TiBAHelper
import matplotlib.pyplot as plt
from reward_system import RewardSystem
from punish_system import PunishSystem
import os
import ast
import requests
import random


class Monitor:
    def __init__(self):
        self.reward_dates = []
        self.efficiencies = []
        self.punish_dates = []
        self.inefficiencies = []
        self.override = False
        self.path = os.path.dirname(os.getcwd()) + r"\local"

        with open(self.path + r"\ifttt_key.txt", 'r') as file:
            self.key = file.readline()

    def check_override(self):
        with open(self.path + r"\override_setting.txt", 'r') as file:
            self.override = bool(file.readline())
        return self.override

    def check_reward_status(self, reward_sys, prob_efficiency, actual_efficiency, r_level, end_datetime):
        current_datetime = datetime.now()

        self.reward_dates.append(current_datetime)
        self.efficiencies.append(actual_efficiency)

        if current_datetime > end_datetime:
            if prob_efficiency[round(actual_efficiency*100, 1)] == 1:
                string = ""
                for reward in reward_sys.rewards[r_level]:
                    string += f" --->  {reward} \n"
                resp = requests.post(f"https://maker.ifttt.com/trigger/rewarded/with/key/{self.key}", data={"value1": r_level, "value2": string})
                plt.scatter(self.reward_dates, self.efficiencies)
                plt.show()
            self.reward_dates = []
            self.efficiencies = []
            return False
        return True

    def check_punishment_status(self, prob_inefficiency, actual_inefficiency,p_type, p_amount, end_datetime):
        current_datetime = datetime.now()

        self.punish_dates.append(current_datetime)
        self.inefficiencies.append(actual_inefficiency)

        if current_datetime > end_datetime:
            if prob_inefficiency[round(actual_inefficiency*100, 1)] == 1:
                string = f"""{p_type} for {p_amount}"""
                resp = requests.post(f"https://maker.ifttt.com/trigger/punished/with/key/{self.key}", data={"value1": string})
                plt.scatter(self.punish_dates, self.inefficiencies)
                plt.show()
            self.punish_dates = []
            self.inefficiencies = []
            return False
        return True

    @staticmethod
    def generate_rp(system, keyword, debug=False):
        # Setting all random parameters
        results = system.sample_pick(debug=debug)

        with open(f"saved_{keyword}.txt", 'a') as file:
            file.write(f"Date created: {datetime.now()}" + "\n")
            file.write(str(results) + "\n" + "\n")
        return results

    @staticmethod
    def load_rp(keyword):
        with open(f"saved_{keyword}.txt", "r") as text_file:
            all_text = text_file.readlines()
            if all_text[-2][0] == "[":
                # String formatting to get str(list) into list.
                results = ast.literal_eval(all_text[-2])
            else:
                raise Exception("Error reading the file")
        return results

    def load_rewards(self):
        return self.load_rp("reward")

    def load_punishments(self):
        return self.load_rp("punish")

    def generate_rewards(self, debug=False, override=False):
        if override:
            return self.load_rewards()
        return self.generate_rp(RewardSystem(), "reward", debug=debug)

    def generate_punishments(self, debug=False, override=False):
        if override:
            return self.load_punishments()
        return self.generate_rp(PunishSystem(), "punish", debug=debug)

    def monitor_rp(self, reward_sys, loader, analyzer):
        reward_running, punish_running = False, False
        # Initializing all variables
        r_start_date, r_end_date, prob_efficiency, r_level, r_end_datetime = [None]*5
        prob_inefficiency, p_type, p_amount, p_end_datetime = [None]*4
        while True:
            # Setting all random parameters
            resp = self.check_override()
            if not reward_running:
                prob_efficiency, r_level, r_period, r_start_date, r_end_date = self.generate_rewards(override=self.override)
                # Calculating date-times for period
                r_end_datetime = datetime.strptime(r_end_date, "%Y-%m-%d") + timedelta(random.random())
                reward_running = True
                # print("reward is now running")

            if not punish_running:
                prob_inefficiency, p_type, p_amount, p_period, p_start_date, p_end_date = self.generate_punishments(override=self.override)
                # Calculating date-times for period
                p_end_datetime = datetime.strptime(p_end_date, "%Y-%m-%d") + timedelta(random.random())
                punish_running = True
                # print("punishment is now running")

            while reward_running and punish_running:
                time.sleep(3600)
                actual_efficiency, actual_inefficiency = TiBAHelper.get_actual_efficiency(loader, analyzer, r_start_date, r_end_date)
                reward_running = self.check_reward_status(reward_sys, prob_efficiency, actual_efficiency, r_level, r_end_datetime)
                punish_running = self.check_punishment_status(prob_inefficiency, actual_inefficiency, p_type, p_amount, p_end_datetime)

        return None
