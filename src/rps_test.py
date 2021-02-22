import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, r'C:\Users\haseab\Desktop\Python\PycharmProjects\RPS\src')
sys.path.insert(1, r'C:\Users\haseab\Desktop\Python\PycharmProjects\TiBA\src')

from reward_system import RewardSystem
from punish_system import PunishSystem
from monitor import Monitor
from toggl_loader import DataLoader
from analyzer import Analyzer

reward_sys = RewardSystem()
punish_sys = PunishSystem()
loader = DataLoader()
analyzer = Analyzer()
monitor = Monitor()

monitor.monitor_rp(reward_sys, loader, analyzer)