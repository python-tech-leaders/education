# 0 - Basic commands shell
>descriptions of basic commands that are used while working with unix shell

`shell` has very many commands. I'll try to show the most useful and common.
Let's separate all commands to groups.
#### 1) Information commands:
|№|command|description|
|---|---|---|
|1|`date`|show current date and time|
|2|`whoami`|show username|
|3|`hostname`|show name of the pc|
|4|`man {command}`|show manual about {command}|
| |example| `man ping`|
|5|`uname {option}`|show info about system, computer, os, and etc|
| |example:|`uname -m` - shows architecture of your OS - 32 or 64 bit|
|6|`groups`|check all user groups|
--------------------------------------
#### 2) Navigation and file commands:
|№|command|description|
|---|---|---|
1|`cd`|change directory
2|`pwd`|path work directory (show current path)
3|`ls`|show files in pwd, using keys `-a` and `-l` you can check hidden files and permissions
4|`cat filename`|show content of file
5|`mkdir dir_name`|create dir with name `dir_name`
6|`touch file_name`|create file with name `dir_name`
7|`cp file_1 file_2`|copy file1 to file2 (or dir)
8|`mv file_1 file_2`|move (or rename) file1 to file2 (or dir)


>There are very many different commands and programms for unzipping (`tar`), networking diagnostic (`ping`, `host`, 
>`nc`,`traceroute`), searching files (`find`), checking system resources (`top`, `ps`) and killing process (`kill`), 
>changing rights for files and folders (`chmod`, `chown`) and atc. I'm not sure, that the task includes
>describe them. That's why, I think it's enough. But also, I want to say about some very powerful tools/tips:
- You can use `>` or `>>` for route out of command to any file.

|examples|description|
|---|---|
|`echo SOMETEXT > file.txt`|write SOMETEXT to file (erase old text, rewrite it)|
|`echo ping ya.ru >> file.txt`| add out of `ping ya.ru` to **file.txt**|

- You can use two or more command, using `&&` and `||`:
    >`command1 && command2` - execute command2 only if comman1 was done successfully
    >
    >`command1 || command2` - execute command2 only if command1 wasn't successfully done
------------
- You can give result of command to other command.
    >Using: `command1 | command2`. Most useful combination - use commands with `grep`:
    >
    >`ls -a ~/ |grep D` - execute `ls -a` and filter results by mask "D"
------------
- You can execute any commands by your user, or superuser (root). For executing command with superuser rights, just put 
    >`sudo` before command:
    >`sudo nano /etc/networks`
    >>hint: if you need execute last entered command with sudo, just run `!!`
------------
- Finally, you can use programming commands, like `if then else`, `for`, `while` and etc.
You can show info about these commands here: https://habr.com/ru/post/471242/



------------
# 1 - Optional: add useful zsh shortcuts
>*I've added the `git` plugin to zsh. And Here are most useful shortcuts:*
* `g` - git
* `gst` - git status
* `ga` - git add
* `gb`	git branch
* `gcb`	git checkout -b
* `gcf`	git config --list
* `gcmsg`	git commit -m
* `gco`	git checkout
* `gd`	git diff
* `gf`	git fetch
* `ghh`	git help
* `gl`	git pull
* `gp`	git push
* `grev` git revert
* `grh`	git reset  
-----------------  
###### All list of commands you can see here: https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git