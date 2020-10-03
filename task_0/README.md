Show current version of your git.
`git --version`

Set the name and email that will be attached to your commits and tags.
`git config --global user.name "<your name>"`
`git config --global user.email "<your email>"`

Initialize a new local repository.
`git init [project name]`

Download a project with the entire history from the remote repository.
`git clone [project url]`

Show the status of changes as untracked, modified, or staged.
`git status`

Prepare files for commit / add file to the staging area.
`git add [file]`

Show changes between working directory and staging area.
`git diff`

Shows any changes between the staging area and the repository.
`git diff --staged`

Show all commits.
`git log`

Show diff of specified commit.
`git show [hash]`

Search in git.
`git grep [something]`

Create a new commit with files from the staging area. Must have a message.
`git commit -m 'commit message'`

Show local branches. With '-a' flag show remote branches also.
`git branch`

Create new branch.
`git branch [branch_name]`

Switch working directory to specified branch.
`git checkout [branch_name]`

Delete untracked files from working direcrory.
`git clean -fd`

Discard changes in working directory.
`git restore [file]`

Move prepared for commit files to unstage area.
`git restore --staged [file]`

Create a new commit, reverting changes from the specified commit.
`git revert [hash]`

Discard number of commits (only if not pushed to remote repo) and move them to working directory.
`git reset HEAD^[number of commits to reset]`

Hide current changes in your working directory into stash for later use.
`git stash`
Restore all hidden files.
`git stash pop`

Join specified branch with your current one.
`git merge [from_branch]`

Updates your local repo with remote one.
`git pull`

Push local changes to remote repo.
`git push [remote]`

Push local branch to remote repo.
`git push -u [remote] [branch]`