import sys
import time
import datetime
import subprocess
from typing import Dict


def run(config: Dict[str, str]):
    shift = int(config.get('shift', 5))

    print(f'Shift time back by {shift}')
    print('Disabling autosync on host...')
    subprocess.check_output(f'sudo timedatectl set-ntp false', shell=True)

    now = datetime.datetime.now()
    print('Was:', now)
    shift = datetime.timedelta(seconds=shift)
    shifted = now - shift
    print('Became:', shifted)

    print('Shifting time bacwards', subprocess.check_output(f'sudo date -s "{shifted}"', shell=True))
    print('Real time from Google:', subprocess.check_output("curl -I 'https://google.com/' 2>/dev/null | grep -i '^date:' | sed 's/^[Dd]ate: //g'", shell=True))
