#!/usr/bin/env python
import os
import sys
# 다른 설치없이 컴퓨터에서 웹 서버 시작가능하게 하는 스크립트.
if __name__ == "__main__":  # 파이썬 프로그램 시작점.
    # 모듈.함수.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
