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