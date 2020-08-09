"""Beta Setup script for Web95."""
# ========= BETA VESION =========

import os
import sys
import subprocess
subprocess.call(["pip3", "install", "scprint"], stdout=open(os.devnull, 'w'))
# ^ Trys to install the module before importing it
from scprint import print  # noqa: E402
# ^ Colored Print module to easly add color to output messages and errors
# ^ https://pypi.org/project/scprint/  |  https://github.com/DanGill/scprint


def install(Verbose=False):
    """Install Web95."""
    if Verbose:  # Allows for a Verbosed output. Default: Silent
        stdout = sys.stdout
        stderr = sys.stderr
    else:
        stdout = open(os.devnull, 'w')
        stderr = open(os.devnull, 'w')

    print("Cloning Repository...", color="Orange1")
    result = subprocess.call(["git", "clone", "https://github.com/Juicy-Jaguars/summer-code-jam-2020"],
                             stdout=stdout, stderr=stderr)
    os.chdir("summer-code-jam-2020/juicy-jaguars")  # Changes directory to our project folder

    if result != 0:  # Checks the returned error code. 0=OK !0=Not OK
        print("Error cloning Repository. Exiting...", color="Red")
        sys.exit()

    print("Repository successfully cloned.", color="Green")
    print()
    print("Installing dependencies...", color="Orange1")
    result = subprocess.call(["pip3", "install", "-r", "requirements.txt"], stdout=stdout)

    if result != 0:  # Checks the returned error code. 0=OK !0=Not OK
        print("Error installing Dependencies. Exiting...", color="Red")
        sys.exit()

    print("Dependencies successfully installed.", color="Green")
    print()
    print("Making migrations...", color="Orange1")
    result = subprocess.call(["python", os.path.join("Web95", "manage.py"), "migrate"], stdout=stdout)

    if result != 0:  # Checks the returned error code. 0=OK !0=Not OK
        print("Error making migrations. Exiting...", color="Red")
        sys.exit()

    print("Made migrations successfully.", color="Green")
    print()
    print("Successfully installed. Run with 'python Web95/manage.py runserver' from summer-code-jam-2020/\
        juicy-jaguars/", color="LightGreen")


if __name__ == "__main__":
    try:
        if sys.argv[1] == "install":
            try:
                if sys.argv[2] == "-v":
                    install(True)
                else:
                    print("Incorrect usage of ", os.path.basename(__file__), "! (3)", file=sys.stderr, sep="",
                          color="Red")
            except IndexError:
                install()
        else:
            print("Incorrect usage of ", os.path.basename(__file__), "! (2)", file=sys.stderr, sep="", color="Red")
    except IndexError:
        print("Incorrect usage of ", os.path.basename(__file__), "! (1)", file=sys.stderr, sep="", color="Red")
        # ^ Red error messages sent to STDERR
