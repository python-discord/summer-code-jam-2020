import subprocess
import os
import sqlite3
import platform


# If an error happens during loading data, empties the table and returns.
def tablewipe():
    conn = sqlite3.connect("mysqlite.db")
    c = conn.cursor()

    # delete all rows from table
    c.execute("DELETE FROM earlydating_profiles;",)

    print("We have deleted", c.rowcount, "records from the table.")

    # commit the changes to db
    conn.commit()
    # close the connection
    conn.close()


# Runs for Windows
if platform.system() == "Windows":
    # Moves thoughout the directory loading the files as needed to to run the app.

    os.chdir("../")
    subprocess.run(["pip", "install", "-r", "requirements.txt"], shell=True)
    os.chdir("./djangoProject")
    subprocess.run(["python", "manage.py", "makemigrations"], shell=True)
    subprocess.run(["python", "manage.py", "migrate"], shell=True)
    subprocess.run(["python", "manage.py", "loaddata", "users.json"], shell=True)

    try:
        subprocess.run(["python", "manage.py", "loaddata", "profiles.json"], shell=True)

    except Exception:
        tablewipe()
        subprocess.run(["python", "manage.py", "loaddata", "profiles.json"], shell=True)

    subprocess.run(["python", "manage.py", "runserver"], shell=True)

# Runs for linux and mac
else:
    os.chdir("../")
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    os.chdir("./djangoProject")
    subprocess.run(["python", "manage.py", "makemigrations"])
    subprocess.run(["python", "manage.py", "migrate"])
    subprocess.run(["python", "manage.py", "loaddata", "users.json"])

    try:
        subprocess.run(["python", "manage.py", "loaddata", "profiles.json"])

    except Exception:
        tablewipe()
        subprocess.run(["python", "manage.py", "loaddata", "profiles.json"])

    subprocess.run(["python", "manage.py", "runserver"])
