# Overview
In this document I will briefly describe the git commands you should know. We will probably not do too much advanced stuff, but this is a really good time to practice.

### Pull & Checkout
The `pull` pulls code from the remote repository (the code that is online), this is how you sync your local files with the files that are remote (from remote to local). Try to pull whenever you start work on a new feature to prevent merge conflicts from occuring. The `checkout` command is a way to manage branches (alternate versions of your code).
Typical usage:
1. Go to the master branch: `git checkout master` 
2. Sync up with remote to get all the latest changes: `git pull`
3. Checkout a new feature branch: `git checkout -b feat/<some feature>` (omit the `-b` if the branch already exists)

### Add, Commit, Push
`add` is a way to mark what files should be staged (in other words: which files will be committed the next time you run `commit`). `commit` is the command for committing the files to the repository alongside with a message. `push` syncs files between local and remote much like pull, only in the other direction (from local to remote). Typical usage:
1. Write some code
2. Add files to staging, you can use a GUI, a vscode plugin, or the command line: `git add <files you have changed>` or `git add .` to add all files.
3. Run `git commit` to open a prompt of a text editor
4. The prompt will show you which files are about to be committed and it will ask you to provide a message describing your change. Add this message and save the file.
5. You could also run `git commit -m "<message>"` but this would entirely skip the prompt, which I discourage
6. Sync up the changes with remote: `git push` or `git push -u origin <branch name>`

### Typical git workflow
The `master` branch will be protected and we will work with feature branches. The reason for this is that the master branch will be mirroring to the project repository and we do not want any merge conflicts there. By keeping our `master` pristine, we are sure the project branch remains intact as well. The reason we aren't working directly from the project repository is because we are using github actions for CI/CD and these changes only get picked up on a master branch. So your workflow will typically be something like:
1. `git checkout master`
2. `git pull`
3. `git checkout -b feat/<name of new feature>`
4. Write your code and `git add`/`git commit` accordingly in logical chunks (commit often!)
5. Once your feature is ready, push to remote: `git push -u origin feat/<name of new feature>`
6. Sign in to github and create a new pull request from the web interface from your new branch into `master`
7. Wait for your code to be reviewed
8. Process the feedback of the code review and `git add`/`git commit` accordingly
9. Push the revised changes to the branch `git push` (no need to specify branch this time)
10. If the code passes code review, it will get merged into master
11. You then sync up with remote again `git checkout master` & `git pull`
12. Delete your old branch `git branch -d feat/<name of new feature>`
13. Rinse and repeat

### How big should commits be?
A commit message has a head (the first line) and a body (anything after that). 
A good convention is to hold yourself to the following rules when it comes to committing:
- The head describes what you did
- The body describes why you did something
- The commit should be as atomic as possible
- Though the body is optional, it is good practice to include it. If you have to explain why you made a change, you are forced to think if about what you actually did :)
- The commit should make sense when placed after the sentence `When applied, this commit will...`

A good commit might be:
```git
Add logging for api endpoints

Periodically some users manage to bypass the authentication, but it is unclear how or why.
Logging is introduced to identify the offending users for further investigation```

This commit describes all the changes in 1 line and gives a good reason for why the change was needed in the first place.

A commit that is less valuable might be something like: 
```git
Add logging for api endpoints and remove commented out code```

This commit doesn't work because:
1. It is actually 2 changes (add logging AND remove commented out code)
2. The second part of this message is not very clear about what exactly is removed
3. There is no reason for why the code needed to be removed
