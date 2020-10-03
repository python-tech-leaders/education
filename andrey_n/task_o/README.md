#  git init will create a new local GIT repository. The following Git command will create a repository in the current directory:
`git init`

#    Alternatively, you can create a repository within a new directory by specifying the project name:
`git init [project name]`

#    git clone is used to copy a repository. If the repository lies on a remote server, use:
`git clone username@host:/path/to/repository`

#   Conversely, run the following basic command to copy a local repository:
`git clone /path/to/repository`

#    git add is used to add files to the staging area. For example, the basic Git following command will index the temp.txt file:
`git add <temp.txt>`

# git commit will create a snapshot of the changes and save it to the git directory.
`git commit –m “Message to go with the commit here”`

#    git config can be used to set user-specific configuration values like email, username, file format, and so on. To illustrate, the command for setting up an email will look like this:
`git config --global user.email youremail@example.com`

#    The –global flag tells GIT that you’re going to use that email for all local repositories. If you want to use different emails for different repositories, use the command below:
`git config --local user.email youremail@example.com`

#    git status displays the list of changed files together with the files that are yet to be staged or committed.
`git status`

#  git push is used to send local commits to the master branch of the remote repository. Here’s the basic code structure:
`git push origin <master>`

#   Replace <master> with the branch where you want to push your changes when you’re not intending to push to the master branch.
` git checkout -b <branch-name>`

#    To switch from one branch to another, simply use:
`git checkout <branch-name>`

#    git remote lets you view all remote repositories. The following command will list all connections along with their URLs:
`git remote –v`

#    To connect the local repository to a remote server, use the command below:
`git remote add origin <host-or-remoteURL>`

#    Meanwhile, the following command will delete a connection to a specified remote repository:
`git remote rm <name-of-the-repository>`

#    git branch will list, create, or delete branches. For instance, if you want to list all the branches present in the repository, the command should look like this:
`git branch`

#    If you want to delete a branch, use:
`git branch –d <branch-name>`

#    git pull merges all the changes present in the remote repository to the local working directory.
`git pull`

#    git merge is used to merge a branch into the active one.
`git merge <branch-name>`

#    git diff lists down conflicts. In order to view conflicts against the base file, use
`git diff --base <file-name>`

#    The following basic command is used to view the conflicts between branches before merging them:
`git diff <source-branch> <target-branch>`

#    To list down all the present conflicts, use:
`git diff`

#    git tag marks specific commits.  Developers usually use it to mark release points like v1.0 and v2.0.
`git tag <insert-commitID-here>`


#    git reset command will reset the index and the working directory to the last git commit’s state.
`git reset --hard HEAD`

#    git rm can be used to remove files from the index and the working directory.
`git rm filename.txt`

#    git stash command will temporarily save the changes that are not ready to be committed. That way, you can go back to that project later on.
`git stash`

#    git show is a command  used to view information about any git object.
`git show`

#    git fetch allows users to fetch all objects from the remote repository that don’t currently reside in the local working directory.
`git fetch origin`

#    git ls-tree allows you to view a tree object along with the name, the mode of each item, and the blob’s SHA-1 value. Let’s say you want to see the HEAD, use:
`git ls-tree HEAD`

#    git cat-file is used to view the type and the size information of a repository object. Use the -p option along with the object’s SHA-1 value to view the information of a specific object, for example:
`git cat-file –p d670460b4b4aece5915caf5c68d12f560a9fe3e4`

#    git grep lets users search through committed trees, working directory, and staging area for specific phrases and words. To search for www.hostinger.com in all files, use:
`git grep "www.hostinger.com"`
