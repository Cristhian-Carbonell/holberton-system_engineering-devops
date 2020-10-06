# System engineering & DevOps - Bash

![image](https://d3pmluylahx1gi.cloudfront.net/wp-content/uploads/2019/12/04212545/Nub8-What-is-Devops-1.png)

DevOps is not a specific position, nor is it a set of tools. It is rather a movement/culture centered around the marriage of development and operations teams, which have traditionally been siloed within a company. It is an outgrowth of the [Agile methodology](https://en.wikipedia.org/wiki/Agile_software_development) which emphasizes rapid software development through small but continuous changes to a company’s codebase, rather than large and infrequent overhauls. DevOps seeks to encourage collaboration between the software developers who write the code, and operations (systems engineers, system administrators, release engineers, database administrators, network engineers, security professionals, etc.) who put the code into production.

Several separate concepts/services have been developed out of the DevOps movement such as:

- **Build Automation**

  - Build automation is the process of using tools to automatically build code from source in order to prepare it for deployment to a live environment. This includes compiling, linting, minifying, transforming, and unit testing.
  - Some of the benefits are that it makes building fast, consistent, repeatable, portable, and reliable.
  
- **Continuous Integration**

  - The process of continuously pushing code and integrating with the code base.
  - It is done with the help of a CI server which executes automated builds/tests.
  - If there is a problem, developers are notified so that they may act upon bugs immediately.
  - It eliminates the scramble to release that is a frequent issue with monolithic architectures, makes frequent releases possible, and makes continuous testing possible.

- **Continuous Delivery**

  - Continuous delivery is about always maintaining code in a state which could be pushed into production.
  - This allows changes to be rolled back much more easily.
  - The benefits include a faster time to market, fewer issues with deployment, and lower risk.

- **Continuous Deployment**

  - Continuous deployment consists of frequently making small changes to code which are pushed to production continuously.
  - This differs from continuous delivery in that it is about actually pushing the code into production, rather than maintaining it in a state which is ready for deployment.

- **Infrastructure as Code (IAC)**

  - IAC is about managing and provisioning infrastructure through code and automation.
  - Infrastructure consists of servers, instances, environments, containers, clusters, etc.
  - IAC allows for consistency, reusability, and scalability.

- **Configuration Management**

  - CM is the process of maintaining and changing the state of infrastructure in a consistent and stable way.
  - eg. upgrade a software package on a bunch of servers automatically rather than manually.
  - CM saves time, provides insight into current state of infrastructure, and is maintainable because the infrastructure is stable.

- **Orchestration**

  - Orchestration is a type of automation that supports processes and workflows, such as the provisioning of resources.
  - eg. a system is experiencing increased load, a customer or monitoring tool recognizes an increased need for resources, and automatically puts together additional resources.
  - It is scalable, stable, time-saving, and self-servicing.

- **Monitoring**

  - It is the collection and presentation of data about the performance and stability of services and infrastructure.
  - It collects information and statistics on memory use, cpu, disk i/o, application logs, network traffic.
  - Provides real-time notifications; postmortem analysis.
  - Allows for fast recovery, better root cause analysis, visibility across teams (both dev and ops), and automated responses.

- **Microservices**

  - A particular software architecture which breaks an application up into a collection of small, loosely-coupled services.
  - The services work together via APIs
  - Microservices are modular which reduces complexity in maintenance, technological flexibility (you can use different tools, languages, etc.), and provide optimized scalability,

As mentioned above, DevOps is not a set of tools, however, in order to make the idea a reality, several tools have been developed.

## Example DevOps Tools:

- **Build Automation**
  - Java - ant, maven, gradle
  - Javascript - npm, grant, gulp
  - Unix-based - Make
  - Machine images and containers - Packer

- **Continuous Integration**

  - Bamboo
  - Gitlab
  - Jenkins
  - Travis CI

- **Configuration Management**

  - Puppet
  - Chef
  - Ansible
  - Salt

- **Virtualization and Containerization**

  - Vagrant
  - Docker

- **Monitoring**
  - SenSu
  - SumoLogic
  - NewRelic
  - AppDynamics
  - DataDog

- **Orchestration**

  - Docker Swarm
  - Kubernetes
  - Zookeeper
  - Terraform

For a more full listing of DevOps tools, see the [Periodic Table of DevOps Tools](https://digital.ai/periodic-table-of-devops-tools)

### Check out:

- [What is DevOps?](https://theagileadmin.com/what-is-devops/)
- [Understanding Agile Methodology](https://digital.ai/resources/agile-101)


# Bash

![imagen](https://opensource.com/sites/default/files/styles/image-full-size/public/lead-images/bash_command_line.png?itok=k4z94W2U)

## Bash is an application

When you start a terminal (such as the GNOME Terminal or Konsole on Linux or iTerm2 on macOS) running the Bash shell, you're greeted with a prompt. A prompt is a symbol, usually a dollar sign ($), indicating that the shell is waiting for your input. Of course, knowing what you're supposed to type is another matter entirely.

This probably comes across as unfriendly, but it's actually a perfectly succinct representation of the many connotations around the term "Bash." To many new users, there's no separation between the concept of Bash and the concept of Linux or Unix: it's the proverbial black-screen-with-green-text into which you're supposed to code what your computer does next. That conflates the Bash shell with the commands you type into the shell. It's important to understand that they're two separate things: Bash is just an application, and its primary job is to run other applications (in the form of commands) that are installed on the same system.

## Linux commands

On Linux and Unix (such as BSD and macOS), most commands are stored by default in system directories like /usr/bin and /bin. By nature, Bash doesn't know these commands any more than you naturally know Klingonese, but just as you can look up Klingon words, Bash can look up commands. When you issue a command to Bash, it searches specific directories on your system to see whether such a command exists. If the command does exist, then Bash executes it.

Bash is also a command, and it's usually the default command executed when you open a terminal window or log into a text console. To find out where any command is located on your system, Bash included, you can use the which command in a terminal:

```shell
$ which bash
/usr/bin/bash
$ which ls
/usr/bin/ls
```
A few commands are built into Bash. Most built-in commands are specific to Bash scripting or low-level environment settings, but a few are universally useful, such as cd (for change directory). Built-in commands don't show up when you search for them because they don't exist in your usual executable path:

```shell
$ which bash
which: no cd in (/usr/local/bin:/usr/bin:/bin:
[...]
```
They're still available, though, because they're built into Bash, and Bash is what you're running.

## Running Bash

Most modern Linux and Unix distributions provide a Bash shell by default. They do this because Bash is well-known, and it has several convenience functions that other shells don't. However, some systems use another shell by default. To find out whether you're running a Bash shell, you can use the echo command along with a special variable representing the name of the currently running process:

```shell
$ echo $0
bash
```
If you're not running Bash, but you'd like to try it, you can probably download and install Bash from your software center, software repository, or ports tree. Or you can use Chocolatey on Windows or Homebrew on macOS. If all else fails, visit the Bash homepage for more information.

## Working in Bash

Bash is a legitimate interface to your computer, and it's not just for server admins and programmers. It can be your desktop, your word processor, your graphics editing application, and much, much more. Some people use Bash more than they use desktop apps.

There are hundreds of commands available for Linux and Unix, and it might surprise you just how diverse they are. For instance, you can resize and crop photos without ever opening the photo in a viewer or editor:

```s
$ mogrify -geometry 1600^x800 \
  -gravity Center \
  -crop 1600x800+0+0 myphoto.jpg
```
You can play music with commands like ogg123 or mpg321, convert audio with sox, adjust and edit video with ffmpeg, edit text with emacs or vim, check email with pine or mutt, browse the internet with elinks, browse files with ranger or midnightcommander, and do much, much more. It's all done in Bash, using the commands you find on your system or in your software repository.

## Bash scripting

One reason Bash (and Linux in general) is considered so powerful is because it's scriptable. Anything you can type into Bash manually, you can also list in a plain-text file and have Bash run it for you. Instead of spending an afternoon manually running a hundred commands, you can script the commands and have your computer execute them while you tend to more important matters. Because nearly everything on Linux runs on top of the Bash shell, nearly everything on Linux can be scripted through Bash. While there are exceptions to this (graphical applications may have their own scripting language, for instance, or no scripting at all), scripting your OS opens up tens of thousands of possible functions you can make happen on your computer without doing them yourself.
The amount of work this saves Linux users each day is impossible to estimate. It's not the usual automation that makes the difference, though; it's the bespoke workflows that people invent for themselves, the things nobody else thinks need automation.

When experienced users say that they want to learn Bash, if they don't mean they want to learn Linux commands, then they probably mean that they want to improve the way they script their commands. For instance, this is an extremely rudimentary Bash script that converts a temporary file (imagine it's a file created by a separate process) to a specific directory:

```s
#!/usr/bin/bash

cp tmp.png ~/public_html/`date +%Y%m%d`.png
```

That's valid Bash. You can verify it by copying and pasting the command (the last line beginning with cp) into a terminal. As long as there's a file called tmp.png and a directory called ~/public_html, the command works.

Learning Bash, though, is all about understanding how a simple command like this can be improved for the sake of automation. For instance, if the file tmp.png doesn't exist, then the script fails. If this script is a key component to, for instance, a blogging site that requires a new image each day so that a custom header image can be constructed, then the script's failure could cause catastrophic errors elsewhere. A user who knows Bash could add resiliency using Bash syntax:

```s
#!/usr/bin/bash

IMG="tmp.png"

[[ -e tmp.png ]] || IMG="generic.png"

cp ~/"${IMG}" ~/public_html/`date +%Y%m%d`.png
```
This is just one example of the process of learning to script with Bash, but it demonstrates how learning both Linux and Bash are equally useful and not entirely separate tasks.

## Advantages of Bash

Bash is as powerful as other shells but adds convenience functions like the double brackets ([[ and ]]) in the sample code. These "Bashisms" are much loved by Bash users because they avoid the sometimes verbose and awkward syntax in other shells like tcsh or ash. However, they are unique to Bash and are not POSIX-compliant, which could cause compatibility issues on systems not running Bash. Then again, Bash is open source free software, so most users can install it if they need it. The lack of compatibility only forces an extra dependency and does not exclude anyone from using a script.