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
    you write a program, even if you don't realize it. To be sure, there are
    IDEs that let you program without ever seeing a command line; on Windows
    and macOS, such environments (in the form of Visual Studio and Xcode) are
    in fact the sanctioned way to develop native applications!  Behind the
    scenes, however, both of these tools invoke command-line tools in order to
    compile your code, run tests, process resource files, sign and package your
    application for distribution, and so on. Knowing how to find and run these
    commands directly will help you figure out what's happening when things go
    wrong and will give you the freedom to go beyond the IDEs in cases where
    they can't do exactly what you need.

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
follow it. [Part of POSIX][posix-scl] defines what syntax and commands a shell
needs to support. Most of the shell features we cover in this course are part
of POSIX, meaning they won't apply just to Bash but to any POSIX shell you
encounter--for example, *zsh*, which is macOS's default shell and a popular
alternative to Bash on Linux.

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
any effect when you run it. You can run `echo $0` (which will make more sense
after lecture 4) to check which shell you're using. If you don't switch to
Bash, tcsh will interpret your commands, meaning much of the more advanced
syntax we cover will result in error messages or unexpected behavior.

[posix-scl]: https://pubs.opengroup.org/onlinepubs/9699919799.2018edition/utilities/V3_chap02.html

[^linux-posix]: The majority of Linux distributions are not actually
    POSIX-certified, but nevertheless are generally accepted to be POSIX
    compliant in all the ways that matter. macOS, on the other hand, is
    officially certified since version 10.5.

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
    Linux, Arch Linux, or Gentoo. The Tufts homework servers run Red Hat.

[^other-userspaces]: It's possible to run the Linux kernel with no GNU project
    code at all: [BusyBox](https://busybox.net/), for example, implements most
    POSIX tools (including a shell!) in a single tiny program that can fit on
    even the most space-constrained systems; Android uses the Linux kernel
    combined with its own BusyBox-inspired implementation of POSIX tools and a
    custom Java runtime; [FreeBSD](https://www.freebsd.org) and other UNIX
    derivatives have their own sets of POSIX tools, many of which are easily
    ported to run on Linux (and which are also the basis for macOS's tools).

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
    and operating systems, in this course we will simply use `$ ` to indicate a
    shell prompt unless we have a good reason otherwise. To learn more, look up
    the `PS1` and `PS2` shell variables.

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
this course's directory, `/comp/50ISDT/`, on the Tufts homework server. Type
`ls /comp/50` (without pressing <kbd>Enter</kbd>) and then press the
<kbd>Tab</kbd> key to trigger tab completion. If you did it right, nothing will
happen immediately. This is because there are lots of different CS 50s on the
server and Bash doesn't know which one you want, which it signals by ignoring
your first press of <kbd>Tab</kbd>. However, if you press <kbd>Tab</kbd> again,
Bash will show you a list of every option it knows about[^no-ls]:

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
    printing a new prompt is known as a *read-eval-print loop*, or a *REPL* for
    short. Some programming languages also have REPLs--modes where you can
    enter one statement at a time instead of running a whole file at once.
    REPLs are common for interpreted languages like Python and Ruby and much
    less common for compiled languages like C and C++.

[^path-security]: This behavior is not only convenient but also improves
    security. If the shell looked in the working directory first for every
    command, an attacker could write a malicious program named `ls`, `cat` or
    similar and place it in a publicly-readable directory. Then anyone who went
    to that directory and typed `ls` or `cat` would unknowingly invoke the
    attacker's program!

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

The path `/h/utln01/`[^trailing-slash] refers to a directory called `utln01`, inside a directory
called `h`, inside the root directory `/`. This style of path--relative to the
root--is called an *absolute path* and always starts with a slash. The other
type of path you'll encounter is called a *relative path* and never starts with
a slash. Relative paths are interpreted relative to your working directory and
so can mean different things at different times:

```
~ $ cd /
/ $ ls /comp/50ISDT/examples/file-zoo/
directory1  file1  file1-link  file2  file3  missing-link
/ $ ls comp/50ISDT/examples/file-zoo/
directory1  file1  file1-link  file2  file3  missing-link
/ $ cd comp
/comp $ ls /comp/50ISDT/examples/file-zoo/
directory1  file1  file1-link  file2  file3  missing-link
/comp $ ls comp/50ISDT/examples/file-zoo/
ls: cannot access  comp/50ISDT/examples/file-zoo: No such file or directory
/comp $ ls 50ISDT/examples/file-zoo/
directory1  file1  file1-link  file2  file3  missing-link
/comp $ 
```

In this example, we've added the working directory to the prompt to make each
command's working directory clearer. We start in our home directory `~` and
immediately move to the root with `cd /`. While in the root, an absolute path
refers to the exact same place as a relative path with the same components. But
as soon as we switch into a subdirectory (`h` in this case), that's no longer
the case: `ls h/utln01/` is now equivalent to `ls /h/h/utln01/`, which refers
to a directory that doesn't exist.

In addition to `/`, there are some other special directory names you should
know about. Every directory has a hidden subdirectory named `..`, which refers
to its parent directory, as well as one named `.`, which refers to
itself[^why-self]. These are most often useful in relative paths, for example
`../../somedir/`, but are also perfectly legal to use in absolute paths:
`/h/utln01/` is the same as `/h/../h/utln01/`.

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

[^trailing-slash]: A trailing slash is optional for paths that refer to a
    directory and forbidden for paths that refer to a file. For most purposes,
    the slash makes no difference to how a path gets treated.  (One exception
    to this is when the final entry in the path is a symbolic link to a
    directory; we'll introduce symbolic links later.) Our convention in these
    notes is to always include a trailing slash in directory paths to make it
    easier to distinguish them from file paths.

[^why-self]: You may wonder why `.` needs to exist at all, since adding or
    removing it from any path doesn't change that path at all. One reason is to
    get around the shell's special treatment of command names without slashes:
    if you really do want to run a program in your current directory, prefixing
    its name with `./` is an easy way to do that. Another reason is because
    some programs assign special meaning to the empty string (for example, as
    an indicator that you want them to use a default value). To explicitly
    signal to these programs that you're talking about the current directory,
    you can use `.` as a path.

## Lecture 2

### Quoting
We mentioned at the end of last lecture that the shell's expansion of the
special home directory shorthand `~` can be suppressed by putting the `~`
inside single quotes. This isn't the only piece of processing that quotes
prevent: many shell features are triggered by command names or arguments that
include special characters. Often you'll want those characters to be taken
literally instead, though--especially if you don't even know that the feature
in question exists! This is where quotes come in.

Any piece of a Bash command that's enclosed in single quotes will be preserved
exactly as typed when the command gets processed, except that Bash will remove
the quotes themselves. Notably, the quotes don't have to be around an entire
command name or argument: you can type a single word that consists of both
quoted and unquoted bits. A useful command for seeing how the shell processes a
word is `echo`. `echo` prints out all the argument values it receives separated
by spaces, so it lets you clearly see which arguments the shell has
proprocessed or expanded:

```
$ echo ~
/h/utln01
$ echo '~'
~
$ echo ~/foobar
/h/utln01/foobar
$ echo '~/foobar'
~/foobar
$ echo '~'/foobar
~/foobar
$ echo '~/fo'obar
~/foobar
$ 
```

Quotes can be used anywhere in a command, even in its name:

```
$ echo 'Hello, world!'
Hello, world!
$ 'ec'ho 'Hello, world!'
Hello, world!
$ 
```

And `~` is far from the only character that would otherwise have special
meaning. POSIX [specifies][posix-scl] the full set of characters that the shell
cares about to be `|`, `&`, `;`, `<`, `>`, `(`, `)`, `$`, `` ` ``, `\`, `"`, `'`,
`*`, `?`, `[`, `#`, `~`, `=`, `%`, space, tab, and newline. Bash also treats
`!` specially[^history-event-number]. We'll talk about what many of these
characters mean to the shell next lecture, but for now just be aware that if
you include them in a command unquoted, that command may not behave as
expected.

[^history-event-number]: This is related to the history event number we
    mentioned last time.

One notable thing about this list of characters is that it includes the single
and double quote characters themselves. And that makes sense, since we've just
seen that the shell treats quoted strings specially. But what if you want to
pass a literal single or double quote to a command? Since single-quoted strings
undergo no processing at all, there's no way to include a single quote inside
one of them; the shell will interpret any it finds to be the ending quote.

Luckily, there are ways to get around this. The shell has two other common ways
to prevent processing of one or more characters. The first is to precede any
character by a backslash `\\`. The backslash causes the character immediately
following it to be treated as if you'd enclosed it in single quotes. This is
known as *escaping* that character. Since the backslash needs no closing
delimiter, it can escape `'` (`\'`) and even itself (`\\`)!

```
$ echo \'
'
$ echo can\'t
can't
$ echo \\
\
$ echo \a\b\c\d
abcd
$ echo \~
~
$ 
```

The second way is to enclose the characters in double quotes. Double quotes
behave similarly to single quotes, except that certain special processing is
still allowed. One such piece of processing is the backslash escape (meaning
you can use a backslash to include double quotes inside a double quoted
string). (We'll go over the other pieces when we discuss variable and command
substitution in a later lecture.)

```
$ echo "can't"
can't
$ echo "The last command printed \"can't\""
The last command printed "can't"
$ 
```

One of the most common uses of quotes is to include spaces, tabs, or newlines
in an argument value. The shell typically treats whitespace as a separator
between arguments, and quotes/backslashes suppress this behavior. In the `echo`
examples so far, we haven't really cared whether we're passing a single
argument containing multiple words or multiple arguments each containing one,
since `echo` joins all its arguments with spaces before printing them anyway.
But the distinction is much more important when we're trying to specify
something like a filename.

To illustrate, let's look at an example directory on the homework server with a
file named `hello` (containing "1"), one named `world` (containing "2"), and
one named `hello world` (containing "3"). When viewing these files using the
`cat` command (which prints the contents of one or more files), quotes make a
big difference:

```
$ cd /comp/50ISDT/examples/file-zoo/directory1/
$ ls
hello  hello world  world
$ cat hello world
1
2
$ cat "hello world"
3
$ 
```

### Argument parsing and flags
Besides the shell's preprocessing we've just discussed, there's no one set of
rules about how arguments work: every program decides how to process its own
arguments. However, there are some common conventions for arguments that the
vast majority of commands follow. Knowing these conventions, which we discuss
here, will help you interpret help text and man pages for many tools.

*As an aside:* There's a family of C library functions called getopt (`man 3
getopt`) that many software packages use to parse arguments, which has
solidified these conventions somewhat. Similar libraries, inspired by getopt,
exist in other languages. For example, [Python's
argparse](https://docs.python.org/3/library/argparse.html) and [Rust's
clap](https://clap.rs/).

Part of these conventions are the notion of *flags*. Flags are optional
arguments that, when provided, alter the behavior of a piece of software. Some
flags operate alone and indicate that a program should (or shouldn't) behave in
a certain way. For example, `ls`'s `-l` flag indicates that `ls` should use its
long listing format. Certain flags require an argument (to the flag!); for
example, in `gcc -o filename`, `filename` indicates to `-o` where the output
file should go.

Because command-line users usually value brevity, flags are often written as
just a single (sometimes cryptic) letter or number. Flags like these are by
convention prefixed with a single dash (`-`) and can often be coalesced
together behind that dash if you want to specify multiple. For example, a pair
of flags `-l -v` could also be written as `-lv`. Note that short-form flags
that take arguments cannot be followed by other short-form flags in this way:
consider, for example, that `gcc -ohello` means `-o hello` and not `-o -h -e -l
-l -o`.

Many programs augment these short-form, single-letter flags with corresponding
long-form versions that consist of whole words and are more descriptive.
Long-form flags are typically prefixed with `--` and cannot be coalesced.

To illustrate, let's look at a sample program, `wc`. `wc`, which stands for
"word count", counts the number of words in its input file. Running `wc myfile`
prints the number of words in `myfile`. But the authors also taught `wc` to
count other things, and they exposed that functionality using flags. `wc -c`,
for example, will count characters, while `wc -l` will count lines. `wc -w` is
another way to ask for the default behavior of counting words. The authors also
added long-form variants--`--bytes`, `--lines`, and `--words`, respectively. In
general, short-form flags are handy at the command line, but long-form ones are
better for shell scripts (which we'll talk about later) and documentation
because they better convey meaning.

Although each program parses its own flags, many different programs recognize
`--version`/`-v` and `--help`/`-h`. Because the command-line ecosystem is
written by thousands of people, and everyone writes software differently, not
all programs adhere to this convention. Some use `-v` to mean `--verbose`, or
use `-version` (one hyphen!) as the long form, or something else entirely. As
usual, your best bet is to look at the manual pages.

Let's learn about some common commands to both apply our new knowledge of
argument parsing and get acquainted with useful CLI tools.

### Common commands
You'll find yourself using some tools more frequently than others. Here is a
shortlist of tools you will likely use often, alongside their descriptions, and
some common invocations. Refer to their man pages for more information.

Many of these commands can read input from a file whose name is given as an
argument, and that's what we'll focus on in this section. However, those same
commands can also read input directly from what you type into the terminal
(also known as `stdin`). If you ever forget to give a command a filename and it
appears to hang forever, it's probably waiting for you to type something. You
can get back to the prompt by pressing <kbd>Ctrl-c</kbd>. We'll talk about more
powerful ways to make use of this mode later in this module.

#### `ls`
Although many of our examples have already used `ls`, they've thus far shown
only its default behavior, which is to print the name of each file in the
directory it's passed (or the working directory if run with no arguments). `ls`
has quite a few flags which alter this behavior, though.

The most common flag you're likely to see is `-l` (which stands for "long
listing" and has no long-form version). This flag causes `ls` to list not only
the name of each file but also its type, link count, permissions, owner, group,
size, and last modification date. Files are printed one per line in this mode
to make room for the extra information:

```
$ ls -l
drwxrwsr-x. 2 thebb01 ta50isdt 4096 Sep  8 00:41 directory1
-rw-rw-r--. 1 thebb01 ta50isdt   11 Sep  8 00:16 file1
lrwxrwxrwx. 1 thebb01 ta50isdt    5 Sep  8 00:10 file1-link -> file1
-rw-rw-r--. 1 thebb01 ta50isdt   13 Sep  8 00:17 file2
-rw-rw----. 1 thebb01 ta50isdt   20 Sep  8 00:24 file3
lrwxrwxrwx. 1 thebb01 ta50isdt    6 Sep  8 00:11 missing-link -> foobar
$ 
```

Some of these fields are of little use and so we'll skip discussing them, and
others are complex enough that we'll discuss them separately later on. The main
things to notice at for the moment are the following:

 * The first character of each line indicates the file's *type*. `-` indicates
   a regular file; `d` indicates a directory; `l` indicates a symbolic link
   (see `ln` below). There are other file types, but these three are the ones
   you'll encounter most.
 * The fifth field of each line shows the file's size in bytes. For
   directories, this will usually be 4096, which is the size of the data
   structure that Linux internally uses to represent directories. (For
   directories with many files, it's sometimes a higher multiple of 4096
   instead.)
 * The sixth field of each line shows the date and time the file was last
   modified. For directories, this changes only when files are added or
   removed. Linux allows modification dates to be changed arbitrarily (see `man
   touch`), so don't rely on this as a guarantee the file hasn't been altered!
 * The seventh field of each line is the name of the file, but for symbolic
   links it additionally includes the name of the file the link points to after
   ` -> `.

Another common flag of `ls` is `--all`/`-a`, which causes it to show files
whose names begin with a `.`. Although such files have no special meaning to
Linux, `ls` hides them by default. This behavior [started out as a
bug](https://superuser.com/a/1293202) ([archive
link](http://web.archive.org/web/20190211031031/https://plus.google.com/+RobPikeTheHuman/posts/R58WgWwN9jp))
but became a feature when people realized it could be used to hide things like
configuration files that you don't normally care about.

#### `mv`
Rename a file, or move it elsewhere in the filesystem with `mv source
destination`. Overwrites the destination by default; be careful! If source and
destination both exist and are different types, `mv` will complain. If the
destination exists and is a directory, `mv` will instead put the source inside
the destination directory.

#### `cp`
Copy a file or copy multiple files into a directory. Overwrites the destination
by default; be careful! `cp` will not copy directories without
`--recursive`/`-r`.

#### `mkdir`
Make a directory with the name specified, like `mkdir foo`. If you want to make
nested directories in one command or avoid an error if the directory already
exists, use `--parents`/`-p`.

#### `rm`
Remove one or more files. Be careful! This deletion is irreversible. Specify
the filenames to be deleted in a list: `rm file1 file2 file3` and so on. To
remove directory contents recursively, use `--recursive`/`-r`. To avoid error
messages when files and directories don't exist, use `--force`/`-f`.

#### `cat`
Join files together and print to stdout. This is useful when sticking two files
end-to-end (e.g. `cat fileA fileB` will print first `fileA` then `fileB` to
stdout) or just showing the contents of one file.

#### `grep`
While programming it is often useful to find where a word, phrase, or regular
expression occurs in a file or folder. `grep` can do all of that.

`grep -r "functionName" projectFolder/` looks for the string "functionName"
recursively (the `-r`) in all of the files in `projectFolder/`. It will print
the matching lines in the format `filename:line`.

If you want to see what line number a match is found, you can use the `-n`
flag. This will add filenames so the format becomes `filename:linenumber:line`.
If you want to see some context around this line, you can also pass `-A NUM`
(shows NUM lines of trailing context), `-B NUM` (shows NUM lines of leading
context), or `-C NUM` (shows NUM lines before and after).

You may want to eventually search for *patterns* of text instead of just small
strings. Imagine you want to find all calls to the function "myfunction". You
could search `grep "myfunction(.*)"`, which would look for a call to
"myfunction" with any number of characters between parentheses. This is called
a regular expression search.

<!-- TODO: Link to more info on regexes -->

Sometimes you might want to find all the lines that do *not* contain a pattern,
because the pattern is very frequent. In this case you can do `grep -v
"pattern" file`, where `-v` stands for "invert".

#### `find`
Searching files by their contents is all well and good but it's also useful to
search for files by their attributes. To find a file by name, you can run `find
myfolder -name filename`. The filename can also be a pattern with `find`'s
limited pattern support. For example, you can find files whose names end in
"ed" by running `find -name "*ed"`. `find` supports many other predicates--you
should read the man page to get some ideas.

`find` also supports a limited number of operations on the files it finds, such
as `-delete`. In the event that you want to delete the files matching your
search, you can add `-delete` to your find command. For more complicated
actions, the `xargs` program can help you run a command for every file found.

You may have noticed that `find` does not follow the expected short/long flag
convention, with single and double hyphens, respectively. The simplest, and
somewhat dissatisfying answer, is that the authors of `find` hand-wrote their
own argument parser instead of using the more standard `getopt` library. The
course staff is not sure what sequence of events led to them writing their own
parser.

#### `sed`
To replace text and text patterns in files and streams, use `sed`. For example,
to replace the word "hello" with "goodbye" in a file `original.txt`, use `sed
's/hello/goodbye/' original.txt`. This will print the output to `stdout`. To
replace it in-place, use the `-i` flag. *Note: doing `sed COMMAND original.txt >original.txt`
will **not** work because the `>` causes the shell to overwrite your file
before `sed` even runs.* We will talk more about this when we get to our
section on pipelines.

Although the above usage is probably the majority of use, `sed` supports some
regular expressions and other commands (other than `s`). Take a look at the
COMMAND SYNOPSIS section of the `sed` manual pages for more information.

#### `cut`
If the input data is separated logically into columns, it's possible to use
`cut` to only print the selected columns. The data need not be space separated;
it's possible to specify a delimiter.

For example, to print column 2 of a file with comma separated columns, use `cut
-f2 -d',' myfile`. It's also possible to specify ranges of columns. Read the
man pages for more information.

#### `sort`
To sort a file or stream's lines, use `sort`. The default behavior is to sort
lexicographically--in alphabetical order--so it will not sort numbers as you
expect. For that, you want `sort --numeric-sort`, or `sort -n`. It also can
reverse the sorting order with `--reverse`/`-r`.

Depending on your system's implementation, there may be some other fun options,
such as a stable sort, a merge of two already sorted lists (to be used in merge
sort), or even sorting in parallel.

#### `head`
To keep only the first part of a file or stream, use `head`. It is useful for
examining only the first line of a file, or the first ten lines, or any number
of lines (`--lines=NUM`, `-nNUM`), really.

#### `tail`
The opposite of `head`! To keep only the last part of a file or stream, use
`tail`. It also takes `--lines`/`-n`, but has additional features, too: if the
file is growing, or there is more information coming in the stream, you can use
`--follow`/`-f` to make `tail` continually print output.

Software engineers often use `tail -f` to observe a continually growing log
file, maybe of a server, or a build process.

#### `man`
To help you make better use of your tools, package maintainers write manual
pages for their software. To read a manual page for a particular piece of
software, use `man PROGRAM`, like `man ls`. Some software is available in two
forms: for example, `printf` is both a program in GNU coreutils and a C
standard library function. Since the manual pages are separated into sections,
you can refer to them separately: `man 1 printf` for the coreutils command and
`man 3 printf` for the stdlib function. To read more about sections, check out
`man man`.

Manual pages are available in a centralized place (like `/usr/share/man`) for
package managers and install scripts to write to and you to read from.

#### `ln`
Create a *symbolic link* to a file, when used with the `--symbolic`/`-s` flag.
The syntax is the same as `cp`--`ln source destination`--but instead of copying
a file, it creates a special kind of file at the destination that forwards all
accesses to the source. Symbolic links can be created to both files and
directories, and you can generally treat the link just as you would the
original file when using it in commands. `ln` with no flags creates *hard
links*, which are a different and lesser-used type of link that we won't
discuss in this course.

#### `diff`
Sometimes you have two files and you don't know if they are different. Or
perhaps you know that they are different and you don't know what is different
about them. The `diff` command will print out a list of differences between two
files (or directories) in a regular format:

```
LINEcCOL
< LEFT-FILE-LINE
---
> RIGHT-FILE-LINE
```

It also changes status code depending on the result: 0 if the same, 1 if
different. This can be useful in shell scripts, so you can do things like `diff
fileA fileB || echo "different"` or `diff fileA fileB && echo "same"`. We will
have more about this coming up in our section on pipelines.

#### `which`
`which` helps find commands. If the command exists as a binary, it will tell
the path. To find all the matching binaries, use `-a`.

While some shells have `which` as a shell built-in, so it can report other
shell built-ins, Bash uses the system `which` binary instead. Therefore, it is
unable to report on other built-ins and aliases.

See also the POSIX utility `type`.

#### `top` and `htop`
`top` and `htop` are interactive commands. Instead of running in a
pipeline--consuming input from stdin and printing to stdout--they are meant to
be used directly by the user. `top` prints live statistics about running
programs, and is helpful for getting an overview of the pressures on your
system--memory, CPU, etc. `htop` is a colorful variant with some more
information about individual CPU cores and graphs.

These tools read from `/proc`, which is a virtual filesystem with information
about processes pretending to be files.

#### `tmux`
`tmux` is another interactive program. It stands for "terminal multiplexer",
which is a fancy way of saying that it allows you to run multiple programs in
the same terminal--kind of like in The Matrix. It is very useful for systems
administrators to see live updating commands like `top`, some kind of live log,
and maybe also have an editor running, all at once.

It also allows you to detach and reattach to the session you started, so you
can persist your work across logins to the homework server. Note that it does
not survive system restarts.

The keybindings are customizable, so read the manual pages for the default
bindings.

See also the `screen` command, which is similar.

<!-- TODO: Talk about `less` -->
<!-- TODO: talk about `uniq` -->

#### `vi`
`vi` is a POSIX-specified text editor that is available on almost every system
you will use. Unlike text editors such as Notepad and Kate, Vi is a *modal*
editor, meaning that when it is open it is in one of several modes: INSERT,
NORMAL, etc. The default mode is NORMAL mode, which means that opening it and
trying to directly start typing will not work. To enter INSERT mode, type
<kbd>i</kbd>, and to go back to NORMAL mode, type <kbd>Esc</kbd>. To quit Vi,
type <kbd>:</kbd><kbd>q</kbd> in NORMAL mode.

Most newer systems include Vim (Vi-iMproved), instead of plain Vi. Check out
this [getting started guide](https://learnxinyminutes.com/docs/vim/) to read
more. We won't get too deep into text editing in this course.

### File ownership and permissions
Nearly every command we've just shown you manipulates files in some way: some
read files, some create, delete or move them, and a few (like `sed` and `vi`)
can write to them as well. So what's stopping you from using these commands to
alter another user's personal files in their home directory? Or to read a
confidential system file[^fhs] such as `/etc/shadow`, which holds the hashed
passwords of users on most Linux systems[^etc-shadow]? Let's see what happens
when we try!

```
$ cat /etc/shadow
cat: /etc/shadow: Permission denied
$ 
```

Unlike other files we've seen (e.g. `/comp/50ISDT/examples/file-zoo/file1`),
`/etc/shadow` can't be read by `cat`. To understand why, you need to understand
the concept of file *permissions*. Let's take another look at some bits of `ls
-l` that we glossed over earlier:

```
$ ls -l /comp/50ISDT/examples/file-zoo/file1 /etc/shadow
-rw-rw-r--. 1 thebb01 ta50isdt   11 Sep  8 00:16 /comp/50ISDT/examples/file-zoo/file1
----------. 1 root    root     1195 Dec 20  2019 /etc/shadow
$ 
```

You know that the first character in each line indicates the file's type, but
what about the rest of that field (`rw-rw-r--.` and `---------.`,
respectively)? These characters encode the file's permissions, which control
who is allowed to access it and in what ways. The first nine of these
characters encode nine individual *permission bits*. When all nine bits are
set, `ls` will show "rwxrwxrwx."[^extra-mode-bits]. If one or more bits are
unset, the corresponding characters are replaced with a dash, as in
`rw-rw-r--.`.

So what do these nine bits actually control? As the characters imply, the nine
bits are split into three groups, each group having a *read* permission (`r`),
a *write* permission (`w`), and an *execute/traverse* permission (`x`). The
first of the three groups specifies what the file's *owner* is allowed to do.
The second specifies what members of the file's *group* are allowed to do. And
the third specifies what everyone else is allowed to do.

That's a lot of information, so dig into it bit by bit. Let's first talk about
owners and groups. Every file in Linux has as its owner exactly one user on the
system. New files are owned by whoever runs the program that creates them
(except in the case of setuid--see the footnote above). A file's owner can't be
changed once it's been set, not even by that owner (with one exception,
described below). `ls -l` shows a file's owner in the third field: the files in
our example are owned by thebb01 and root, respectively. If you own a file, the
first group of `rwx` bits tells you how you can access it.

Every file on Linux also belongs to exactly one group. Groups are named, just
like users, and every user is a member of one or more groups. (You can run
`groups` to see which groups you're in.) `ls -l` shows a file's group in the
fourth field. In our example, the files belong to the ta50isdt and root groups,
respectively. (The group named root is distinct from the user named root.) If
you are a member of a file's group, the second group of `rwx` bits tells you
how you can access it.

Finally, if you are neither a file's owner or in its group, the final group of
`rwx` bits tells you how you can access it.

Let's next talk about the bits themselves. If the group of bits your user is
subject to has an `r`, it means you can read the file in question (and for
directories, list their contents). If it has a `w`, it means you can write to
that file (and for directories, add, remove, and rename the contents). If it
has an `x` and is for a regular file, it means you can execute that file as a
program. If it has an `x` and is for a directory, it means you can access files
within that directory (a.k.a. *traverse* the directory). In the case where you
can traverse but not read a directory, you aren't allowed to list its contents,
so you must already know the name of the file you want to access.

The final character in the mode string, if present, indicates that the file is
subject to extra access checks beyond the user/group/owner permissions just
described. A `.` indicates that a Linux-specific framework called
[SELinux](http://www.selinuxproject.org/page/Main_Page), which lets the system
administrator set access rules on files that even their owner can't change, is
in use. A `+` usually indicates the presence of an *access control list* (ACL),
a more granular but infrequently-used way of specifying permissions. We won't
cover ACLs or SELinux in this course, but you can read `man acl`, `man
getfacl`, and `man setfacl`, and `man selinux` to learn about them on your own.

We can now go back to our original listing (reproduced below) and make sense of
it:

```
$ ls -l /comp/50ISDT/examples/file-zoo/file1 /etc/shadow
-rw-rw-r--. 1 thebb01 ta50isdt   11 Sep  8 00:16 /comp/50ISDT/examples/file-zoo/file1
----------. 1 root    root     1195 Dec 20  2019 /etc/shadow
$ 
```

We can see that, for `/comp/50ISDT/examples/file-zoo/file1`, its owner
(thebb01) is allowed to read and write but not execute, members of its group
(ta50isdt) are allowed to do the same, and everyone else can read but not write
or execute. But for `/etc/shadow`, no one is allowed to do anything! Not even
its owner (root) can read or write to it.

This latter setup isn't quite as perplexing as it sounds for two reasons:
firstly, a file's owner is always allowed to change that file's permissions
(see `man chmod` for how). So if root wanted to read or write `/etc/shadow`, it
could first grant itself permissions, then perform the operation, then take the
permissions away again.

However, it turns out that not even this is necessary, and that's because the
user root is special. Also known as the *superuser*, root on Linux is a user
account with ultimate administrative privileges. One of the privileges unique
to root[^capabilities] is that any file access by root bypasses all permission
checks: root can read or write any file on the system without having to change
its permissions first. root is also the only user that can change the ownership
of an existing file.

Because of all these extra powers, it's incredibly easy to accidentally make a
system unusable (for example, by deleting core system files) when operating as
root. As such, most system administrators generally use a standard user account
and use the `sudo` and `su` commands to run individual commands as root when
needed. Note that the root *account* has no special relation to the root
*directory* you learned about last lecture.

[^fhs]: The location of system files is no secret: directories like
    `/usr/bin/`, and `/etc/` will exist on nearly every Linux system you'll
    encounter and will contain many of the same files. These common paths are,
    like POSIX, a historical artifact that was later standardized. The standard
    was named the [Filesystem Hierarchy Standard
    (FHS)](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html), and it
    defines the paths where different kinds of system artifacts should live.
    Most Linux distributions--and programs written for Linux--at least loosely
    respect FHS. (For a fun distro that doesn't, check out
    [NixOS](https://nixos.org/).)

[^etc-shadow]: See `man 5 shadow` and `man 5 passwd` for more information on
    these files specifically, and [OWASP's password storage cheat
    sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
    for a decent overview of password hashing in general.

[^extra-mode-bits]: Occasionally, you might see an `s`, `S`, `t`, or `T` in
    place of an `x`. These characters indicate special behavior of the file
    beyond its basic permissions. When an `s` replaces an `x` in the owner or
    group permissions, it means that, when the file is executed, the resulting
    program will run as its owner or group, respectively, rather than as those
    of the user who ran it. An `S` indicates the same thing but replaces a `-`.
    Look up the *setuid* and *setgid* bits for more information on how this is
    useful.

    When a `t` replaces an `x` or a `T` replaces a `-` in the other permissions
    for a directory, it means that files inside that directory can be moved or
    removed by their owner as well as by anyone with write permission for the
    directory. Normally, only the latter is true.

[^capabilities]: On Linux, the various special powers of the superuser can
    actually be granted and revoked more granularly using a system called
    *capabilities* (`man capabilities`), but it's generally still the case that
    programs run by root have every capability and others don't have any.

## Lecture 3
Last lecture, we talked about argument parsing and some common tools that
you'll likely encounter during your illustrious career in computing. This
lecture, we'll talk about some shell syntax that lets you combine these and
other tools together in powerful ways. We'll also introduce some more shell
features that make it easier to find, edit, and run commands.

For a fun bit of history, take a look at [this
video](https://www.youtube.com/watch?v=tc4ROCJYbm0), which depicts some of the
original authors of UNIX first introducing concepts we'll cover today.

### More ways to find previous commands
In our very first lecture, we showed you how you can use the up and down arrow
keys to cycle through past commands. Although that's probably the most
commonly-used history navigation shortcut, the shell has other features that
can make history navigation even more efficient.

The first of these features is *history search*. If you know a piece of a
command you want to rerun but can't quite remember when you last ran it, press
<kbd>Ctrl-r</kbd>. You will see your prompt replaced with a new
``(reverse-i-search)`':`` prompt. Within this prompt, you can type any snippet
of a command from your history, and Bash will find the most recent command
matching that snippet. To find older commands matching the same snippet, you
can keep pressing <kbd>Ctrl-r</kbd>.

Once you've found what you're looking for, you can either run it immediately by
pressing <kbd>Enter</kbd> or bring it into a normal prompt for editing by
pressing <kbd>Esc</kbd>, <kbd>Tab</kbd> or a left/right arrow key. If you can't
find what you're looking for and want to get back to a blank prompt, you can
always press <kbd>Ctrl-c</kbd>.

The next feature is *history expansion*. Just as Bash expands `~` to your home
directory, it also expands the special sequence `!!` to the last command you
ran. You can use this to rerun the last command verbatim (e.g. to repeatedly
compile a program) or to add something to the beginning or end of it (e.g. to
rerun the previous command as root with `sudo !!`).

History expansion isn't confined to the last command you ran. Remember the
history event number in the example shell prompt from Lecture 1?[^ps1] By
prefixing the history event number of a given command with a single `!`, you
can rerun that command. Here's an example:

```
vm-hw03{thebb01}1013: gcc -Wall -Werror -o hello hello.c
vm-hw03{thebb01}1014: ./hello
Hello wordl!
vm-hw03{thebb01}1015: vim hello.c  # fix the typo
vm-hw03{thebb01}1016: !1013
gcc -Wall -Werror -o hello hello.c
vm-hw03{thebb01}1017: !1014
./hello
Hello world!
vm-hw03{thebb01}1018: 
```

Note that Bash prints a line after each command with a history expansion, prior
to the command's output, showing what was actually run. This is for clarity and
also happens with `!!`.

[^ps1]: If the prompt on your local system doesn't have a history event number,
    you can add one by changing the `$PS1` shell variable. See the PROMPTING
    section of `man bash` for details.

### Variables in the shell
We now change focus from shell features that help you run simple commands at an
interactive prompt to ones that let you express complex relations and
interdependencies between commands. Although you can use these features
interactively, they really shine as part of shell scripts (which we'll cover
next lecture).

Let's start with *variables*. Any programming language needs a way to store
data, and the shell is no exception. Every running shell holds a set of
variables, which persist between commands but go away when the shell exits.
Each variable has a name made up of letters, numbers, and underscores. (By
tradition, variable names are all uppercase, but this isn't enforced anywhere.)
To create or change a variable, separate the name and desired value with an
equals sign (`=`). You must **not** put spaces around the `=`:

```
$ FOOBAR=somevalue
$ 
```

To read a variable, prefix its name with a dollar sign (`$`) and use it in a
command:

```
$ echo $FOOBAR
somevalue
$ 
```

The shell expands `$VARNAME` to the contents of VARNAME, just like it expands
`~` to your home directory. Variable names can be used inside double quotes but
not inside single quotes, and the `$` can be escaped with a backslash just like
any special character:

```
$ echo $FOOBAR
somevalue
$ echo "$FOOBAR"
somevalue
$ echo '$FOOBAR'
$FOOBAR
$ echo \$FOOBAR
$FOOBAR
$ 
```

Shell variables hold strings. The value you assign to a variable is substituted
textually when you use that variable in a command. As such, you can put
variable expansions nearly anywhere:

```
$ COMMAND=ls
$ DIRECTORY=/comp/50ISDT/examples/file-zoo/
$ "$COMMAND" "$DIRECTORY"
directory1  file1  file1-link  file2  file3  missing-link
$ 
```

Because of this direct textual expansion, **variable names should almost always
be used inside double quotes**. Consider what would happen if the variable
contained a string with spaces! Well, we're right back to our old
"hello"/"hello world"/"world" example from before:

```
$ cd /comp/50ISDT/examples/file-zoo/directory1/
$ FILENAME="hello world"
$ cat $FILENAME
1
2
$ cat "$FILENAME"
3
$
```

Sometimes, it can be ambiguous where a variable name ends and subsequent text
begins. In those situations, you can make it clear by enclosing the name in
curly braces:

```
$ "$COMMAND" -l "${DIRECTORY}file3"
-rw-rw----. 1 thebb01 ta50isdt 20 Sep  8 00:24 /comp/50ISDT/examples/file-zoo/file3
$ 
```

If you're done with a variable and want to get rid of it, you can use `unset`.
Note that it's not an error to access a variable that doesn't exist, although
next lecture we'll show you how to change that to make debugging scripts
easier:

```
$ unset FOOBAR
$ echo "$FOOBAR"

$ 
```

#### Environment variables
The variables we created in the preceding example exist only within the shell.
But Linux itself also has a concept of variables. These variables, called
*environment variables*, provide another way of passing data to programs. Like
arguments, environment variables can be read by programs and used to make
decisions. Unlike arguments, environment variables are passed implicitly: new
programs automatically inherit the environment of their parent unless the
parent explicitly decides otherwise. This makes the environment a good place to
hold system or user configurations that many programs care about.

To see the environment variables in your shell session (which will be inherited
by any command you run), run `env`:

```
$ env
HOSTNAME=vm-hw01
SHELL=/bin/bash
USER=thebb01
PATH=/h/thebb01/local/bin:/comp/105/bin:/comp/105/submit/bin:/usr/lib64/qt-3.3/bin:/usr/condabin:/usr/sup/bin:/usr/bin:/usr/sup/sbin:/usr/sbin:/h/thebb01/bin:/usr/cots/bin:/bin:/opt/puppetlabs/bin
PWD=/h/thebb01
EDITOR=vim
LANG=en_US.UTF-8
HOME=/h/thebb01
$ 
```

The homework server has a much bigger environment than this, but I've omitted
most of the variables so we can focus on these. Some of these variables hold
system information: HOSTNAME is the computer's name and LANG is the language
that programs should prefer. Others hold information about my user: USER and
HOME are my username and home directory; SHELL is the shell that I use by
default (but *not* necessarily the currently-running one); EDITOR is my
preferred text editor. PWD is my working directory and holds the same value
that `pwd` prints.

Notably, PATH is how the shell knows where to look for commands. Like we
mentioned in the first lecture, commands without a `/` in their name execute a
program with a matching name from one of several system directories; PATH holds
a `:`-separated list of those system directories. In the middle of my PATH, you
can see `/usr/bin/`, which is where `ls` and most of the other commands we've
used so far live.

It's no coincidence that `env` formats its output to look like shell variable
assignments. **Every environment variable is accessible as a shell variable**,
and you can read and modify them as such:

```
$ echo "I am $USER, my home is at $HOME, and this place is called $HOSTNAME"
I am thebb01, my home is at /h/thebb01, and this place is called vm-hw01
$ 
```

However, the reverse is not true: a shell variable is not part of the
environment automatically, but you can add it using `export` (and remove it
using `export -n`):

```
$ FOOBAR=somevalue
$ env | grep FOOBAR
$ export FOOBAR
$ env | grep FOOBAR
FOOBAR=somevalue
$ 
```

### Chaining commands together
Sometimes you'll find yourself with a problem that can't be exactly solved by
any one program. Luckily, the shell offers a number of powerful operators that
let you run multiple programs with a single command, connecting the inputs and
outputs of those programs in various ways. Before we get into the specifics of
these operators, let's talk about what inputs and outputs a program can have.

There are three ways the shell can send input to a program. We've already
discussed the first two, arguments and environment variables. The third is
*standard in* (a.k.a. *stdin*). stdin refers to text that a program reads while
it's running. For those who've written C++ programs, this is where `cin` gets
its data from. Many of the commands we've already shown, like `cat` and `grep`,
will default to reading from stdin if no filename is given as an argument.

There are also three ways a program can send output to the shell--*standard
out* (a.k.a. *stdout*), *standard error* (a.k.a. *stderr*), and its *exit
code*. stdout and stderr are both text streams that programs can write to while
they're running (`cout` and `cerr` in C++), and the contents of both are
printed to the terminal by default (but we'll see how that can change shortly).
stdout is used for normal output of a program, such as filenames located by
`find` or lines matched by `grep`. stderr is reserved for error and diagnostic
messages, such as those printed when a program doesn't have permission to
access a file. In the following example, `cat` prints `Hello, world` to stdout
and `cat: file3: Permission denied` to stderr:

```
$ cd /comp/50ISDT/examples/file-zoo/
$ cat file2 file3
Hello, world
cat: file3: Permission denied
$ 
```

The final way of producing output, the *exit code*, is a number that every
program returns when it exits. This number is traditionally used to report
whether the program succeeded, indicated by a value of zero, or failed in some
way, indicated by any nonzero value. (Individual programs assign their own
meanings to different failure values.) You don't see the exit code of commands
you run interactively, as the text they print is usually enough to tell whether
they succeeded or failed. However, the shell always keeps track of the last
command's exit code. You can view it through the special shell variable `$?`:

```
$ cd /comp/50ISDT/examples/file-zoo/
$ cat file2
Hello, world
$ echo $?
0
$ cat file3
cat: file3: Permission denied
$ echo $?
1
$ 
```

Here, `cat` returned a success code of zero when it completed normally but a
failure code of one when it couldn't read its input file. You can try out other
programs on your own to see what codes they return in different situations.

<!-- TODO: Move this section to the next lecture -->

#### `test`
There is a command, `test`, dedicated to producing error codes for use in
conditionals. It comes bundled with a bunch of different *predicates*. (A
predicate is a function that takes an input or multiple inputs and produces a
boolean result.) If the predicate returns true, the exit code is zero, and if
it returns false, the exit code is one. This is different from C, where true is
one, but matches the POSIX convention of returning zero on success.

To test if a string is the empty string `""`--if it has length zero--use `test
-z "$STRING"`.

```
$ test -z ""
$ echo $?
0
$ test -z "hello"
$ echo $?
1
$ 
```

To test if a string is not the empty string--if it has nonzero length--use
`test -n "$STRING"`:

```
$ test -n ""
$ echo $?
1
$ test -n "hello"
$ echo $?
0
$ 
```

`test` also provides a string equality predicate. To test if two strings are
equal, use `test "$LEFT" = "$RIGHT"`. Note that this uses *one* equals sign
instead of the two you may be used to. To check inequality, use `!=`:

```
$ test "hello" = "hello"
$ echo $?
0
$ test "hello" = "world"
$ echo $?
1
$ 
```

Even though variables are always strings, the text in those variables can
represent other types of data. To that end, `test` also provides predicates for
numbers and files. For numbers, use `-lt` for "less than", `-ge` for "greater
than or equal", and so on (see `help test` for a full listing):

```
$ test 5 -lt 7
$ echo $?
0
$ test 5 -lt 5
$ echo $?
1
$ 
```

To test if a file or directory exists, use `test -e "$FILENAME"`. To test if it
exists *and is a file*, use `test -f`. To test if it exists *and is a
directory*, use `test -d`.

#### Running programs sequentially
Now that we've seen how programs can communicate with the shell, we come to our
first few shell operators for combining multiple commands into a single, larger
command. The first of these operators is the semicolon (`;`). By separating two
commands with `;`, you tell the shell to run the first one followed by the
second, just as if you'd put them each on their own line. We can use this
operator to rewrite the last example more concisely:

```
$ cd /comp/50ISDT/examples/file-zoo/
$ cat file2 ; echo $?
Hello, world
0
$ cat file3 ; echo $?
cat: file3: Permission denied
1
$ 
```

As the third command demonstrates, each command in the chain will run
regardless of whether the one preceding it succeeded or not. This is sometimes
desirable, as in the case of printing an exit code. But sometimes a later
command depends on an earlier one, as in the case of making a directory and
then creating a file there. For situations like this, you can use the `&&`
operator, which runs the second command only if the first is successful (and
returns success only if both are). Here, the failure of the second `mkdir`
prevents `touch file2` from ever running:

```
$ mkdir dir1 && touch dir1/file1
$ echo $?
0
$ ls dir1
file1
$ mkdir dir1 && touch dir1/file2
mkdir: cannot create directory 'dir1': File exists
$ echo $?
1
$ ls dir1
file1
$ 
```

As you might expect, there's also a `||` operator, which runs the second
command only if the first fails and returns success if either succeeds. You can
chain as many commands you want together using any of these three operators,
and they'll be run left-to-right.

#### Pipelines
The next operator we'll discuss is one of the hallmarks of POSIX shells. It's
the foundation upon which the [UNIX
Philosophy](https://en.wikipedia.org/wiki/Unix_philosophy)--to write small
programs that do one thing well--is built. This operator is known as the
*pipe*, and it's denoted with a vertical bar (`|`).

When you separate two commands with `|`, the shell connects stdout of the first
command to stdin of the second, forming a *pipeline*. Pipelines can be
arbitrarily long, and they let you express complex data processing operations
in terms of the basic operations provided by individual programs.

To illustrate this, let's build a pipeline to find which header file in
`/usr/include/` has the most lines. (`/usr/include/` is the standard location
for system headers like `stdio.h`.) We'll start with a command to find all the
header files in the directory. We learned about `find` last lecture, so let's
use that:

```
$ find /usr/include/ -type f -name '*.h'
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf-xlib/gdk-pixbuf-xlib.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf-xlib/gdk-pixbuf-xlibrgb.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-loader.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-autocleanups.h
<lots more lines>
$ 
```

Here, we're looking for files in `/usr/include/` whose name ends in `.h`. As
you can see, there are lots of them. We're using `find` instead of `ls` because
`find` also looks in subdirectories.

The next thing we'll do is count the number of lines in each file. We know that
`wc` can count lines in a file, but there's a problem: `wc` as we've used it so
far wants filenames as arguments, but if we add it to our pipeline it will get
the list of files on stdin instead. As it happens, however, `wc` has an
alternate mode that does nearly what we need[^files-as-args]. From its man
page:

>     --files0-from=F
>            read input from the files specified by NUL-terminated names in
>            file F; If F is - then read names from standard input

[^files-as-args]: If you ever encounter a command that doesn't have such a mode
    and can only take filenames as arguments, worry not! There is a special
    tool called `xargs` (`man xargs`) designed specifically for using such
    tools in pipelines. In the case of piping from `find` specifically, you can
    also use `find`'s `-exec` flag (`man find`).

By passing `--files0-from=-`, we can have `wc -l` read a list of files to count
from standard in! "NUL-terminated" is a concept you'll see often when dealing
with pipelines containing filenames: POSIX tools typically operate on a
line-by-line basis, but this becomes problematic when working with filenames,
since filenames are allowed to contain newlines[^filename-chars]. To work
around this issue, many programs that read or write lists of files offer an
alternate mode where each entry is separated by the unprintable character `\0`,
which can't occur in filenames. As luck would have it, `find` offers such a
mode with its `-print0` flag.

[^filename-chars]: And a lot of other unexpected characters, unfortunately.
    Don't treat your filenames as nicely encoded strings; instead, treat them
    as byte arrays.

Adding this flag to our `find` invocation and piping into `wc` yields the
following:

```
$ find /usr/include/ -type f -name '*.h' -print0 | wc --files0-from=- -l
92 /usr/include/gdk-pixbuf-2.0/gdk-pixbuf-xlib/gdk-pixbuf-xlib.h
233 /usr/include/gdk-pixbuf-2.0/gdk-pixbuf-xlib/gdk-pixbuf-xlibrgb.h
119 /usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-loader.h
37 /usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-autocleanups.h
<lots more lines>
83 /usr/include/netrom/netrom.h
70 /usr/include/H5Object.h
4233248 total
$ 
```

We've made some progress! Now every filename is preceded by its line count.
(Note that this command may take a while to run, since `wc` has to read
thousands of files.)

Wait a minute, though--what's this `4233248 total` line? That's not a file
ending in `.h`! As it turns out, `wc` prints a total line count at the end of
its output, and there's no flag to disable it. Such an inconvenience is no
match for the power of pipelines though: we can use `head -n -1` (note: `-1`,
not `1`) to discard the last line of output from `wc`[^annoying-edge-case]:

```
$ find /usr/include/ -type f -name '*.h' -print0 | wc --files0-from=- -l | head -n -1
92 /usr/include/gdk-pixbuf-2.0/gdk-pixbuf-xlib/gdk-pixbuf-xlib.h
233 /usr/include/gdk-pixbuf-2.0/gdk-pixbuf-xlib/gdk-pixbuf-xlibrgb.h
119 /usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-loader.h
37 /usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-autocleanups.h
<lots more lines>
83 /usr/include/netrom/netrom.h
70 /usr/include/H5Object.h
$ 
```

[^annoying-edge-case]: Unfortunately, this has an annoying edge case. If `find`
    produces zero or one filenames to pass to `wc`, `wc` won't print the
    `total` line. And in the general case, we can't use `grep -v` to filter out
    lines that contain `total` either, since a file could be named `total`. In
    this case, however, we're exclusively looking for files that end in `.h`,
    so adding `grep -v 'total$'` to the pipeline would be a more robust
    solution.

But how do we pick the biggest one out of this list? We haven't learned about
any utility to do this directly, but we have learned about `sort`, which can
ensure that the biggest number is at one end of the list. Let's sort the list
such that the biggest number is on top:

```
$ find /usr/include/ -type f -name '*.h' -print0 | wc --files0-from=- -l | head -n -1 | sort -rn
4233248 total
40496 /usr/include/php/Zend/zend_vm_execute.h
20054 /usr/include/opencv2/ts/ts_gtest.h
19634 /usr/include/epoxy/gl_generated.h
19455 /usr/include/openblas/lapacke.h
<lots more lines>
$ 
```

Now we have the line we care about at the very top, and all we have to do is
get rid of all the other uninteresting lines. For that, let's again use `head`:

```
$ find /usr/include/ -type f -name '*.h' -print0 | wc --files0-from=- -l | head -n -1 | sort -rn | head -n 1
40496 /usr/include/php/Zend/zend_vm_execute.h
$ 
```

It would probably be fine to call the pipeline finished at this point, but if
we really want we can also get rid of the line count and leave just the
filename using `cut -d' ' -f2`. The `-d` stands for `--delimiter`, which in our
case is a space, and the `-f` stands for `--fields`, where we specify that we
only want field number 2. (The fields are 1-indexed.)

```
$ find /usr/include/ -type f -name '*.h' -print0 | wc --files0-from=- -l | head -n -1 | sort -rn | head -n 1 | cut -d' ' -f2
/usr/include/php/Zend/zend_vm_execute.h
$ 
```

And we're done! By combining six commands, we answered our question, and we now
have a pipeline skeleton that can be modified in minor ways to answer all sorts
of related questions, too. (What about the top 5 longest files? Top 10
shortest? And so on.) Hopefully, this example illustrated some of the
flexibility the pipe operator brings.

### Redirection
One limitation of pipelines is that they write their final output to the
terminal. In the case of our example above, that's fine because the output is
just one file. But what if we wanted to save a report of how many lines were in
each header file at a given time? On the homework server, `find /usr/include/
-type f -name '*.h' -print0 | wc --files0-from=- -l` outputs over 18,000 lines,
so manually retyping, or even copy/pasting, the output would not be fun.

The shell's *redirection* operators can help in situations like this. `>`, the
output redirection operator, saves stdout to a given file. Similarly, `<`, the
input redirection operator, copies a file's contents to stdin.

Let's split our pipeline from above into two commands using redirection:

```
$ find /usr/include/ -type f -name '*.h' -print0 | wc --files0-from=- -l >header-line-counts
$ ls
header-line-counts
$ cat header-line-counts
92 /usr/include/gdk-pixbuf-2.0/gdk-pixbuf-xlib/gdk-pixbuf-xlib.h
233 /usr/include/gdk-pixbuf-2.0/gdk-pixbuf-xlib/gdk-pixbuf-xlibrgb.h
119 /usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-loader.h
37 /usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-autocleanups.h
<lots more lines>
$ head -n -1 <header-line-counts | sort -rn | head -n 1 | cut -d' ' -f2
/usr/include/php/Zend/zend_vm_execute.h
$ 
```

The filename always goes after the redirection character, meaning the arrow
points in the direction data flows. For output redirection (`>file1`) , the
file gets written and so the arrow points towards it. For input redirection
(`<file1`), the file gets read and so the arrow points away from it.

Be careful with the filenames you specify for output redirection! If you
redirect into a file that  already exists, that file's contents will be
completely replaced with no warning! **Output files are overwritten before the
command runs, so a command like `sed 's/a/b/' file1 >file1` will empty your
file!** There is a variant of output redirection, `>>`, that appends to a file
that already exists instead of overwriting it.

You may have noticed that the last command in our example can be written
without input redirection at all, as `head -n -1 header-line-counts | sort -rn
| head -n 1 | cut -d' ' -f2`. This is indeed true, and it's why you'll see
output redirection used a lot more than input redirection: most tools can read
from a filename given as an argument, so input redirection is usually
unnecessary.

Output redirection, like pipelines, only redirects stdout by default. stderr is
still sent to the terminal so you can see errors and so that the output file
doesn't contain error messages that might confuse a later tool. If you have
reason to redirect stderr, you can do it with `2>`. (2 is the number POSIX
assigns to stderr; 1 is stdout, so `1>` is the same as `>`.)

### Job control
One thing common to every command you've seen so far is that, once you run it,
you can't run anything else until it finishes and the shell prints a new
prompt. In fact, we told you that this was core to how shells work when we
talked about REPLs in Lecture 1.

As it turns out, though, Bash and other POSIX shells provide a way to opt out
of this behavior. By suffixing a command with an ampersand (`&`), you can tell
Bash to start that command and then immediately print a new prompt without
waiting for it to finish. Although it's hard for us to show this in a pasted
transcript, you can try it out for yourself using the `sleep` command! `sleep`
takes a number as its only argument and waits that many seconds before exiting.
Try running `sleep 3`; you'll see that it takes three seconds for a new prompt
to appear. Now try running `sleep 3 &`; this time, a new prompt should appear
immediately and you'll see a message like this:

```
[1] 8328
```

This message is from the shell's *job control* subsystem, which is responsible
for keeping track of and reporting the state of *background jobs* like the one
you just created. It includes two pieces of information: the first, `[1]` is
the *job ID* that the shell assigned the newly-created job. The second piece of
information, `8328`, is the *process ID* of the command you just
ran[^process-ids].

Once a job is in the background, it will run to completion on its own time. You
will be able to see its output[^interspersed-output], but you won't be able to
give it input because anything you type will go to the shell or foreground job
instead. You can bring the last background job you ran back into the foreground
by typing `fg`, at which point it will accept input again.

You can also move foreground jobs to the background. To do this, first press
<kbd>Ctrl-z</kbd>. This will temporarily pause the job and bring you back to a
prompt. You can then either leave the job stopped until you bring it back to
the foreground with `fg` or tell it to continue as a background job with `bg`.

To see a list of jobs that haven't finished yet, use the built in `jobs`
command:

```
$ jobs
[1]+  Running                 sleep 3 &
$ 
```

Each line shows the ID, state ("Running" or "Stopped") and command for a single
job. The last and second-to-last jobs to run are annotated with `+` and `-`,
respectively. When a background job finishes, the job control subsystem will
notify you of that fact by printing a message following much the same format
before your next prompt:

```
[1]+  Done                    sleep 3
$ 
```

The `fg`, `bg`, and `jobs` commands can all take a *job specifier* as an
optional argument, which if present will tell them which job to act on. `%%`
and ``%+`` both refer to the current job, while `%` followed by a job ID refers
to that job. For more ways to refer to a given job, as well as details on how
Bash leverages features of the Linux kernel to implement job control, see the
JOB CONTROL section of `man bash`.

[^process-ids]: Process IDs (a.k.a. PIDs) are what the Linux kernel uses to
    keep track of running programs, and every program you run (regardless of
    `&`) has one. The shell prints the PID prominently for background jobs
    because commands that aren't part of the shell don't know about job IDs but
    might still want to interact with the process as it runs.

[^interspersed-output]: If you run a background job that prints output, that
    output will end up interspersed with the output of whatever's in the
    foreground. This can be confusing, especially if you're running something
    that expects to have full control of the terminal, like vi, in the
    foreground. To prevent this, you can redirect the background job's output
    to a file. *Tip:* the special file `/dev/null` will discard any data
    written to it and so can be a redirection target for output you don't care
    about.

## Lecture 4

### Command substitution
Last lecture, you saw how the shell will substitute a variable name, like
`$FOOBAR`, with that variable's value when you use it as part of a command.
Another similar feature, *command substitution*, lets you include a program's
standard output as part of a command. To do so, put the command you want to run
inside the parentheses in `$()`[^backtick-substitution]. For example:

```
$ echo "The last word in the dictionary is $(tail -n 1 /usr/share/dict/words)."
The last word in the dictionary is ZZZ.
$ 
```

Here, we asked the shell to run `tail`, which extracted the last line of
`/usr/share/dict/words`[^words-file], and substituted its output directly into
a string that then got passed to `echo` for printing.

Like variable substitutions, command substitutions can and should be put inside
double quotes but don't work inside single quotes. The risk of using an
unquoted command substitution is the same: if the command's standard output
contains spaces, it will be treated as multiple words by the shell unless
quoted.

You can use all the syntax you've learned so far inside a command substitution,
just as if you were writing a standalone command. For example, we can pass the
output of last week's whole shell pipeline to `head`:

```
$ head "$(find /usr/include/ -type f -name '*.h' -print0 | wc --files0-from=- -l | head -n -1 | sort -rn | head -n 1 | cut -d' ' -f2)"
/*
   +----------------------------------------------------------------------+
   | Zend Engine                                                          |
   +----------------------------------------------------------------------+
   | Copyright (c) 1998-2013 Zend Technologies Ltd. (http://www.zend.com) |
   +----------------------------------------------------------------------+
   | This source file is subject to version 2.00 of the Zend license,     |
   | that is bundled with this package in the file LICENSE, and is        |
   | available through the world-wide-web at the following url:           |
   | http://www.zend.com/license/2_00.txt.                                |
$ 
```

[^backtick-substitution]: An alternate way to do the same thing is to put the
    command name between backticks (``` `` ```). You may see this style in old
    shell scripts, but it's rarely used in new scripts because it's not
    nestable.

[^words-file]: `/usr/share/dict/words` comes with most Linux distributions and
    holds a list of commonly-used English words. It's used by some programs for
    spell checking, so onomatopoeias like "ZZZ" are included.

### Glob patterns
We spoke about patterns briefly in Lecture 2 when describing arguments for
tools like `grep` and `sed`. Those tools incorporate extremely powerful (and
confusing) regular expression languages that allow you to express a huge
variety of different patterns. What we have not discussed yet is the shell's
own less-powerful (and less-confusing) pattern language.

The piece of this language you'll see used most often is the `*` character. If
you include it in a word, the shell will interpret that word as a file path
where the `*` represents any set of zero or more characters. Such a pattern is
known as a *wildcard* or *glob*, and, if any files match it, the shell will
substitute it with *all* of them:

```
$ cd /comp/50ISDT/examples/file-zoo/
$ ls
directory1  file1  file1-link  file2  file3  missing-link
$ echo *
directory1 file1 file1-link file2 file3 missing-link
$ echo file*
file1 file1-link file2 file3
$ 
```

You can see that `echo *` behaves much the same as ls with no arguments, as it
matches all files in the current directory. (`*`, like ls, doesn't match files
beginning with `.` by default.)

Unlike variable and command substitutions, `*` does not work inside either
single or double quotes. However, you don't need to worry about quoting it, as
it will correctly handle the expansions of paths containing spaces even when
unquoted:

```
$ ls -l directory1/hello*
-rw-rw-r--. 1 thebb01 ta50isdt 2 Sep  8 00:43 directory1/hello
-rw-rw-r--. 1 thebb01 ta50isdt 2 Sep  8 00:43 directory1/hello world
$ 
```

Globs behave somewhat unexpectedly when they don't match anything: instead of
expanding to an empty string as you might expect, they remain completely
unchanged! You should be careful of this behavior when writing scripts.
The`shopt -s nullglob` or `shopt -s failglob` commands make the behavior more
consistent; consider using one of these in conjunction with `set -euo pipefail`
(see below) when writing glob-heavy scripts:

```
$ echo foobar*
foobar*
$ shopt -s nullglob
$ echo foobar*

$ shopt -s failglob
$ echo foobar*
-bash: no match: foobar*
$ echo "foobar*" # Quotes still prevent processing
foobar*
$ 
```

### Shell scripts (and when not to use them!)
As we've hinted, typing commands at a prompt isn't the only way to use Bash.
You may sometimes find yourself in a situation where you frequently rerun the
same sequence of commands, perhaps with minor variations. Or perhaps you want
to let others run those commands without having to remember them or understand
exactly how they work. This is where *shell scripts* come in.

A shell script is a text file containing commands. When you ask the shell to
run a script, it interprets and executes each line in sequence, just as if
you'd typed the lines one after another at a prompt. You've already seen shell
variables, and we'll learn about a number of other shell features today--like
conditionals, loops, and functions--that give shell scripts a similar level of
expressiveness to normal programming languages like C, C++, or Python.

Before we talk about those features, though, a word of warning: although you
can in theory solve any programming problem with a shell script, that doesn't
mean you *should*. The shell lacks a number of features, like data types and
variable scoping, that are crucial to writing scalable and maintainable
programs, and as such any shell script that grows past a few tens of lines
quickly becomes incomprehensible. Shell scripts work best as lightweight "glue"
between other software that already exists.

If you find yourself wanting to do any of the following things in a shell
script, there's a good chance that your problem has outgrown the capabilities
of the shell. In these cases, you should move at least part of your solution
into its own program written in some other language:

#### Non-textual I/O
Not all software deals with text. If you need to process structured data that's
kept in a binary format (i.e. not something you can process using tools like
`cut` and `grep`), pick another language. If you have input or output that
can't be represented as text (e.g. audio or image data), pick another language.

#### External libraries
Shell scripts excel at interacting with command-line programs. Pipelines,
redirection, and argument substitution make shell scripts the easiest way to
solve problems in terms of programs that already exist. But if you need to
interact with a piece of software that *isn't* exposed through a command-line
utility--for example, a database like PostgreSQL or MariaDB[^db-clis]--pick
another language.

[^db-clis]: Both these databases do actually come with command-line tools, but
    those tools are designed for administrators to interactively configure and
    debug the database and don't provide a means for efficiently running
    queries and returning data in a format easily usable by scripts.

#### Graphics
Graphical user interface (GUI) libraries like Qt and GTK provide bindings for
languages like C, C++, and Python that allow you to build complex visual
interfaces with buttons, lists, tables, and images. These libraries, like the
databases mentioned above, are not directly accessible via shell scripts. In
general, if your program needs to use the mouse, pick another language.

*Tip:* If you need to work with images, videos, or other binary data, pick a
language with a good binary data library. People often reach for C or C++ in
these cases, but languages like Python and Erlang provide just as good (and
sometimes better) tooling! People use both format-specific libraries (such as
libjpg, for working with JPGs) and format-agnostic libraries (like Python's
`struct` module or Erlang's binary pattern matching).

#### Data structures
Even if your data is textual, you should probably pick another language if you
need to store and later query that data as opposed to processing it all in one
pass like a pipeline does. Because shell variables aren't typed, you can't
build any of the data structures you might have learned about in CS 15 in a
shell script. The best you can do is organize your data as files on disk.
Languages like Python and Ruby, on the other hand, likely have the data
structures you need built-in. And if they don't, you can build those
structures.

#### Complex logic
If you need to do math, nest conditionals more than a couple levels deep, or
express any logic more complex than a few `if` statements, pick a different
language. The shell is fine for simple string and numeric comparisons, but
larger boolean expressions get tricky fast. There's a reason that compile-time
type checking, run-time type errors, and the like exist in other programming
languages: they help people catch bugs. We'll talk more in depth about this in
our last module.

If you find yourself writing a bunch of logic in Bash, stop. Think hard about
the problem you're trying to solve. Does a command-line tool exist that can
solve that problem for you? If so, run it from your script instead of
implementing the logic yourself. If not, consider writing such a command-line
tool in something like C++ or Python for your script to run.

### Creating and running scripts
Let's make a first shell script. Open up your editor and type the following
into a file. Say, `myscript.sh`:

```bash
echo "Hello, world!"
echo "I am in a script and I am being run by $USER."
```

Save it. If you try and run it like a program you compiled in your CS courses
-- by running `./myscript.sh` -- you will get the following error:

```
bash: ./myscript.sh: Permission denied
```

This is because you don't have execute (`x`) permission on the file, which you
can verify with `ls -l`. If you would like to execute the script without
execute permission, you will have to explicitly run the program using another
program that has execute permission... like a shell. Try running `bash
myscript.sh`.

If you add execute permissions (`chmod +x myscript.sh`), you will be able to
run your script using `./myscript.sh`. But what shell is running this file? We
will find out more about this later (or read ahead to the `#!`
section).[^shell-complication]

<!-- TODO: Mention that Windows line endings will stop scripts from working -->

[^shell-complication]: As it turns out, if you run your executable script with
    `./myscript.sh` and there is no shebang, the kernel will refuse to execute
    it. However, your shell (Bash, Zsh, whichever) can choose to execute it if
    the kernel refuses. Bash and Zsh both make a guess if the file is a shell
    script and attempt to execute it with either Bash or Zsh, respectively. So
    it's a one- and sometimes two-step dance.

#### Comment your code
Bash scripts, as we mentioned, are harder to write and read than programs in
other programming languages. Make sure to comment on the intent of any
particularly tricky areas. Comments begin with the `#` character and continue
until the end of the line.

```bash
# I am a comment
echo "foo" # I am another comment
```

### Control flow in the shell
So, you've chosen to use Bash to solve your problem; after you pass this class,
we'll trust your judgement. Let's learn the missing pieces of shell syntax
needed to write programs! Most of these will be familiar from CS 11, so we'll
focus more on "how" than on "why" for each.

In this section, we'll try to stick to syntax that's part of POSIX, so that
your programs don't depend on Bash specifically. Bash does actually have some
non-POSIX features that address a few of the limitations we mentioned in the
last section, but those features aren't nearly enough to make it competitive
with a language like Python. As such, we believe that all our advice above
still stands and that, if you find yourself reaching for a Bash-specific
feature, you probably shouldn't be using a shell script in the first place.

#### if

The basic structure for `if` statements in Bash is as follows:

```bash
if CONDITION; then
  CONSEQUENT
elif OTHER-CONDITION; then
  OTHER-CONSEQUENT
else
  ALTERNATIVE
fi
```

As with other programming languages, the `elif` (else if) and `else` components
are optional. So the minimal `if` statement would look like:

```bash
if CONDITION; then
  CONSEQUENT
fi
```

Any command can be a condition, and its exit code will determine As we talked
about earlier, you can use programs like `test` for your conditions. For
example, to check if two strings are equal, you can use:

```bash
if test "$LEFT" = "$RIGHT"; then
  echo "they are the same"
fi
```

POSIX also provides a more natural-looking way of doing conditionals in your
program. POSIX defines `test` to be equivalent to `[`, so you can instead
write:

```bash
if [ "$LEFT" = "$RIGHT" ]; then
  echo "they are the same"
fi
```

Note that the spaces around the braces `[` and `]` are required, just as they
are for any command--`[` is just a regular command with an unusual name:

```
$ ls -l /bin/\[
-rwxr-xr-x 1 root root 59736 Sep  5  2019 '/bin/['
$ 
```

(Though it is often implemented as a shell built-in, too.)

#### Loops
Because a programming language wouldn't be complete without a friendly loop,
Bash includes not one but several looping constructs. In this section, we will
present `while`, `for`, and `until`. These can be used like other programming
languages' loop constructs, but they can also be used in conjunction with
pipelines.

Let us begin with the `while `loop. The basic structure for `while` in Bash is
as follows:

```bash
while CONDITION; do
  LOOP-BODY
done
```

All of the same kinds of conditions you might use with `if` work with `while`,
too.

For example, to count up to four from zero, you can do:

```bash
i=0
while [ "$i" -lt 5 ]; do
  echo "$i"
  i="$(($i+1))"
done
```

The `$(($i+1))` is yet another type of expansion, called an *arithmetic
expansion*. The shell will evaluate whatever's between the set of double
parentheses as a mathematical expression and substitute the result. We won't
cover this in detail, as you should in general avoid arithmetic in shell
scripts, instead delegating to other commands when possible. For example, a
command called `seq` can replace our whole loop:

```bash
seq 0 4
```

These scripts are equivalent. In fact, `seq` is even more flexible, allowing
you to format the numbers, choose a separator, and pad with leading zeroes. It
also supports an arbitrary increment. Go check out the manual page for more
information.

Now, onto `for` loops. Unlike in C, POSIX `for` loops do not have the `for
(INIT; CONDITION; POST)` structure. They are instead based on iterating over
sequences and are of the form:

```bash
for VAR in SEQUENCE; do
  LOOP-BODY
done
```

Let's take a look at an example:

```bash
for i in $(seq 99 -1 1); do
    echo "$i bottles of beer on the wall..."
done
```

Note that in this case the command substitution is **not quoted** because we
want to treat every separate line from `seq` as a different input to the for
loop.

In this case, the sequence is a newline-separated list of numbers counting down
from 99 to 1. The `for` loop binds each number to the variable `$i` for use in
the body, and we sing a little song.

Last, POSIX specifies a funny little loop called `until`. This is an inverted
`while` loop, so instead of using the negation operator `!` to write something
like:

```bash
while ! CONDITION; do
  LOOP-BODY
done
```

we can instead use:

```bash
until CONDITION; do
  LOOP-BODY
done
```

This is intended to remove visual clutter. The course staff has not often seen
it used in real-world shell scripts, however.

You can also [pipe to
loops](https://unix.stackexchange.com/questions/7011/how-to-loop-over-the-lines-of-a-file/580545#580545),
but that is outside the scope of this course's material and definitely falls
into a "more advanced shell scripting" course.

#### Referring to script arguments
Scripts can read arguments from the special shell variables `$0` to `$N`, where
`N` is a [rather large number](https://stackoverflow.com/a/22747030/569183).
For argument indices larger than 9, however, you must use curly braces, like
`${10}`.

For example, the following script:

```bash
# myscript.sh
echo "$1, world!"
```

can will print out "Hello, world!" when run like so:

```
$ bash myscript.sh Hello
Hello, world!
$
```

#### Defining functions
It may be the case that you require a level of abstraction in your shell
scripts that is somewhere between 1) writing a whole other shell script to call
from your main script and 2) copy/pasting lines of code. For this, Bash allows
you to define functions of your own. The syntax is rather terse:

```bash
FN-NAME () {
  FN-BODY
}
```

There are no static types. There are no argument declarations. Despite this,
functions can read arguments from the special shell variables `$0` to `$N`,
where `N` is a [rather large
number](https://stackoverflow.com/a/22747030/569183). For argument indices
larger than 9, however, you must use curly braces, like `${10}`.

Here is a function to write a greeting to the person specified:

```bash
greet() {
    echo "Welcome to CS 50ISDT, $1!"
}
```

Function invocations look like normal command invocations -- unlike other
programming languages, parentheses are not required:

```bash
greet "max"
# => Welcome to CS 50ISDT, max!
```

Now that you are an expert shell script programmer (TM), you may find it
educational to take a look at some of the shell scripts on your system and
figure out what they do. To do that, we can list all of the available shell
scripts and pick randomly:

```
$ grep -lrF '#!/bin/sh' /usr/bin > scripts.txt
<you may see some permissions errors>
$ vim $(sort -R scripts.txt | head -n 1)
<vim opens>
$
```

How long is the script? Is it well-commented? Does it follow the shell best
practices we outline here?

### Error handling (`set -euo pipefail` is your friend)
Error handling in shell scripts is somewhat fraught. Normally in a programming
language when there is an error, you find out right away -- or it is explicitly
squashed. For example, in C, your program might segfault. Or, if you are
luckier, it might print an error message and `exit()`. Or in C++, Python, and
other programming languages that support it, it might raise an exception.

In Bash, by default, things just kind of go... sideways. Exit codes are the
only method of error reporting, and you have two standard options: zero and
non-zero. But a non-zero error code does not necessarily meant that a command
has *failed*, and that the error should be propagated up the call stack.

Consider the case of searching for a string with `grep`. If a match is found,
`grep` will exit with 0. If a match is not found, `grep` will exit with 1. You
probably don't want your shell script crashing if a match is not found, so the
shell surfaces that exit code for use in conditions. And that's it.

Unfortunately, the same happens for commands that really truly have an error,
like reading from a file that does not exist. If the entirety of your shell
pipeline, for example, relies on reading from a file called `contact-list`, and
that does not exist, the shell will happily continue trying to execute the rest
of your shell script anyway--often with unexpected results.

Fortunately, there is a *magic incantation* you can put at the top of your
shell scripts: `set -euo pipefail`. This magic incantation is not actually
magic, but instructs your shell to enter a particular mode. We'll go over it
piece by piece.

First, `set -e` exits the shell immediately if a command exists with a non-zero
exit code. This helps avoid the aforementioned fiasco.

Second, `set -u` changes the default behavior of reading undefined variables.
By default, reading from an undefined variable returns the empty string, but
with `set -u`, this is treated as an error. This enforces some amount of rigor
for ensuring your variables are defined.

Third, `set -o pipefail` causes pipelines to exit early if an intermediate
command fails. The exit code of the whole pipeline is set to the exit code of
the failed command. This helps `set -e` work in more cases; otherwise, a broken
pipeline would not cause the entire shell script to exit early.

All of these put together produce: `set -euo pipefail`.[^setx]

[^setx]: There is another helpful option, `set -x`, that prints out every
    command before it exits, including from invoked functions. This is useful
    for debugging, or if you feel particularly nosy.

We have listed one common incantation to ease your shell script debugging, but
we have certainly not listed all of the available options to `set`. There are
more options; check out the manual page.

These options are useful both for you, the novice shell programmer, and for
professionals. Recently, the video game launcher Steam had [a shell script
bug](https://www.theregister.com/2015/01/17/scary_code_of_the_week_steam_cleans_linux_pcs/)
that destroyed data in rare cases.

### `#!` lines and how the kernel interprets them
As we mentioned earlier, file extensions have little meaning on a Linux system.
Linux reads, writes, and executes files of every extension identically;
extensions, when present, only offer a hint to human readers about what's
inside.

This makes file types seem unknowable. So how does anyone get anything done if
every file is completely opaque?

As it turns out, not all is lost, and files are not as opaque as they seem.
There is a notion of "magic numbers" (see `man magic`) that file formats can
use to identify themselves to external viewers. For example, the magic number
for executable files on Linux (ELF) is hex `7f 45 4c 46`, or `7f` followed by
"ELF". This allows utilities like `file` (`man file`) to figure out if a file
is an ELF binary or not, from looking at the first couple of bytes[^kind-of].

[^kind-of]: This is still just a guess, but it is a more educated guess. You
    could very well decide to write those bytes into a file and use them for
    some other purpose -- bytes are bytes are bytes are bytes, after all. But
    it is a *convention* to use these bytes to denote an ELF binary.

There is another kind of magic number, hex 23 21 ("#!", pronounced any number
of ways, but commonly "shebang" or "hash bang"), that denotes that a file is a
script. It *does not* mean that the file is necessarily a *shell* script, but
instead allows the programmer to specify an arbitrary interpreter for that
particular file.

For example, if you execute a file with `./myscript`, and it begins with
`#!/bin/bash`, that means that the file should be treated as a Bash script and
executed using `/bin/bash`. It is executed as if you manually typed `/bin/bash
./myscript`. If a file starts with `#!/usr/bin/python`, the file should be
treated as a Python script and executed using the specified Python interpreter.

The [Linux kernel reads the shebang](
https://github.com/torvalds/linux/blob/d4d016caa4b85b9aa98d7ec8c84e928621a614bc/fs/binfmt_script.c#L34)
and the interpreter. Then, it runs the interpreter with the file as an
argument. Magic.

You may be wondering: but what do Bash and Python do about the line with the
funny `#` character? Why isn't that a syntax error? For both of those
languages, `#` denotes the beginning of a comment, which is ignored.

### Shellcheck
You may find [Shellcheck](https://www.shellcheck.net/) helpful. It statically
analyzes your shell scripts for potential bugs and lets you know about the
problems. We will talk more about tools like this in the fourth module,
Correctness.
