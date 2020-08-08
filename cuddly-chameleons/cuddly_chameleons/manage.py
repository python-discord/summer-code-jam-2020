#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import time

import psycopg2


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cuddly_chameleons.settings')
    os.environ.setdefault('ADMIN_USERNAME', 'admin')
    os.environ.setdefault('ADMIN_PASSWORD', 'admin')
    try:
        import django
        from django.contrib.auth import get_user_model
        from django.core.management import call_command, execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    if len(sys.argv) > 1 and sys.argv[1] == "run":
        attempts = 0
        success = False

        while attempts < 10 and success is False:
            try:
                psycopg2.connect(os.getenv('DATABASE_URL'))
                success = True
                print(f"Try {attempts + 1}: Success")
            except Exception:
                print(f"Try {attempts + 1}: Failed")
                time.sleep(5)
            finally:
                attempts += 1

        django.setup()
        call_command("makemigrations")
        call_command("migrate")

        name = os.getenv('ADMIN_USERNAME')
        password = os.getenv('ADMIN_PASSWORD')
        user = get_user_model()

        if not user.objects.filter(username=name).exists() and os.getenv('DEBUG') == 'true':
            user.objects.create_superuser(name, '', password)
            print(f"Created superuser {name} with password '{password}'")

        call_command("runserver", "0.0.0.0:8000")
    else:
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
