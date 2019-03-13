#!C:\Users\upapa\PycharmProjects\pyhton_refactored_pub\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'drink==0.0.10','console_scripts','drink'
__requires__ = 'drink==0.0.10'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('drink==0.0.10', 'console_scripts', 'drink')()
    )
