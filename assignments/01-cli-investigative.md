---
---

# Homework 1: CLI, Investigative

## Important: use Bash!

For this and all future assignments, please make sure you are using Bash as
your shell, as that's what this course will focus on for the reasons described
in [lecture](../lecture-notes/1-cli.html). The Tufts CS department's default
shell for new users is tcsh, so unless you've asked to have yours
changed[^change-shell], you'll need to run `bash -l` *each time you connect to
the server prior to working on coursework*. Your prompt won't look any
different after running this command, but you can run `echo $0` to check which
shell you're using.

[^change-shell]: On most Linux systems, you can use the `chsh` command to
    change your own shell, but this method doesn't work on the Tufts homework
    servers. This is because they don't store user account information
    (including each account's shell) locally, but rather in a centrally-managed
    database of students and staff, which only the department administrators
    can modify. To change your default shell to bash, write an email to
    [staff@eecs.tufts.edu](mailto:staff@eecs.tufts.edu).

## CaLIsthenics: what's on the homework server?

Many software engineers use the command-line in their day-to-day lives. The
whole "command-line experience" is composed of a bunch of programs, working
together, to help you solve problems.

Since we're going to be using the command-line frequently in this course,
developing muscle memory is going to be important. Building an intuition for
what commands to use when will come in handy.

To get started, you're going to poke around the homework server using the tools
we discussed in lecture. You'll get some hands-on experience with `pwd`, `cd`,
`ls`, `cat`, `tree`, and `man`. Please answer the following questions and "show
your work" (see [Grading](https://www.cs.tufts.edu/comp/50ISDT/#grading) on the
syllabus for an example) with each:

1. When you log into the homework server, what directory are you in?
2. How many files are in your current directory? How many directories?
3. Give a **relative** path that you can use to refer to this course's
   directory, which lives at `/comp/50ISDT/`, while in your home directory.
   Remember that relative paths cannot start with a slash.
4. The website for this course, among other things, lives in our directory at
   `/comp/50ISDT/`. Take a look around! What's the password?
5. How can you make `cat` number each line in a file? (Answer this question
   without referencing the internet, please!)
6. Files inside the special filesystem `/dev/` are used to communicate with the
   Linux kernel. Choose a file that looks interesting inside `/dev/` and tell
   us what it's for. You are free to use Google or any other internet or
   printed resource, but cite your source.
7. `/etc/` is a standard directory on Linux that contains system configuration
   files. Although file extensions (like `.txt` and `.jpg`) have no intrinsic
   meaning on Linux, many configuration files in `/etc/` have them anyway.

   <!-- TODO: We should clarify if "files" here includes directories. -->

   Write a shell pipeline that prints the top ten most frequently occurring
   extensions of files inside `/etc/`, taking the "extension" to be the part of
   a file's name that occurs after the final `.` character. Your count should
   include files in subdirectories, except those you don't have permission to
   see. You may include or omit files that have no extension from the count at
   your discretion.

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
directory tree in `/comp/50ISDT/cli1-murder-mystery/`) to see what you can
find! Start your journey in the *entryway*.

Please provide the name of the murderer (and an outline of your investigation)
as your answer.

## Submitting your work

Please format your answers in a text file, `answers.txt`, split into two
sections (CaLIsthenics and mystery), and numbered where appropriate.

When you are done, submit your work with `provide comp50isdt
cli-investigative answers.txt`. You must be logged into the homework server to
use Provide.
