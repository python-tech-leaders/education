# Linux Commands - Basic Bash Command Line

`ls`
List directory contents.
Example: ls /applications will display all the files and folders stored in the applications folder.

`cd`
Change to a directory.
Example: Change from the current directory to /usr/local with cd /usr/local.

`mv`
Rename or move file(s) or directories.
Example: the command mv todo.txt /home/qlarson/Documents would move "todo.txt" to the "Documents" directory.

`mkdir`
Create a new directory.
Example: mkdir freecodecamp will make a directory named "freecodecamp".

`rmdir`
Delete empty directories.

`touch`
Create an empty file with the specified name.

`rm`
Remove file(s) and/or directories.
Example: rm todo.txt will delete the file.

`locate`
Locate a specific file.
Example: locate -i vacuum*mop command will search for any file that contains the word "vacuum" and "mop". The -i makes the search case-insensitive.

`clear`
Clear a command line screen/window for a fresh start.

`cp`
Copy files and directories.
Example: the command cp todo.txt /home/qlarson/Documents would create a copy of "todo.txt" to the "Documents" directory.

`alias`
Create an alias for Linux commands.
Example: alias search=grep will allow you to use search instead of grep.

`cat`
Display the contents of a file on the screen.
Example: cat todo.txt will show the text of "todo.txt" on the screen.

`chown`
Change who owns a file.
Example: chown qlarson todo.txt will make "qlarson" the owner of "todo.txt".

`chmod`
Change a file’s permissions.
Example: chmod 777 todo.txt will make "todo.txt" readable, writable, and executable by everyone. The digits in "777" specify the permissions for user, group, and others, in that order.

`sudo`
Perform tasks that require administrative or root permissions.
Example: Use sudo passwd quincy to change the password of user "quincy".
"Sudo make me a sandwich."

`find`
Search for files matching a provided pattern. This command is for searching file(s) and folder(s) using filters such as name, size, access time, and modification time.
Example: find /home/ -name todo.txt  will search for a file named "todo.txt" within the home directory and its subdirectories.

`grep`
Search files or output for a particular string or expression. This command searches for lines containing a specified pattern and, by default, writes them to the standard output.
Example: grep run todo.txt will search for the word "run" in the "todo.txt" file. Lines that contain "run" will be displayed.

`date`
Display or set the system date and time.

`df`
Display report on the system’s disk space usage.

`du`
Show how much space each file takes up. This will show the size in disk block numbers. If you want to see it in bytes, kilobytes, and megabytes, add the -h argument like this: du -h.

`file`
Determine the type of a file.
Example: file todo.txt would likely show the type of "ASCII text".

`history`
Shows the command history.

`kill`
Stop a process.
Example: Stop a process with a PID of 485 using the command kill 485. Use the ps command (below) to determine the PID of a process.

`less`
View the contents of a file one page at a time.
Example: less todo.txt will display the contents of "todo.txt".

`ps`
Display a list of the currently running processes. This can be used to determine PIDs needed to kill processes.

`pwd`
Display the pathname for the current directory. "print working directory"

`ssh`
Remotely log in to another Linux machine, over the network.
Example: ssh quincy@104.25.105.32 will login to 104.25.105.32 using the username "quincy".

`tail`
Display the last 10 lines of a file. See fewer or more lines by using the -n (number) option.
Example: tail -n 5 todo.txt will display the last 5 lines of "todo.txt".

`tar`
Store and extract files from a tarfile (.tar) or tarball (.tar.gz or .tgz).

`top`
Displays the resources being used on your system, similar to the task manager in Windows.