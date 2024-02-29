---
---

# Homework 2: CLI, Constructive

This is the first of four "constructive" assignments---most of which ask
you to write a small amount of code. While writing that code, you will likely
make mistakes that highlight gaps in your understanding and require you to
fill those gaps by referencing lecture notes or documentation. Not only is that
expected, it's the main reason we created these assignments. The programs
you produce are secondary to the experience you gain while producing them.

In the past couple of years, it has gotten dramatically easier to bypass the
trial-and-error portion of a programming assignment by generating a program
using a large language model like ChatGPT or Copilot. Although such tools
have their place, they do not in general help you build understanding, which is
the primary purpose of these assignments.

You are in school, we hope for the purpose of learning something. It has always
been possible to cheat yourself of learning by copying code. In the past couple
of years, it has gotten dramatically easier to do so by asking large language
models such as ChatGPT or Copilot to write programs for you. There is no way to
prevent you from doing so and it would be detrimental to your learning to
assign so complex and specific an assignment that such LLMs fail.

So remember this: the academic integrity policies of NEU and of this course
still hold. Please do your own work. The course staff do not like reporting
possible violations---it feels bad and is a lot of paperwork. We would much
prefer you do your work. And, if there are extenuating circumstances, we would
prefer if you approached us or the dean privately and explained what is going
on.

With that out of the way, let's get to it.

## `build.sh`: making trouble

A lot of systems programming is done in languages such as C, C++, and Rust.
These languages all have one thing in common: programs written in them are
predominantly compiled before being executed[^interpreters]. This two-step
tango means that every time you modify your program, you have to compile it
before running it.

[^interpreters]: We say *predominantly* because the evaluation strategy is not
    necessarily part of the language! The language is the abstract concept and
    the implementation makes it go zoom. There are C and Rust interpreters and
    there are (for example) Ruby and Python compilers.

That's not fun, especially if it requires arcane compiler flags that are hard
to remember. Or maybe your program has a lot of files and your build command is
getting unwieldy. Either way, you are going to solve your own problems today by
*writing a build script*.

This part of the assignment uses the C compiler as an example, but it doesn't
require you to write C: we provide sample C code you can use to test your build
system. Later, though, you *will* write some C code and integrate it into your
build system.

Your job is to write a program in Bash or POSIX shell, `build.sh`, that
compiles some C program. The minimal functional (but not acceptable to submit)
solution looks something like this:

```sh
#!/bin/sh
cc -o foo foo.c rng.c
```

If only it were that simple for your assignment. We'll get more into all this
later in the term, but this program is not ideal: it builds `foo.c` and `rng.c`
into `foo` every time `build.sh` is executed, even if `foo.c` and `rng.c` have
not changed. The script you submit, in contrast, must only rebuild `foo` if either of those
dependencies have changed. In addition, your program must build intermediate
object files for each C file.

This means example runs might look like this:

```console?prompt=$
$ ls
build.sh  foo.c  foo.h  rng.c  rng.h
$ ./build.sh 
cc -c foo.c
cc -c rng.c
cc -o foo foo.o rng.o
$ ./build.sh 
$ touch rng.c
$ ./build.sh 
cc -c rng.c
cc -o foo foo.o rng.o
$ ./foo 
hello, world! your randomly chosen number is 4
$
```

Notice three things:

* We can run `build.sh` and if nothing needs to get rebuilt, nothing will be
  rebuilt
* We can update individual C files without recompiling other C files (we do
  need to link them at the end, though)
* By "changed", we mean that the file's modification time is newer than its
  target; the file contents may not have changed

This is a pretty standard set of features for build systems. Many people have
put many years into making build systems great. Because we are dealing with
small code and don't have a lot of strange requirements, you are only going to
peek a little bit into that yawning abyss. We hope that after writing your
build script, you look at Make with a little less apprehension. You too could
write such a tool given enough time.

Unlike other build systems, you are going to put the "should we recompile this"
logic in the same file as the project-specific components. Together, they will
form the build script for `foo`.

### Requirements

This all might sound a little bit scary but we promise that explicitly laying
out the behavior like this makes for easier implementation. You can think of it
like a checklist.

> Note: The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
> "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this
> document are to be interpreted as described in [RFC
> 2119](https://datatracker.ietf.org/doc/html/rfc2119).

You MUST:

* Be able to build `foo` by running `./build.sh`
* Only recompile a target if any of its dependencies' modified-time (mtime) is
  later than the target's mtime
* Write your program so that it runs under `sh` or `bash`
* Write your program entirely in one file
* Include a shebang line at the beginning of your script for either `sh` or
  `bash`
* Use the error-handling practices we encouraged in lecture
* Exit with error code 0 if the script succeeded
* Exit with a non-zero error code if the script did not succeed

You MUST NOT:

* Use `make` or `watchman` or `entr` or any other software that would do
  substantive work for you
* Modify any of the C source files we provide to you

You SHOULD:

* Define functions to make your code more readable

You MAY:

* Print the commands executed by your script as they are executed
* Take an optional argument to `build.sh` to specify what target to build
* Use (small) standard Unix utilities. When in doubt, ask on Piazza
* Support modifying the build by setting `CC`, `CFLAGS`, `LDFLAGS`, and other
  assorted environment variables

In general, you MAY go above and beyond if you want to, as long as your
extended program still meets the requirements. This MAY result in some light
sprinkling of extra points.

Note: `/bin/sh` points to different shells on different systems but is always
guaranteed to be a POSIX-compliant shell; `/bin/bash` is always Bash
specifically.

To give you rough idea of the complexity of the program, the course reference
solution is 24 [SLOC](https://en.wikipedia.org/wiki/Source_lines_of_code) for
the "build system" part and 6 SLOC for the project-specific component. Your
solution may be longer or shorter; both are fine.


## Using syscalls: write your own `ls`!
Now that you have a tool that can be used to compile the course-provided sample
C program, we're going to have you write some C.

We discussed in lecture how system calls (also known as "syscalls") are the
primary way for userspace programs to communicate with the Linux kernel. Now
it's time to get your hands dirty and make a syscall of your own. You're going
to write a stripped-down version of `ls` that prints the contents of a
directory.

This piece of the assignment involves writing C code, but we’re confident that
you'll be able to do it with what you know already and the `our-friendly-cat`
implementation we showed in class. You can take a look at this old [Tufts CS 40
lab](https://bernsteinbear.com/resources/comp40-lab0.pdf) to learn some of the
notable differences between C and C++ (if that's helpful), plus details on
`argc` and `argv`.

You'll be calling some system functions from C, including one called `fputs()`
to print to stdout as well as a number of syscall shim functions (described
below). These functions are part of the *C standard library* (a.k.a.  *libc*),
which is a set of function implementations that are available to any C program
running on a POSIX system. Nearly all C library functions have their own man
pages; don't be afraid to use them!

Your program, `myls.c`, MUST take as its only argument a path to a directory
and print the name of each file inside that directory, one per
line. You MAY include files starting with `.` at your discretion. If your
program is run without a directory name or the given name is not a directory,
your program MUST print an error and return a nonzero exit code.

This assignment asks you to print a list of files. The word "file" is often
used to refer specifically to a *regular file*, which is the "normal" kind of
file that holds data and shows up in `ls` with a type of `-`. However, the
strict POSIX definition of "file" encompasses not only regular files but also
directories, symlinks, devices, and every other thing that can go inside a
directory. For this assignment, we are referring to the POSIX definition
whenever we say "file." Your implementation of `myls.c` should consider
directories, symlinks, and all other types of file when producing its output.

Now, on to implementation notes. We suggest looking into a couple of different
syscalls and their C wrappers as starting points.

Internally, GNU's implementation of `ls` calls the `readdir()` function from
libc. `readdir()` behaves as a transparent wrapper around the `readdir`
<!-- TODO(tom): make explanation of readdir and its relationship to syscalls
more accurate -->
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
immediately with a nonzero exit code[^perror].

[^perror]: We won't require you to use it, but you may find the `perror`
    function (`man 3 perror`) helpful.

You MAY start with the following skeleton:

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

This is a small program. You may feel tempted to copy it off the internet or
classmate. **Don't.** You are robbing yourself of learning. We have given you
enough function names to get started. Check out their manual pages.

## Using `build.sh` to compile `myls.c`

Now integrate by adding `myls` as a target to `build.sh`! You MUST be able to
compile `myls` by running `./build.sh` (and also follow all the other rebuild
requirements listed above).

## Submitting your work
Please submit your two files, `build.sh` and `myls.c`, on Gradescope.

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
