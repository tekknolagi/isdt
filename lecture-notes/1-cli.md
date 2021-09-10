---
---

# Lecture Notes: Command Line

## Lecture 1

### Module overview
In the first of our four modules, you'll learn to effectively use the Linux
command line. You've all likely encountered a command line at some point, be it
in the "Command Prompt" app on Windows, the "Terminal" app on macOS or Linux,
or elsewhere. You may have run simple commands there, perhaps to walk the
filesystem with `ls`, `dir` or `cd`; to compile programs with `gcc`, `clang`,
or `cl.exe`; or to run scripts with `python`, or `ruby`, or `perl`.

But the command line is far more powerful than these simple commands might lead
you to believe. There's a rich suite of standard tools, accessible via the
command line, for working with files and interacting with your operating
system. In this module, we'll teach you about these tools and about the
operating system features and abstractions that they expose.

We'll also teach you how to use the *shell*, which is the program that
interprets the commands you type. The shell makes it easy to interact with
files and programs on your computer by letting you find and rerun past
commands, chain together commands to perform complex operations, and even write
scripts to automate running long sequences of commands.

Learning this material will let you make more effective use of the tools you'll
learn about in this course as well as command-line tools you've already
encountered like compilers. Command-line tools are ubiquitous in all areas of
software engineering, and you'll frequently interact with tools that can't be
used any other way[^ide-abstraction]. Even when a tool has a graphical
interface (or a third-party wrapper that adds one), it's rare for that
interface to expose the full set of functionality that's available from the
command line.

[^ide-abstraction]: You almost certainly rely on command-line tools any time
                    you write a program, even if you don't realize it. To be
                    sure, there are IDEs that let you program without ever
                    seeing a command line; on Windows and macOS, such
                    environments (in the form of Visual Studio and Xcode) are
                    in fact the sanctioned way to develop native applications!
                    Behind the scenes, however, both of these tools invoke
                    command-line tools in order to compile your code, run
                    tests, process resource files, sign and package your
                    application for distribution, and so on. Knowing how to
                    find and run these commands directly will help you figure
                    out what's happening when things go wrong and will give you
                    the freedom to go beyond the IDEs in cases where they can't
                    do exactly what you need.

#### Bash
Every major OS has a shell (and some have multiple!), and they all provide the
general functionality mentioned above. However, the specific syntax and
commands available vary quite significantly. As such, we needed to pick a
specific shell to teach for this module. The shell we chose is called *Bash*,
and it's the default shell used by the vast majority of Linux distributions as
well as by WSL, Windows' Linux compatibility layer.

There are a number of things that make Bash a good shell to learn. First and
foremost, it's what's called a *POSIX* shell. POSIX is the IEEE standard that
defines UNIX-like operating systems, and both Linux[^linux-posix] and macOS
follow it. [Part of
POSIX](https://pubs.opengroup.org/onlinepubs/9699919799.2018edition/utilities/V3_chap02.html)
defines what syntax and commands a shell needs to support. Most of the shell
features we cover in this course are part of POSIX, meaning they won't apply
just to Bash but to any POSIX shell you encounter--for example, *zsh*, which is
macOS's default shell and a popular alternative to Bash on Linux.

Bash does have some nice quality-of-life features that go beyond what POSIX
mandates, though. For example, POSIX doesn't say anything about interactive
shell usage (the process of entering commands at a prompt), so things like
command history and search aren't something you'll find in more barebones POSIX
shells. We'll also cover some Bash-specific command syntax that you'll likely
encounter when reading shell scripts, as the vast majority of scripts you'll
find in the wild are written for Bash.

If you want to follow along with this module on the Tufts homework servers, you
should run `bash --login` to start Bash each time you connect. This is because
the homework servers are in a small minority of Linux systems that are not
configured to use Bash by default. Instead, they default to a non-POSIX shell
called tcsh for historical reasons that we are not privy to. tcsh's prompt on
the servers looks identical to Bash's, so `bash --login` won't appear to have
any effect when you run it. However, if you don't do so, tcsh will interpret
your commands, meaning much of the more advanced syntax we cover will result in
error messages or unexpected behavior.

[^linux-posix]: The majority of Linux distributions are not actually
                POSIX-certified, but nevertheless are generally accepted to be
                POSIX compliant in all the ways that matter. macOS, on the
                other hand, is officially certified since version 10.5.

#### GNU + Linux
As you'll see shortly, most of the command line's power comes from programs you
run. Those programs are not part of the shell but are instead provided by your
operating system. All POSIX operating systems (which are the only kind Bash
will run on) provide a standard set of tools with names and functionality
specified by POSIX. However, just like POSIX shells, there are many different
implementations of these tools and most have extra features beyond what POSIX
mandates. And that's not to mention the numerous non-POSIX tools that come with
any given operating system.

In this course, we'll constrain our studies to the tools you'll find on desktop
and server Linux distributions[^linux-distros]. These distributions rely on
[*GNU Coreutils*](https://www.gnu.org/software/coreutils/) to provide their
POSIX tools. Many other programs and libraries on these distributions also come
from GNU, which is why some people refer to them as
*GNU+Linux*[^other-userspaces] instead of simply Linux.

We've chosen GNU+Linux because it's freely available to anyone, will run on
almost any hardware (unlike, say, macOS), and is what the Tufts homework
servers run. Much of what you will learn is transferable to other POSIX
operating systems like macOS, but some of it (for example, the directory
hierarchy) is not.

[^linux-distros]: For example, Ubuntu, Debian, Fedora, Red Hat Enterprise
                  Linux, Arch Linux, or Gentoo. The Tufts homework servers run
                  Red Hat.

[^other-userspaces]: It's possible to run the Linux kernel with no GNU project
                     code at all: [BusyBox](https://busybox.net/), for example,
                     implements most POSIX tools (including a shell!) in a
                     single tiny program that can fit on even the most
                     space-constrained systems; Android uses the Linux kernel
                     combined with its own BusyBox-inspired implementation of
                     POSIX tools and a custom Java runtime;
                     [FreeBSD](https://www.freebsd.org) and other UNIX
                     derivatives have their own sets of POSIX tools, many of
                     which are easily ported to run on Linux (and which are
                     also the basis for macOS's tools).

### Anatomy of a shell prompt
The first thing you see when you open a command line is what's known as a
*prompt*. On the Tufts homework server, it looks like this:

```
vm-hw09{utln01}31:
```

The prompt is printed by the shell (which is Bash for all examples in this
course) and serves both to inform you that the shell is ready to accept a new
command and to orient you with basic information about the state of the command
line.

In the example above, the prompt consists of three parts: the first, `vm-hw06`,
is the name (or *hostname*) of the computer you're using. In this case, that's
one of Tufts' homework servers (which are virtual machines, hence the `vm-`
naming convention). The second part, `utln01`, is your username, which at Tufts
is your UTLN. The final part, `31`, is something called the "history event
number", which increases by one with each command you run.

Each of these pieces of information serves a purpose: the hostname and username
together tell you where you're executing the command. Accidentally running a
command on the wrong computer (for example, if you forget you've run `ssh`) or
as the wrong user (if you forgot you've run `su` or `sudo`) can be
catastrophic--imagine accidentally rebooting a server that dozens of people are
using instead of your local workstation--and so nearly every shell prompt you
see will include this information prominently. The history event number is
useful when using advanced shell features that let you reference and edit old
commands, which we'll cover in a future lecture.

The punctuation that separates this information is considerably less important
and has no standardized meaning. On the Tufts servers, your username is in
curly braces and the prompt ends with `: `. But the Bash prompt is
customizable, and other systems you encounter will use different punctuation
and include slightly different information[^prompt-shorthand]. In fact, there's
one notable piece of information missing from the Tufts prompt. To illustrate,
let's look at a different prompt. Here's the Bash prompt from the computer I'm
writing these notes on, which runs Arch Linux:

```
[thebb@stingray ~]$
```

You can see that the username and hostname are still there, although now in
reverse order and separated by an at sign. But the history event number is
missing and instead there's a tilde (~) character. The tilde indicates my
*working directory*, which is the place in the filesystem I'm currently "at".
You'll learn a more rigorous definition for this later, but for now you can
think of it as the place where commands look for files by default. (For
example, running `ls` with no arguments shows you the files in your working
directory.) The tilde character is shorthand for my *home directory*, which is
a place for me (as the user "thebb") to put files without worrying about
interference from other users on the system.

Most prompts you'll encounter will show your working directory, as it's another
piece of information that can affect how commands behave. For systems like
Tufts' that don't, you can run the `pwd` (short for "print working directory")
command to see where you are. Most Bash prompts also end with `$ `, for
historical reasons that have been lost to time.

[^prompt-shorthand]: Because prompts vary between people, computers, shells,
                     and operating systems, in this course we will simply use
                     `$ ` to indicate a shell prompt unless we have a good
		     reason otherwise. To learn more, look up the `PS1` and
		     `PS2` shell variables.

### Entering commands
But the prompt isn't just a pretty thing to look at: it's also a rich interface
for composing and editing commands. Have you ever wondered why you can use the
left and right arrow keys to move the cursor around while typing a command but
can't do the same inside a program you've written? It's because interactive
shells like Bash know how to[^readline] handle the special characters that the
kernel emits when you press an arrow key and respond to them appropriately.

The features don't stop there! We'll talk about lots more features of the Bash
prompt in a future lecture, but there are two essential ones that you should
know about now, as they'll save you oodles of typing. These two features are
*history navigation* and *tab completion*.

History navigation refers to the ability to populate the prompt with a
previously-run command by pressing the up arrow. Each time you press it, you'll
go back by one command; once you've found the one you want (and maybe edited it
slightly), just press <kbd>Enter</kbd> to run it! If you go too far, the down
arrow will bring you back, and you can press <kbd>Ctrl-c</kbd> to go straight
to a fresh prompt no matter how far back you are.

Tab completion is how you ask the shell to figure out what you want to type
before you're done typing it. For example, let's say you want to list files in
this course's directory, `/comp/50ISDT`, on the Tufts homework server. Type `ls
/comp/50` (without pressing <kbd>Enter</kbd>) and then press the <kbd>Tab</kbd>
key to trigger tab completion. If you did it right, nothing will happen
immediately. This is because there are lots of different CS 50s on the server
and Bash doesn't know which one you want, which it signals by ignoring your
first press of <kbd>Tab</kbd>. However, if you press <kbd>Tab</kbd> again, Bash
will show you a list of every option it knows about[^no-ls]:

```
50/     50AIR/  50BIO/  50cog/  50CP/   50FCD/  50GD/   50IOT/  50ISDT/ 50NLP/  50PSS/  50SDT/  50WD/
```

Now, add `IS` to your command so you have `ls /comp/50IS` and press
<kbd>Tab</kbd> again. This time, Bash can see there's only one choice that
matches and so it will immediately fill in the `DT/`, no confirmation required.
Tab completion also works with command names (although since POSIX commands are
almost universally four letters or less, it's not usually as useful there) and
some other command-specific things as well. If ever in doubt, just try it!

[^readline]: See `man 3 readline` for more information on this wondrous
             ability.

[^no-ls]: This means you don't have to abandon your command to run `ls` every
          time you forget a file name! You can tab complete without losing what
          you've already typed.

### Anatomy of a command
Now that you're a pro at typing in commands, let's talk about the things you
can type! Although the shell provides the interface you use to enter and edit
commands, it's not what implements the commands themselves (with a few
exceptions). As its name implies, the shell is a thin layer through which you
can access the functionality of your operating system and other programs on
your computer. As such, most commands you'll run instruct the shell to execute
some other program. Here are three examples of such commands, all of which run
the program `/usr/bin/ls`.

```
$ ls
file1    file2    file3
$ /usr/bin/ls
file1    file2    file3
$ ls /
bin  boot  dev  etc  home  lib  lib64  lost+found  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
$ 
```

All the lines starting with `$` in this example were printed by the shell; each
consists of the prompt followed by some command. The other lines, however, were
printed by the various invocations of `ls`. After running a program, the shell
gets out of the way until that program completes, leaving the program free to
print output and read input without interference. Once the program exits, the
shell prints a new prompt and is ready for another command[^repl].

A command is made up of multiple parts. The first word of each of these three
commands (i.e. `ls` or `/usr/bin/ls`) is known as the *command name* and tells
the shell what program to run. All following words (like `/` for the third
command) are known as *arguments* and get sent to the program for
interpretation. In programming terms, you can think of each command like a
function invocation, where the first word is the function's name and the rest
make up the argument list.

So how does the shell know what program to run? For the `/usr/bin/ls` command,
this might seem obvious (and certainly will once you've read the next section):
the shell takes the command name and executes the program at that file path.
But where does it look to find just `ls`? Since there's no file called `ls` in
the working directory, the shell must find the ls program somewhere else.

As it turns out, command names without slashes in them get special treatment:
instead of parsing them like a file path, the shell looks in a set of
predefined directories (typically including `/usr/bin/`) for files with
matching names and runs the first one it finds. Because system tools like `ls`
are in these directories, you don't need to remember or type their full file
paths[^path-security]. If you ever want to know what program a command runs,
you can use the `which` command with the command name as an argument:

```
$ which ls
/usr/bin/ls
$ 
```

Name parsing is the same for every command, but argument parsing is anything
but. Because a command's arguments are interpreted by that command and not by
the shell, every command you use will accept different arguments and assign
those arguments different meanings. Some of these meanings are easy to
guess--for example, `ls` can take as an argument a file path to list; if you
don't give it one, it lists your working directory. But many aren't, and in
those cases you'll need to find them out some other way.

This is where *man pages* come in. Short for "manual page", a man page holds
documentation for a command that's accessible directly from the command
line--no Google needed! To access a man page, run the `man` command and give it
the command you want to learn about as an argument (for example, `man ls`).
This will open up a full-screen view of the man page, which you can navigate
with the arrow or <kbd>PgUp</kbd>/<kbd>PgDn</kbd> keys and leave by pressing
<kbd>q</kbd>. Most man pages follow a common structure, but we'll leave the
details of that structure for later, after you've learned a bit more about some
common conventions for arguments.

[^repl]: This flow of you typing a command at the shell prompt, that command
         taking control of the terminal and running to completion (optionally
         printing output or reading input in the process), and then the shell
         printing a new prompt is known as a *read-eval-print loop*, or a
         *REPL* for short. Some programming languages also have REPLs--modes
         where you can enter one statement at a time instead of running a whole
         file at once. REPLs are common for interpreted languages like Python
         and Ruby and much less common for compiled languages like C and C++.

[^path-security]: This behavior is not only convenient but also improves
                  security. If the shell looked in the working directory first
                  for every command, an attacker could write a malicious
                  program named `ls`, `cat` or similar and place it in a
                  publicly-readable directory. Then anyone who went to that
                  directory and typed `ls` or `cat` would unknowingly invoke
                  the attacker's program!

### The Linux filesystem
Many of the examples so far have revolved around files and directories: the
shell prompt shows your working directory, `ls` lists files in a directory, the
shell runs programs stored in files, and so on. You're most likely already
familiar with the basics of files and directories: files hold data and can be
arbitrarily nested within directories, which hold files. But there are some
POSIX- and Linux-specific details about how files work that you might not know
about.

On POSIX operating systems, all files live somewhere within a special directory
called the root directory. The root directory is referred to by a single slash.
(This is in contrast to an operating system like Windows, where multiple
directory trees exist with names like `C:\` and `D:\`.) When you run `pwd`, you
see where your working directory lives under the root directory:

```
$ pwd
/h/utln01
$
```

The path `/h/utln01` refers to a directory called `utln01`, inside a directory
called `h`, inside the root directory `/`. This style of path--relative to the
root--is called an *absolute path* and always starts with a slash. The other
type of path you'll encounter is called a *relative path* and never starts with
a slash. Relative paths are interpreted relative to your working directory and
so can mean different things at different times:

```
~ $ cd /
/ $ ls /comp/50ISDT/examples/file-zoo
directory1  file1  file1-link  file2  file3  missing-link
/ $ ls comp/50ISDT/examples/file-zoo
directory1  file1  file1-link  file2  file3  missing-link
/ $ cd comp
/comp $ ls /comp/50ISDT/examples/file-zoo
directory1  file1  file1-link  file2  file3  missing-link
/comp $ ls comp/50ISDT/examples/file-zoo
ls: cannot access  comp/50ISDT/examples/file-zoo: No such file or directory
/comp $ ls 50ISDT/examples/file-zoo
directory1  file1  file1-link  file2  file3  missing-link
/comp $
```

In this example, we've added the working directory to the prompt to make each
command's working directory clearer. We start in our home directory `~` and
immediately move to the root with `cd /`. While in the root, an absolute path
refers to the exact same place as a relative path with the same components. But
as soon as we switch into a subdirectory (`h` in this case), that's no longer
the case: `ls h/utln01` is now equivalent to `ls /h/h/utln01`, which refers to
a directory that doesn't exist.

In addition to `/`, there are some other special directory names you should
know about. Every directory has a hidden subdirectory named `..`, which refers
to its parent directory, as well as one named `.`, which refers to
itself[^why-self]. These are most often useful in relative paths, for example
`../../somedir`, but are also perfectly legal to use in absolute paths:
`/h/utln01` is the same as `/h/../h/utln01`.

Finally, we mentioned the home directory shorthand `~` earlier in the lecture.
Although this behaves similarly to the special directories mentioned above
(`~/file1`, for example, means `file1` inside your home directory), it's
actually implemented very differently. While `/` and `..` and `.` are
implemented by the Linux kernel and work as part of any path, `~` is
implemented by the shell and so only works when you're running a shell command.
It won't work, for example, from an `fopen()` call in C. To see this for
yourself, you can put some of these special directory names inside single
quotes when passing them to shell commands. As you'll see next lecture, quotes
(both single and double) suppress some of the shell's processing, including `~`
expansion:

```
$ ls '/comp/50ISDT/examples/file-zoo'
directory1  file1  file1-link  file2  file3  missing-link
$ ls '/comp/50ISDT/examples/file-zoo/directory1/..'
directory1  file1  file1-link  file2  file3  missing-link
$ ls '~'
ls: cannot access ~: No such file or directory
$ 
```

[^why-self]: You may wonder why `.` needs to exist at all, since adding or
             removing it from any path doesn't change that path at all. One
             reason is to get around the shell's special treatment of command
             names without slashes: if you really do want to run a program in
             your current directory, prefixing its name with `./` is an easy
             way to do that. Another reason is because some programs assign
             special meaning to the empty string (for example, as an indicator
             that you want them to use a default value). To explicitly signal
             to these programs that you're talking about the current directory,
             you can use `.` as a path.
