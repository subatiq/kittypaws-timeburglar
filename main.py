import time
import datetime
import subprocess
from typing import Dict


def run(config: Dict[str, str]):
    print('[timeburglar] Disabling autosync', subprocess.check_output(f'sudo timedatectl set-ntp false', shell=True))

    while True:
        now = datetime.datetime.now()
        print(now)
        shift = datetime.timedelta(seconds=5)
        shifted = now - shift
        print(shifted)

        print('[timeburglar] Shifting time backwards', subprocess.check_output(f'sudo date -s "{shifted}"', shell=True))
        time.sleep(20)

    print('[timeburglar] Enabling autosync', subprocess.check_output(f'sudo timedatectl set-ntp true', shell=True))
