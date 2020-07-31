#!/usr/bin/env python
"""Django's command-line utility."""
import os
import sys
from typing import List

import django
from django.core.management import call_command


class SiteManager:
    """
    Manages the preparation and serving of the website.

    Handles both development and production environments.
    Usage:
        manage.py run [options]...
    Options:
        --silent      Sets minimal console output.
        --verbose     Sets verbose console output.
        --no-migrate  Disable automatic migrations.
        --no-collect  Disable automatic static collection.
        --check       Force django checks to be executed.
    """

    def __init__(self, args: List[str]) -> None:
        self.silent = "--silent" in args
        self.migrate = '--no-migrate' not in args
        self.collectstatic = '--no-collect' not in args
        self.check = '--check' in args

        if self.silent:
            self.verbosity = 0
        else:
            self.verbosity = 2 if "--verbose" in args else 1

    def prepare_server(self) -> None:
        """Perform preparation tasks before running the server."""
        django.setup()

        if self.migrate:
            print("Applying migrations.")
            call_command("migrate", verbosity=self.verbosity)
        if self.collectstatic:
            print("Collecting static files.")
            call_command("collectstatic", interactive=False, clear=True, verbosity=self.verbosity)

    @staticmethod
    def perform_security_check() -> None:
        """Perform django security tests."""
        print('Running security checks.')
        call_command('check', '--deploy', '--fail-level', 'WARNING')

    def run_server(self) -> None:
        """Prepare and run the web server."""
        in_reloader = os.environ.get('RUN_MAIN') == 'true'

        if in_reloader:
            self.prepare_server()

            if self.check:
                self.perform_security_check()

        print("Starting server.")
        # Run the server
        call_command("runserver", "0.0.0.0:5000")
        return


def main() -> None:
    """Process command line execution."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_htvms.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        SiteManager(sys.argv[1:]).run_server()
    else:
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
