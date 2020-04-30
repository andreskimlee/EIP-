Useful shortcuts

Ctrl + Option + T = will open up your terminal


# Useful Terminal Command Debugging: 

    "Program Must be Run with Administrator priviledges" - run the file with "sudo" (Sudo allows you to run a file with the security priviledges of another user and in default is the super user)

    PWD - prints working directory
    cd ~ takes you to home directory. 
    cd /path takes you to this exact path. 
    cd ./path takes you to a path within the current working directory
    cd ../ go up one level
    ls list content         
    ls -l list in long form (will also show permissions)
        permissions are read via columns. Here is an example :
            -rw-r--r-- 
            1. the owner (First column) can read and write the file
            2. groups can only read.(second column)
            3. public can only read. (third column)


    ls -r reverse order
    ls -s (sort by file size)
    ls --help (all the options you can run with the command)

    nano ./(filename) - file you want to edit / make 
    sudo nano ./file - file you want to edit with superuser (ctrl o to save plus enter)

    sudo su - switch to power user. (if you expect to use a lot of sudos it will be useful to use this)

    sudo apt-get install bluefish (apt-get install) will install the application (Apt-get is kind of like a package manager like npm. It is hosts repositories of applications for ubuntu) Apt is short for aptitude 

    !! (Repeats the previous command) 

    sudo apt-get remove (application-name) removes an application

    apt-cache search item* - will find an app with name closest to the search term 

    apt-cache policy "package-name" will show you the version you have installed and the version available in the repo. 

    sudo dpkg -i "file path" - installs a deb file For example google chrome. 

    sudo apt-get upgrade - upgrades packages to most recent version for your packages

    sudo chown root:name filename.txt - will change ownership of the file to the user you specify

    sudo chmod 646 file.txt - 6 represents read and write. 4 represents read only. In this example, sudo chmod will change the file to be read and write for public. 

    rm filename - removes the file.

    sudo mkdir mydir - creates a directory name mydir

    sudo chown -R andres:andres ./mydir  - all files within myDir ownership change to the specified user. (does this recursively) as well as the directory 

    Review : chmod change permissions / chown changes ownership. 

    touch - creates a file 
    
    rm ./*cpp - would remove all files with the extension cpp

    cp file ./mydir/filename   - copy files you can also change the name while copying. it will look like cp a.txt ./mydir/b.text

    rm dir/mytext.txt - delete specific file

    rm -rf mydir - removes directory 

    mv filename path - move file to the path.

    mv filename newname - change name to that file 

## Search Methods 

    find . -type f -name "*.php" - find all files, case sensitive 
    find . -type f -iname "*.php" - case insensitive search
           type f is files type d is directories

    find . -type f -perm 0664 - returns all the files with the permission values of 664
    find . -type f -size +1M - reutnrs all files greater than 1 mb 
                         -1M (less than 1megabyte)
    find . -type f not -iname "*.php" - returns all files not php

    Find uses recursion to search through the files. You can apply a detailed search such as :

        find . -maxdepth 2 -type f -iname  "*.conf" -size 1m 



    grep "searchterm" filename.tct - will search within your file for that word. You can specify multiple files 
    grep -i (ignore case insensitivity)
    grep -n gives you the line number where the instance is found 

    How to chain the find and grep commands into one

        find . -type f -iname ".txt" -exec grep -i -n  "function" {} + > new.txt
                                                                bracket implys when the exec function has ended.
                                                                after the bracket the > and textfile, it will write into the textfile your 
                                                                output from the command. 
                                                        
            look through all text files with the search term function with the term function canse insensitive and with the line number 

            | tee filename.txt - will print on terminal your output as well as writing to the file. Same as above command but you can see your output. 


## Processes 
   
   top - will return running processes (realtime) (has PID column and a command column)
   
   pgrep processname - will return the PID for each process. They are also in chronological order.
   kill -9 processID - kills the process with the processID.
   killall processname(command) - kills all process and its instances given the command name

   sudo systemctl start applicationname - start app 
   sudo systemctl end elasticsearch - end app

   you can modify the port it runs on by searching for that service's yml file and then editing the port.

   sudo service elasticsearch restart - restart useful for after you updated the yml file. 
        

## crontab

    crontab -e - will open a crontab file which has columns of month date time command, etc and it will run on schedule of the command.
    Use cases: you can make backup of files. etc 
    sudo crontab -e (root user crontab) 



Linux Vocab

    Kernal : The kernal essentially has one job: to translate between the software and the hardware. 



# General Knowledge: 
    ● How systems boot and load Linux
        1. The BIOS which is the software that checks to ensure your hardware is functioning and if it is will initialize it. 
        2. Next the bootloader is run in three steps. (the steps include a way to load your linux kernal)
        3. Kernal is loaded and systemd is loaded
        4. Startup follows the boot process and brings the linux computer to an operable state. 
        5. systemd is the mother of all processes and it is responsible for bringing the Linux host up to a state in which productive work can be done. Some of its functions, which are far more extensive than the old init program, are to manage many aspects of a running Linux host, including mounting filesystems, and starting and managing system services required to have a productive Linux host. Any of systemd's tasks that are not related to the startup sequence are outside the scope of this article.

    ● The shell, and how it interacts with the underlying operating system
        1. Essentiall the terminal (Look above for more indepth CLI commands) 


    ● UNIX file systems and storage
        filess are stored in the directory tree. (Tree like structure). Interesting because the system uses recursion to traverse the nodes of the tree when doing a search.

    ● Process management and state
        recall you can run top to find a bunch of processes and locate command line name for those process or process ID's 

    ● The Linux virtual memory model
        Behaves sort of like a cache and helps with memory management.

        Linux supports virtual memory, that is, using a disk as an extension of RAM so that the effective size of usable memory grows correspondingly. The kernel will write the contents of a currently unused block of memory to the hard disk so that the memory can be used for another purpose. When the original contents are needed again, they are read back into memory. This is all made completely transparent to the user; programs running under Linux only see the larger amount of memory available and don't notice that parts of them reside on the disk from time to time. Of course, reading and writing the hard disk is slower (on the order of a thousand times slower) than using real memory, so the programs don't run as fast. The part of the hard disk that is used as virtual memory is called the swap space.

    ● Techniques for resource control



    ● Common system troubleshooting tools and techniques

What happens when a linux system boots?

1. BIOS which controls the computers hardware is run on the first step. It tests the hardware of the computer by doing a system integrity check. 

fatal error -> hardware issue
non - fatal -> software issue 

the BIOS searches, loads and executes the bootloader program. Once found it handshakes over control to the bootloader

2. Boot Loader Pt1

the MBR is located in the first sector of the bootable disk typically at (dev/sda) MBR is 512 bytes in size. Master boot record identifies how and where an operating system is located so that it can be boot (loaded) into the computer's main storage or random access memory.

3. Boot Loader Pt2  (Grub)
Grand unified Bootloader

Grub is responsible for loading the Operating system for your computer. In our case it will load linux by invoking the operating system's kernal from disk or network. 
The GRUB starts the kernel and tells the memory address of this image file. The kernel then mount this image file as a starter memory based root file system.

4. Kernal. 

kernal is the software that operates your machine. 

The kernel then starts to detect the system’s hardware. The root file system on disk takes over from the one in memory. The boot process then starts INIT (SYSTEMD) and the software daemons according to the Sys Admin’s settings. This can be done at next stages.

5. INIT

When init starts, it become the first or parent process on your Linux machine/server.

First thing init does is it reads the initialization file located in /etc/inittab (Checks to see which initial programs are loaded at startup)

init starts daemon (all background processes) which is responsible for the graphical user interface 

finally GUI shows the login. 


Why linux preferred over other operating systems especially for servers?

1. no licensing fee, its free
2. because it is open source, bugs can be fixed far faster 
3. less likely to crash. 
4. Linux uses fewer resources 

swap partition is a partition created by your choice that will be used when your ram is overflowed. 


What is Bash? What happens when you run ls -l *foo?

Bash is a programming language for your terminal. The terminal exists as a software layer to speak with the kernal

the terminal listens for inputs and once a command is entered bash starts whats called fork-execute-wait-cycle

Fork-execute-wait-cycle: 

    Essentially bash forks the command (creates a child prcoess) that child process then executes the ls command and then waits for the child process to finish.

Terminal is a bash program
Bash program is listening for inputs
Every time I press a keyboard button, hardware interrupt to cpu
CPU switches to kernel mode, reads keyboard input, serves process
bash displays keyboard input
when enter is pressed, bash starts something called as Fork-Execute-Wait Cycle
bash forks and creates replica
I talked about switching into kernel mode too.
replica runs exec to switch into ls
ls takes command line arguments
the *foo part gets sent to a shell globbing program (essentially reads the *foo part) 
ls runs and prints and exits
returns and bash which was waiting now continues


What is fork-execute-Wait cycle

    FORK 

        Pattern where fork creates a replica to the point pc 
        The parent-child processes are differentied by the return value of the fork.
        returns zero PID for a child and non zero for parent.

        Can fork fail? 

        yes PID's are limited if a parent process keeps creating zombie children process, PID's will run out. 
    

    EXEC 

        Replica or child process runs the command given from the commmand line. 
    
    WAIT 

        waits for child process to finish


Zombie Processes 

    Child processes that have finished executing but their parents are still waiting for their return. One way to fix this is to wait on the child by using a waitpid command 

when you run ls -l *foo bash picks up the comman ls which is listing all directories in the current directory. 

then it picks up the -l which is long form. Next the *foo which is a 