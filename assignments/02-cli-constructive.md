---
---

# Homework 2: CLI, Constructive

## `whats-new.sh`: finding newly-added files on the homework server
The server that Tufts uses to host home directories has a special feature to
help prevent data loss: in every directory, the server adds a hidden, read-only
directory named `.snapshot`. Inside `.snapshot` is a set of directories with
names like `daily.2021-09-22_0010`. Each of these directories holds a copy of
the contents of the original directory from a certain point in time.  Take a
moment to SSH to the server and see for yourself!

The first piece of each snapshot's name--`daily`, in this example--represents
the frequency at which those snapshots are taken. The second
part--`2021-09-22_0010`--is the date and time at which it was taken. Snapshots
that happen more frequently are also deleted more aggressively, meaning that
the granularity of snapshots goes down the further you go back.

Note that, to prevent overwhelming tools that recursively traverse a directory
tree, the `.snapshot` directory only shows up in listings (`ls -a`) in your
top-level home directory. However, it is also present in every subdirectory if
you specifically ask for it:

```
$ ls -a Documents/  # No .snapshot listed!
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
servers that Tufts uses. Nevertheless, `.snapshot` can be very useful when you
accidentally remove or overwrite an important file and want to get the old
version back. (In the next module, we'll learn about version control systems,
which are like `.snapshot` but supercharged.) In this part of the assignment,
you'll write a shell script that automates the process of finding what files
have been added to a directory since its most recent snapshot.

Your script, named `whats-new.sh`, should take as its only argument a path to a
directory to find new files in. If the argument is missing or does not point to
a directory with snapshots, your script should print an error message and exit
with a nonzero exit status. (The `exit` command immediately exits a shell
script and takes the exit status as an argument.)

If the argument is valid, your script should compare the contents of the
directory with the contents of the most recent snapshot. We define the *most
recent snapshot* as the one with the highest timestamp in its name, regardless
of whether it's `daily`, `weekly`, or something else. We define the *contents*
of a directory as all the non-hidden files (including directories and links)
that are directly contained within it.

In other words, you do not need to show new hidden files (ones that start with
`.`), nor do you need to recurse into subdirectories. You may do either of
these if you so choose, however. (If you do decide to handle hidden files, try
to not list `.snapshot` itself as a new file!)

Your output should take the form of a list of new files, one per line. These
should be valid paths relative to the given directory (so either `file1` or
`./file1` is acceptable). You may find the `comm` utility useful in generating
this list; see `man comm`.

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
and print the name of each file inside that directory, one per line. You may or
may not include files starting with `.` at your discretion. If your program is
run without a directory name or the given name is not a directory, your program
should print an error and return a nonzero exit code.

Internally, GNU's implementation of `ls` calls the `readdir()` function from
libc. `readdir()` behaves as a transparent wrapper around the `readdir`
syscall[^getdents]. Read the man pages for `opendir` (`man 3p
fdopendir`[^sections]), `readdir` (`man 3p readdir`), and `closedir` (`man 3p
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

