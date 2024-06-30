---
---

# Homework 1: CLI, Investigative

## Important: use Bash!

For this and all future assignments, please make sure you are using Bash as
your shell, as that's what this course will focus on for the reasons described
in [lecture]({{site.baseurl}}/lecture-notes/1-cli/). You may already be using Bash, or
you may be using another shell such as Zsh. For coursework, we recommend either
running `bash -l` each time you do coursework or changing your shell with
`chsh` until the term is over.

## CaLIsthenics: what's on the homework server?

Many software engineers use the command line in their day-to-day lives. The
whole "command-line experience" is composed of a bunch of programs, working
together, to help you solve problems.

Since we're going to be using the command line frequently in this course,
developing muscle memory is going to be important. Building an intuition for
what commands to use when will come in handy.

To log in:

```console?prompt=$,1857771c4d3278:~$
$ ssh YOUR_USERNAME@isdt.fly.dev
1857771c4d3278:~$
```

> NOTE: If you get asked for a password or get some kind of authentication
> error, you have not correctly set up your public key authentication. Make a
> post on Piazza if you need help.

To get started, you're going to poke around the homework server using the tools
we discussed in lecture. You'll get some hands-on experience with `pwd`, `cd`,
`ls`, `cat`, `tree`, and `man`. Please answer the following questions and "show
your work" (see [Grading]({{site.baseurl}}/#grading) on the syllabus for an
example) with each:

1. When you log into the homework server, what directory are you in?
2. How many files are directly inside your current directory? How many
   directories? Don't count files and directories that are inside
   subdirectories.
3. Give a **relative** path that you can use to refer to this course's
   directory, which lives at `/comp/50ISDT/`, while in your home directory.
   Remember that relative paths cannot start with a slash.
4. The website for this course, among other things, lives in our directory at
   `/comp/50ISDT/`. Take a look around! What's the password?
5. How can you make `cat` number each line in a file? (Answer this question
   without referencing the internet, please!)
6. Files inside the special filesystem `/dev/` are used to communicate with the
   Linux kernel. Choose a file that looks interesting inside `/dev/` and tell
   us what it's for. Please don't choose `/dev/null`, as we will discuss that
   in lecture. You are free to use Google or any other internet or printed
   resource, but cite your source.
7. `/etc/` is a standard directory on Linux that contains system configuration
   files. Although file extensions (like `.txt` and `.jpg`) have no intrinsic
   meaning on Linux, many configuration files in `/etc/` have them anyway.

   Write a shell pipeline that prints the top ten most frequently occurring
   extensions of files inside `/etc/`, taking the "extension" to be the part of
   a file's name that occurs after the final `.` character. Your count should
   include files in subdirectories, except those you don't have permission to
   see. Your count should not include the names of subdirectories themselves.
   (e.g. `/etc/sysctl.d/` should not count as a `.d` extension.) You may
   include or omit files that have no extension from the count at your
   discretion.

   Your output should contain ten lines (unless there are fewer than ten unique
   extensions inside `/etc/`). Each line should include the extension (with or
   without the dot, at your discretion) and a count of files with that
   extension. We do not care about whitespace, field order, or whether each
   line includes extra fields beyond these two.

   *Hint:* `\.[^/.]*$` is a regular expression that matches a literal dot
   (`.`), followed by any number of characters that are not a dot or a forward
   slash, followed by the end of a line. In other words, it matches the
   extension of files from line(s) containing file paths.

   This is not a trivial problem. Expect to have several different commands in
   your pipeline. Please ask for help early if you are struggling.

## Exploring files: murder mystery in `/comp/50ISDT/`!

There was a murder last night at your old university colleague David's dinner
party! A guest found a body in the living room, and nobody knows who did it.
You, the premiere private investigator in Medford, MA, have been called in to
help. Explore David's magnificent mansion (represented conveniently by a
directory tree in `/comp/50ISDT/mystery/`) to see what you can find! Start your
journey in the *entryway*.

Please provide the outline of your investigation (we hope this is reasonably
detailed and includes the commands you ran) and the name of the murderer as
your answer.

## Submitting your work

Write your answers in a text file, `answers.txt`. It should be split into two
sections (CaLIsthenics and mystery), and numbered where appropriate. Submit
this file on Gradescope.
