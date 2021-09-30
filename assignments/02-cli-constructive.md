---
---

# Homework 2: CLI, Constructive

## Note: what counts as a "file"?
Both pieces of this assignment ask you to print a list of files. The word
"file" is often used to refer specifically to a *regular file*, which is the
"normal" kind of file that holds data and shows up in `ls` with a type of `-`.
However, the strict POSIX definition of "file" encompasses not only regular
files but also directories, symlinks, devices, and every other thing that can
go inside a directory. For this assignment, we are referring to the POSIX
definition whenever we say "file." Your implementations of `whats-new.sh` and
`myls.c` should consider directories, symlinks, and all other types of file
when producing their output.

## `whats-new.sh`: finding newly-added files on the homework server
The server that Tufts uses to host home directories has a special feature to
help prevent data loss: in every directory, the server adds a hidden, read-only
directory named `.snapshot/`. Inside `.snapshot/` is a set of directories with
names like `daily.2021-09-22_0010`. Each of these directories holds a copy of
the contents of the original directory from a certain point in time.  Take a
moment to SSH to the server and see for yourself!

The first piece of each snapshot's name--`daily`, in this example--represents
the frequency at which those snapshots are taken. The second
part--`2021-09-22_0010`--is the date and time at which it was taken. Snapshots
that happen more frequently are also deleted more aggressively, meaning that
the granularity of snapshots goes down the further you go back.

Note that, to prevent overwhelming tools that recursively traverse a directory
tree, the `.snapshot/` directory only shows up in listings (`ls -a`) in your
top-level home directory. However, it is also present in every subdirectory if
you specifically ask for it:

```
$ ls -a Documents/  # No .snapshot/ listed!
.  ..  do-not-read  top-secret-file
$ ls Documents/.snapshot/
daily.2021-09-19_0010             every_four_hours.2021-09-23_1205
daily.2021-09-20_0010             every_four_hours.2021-09-23_1605
daily.2021-09-21_0010             every_four_hours.2021-09-23_2005
daily.2021-09-22_0010             every_four_hours.2021-09-24_0005
daily.2021-09-23_0010             weekly.2021-09-05_0015
daily.2021-09-24_0010             weekly.2021-09-12_0015
every_four_hours.2021-09-23_0405  weekly.2021-09-19_0015
every_four_hours.2021-09-23_0805
$ 
```

This is not a standard feature of Linux or POSIX--it's specific to the network
servers that Tufts uses. Nevertheless, `.snapshot/` can be very useful when you
accidentally remove or overwrite an important file and want to get the old
version back. (In the next module, we'll learn about version control systems,
which are like `.snapshot/` but supercharged.) In this part of the assignment,
you'll write a shell script that automates the process of finding what files
have been added to a directory since its most recent snapshot.

Your script, named `whats-new.sh`, should take as its only argument a path to a
directory to find new files in. If the argument is missing or does not point to
a directory that has been snapshotted, your script should print an error
message and exit with a nonzero exit status. (The `exit` command immediately
exits a shell script and takes the exit status as an argument.)

If the argument is valid, your script should compare the contents of the
directory with the contents of the most recent snapshot. We define the *most
recent snapshot* as the one with the highest timestamp in its name, regardless
of whether it's `daily`, `weekly`, or something else. We define the *contents*
of a directory as all the non-hidden files (see note above) that are directly
contained within it.

In other words, you do not need to show new hidden files (ones that start with
`.`), nor do you need to recurse into subdirectories. You may do either of
these if you so choose, however. (If you do decide to handle hidden files, try
to not list `.snapshot/` itself as a new file!)

Your output should be a list of files that are present in the directory but not
in the snapshot, one per line. In other words, print out the files that have
been added since the snapshot was taken. These should be valid paths relative
to the given directory (so either `file1` or `./file1` is acceptable). You may
find the `comm` utility useful in generating this list; see `man comm`.

Please include a `#!` line at the beginning of your script that indicates it
should be executed with either `/bin/sh` or `/bin/bash`. (`/bin/sh` points to
different shells on different systems but is always guaranteed to be a
POSIX-compliant shell; `/bin/bash` is always Bash specifically.) And use the
error handling practices we encouraged in lecture.

Your program may write data to files as part of generating its result. If it
does, please use the `mktemp` utility to create them. `mktemp` generates a new
file with a random name inside `/tmp`, a system directory designed to hold
temporary files that don't need to stick around. We encourage you to remove any
temporary files you use once your script finishes, but you will not lose points
if you don't.

## Using syscalls: write your own ls!
We discussed in lecture how system calls (also known as "syscalls") are the
primary way for userspace programs to communicate with the Linux kernel. Now
it's time to get your hands dirty and make a syscall of your own. You're going
to write a stripped-down version of `ls` that prints the contents of a
directory.

This piece of the assignment involves writing C code, but we’re confident that
you’ll be able to do it with what you know from CS 15 and the
`our-friendly-cat` implementation we showed in class. C is very similar to the
pieces of C++ you already know, and you can take a look at this old [CS 40
lab](https://bernsteinbear.com/resources/comp40-lab0.pdf) to learn some of the
notable differences (plus details on `argc` and `argv`).

You'll be calling some system functions from C, including one called `fputs()`
to print to stdout as well as a number of syscall shim functions (described
below). These functions are part of the *C standard library* (a.k.a.  *libc*),
which is a set of function implementations that are available to any C program
running on a POSIX system. Nearly all C library functions have their own man
pages; don't be afraid to use them!

Your program, `myls.c`, should take as its only argument a path to a directory
and print the name of each file (see note above) inside that directory, one per
line. You may or may not include files starting with `.` at your discretion. If
your program is run without a directory name or the given name is not a
directory, your program should print an error and return a nonzero exit code.

Internally, GNU's implementation of `ls` calls the `readdir()` function from
libc. `readdir()` behaves as a transparent wrapper around the `readdir`
syscall[^getdents]. Read the man pages for `opendir` (`man 3p
opendir`[^sections]), `readdir` (`man 3p readdir`), and `closedir` (`man 3p
closedir`) to get an idea for how you might write your program. Although these
three functions are syscall shims, you don't have to implement your entire
program directly using syscalls. Specifically, you'll probably want to use
`fputs` (`man 3 fputs`) to print the filenames.

[^getdents]: In reality, some implementations use a different syscall called
    `getdents` under the hood, just like `open()` uses `openat`. This is an
    implementation detail that shouldn't concern you.

[^sections]: Manual pages are divided into sections. Since some commands like
    `chmod` are both shell utilities and syscalls, referencing man pages by
    name alone can be ambiguous. According to `man man`, section 3 of the man
    pages are for library calls (C functions). There is also a section for
    POSIX specifications, section 3p.

These functions can return a whole host of different errors in different
conditions. If any of them returns a value that signals an error (check the man
page for each one), you should print a helpful error message and exit
immediately with a nonzero exit code.[^perror]

[^perror]: We won't require you to use it, but you may find the `perror`
    function (`man 3 perror`) helpful.

You can start with the following skeleton, or you can write your own:

```c
#include <stdio.h>

int main(int argc, char **argv) {
  if (argc != 2) {
    fprintf(stderr, "Expected one argument but got %d instead.\n", argc-1);
    return 1;
  }

  // your code here
}
```

As an extension, you may allow the user to omit the argument and have your
program list the contents of the current working directory. This is not
required for full marks.

## Submitting your work
Please submit your two files, `whats-new.sh` and `myls.c`, with `provide
comp50isdt cli-constructive whats-new.sh myls.c`. You must be logged into the
homework server to use Provide.

## Just for fun...
**At this point, you are done with the assignment. You need not read anything
past this point if you don't want to.** However, if you're looking for a
challenge, or if you want to learn some tricks involving syscalls and shared
libraries in Linux, feel free to take a stab at the following. Expect to do a
lot of Googling here, as we have not taken care to define every term we use.

### Step 1: use `LD_PRELOAD` to intercept `opendir`
`opendir()` and `readdir()` are not themselves syscalls; instead, they're
functions in the C standard library that invoke syscalls. When you run myls, it
loads the implementations of those functions from a *shared object* containing
the C standard library. (This shared object is generally located at
`/usr/lib/libc.so.6` on GNU/Linux systems.)

In this exercise, you'll use a fun feature of the GNU dynamic loader (whose job
it is to load shared objects at runtime) to *replace* the system's
implementation of `opendir()` with one you write yourself. To do this, you'll
set an environment variable named `LD_PRELOAD` to the path of a shared object
you write yourself in C.

When `LD_PRELOAD` is set, the loader looks in that library first for *any*
library function your program uses. So, by setting it to a library you write
containing a function named `opendir`, you can have your own code run when myls
(or any other program!) calls `opendir()`.

Here's how to compile a shared library that contains functions from a source
file named `shim.c` and run myls with that library preloaded:

```
$ clang -shared -fpic shim.c -o shim.so
$ LD_PRELOAD="$(pwd)/shim.so" ./myls
<...>
$ 
```

Please note that the `$(pwd)/` is *essential*, as `LD_PRELOAD` does not allow
relative paths.

Try creating a shim with an `opendir` implementation that first prints to the
terminal its `name` argument and then calls the real libc version of `opendir`,
returning its result so that programs like myls still get what they asked for.
Calling the real version of `opendir()` is a bit tricky, since the name
`opendir()` now refers to your shim. You can get around this using a function
called `dlsym` (see `man dlsym`).

When you run myls with this shim, you should see the path of the directory
you're listing printed out before the rest of its output. This is your shim's
code running when myls initially calls `opendir()`!

### Step 2: cover your tracks
Spoiler alert: David Knifehands did *not* kill Alexander Henshawe. But you've
just heard that he's been framed by the real murderer, and the authorities are
after him! You have to save Dave by hiding the evidence before he's caught by
Mike Bauer & co, our eagle-eyed sysadmins. Mike will go spelunking through the
directory tree (using system ls, not myls), looking for clues like a murder
weapon.

For inexplicable reasons, Mike will load your shim when he runs `ls`. In order
to interfere with his investigation, you must use your new `LD_PRELOAD` skills
for good. This time, instead of just logging a function call, you'll alter the
results!

Change your shim to intercept `readdir()` instead of `opendir()`, then see if
you can write an implementation of `readdir()` that skips returning any
directory entries that contain the word "trapdoor". That is, if ls (or myls)
would normally produce[^different-layout]:

```
carpet
trapdoor
another-trapdoor-wow
table
```

Instead, it should now produce:

```
carpet
table
```

Good luck!

[^different-layout]: This example has a slightly different directory listing
    than the actual directories from the murder mystery, but it is only meant
    to be illustrative.

### Step 3: try it with other binaries
What happens when you run `find`, `tree`, `grep -r`, or some other command that
does directory traversals? Does your shim work? How do you know?

For example, try `LD_PRELOAD="$(pwd)/shim.so" tree
/comp/50ISDT/murder-mystery/`.
