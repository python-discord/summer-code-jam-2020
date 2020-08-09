"""Setup script for Web95."""
import os
import sys
import subprocess


def supports_color():
    """Check if system supports ANSI colour."""
    plat = sys.platform
    supported_platform = plat != 'Pocket PC' and (plat != 'win32' or 'ANSICON' in os.environ)
    is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    return supported_platform and is_a_tty


def install(color=False):
    """Install Web95."""
    if color:
        green = "\u001b[32m\u001b[1m"
        yellow = "\u001b[33m\u001b[1m"
        red = "\u001b[31m\u001b[1m"
        reset = "\u001b[0m"
    else:
        green, yellow, red, reset = "", "", "", ""

<<<<<<< HEAD
    print(yellow + "Cloning Repository..." + reset)
=======
    print(yellow+"Cloning Repository..." + reset)
>>>>>>> 9c34ed224026bde375190676c9c1e370c4c362e4
    result = subprocess.call(["git", "clone", "https://github.com/Juicy-Jaguars/summer-code-jam-2020"])
    os.chdir("summer-code-jam-2020/juicy-jaguars")

    if result != 0:  # Checks the returned error code. 0=OK !0=Not OK
        print(red + "Error cloning Repository. Exiting...")
        sys.exit()

    print(green + "Repository successfully cloned." + reset)
    print()
    print(yellow + "Installing dependencies..." + reset)
    result = subprocess.call(["pip3", "install", "-r", "requirements.txt"])

    if result != 0:  # Checks the returned error code. 0=OK !0=Not OK
        print(red + "Error installing Dependencies. Exiting...")
        sys.exit()

    print(green + "Dependencies successfully installed." + reset)
    print()
    print(yellow + "Making migrations..." + reset)
    result = subprocess.call(["python", os.path.join("Web95", "manage.py"), "migrate"])

    if result != 0:  # Checks the returned error code. 0=OK !0=Not OK
        print(red + "Error making migrations. Exiting...")
        sys.exit()

    print(green + "Made migrations successfully." + reset)
    print()
    print(green + "Successfully installed. Run with 'python Web95/manage.py runserver' from summer-code-jam-2020/\
        juicy-jaguars/" + reset)


if __name__ == "__main__":
    color = supports_color()
    if sys.argv[1] == "install":
        install(color)
