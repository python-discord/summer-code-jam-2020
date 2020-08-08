"""Setup script for Web95."""
import os
import sys
import subprocess

subprocess.call(["pip3", "install", "scprint"], stdout=open(os.devnull, 'w')); from scprint import print

def install(Verbose=False):
    """Install Web95."""
    if Verbose:
        stdout = sys.stdout
    else:
        stdout = open(os.devnull, 'w')
    
    print("Cloning Repository...", color="Aqua")
    result = subprocess.call(["git", "clone",
                              "https://github.com/Juicy-Jaguars/\
summer-code-jam-2020"])
    os.chdir("summer-code-jam-2020/juicy-jaguars")

    if result != 0:
        print("Error cloning Repository. Exiting...", color="Red")
        sys.exit()

    print("Repository successfully cloned.", color="Green")
    print()
    print("Installing dependencies...", color="Aqua")
    result = subprocess.call(["pip3", "install", "-r", "requirements.txt"])

    if result != 0:
        print("Error installing Dependencies. Exiting...", color="Red")
        sys.exit()

    print("Dependencies successfully installed.", color="Green")
    print()
    print("Making migrations...", color="Aqua")
    result = subprocess.call(["python",
                              os.path.join("Web95", "manage.py"),
                              "migrate"])

    if result != 0:
        print("Error making migrations. Exiting...", color="Red")
        sys.exit()

    print("Made migrations successfully.", color="Green")
    print()
    print("Successfully installed. Run with 'python Web95/manage.py\
 runserver' from summer-code-jam-2020/juicy-jaguars/", color="Green")


if __name__ == "__main__":
    try:
        if sys.argv[1] == "install":
            try:
                if sys.argv[2] == "-v":
                    install(True)
                else:
                    print("Incorrect usage of ", os.path.basename(__file__), "! (3)", file=sys.stderr, sep="", color="Red")
            except IndexError:
                install()
        else:
            print("Incorrect usage of ", os.path.basename(__file__), "! (2)", file=sys.stderr, sep="", color="Red")
    except IndexError:
        print("Incorrect usage of ", os.path.basename(__file__), "! (1)", file=sys.stderr, sep="", color="Red")