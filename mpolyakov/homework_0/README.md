`git --version`\
Show current version of your git

`git config --global user.name "<your name>"`\
`git config --global user.email "<your email>"`\
Set the name and email that will be attached to your commits and tags

`git init [project name]`\
Initialize a new local repository

`git clone [project url]`\
Download a project with the entire history from the remote repository

`git status`\
Show the status of changes as untracked, modified, or staged

`git add [file]`\
Prepare files for commit / add file to the staging area

`git diff`\
Show changes between working directory and staging area

`git diff --staged`\
Shows any changes between the staging area and the repository

`git log`\
Show all commits

`git show [hash]`\
Show diff of specified commit

`git grep [something]`\
Search in git

`git commit -m 'commit message'`\
Create a new commit with files from the staging area. Must have a message

`git commit --amend`\
Change your last commit (if not pushed)

`git branch`\
Show local branches. With '-a' flag show remote branches also

`git branch [branch_name]`\
Create new branch

`git checkout [branch_name]`\
Switch working directory to specified branch

`git checkout -b myFeature develop`\
Create 'myFeature' branch and switch to it

`git clean -fd`\
Delete untracked files from working direcrory

`git restore [file]`\
Discard changes in working directory

`git restore --staged [file]`\
Move prepared for commit files to unstage area

`git revert [hash]`\
Create a new commit, reverting changes from the specified commit

`git reset HEAD^[number of commits to reset]`\
Discard number of commits (only if not pushed to remote repo) and move them to working directory

`git stash`\
Hide current changes in your working directory into stash for later use

`git stash pop`\
Restore all hidden files

`git merge [from_branch]`\
Join specified branch with your current one

`git pull`\
Updates your local repo with remote one

`git push [remote]`\
Push local changes to remote repo

`git push -u [remote] [branch]`
Push local branch to remote repo, i.e. `git push -u origin myFeature`