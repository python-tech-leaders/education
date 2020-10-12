## Main Bash Shell commands

### Basic terminal navigation
command|description|
|---|---|
`pwd`|print working directory
`ls`|list directory contents
`ls -a`|do not ignore entries starting with .
`ls -l`|use a long listing format with additional info
`cd`|change directory
`man <command>`|show manual of given command
`history`|show commands history

### Basic file manipulation
command|description|
|---|---|
`cat`|show  the whole content of file
`less`|display the contents of a file or a command output, one page at a time
`head`|show the first 10 lines of file
`tail`|show the last 10 lines of file
`grep`|(global regular expression print) - print lines that match patterns
`tail -f path/to/file`|output appended data as the file grows; to stop use `Ctrl + C`
`touch`|change file timestamps. A file argument that does not exist is created empty.
`rm`|remove file. with `-r` flag removes all subdirectories
`mv`|move (rename) files
`cp`|copy files
`cp -r`|copy directories
`makedir`|create directory

### Others
command|description|
|---|---|
`whoami`|show current user
 `chmod`|modify user access
`ps`|process list
`kill <PID>`|kill a process
`>`|redirect the result to a file (rewrite the file)
`>>`|add the result to the end of a file
`command1 \| command2`|chain commands: `cat file \| grep one \| grep two`
