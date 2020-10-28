#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if int(os.environ.get("PRODUCTION", 0)):
        print("\n\n\n\n\n Production Environment \n\n\n\n\n\n")
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mainsite.settings.production")
    else:
        print("\n\n\n\n\n Development Environment \n\n\n\n\n\n")
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mainsite.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
