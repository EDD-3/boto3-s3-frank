#!c:\users\eduardo\documents\pythonprojects\boto3-s3-frank\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'python-slugify==4.0.0','console_scripts','slugify'
__requires__ = 'python-slugify==4.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('python-slugify==4.0.0', 'console_scripts', 'slugify')()
    )
