from numpy.random import choice
import json
import sys

password = 'pbkdf2_sha256$180000$rIY0NVmswzaj$CHEAdXxSdOcKF6m1McG51wWWNrJ6Ynl6nGLxEnhqqoA='


MG = ['Male', 'Other']
FG = ['Female', 'Other']

PREF = ['straight', 'gay', 'bisexual']

with open('raw.json', 'r') as f:
    raw = json.load(f)


def email_gen(first_name, last_name):
    pass


def genusers():
    for row in raw:
        del row['fields']['age']
        del row['fields']['gender']
        row['pk'] += 1
        row['model'] = 'auth.user'
        row['fields']['username'] = f"{row['fields']['first_name']} {row['fields']['last_name']}"
        row['fields']['password'] = password
        row['fields']['email'] = f"{row['fields']['first_name']}{row['fields']['last_name']}@aol.com"
    with open('users.json', 'w') as f:
        json.dump(raw, f, indent=4)


def genprofiles():
    for ind, row in enumerate(raw):
        if ind < 200:
            row['fields']['sex'] = 'Male'
            row['fields']['preference'] = PREF[choice(3, 1, p=[0.6, 0.2, 0.2])[0]]
        else:
            row['fields']['sex'] = 'Female'
            row['fields']['preference'] = PREF[choice(3, 1, p=[0.6, 0.2, 0.2])[0]]
        del row['fields']['first_name']
        del row['fields']['last_name']
        del row['fields']['gender']
        row['pk'] += 1
        row['fields']['user'] = row['pk']
    with open('profiles.json', 'w') as f:
        json.dump(raw, f, indent=4)


if __name__ == '__main__':
    if sys.argv[1] == '-u':
        genusers()
    elif sys.argv[1] == '-p':
        genprofiles()
    else:
        print("Use -u or -p")