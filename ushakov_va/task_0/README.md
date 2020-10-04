Adding README file and .gitignore:
>touch README.md
>touch .gitignore

Git initialization
>git init

Adding separate files to track, such as the README file and .gitignore:
>git add README.md
>git add .gitignore

Adding all files to git for tracking:
>git add.

First commit:
>git commit -m "first commit" [-m -message; "first commit" - a description of what was done]

Checking the change status of files in git
>git status

Viewing commit history in git
>git log
>gitk

Publishing files to a remote server:
>git push -u repos branch [repos is the name of the repository, branch is the branch]

Receiving changes on a remote server
>git fetch repos [repos - name of fetch. server]

Cloning a remote git repository
>git clone git: //github.com/schacon/ticgit.git

Removing files from tracked in git:
>git rm file_name [file_name - filename]

Removing files from git index
>git rm --cached path_to_file [path_to_file - path to file or folder]

Adding a new remote repository:
>git remote add short_rep_name https://github.com/path_to_rep [short_rep_name - repository name; https://github.com/path_to_rep - link to the username]

Retrieving information about a remote server
>git remote show server_name [server_name - remote name. server]

Retrieving all remote git servers (meaning the servers you are working with.)
>git remote
>git remote -v [-v - add. parameter, shows links to the remote server]

Rename deleted rep.
>git remote rename old_name new_name [old_name - old name; new_name - new name]

Delete deleted rep.
>git remote rm rep_name [rep_name - rep name. which should be removed]

Creating a new branch in git
>git branch branch_name [branch_name - branch name]

Switching to the desired branch in git
>git checkout branch_name [branch_name - branch name]

Create a new branch in git and switch to it instantly
>git checkout -b branch_name [branch_name is the name of the branch]

Merging branches in git
>git merge branch_name [branch_name - branch name]

Deleting a branch in git
>git branch -d branch_name [branch_name - branch name]

Changing the last commit in git [all three commands together make one commit - the second commit replaces the result of the first.]
>git commit -m 'initial commit'
>git add forgotten_file
>git commit --amend

Un-indexing a file in git
>git reset HEAD file_name [file_name - filename]

Discarding file changes in git
>git checkout file_name [file_name - file name]

>cd / path / to / my / repo
>git remote add origin ... - path
>git push -u origin --all # pushes up the repo and its refs for the first time
>git push -u origin --tags # pushes up any tags