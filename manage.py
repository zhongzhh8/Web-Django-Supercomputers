# -*- coding:utf-8 -*-
import sys
import importlib
importlib.reload(sys)
import os
os.environ['NLS_LANG'] = 'Simplified Chinese_CHINA.ZHS16GBK'


#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
default_encoding = 'utf-8'


import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Web_Django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
