#!/usr/bin/env python
import os
import sys
# 장고 관리의 진입점
if __name__ == '__main__':
    # 꼭 써줘야 한다 DJANGO SETTINGS MODULE~오류 뜨면 이거 확인.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askcompany.settings.dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# lt: less than
# lte: less than equal
# filter(~~lt = ~~)
