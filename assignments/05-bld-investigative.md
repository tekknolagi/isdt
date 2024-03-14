---
---
# Homework 5: BLD, Investigative

For this assignment, you'll explore the Makefile of scdoc. scdoc is an
open-source project used to generate man pages---which have a notoriously ugly
formatting language---from a more friendly, Markdown-like language. The scdoc
source repository is located
[here](https://git.sr.ht/~sircmpwn/scdoc)[^different-forge]. You can click
"tree" to see a web listing of the repository's files, or you can clone it and
browse around using the CLI. You'll eventually need to clone it to answer some
questions.

[^different-forge]: You may notice that, unlike many of the other projects
    you've encountered, scdoc is hosted on SourceHut and not GitHub. SourceHut
    and GitHub are just two examples of Git hosting platforms; GitLab is
    another.  Regardless of what hosting platform a project's main repository
    uses, the repository itself is still plain Git. That means you can clone
    it, make local commits, and even push your own copy (or fork) to a
    different hosting provider! This illustrates the distributed nature of
    Git---your local clone contains the entire repository and all metadata
    needed to reconstruct it elsewhere.

Navigate to [the tree at commit 5ea8873e][tree], open up the Makefile for the
"scdoc" project, and answer the following questions. Please provide *both* the
answer and how you arrived at that answer (show your work or cite your sources,
as appropriate):

[tree]: https://git.sr.ht/~sircmpwn/scdoc/tree/5ea8873e33a5be55625e05673a47e440182bc09e

1. In general, how does Make determine which target to build if you run it with
   no arguments?
1. For scdoc specifically, which target does `make` build if you run it with no
   arguments? Assume GNU Make.
1. The command on line 30 of the Makefile, used to link the final `scdoc`
   binary, includes a number of Make variable expansions (the words starting
   with `$`).
   1. What is an automatic variable? How does the visible behavior of automatic
      variables differ from that of other kinds of variables? Please provide at
      least two examples.
   1. Which of the variables used in the command on line 30 are automatic
      variables? For each one, what is the meaning?
   1. The Makefile does not explicitly define some variables it uses, such as
      `LDFLAGS`. What three places can these values come from?
   1. What does the entire line expand to when Make runs it? Explain where the
      value of each variable came from. Assume that no variables are overridden
      by the outside environment.
1. If you run `make scdoc` from a clean directory (i.e. after initial checkout
   or running "make clean"), you will see 10 commands that get run. Please do
   this and tell us the commands. Annotate each command with the line number of
   the Makefile that generated the command. Many of these will share a line
   number---that's okay.
1. Are any additional commands run by `make scdoc` beyond the ones you
   annotated in the previous question? If so, what are they and why were they
   not included in the output?
1. Pretend you are the Make program. What does Make do when you run `make
   .build/main.o`? Be specific and do not assume anything about the state of
   the `.build/` directory.
1. The `install` rule copies the resulting binary and documentation to various
   special system directories so that you can use the program from anywhere on
   your system. To do this, it runs the `install` command. What does the
   `install` program do? Why might you use it instead of `cp`?
1. Line 62 looks different from most other lines. It starts with `.PHONY` and
   lists a number of targets. What is the purpose of this line? What could
   happen if it were not present?

## Submitting your work

You should write your answers in a file, `answers.txt`.

Please submit with `provide comp50isdt bld-investigative answers.txt`. You must
be logged into the homework server to use Provide.
