# Sarcastic Sparrows

---
### Usage

To run in production (assuming you're in the sarcastic-sparrows project directory):

```bash
docker-compose -f production.yml up --build
```

Finally, open the website at [0.0.0.0:8000](http://0.0.0.0:8000).

#### Hacking

Run the app using docker-compose:
```
docker-compose -f local.yml up --build
```

To run the tests:
```
docker-compose -f local.yml run --rm django pytest
```

Please use the pre-commit hook, as well
to allow for lint checks on commit.
Assuming you are in the sarcastic-sparrows
directory:

```
cp .pre-commit-config.yaml ../.pre-commit-config.yaml
pip install pre-commit
pre-commit install
```

The first command will copy the pre-commit config file
to the project root directory (where all the teams' files
are). The latter will pip install pre-commit, and finally,
install the hook in .git.

If you don't want to commit the files but want to check
with pre-commit first, run: `pre-commit run --all-files`

---
### License and Credit

This project is licensed under the MIT License.

This project was created by:

- [rdcox](https://github.com/rdcox)
- [sschar15](https://github.com/sschr15)
- [andrewrhunt](https://github.com/andrewrhunt)
- [TheGermanAZ](https://github.com/TheGermanAZ)
- [Yoom](https://github.com/YoomamaFTW)
