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
any effect when you run it. However, if you don't do so, tcsh will interpret
your commands, meaning much of the more advanced syntax we cover will result in
error messages or unexpected behavior.

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
delimiter, it can escape `'` (`\\'`) and even itself ('\\\\')!

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
replace it in-place, use the `-i` flag. *Note: doing `sed COMMAND original.txt
> original.txt` will **not** work because the `>` causes the shell to overwrite
your file before `sed` even runs.* We will talk more about this when we get to
our section on pipelines.

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

#### `vi`
`vi` is a POSIX-specified text editor that is available on almost every system
you will use. Unlike text editors such as Notepad and Kate, is a *modal*
editor, meaning that when it is open it is in one of several modes: INSERT,
NORMAL, etc. The default mode is NORMAL mode, which means that opening it and
trying to directly start typing will not work. To enter INSERT mode, type
<kbd>i</kbd>, and to go back to NORMAL mode, type <kbd>Esc</kbd>. To quit Vi,
type `<kbd>:</kbd><kbd>q</kbd>` in NORMAL mode.

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
