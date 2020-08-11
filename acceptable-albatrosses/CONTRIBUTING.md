# Contributing Guidelines (for the team)

## Setup

0. The code jam organizers will create a repository on GitHub with each team as a separate directory (folder).
    ```
    code-jam-7
    |
    |- Acceptable Albatrosses
    |- Accidental Alpacas
    |- Adventurous Anteaters
    ...
    ```
    The team lead will fork the repository (making a copy on GitHub). We will work on that forked repository.
1. Clone the forked repository.
    ```bash
    git clone https://github.com/charliedua/code-jam-7.git
    ```
2. Before starting work, dependencies need to be setup.<br>
   Please see `README.md` and install development dependencies.
   You may need to install or update new dependencies throughout the project.

## Git workflow

0. Create an issue with details of what, how, why is something going to change especially for bigger ones
1. Create a new branch or continue work off another. Examples:
    - `master` (the original, main branch that every repository starts off)
    - `i18n` (short for internationalization, this branch wants to add multilingual support)
    - `colorblind` (this branch wants to add colorblind support)
    - ... (Work on an appropriate branch even if it's the smallest change ever.)
2. Make a draft pull request merging the branch
    - PR title must follow convention (limit 70? characters, or what GitHub suggests)
    - It is good to add a helpful description of what is changed
3. Make changes
4. Run tests
5. Pull changes from GitHub first
    - If there are new commits, run tests again then move on if no issues
    - If there are new conflicts, stash and hopefully resolve them, and go back to step 4
    - What happens if you get into an endless loop? Good luck?
6. Add files, commit and push
    - Commit message must follow convention (see below)
    - Do not amend or force push, these can be handled later when merging the PR
7. When feature branch is complete, set the PR as ready for review
    - Commits may still be pushed to fix things
8. After at least one OK from the team, an experienced member (who?) may help merge the branch into master either by:
    - Squashing commits into one?
      (suitable for grouping small, inconsequential commits into one,
      commit messages will be combined into the squash commit)
    - Merging? (it will result in an extra, possibly ugly merge commit though)
    - Rebasing? (is this easy?)

## Other workflow

-   Update `NOTICES.md` whenever third-party content is added
    (refer to [Chisel][chisel-url] and [Windows Terminal][terminal-url])

[chisel-url]: https://github.com/salt-die/Chisel
[terminal-url]: https://github.com/microsoft/terminal/blob/master/NOTICE.md

## Testing

-   coverage (test coverage)
-   pytest (functional tests)
-   mypy (static type checking)
-   flake8 (general format linting) + flake8-django
-   pylint (flake8 but more, to check for docstrings and others) + pylint-django
-   black (very opinionated but relieves the issue of maintaining style) + django-stubs
-   CSS?
-   JS?

You can add a pre-commit hook to run all tests and checks by running this:

```bash
git config core.hooksPath acceptable-albatrosses/hooks
```

You may also want to edit the executable used in the pre-commit hook locally:

```bash
# default
pipenv run mypy project
# specific Python executable (use "which python3" to get the path)
/usr/bin/python3 -m pipenv run mypy project
```

GitHub Actions (or other CI/CD if needed) will also be used to run automated tests on push/PR.

## Deployment

(I've never done true continuous deployment, any insights?)
(Deploy to whose server?)

## PR/Commit convention

-   Imperative mood (Verb + object + ...)
    -   Do this
    -   Add tests
    -   Change SQL queries to ORM calls
-   Limit to 50 characters and no period in the subject line or PR title
-   Start with an initial capital letter
-   Append "(Fix #issueno)" for issue fixes
-   Append "(#prno)" for squash commits and merge commits ("(Fix #issueno)" only need be in the PR title then)
-   Please add a body description if there is significant changes (Line length limit: 72 characters, no line limit)
-   Focus on what and why instead of how in the body description
-   Individual commits should only do small changes

```
Implement colorblind support

Several modes of colorblind palettes have been added which are
red-green, monotone and grayscale. This is done to aid in accessibility
for the visually impaired...
...
```

## Code convention

-   As much static typing as possible (`from __future__ import annotations`, `django-stubs` plugin)
-   Black helps eliminating style worries
-   Always have a docstring (imperative mood, actual documentation with sphinx can be considered if complex enough)
-   Always use descriptive, helpful identifiers
-   Please add comments explaining how less straightforward code work
-   Follow PEP8 (should be handled by black)
-   Line length limit: 119 characters (should be handled by black)
-   American English only (colour → color, centre → center, initialise → initialize, analyse → analyze, grey → gray)
