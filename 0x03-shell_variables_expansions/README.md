# Project 0x03. Shell, init files, variables and expansions

![imagen](https://cloudaffaire.com/wp-content/uploads/2020/05/5_Shell-Scripting-%E2%80%93-Shell-Variables.jpg)
## Resources

#### Read or watch:

- [Expansions](http://linuxcommand.org/lc3_lts0080.php)
- [Shell Arithmetic](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html)
- [Variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html)
- [Shell initialization files](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html)
- [The alias Command](http://www.linfo.org/alias.html)
- [Technical Writing](https://students-support.hbtn.io/hc/en-us/restricted?return_to=https%3A%2F%2Fstudents-support.hbtn.io%2Fhc%2Fen-us%2Farticles%2F360023750254)

#### man or help:

- ```printenv```
- ```set```
- ```unset```
- ```export```
- ```alias```
- ```unalias```
- ```.```
- ```source```
- ```printf```

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/2012/04/feynman-technique/), **without the help of Google:**

### General
- What happens when you type ```$ ls -l *.txt```

## Shell Initialization Files
- What are the ```/etc/profile``` file and the ```/etc/profile.d``` directory
- What is the ```~/.bashrc``` file

## Variables
- What is the difference between a local and a global variable
- What is a reserved variable
- How to create, update and delete shell variables
- What are the roles of the following reserved variables: HOME, PATH, PS1
- What are special parameters
- What is the special parameter ```$?```?

## Expansions
- What is expansion and how to use them
- What is the difference between single and double quotes and how to use them properly
- How to do command substitution with ```$()``` and backticks

## Shell Arithmetic
- How to perform arithmetic operations with the shell

## The ```alias``` Command
- How to create an alias
- How to list aliases
- How to temporarily disable an alias

## Other ```help``` pages
- How to execute commands from a file in the current shell

## Requirements
### General
- Allowed editors: ```vi```, ```vim```, ```emacs```
- All your scripts will be tested on Ubuntu 14.04 LTS
- All your scripts should be exactly two lines long (```$ wc -l file``` should print 2)
- All your files should end with a new line ([why?](https://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
- The first line of all your files should be exactly ```#!/bin/bash```
- A R```EADME.md``` file, at the root of the folder of the project, describing what each script is doing
- You are not allowed to use ```&&```, ```||``` or ```;```
- You are not allowed to use ```bc```, ```sed``` or ```awk```
- All your files must be executable

## More Info

Read your ```/etc/profile```, ```/etc/inputrc``` and ```~/.bashrc``` files.

Look at some files in the ```/etc/profile.d``` directory.

Note: You do not have to learn about ```awk```, ```tar```, ```bzip2```, ```date```, ```scp```, ```ulimit```, ```umask```, or shell scripting, yet.