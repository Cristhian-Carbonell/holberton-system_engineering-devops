# Project 0x04. Loops, conditions and parsing

![imagen](https://noelyoung.net/wp-content/uploads/2019/07/useful-bash-commands.jpg)

For this project, students are expected to look at this concept:
- [shell](https://intranet.hbtn.io/concepts/9)

## Background Context

![imagen](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/b07e3333b1edfb9beed5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201022%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201022T181032Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1e5523eff8ea2600b36a1609dd4e031840ec5a939fd86efb9f627ddb2eaa4aa8)

## Resources
#### Read or watch:

- [Loops sample](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html)
- [Variable assignment and arithmetic](https://tldp.org/LDP/abs/html/ops.html)
- [Comparison operators](https://tldp.org/LDP/abs/html/comparison-ops.html)
- [File test operators](https://tldp.org/LDP/abs/html/fto.html)
- [Make your scripts portable](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html)

#### man or help:

- ```env```
- ```cut```
- ```for```
- ```while```
- ```until```
- ```if```

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/2012/04/feynman-technique/), **without the help of Google:**

## General

- How to create SSH keys
- What is the advantage of using ```#!/usr/bin/env bash``` over ```#!/bin/bash```
- How to use ```while```, ```until``` and ```for``` loops
- How to use ```if```, ```else```, ```elif``` and ```case``` condition statements
- How to use the ```cut``` command
- What are files and other comparison operators, and how to use them

## Requirements

### General

- Allowed editors: ```vi```, ```vim```, - ```emacs```
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- You are not allowed to use ```awk```
- Your Bash script must pass ```Shellcheck``` (version ```0.3.3-1~ubuntu14.04.1``` via ```apt-get```) without any error
- The first line of all your Bash scripts should be exactly ```#!/usr/bin/env bash```
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## More Info
### Shellcheck
[Shellcheck](https://github.com/koalaman/shellcheck) is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. ```Shellcheck``` is your friend! **All your Bash scripts must pass ```Shellcheck``` without any error or you will not get any points on the task**.

```Shellcheck``` is available on the school’s computers. If you want to use it on your own computer, here is how to [install it](https://github.com/koalaman/shellcheck#installing).

Examples:

Not passing ```Shellcheck```:

![imagen](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/Vxotqyj.png)

Passing ```Shellcheck```:

![imagen](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/ubHWxDU.png)

For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code ```SC2034```, you can browse [https://github.com/koalaman/shellcheck/wiki/SC2034](https://github.com/koalaman/shellcheck/wiki/SC2034).