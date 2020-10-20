# Project 0x01. Shell, permissions

![imagen](https://www.oreilly.com/library/view/learning-linux-shell/9781788993197/assets/99c02f63-3014-4df0-8990-b9474944f298.jpg)

## Resources

#### Read or watch:

- [Permissions](https://intranet.hbtn.io/rltoken/5uUsOHrMbVBOpZFteNyBLg)

#### man or help:

- ```chmod```
- ```sudo```
- ```su```
- ```chown```
- ```chgrp```
- ```id```
- ```groups```
- ```whoami```
- ```adduser```
- ```useradd```
- ```addgroup```

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/2012/04/feynman-technique/), **without the help of Google:**

### Permissions

- What do the commands ```chmod```, ```sudo```, ```su```, ```chown```, ```chgrp``` do
- Linux file permissions
- How to represent each of the three sets of permissions (owner, group, and other) as a single digit
- How to change permissions, owner and group of a file
- Why can’t a normal user ```chown``` a file
- How to run a command with root privileges
- How to change user ID or become superuser

### Other Man Pages

- How to create a user
- How to create a group
- How to print real and effective user and group IDs
- How to print the groups a user is in
- How to print the effective userid

## Requirements

### General

- Allowed editors: ```vi```, ```vim```, ```emacs```
- All your scripts will be tested on Ubuntu 14.04 LTS
- All your scripts should be exactly two lines long (```$ wc -l file``` should print 2)
- All your files should end with a new line ([why?](https://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
- The first line of all your files should be exactly ```#!/bin/bash```
- A ```README.md``` file, at the root of the folder of the project, describing what each script is doing
- You are not allowed to use backticks, ```&&```, ```||``` ```or``` ;
- All your files must be executable

