---
---

<style type="text/css">
kbd {
    background-color: #eee;
    border-radius: 3px;
    border: 1px solid #b4b4b4;
    box-shadow: 0 1px 1px rgba(0, 0, 0, .2), 0 2px 0 0 rgba(255, 255, 255, .7) inset;
    color: #333;
    display: inline-block;
    font-size: .85em;
    font-weight: 700;
    line-height: 1;
    padding: 2px 4px;
    white-space: nowrap;
}
code {
    color: green;
}
</style>

# Home

*Introduction to Software Development Tooling* is a course being taught by [Max
Bernstein](https://bernsteinbear.com) and [Tom Hebb](https://tchebb.me/) in the
Fall 2021 semester at Tufts University.

## Overview

Tufts' core computer science curriculum mainly focuses on teaching students how
to program: it teaches them to break down problems and solve them in terms of
primitive operations that a computer can perform, and it teaches them to
express those solutions using various programming languages. However, there is
a lot more to software engineering than just programming. The existing
curriculum does not spend much time focusing on the ubiquitous tooling--like
source control, build systems, and testing infrastructure--that makes
efficient development and maintenance of large software systems possible.

Even tools that students are exposed to, like the POSIX shell, are not part of
the explicit learning objectives for the existing courses. Instead, our
courses treat them as obstacles in the "real work" of programming.

To solve this problem, we propose a new course covering the fundamentals of
four different categories of tooling, taught via concrete examples that
students are likely to encounter. We will cover source control, focusing on
Git; OS utilities, focusing on Linux and the POSIX shell; build systems,
focusing on Make; and testing and continuous integration, focusing on UTest and
GitHub Actions.

Knowing these tools will help students both to write high quality software and
to get up to speed quickly in the large, unfamiliar codebases that they will
undoubtedly encounter outside of the classroom.

## Administrivia

**Soft prerequisite:** CS 15 or permission of instructor

**Textbook:** none

**Equipment:** none

**Lectures:** via video call (maybe one in-person visit) at TBD. Course
communication happens primarily on Piazza. Assignments are to be submitted via
TBD.

**Exams:** none

**Teaching Assistants:** TBD, TBD

## Learning objectives

By the end of this course, we hope that students will be able to do the
following:

1. Track changes in their software projects, including developing multiple
   parallel changesets, using Git.
2. Carry out development comfortably on a Linux system by using shell commands
   and OS utilities, including synthesizing multiple utilities together to
   answer novel questions.
3. Write and understand simple Makefiles for building C projects.
4. Write software that is designed to be tested as well as used.
5. Write tests for their software using UTest.
6. Set up continuous integration to run tests on new code changes using GitHub
   Actions.
7. Search for and read documentation for new and unfamiliar tools using `man`
   and the internet.
8. Independently answer questions about unfamiliar systems by reading
   documentation, carrying out experiments, and exploring the underlying source
   code using the tools they've learned.

## Schedule

### Week 1, Lecture 1a: Course administrivia

1. Who are we?
2. What will you get out of this course?
3. How will this course be conducted? Why?
4. What do we expect of students?
5. This course is not about writing lines of code. It is about the ecosystem
   and practices that surround the code you write.

### Week 1, Lecture 1b: Intro to version control (VCS 1)

1. What problem does version control solve? (Did you ever break your COMP 11
   code somehow without knowing what you changed? How is a COMP 11 project
   different from another project - what different needs might they have?)
2. How does it solve it? (Globally applicable concepts like commits/changesets,
   a log/history, and checking out historical tree states)
3. Why will we focus on Git in this class? (Widely used in industry and
   open-source)
4. Git vs GitHub (i.e. local vs remote repositories)

### Week 1, Lecture 2: Intro to Git & structure of a repo (VCS 2)

1. Live demo: show how to create a trivial Git repo, add commits, and move
   between them
2. Git data structures (commits, trees, blobs; the commit graph)
3. Operations on the index (`add`, `rm`, `mv`)
4. Operations on the commit graph (`commit`, `rebase`, `cherry-pick`, `merge`, `revert`)
5. Operations on the working tree (`checkout`, `stash`)

### Week 2, Lecture 1: Collaboration with Git (VCS 3)

1. What does it mean that Git is a DVCS? (No authoritative copy of any repo,
   all contain the same info. Use "torvalds/linux" as an example.)
2. Live demo of `git remote`: add SSH remote to homework server, push and pull
   from multiple computers / VMs
3. Operations to sync local and remote repos (`push`, `fetch`, `pull`)
4. Merge requests & patches (as a concept, not specifically GitHub PRs)
5. Using GitHub to host repositories (demo that basic functionality is
   identical to Git, but highlight extra features, e.g. Pull Requests)

### Week 2, Lecture 2: Git Internals (VCS 4)

1. What data is stored in each type of object (blob, tree, commit)?
2. UI representation of commits (as diffs from parent) vs internal
   representation (as complete trees), and performance implications
3. What is hashing? Why can't an object change and keep the same hash?
4. Implication: a commit hash depends on not only that commit's contents and
   metadata, but those of every commit before it in the entire lineage.

### Week 3, Lecture 1: Git Internals, continued (VCS 5)

1. What is a DAG? And why do Git graphs have to be acyclic?
2. What is a branch? (Just an alias to a hash; `cat .git/refs/heads/$BRANCH`)
3. Operations that "change" branches (`rebase`, `reset`) and what they actually
   do (construct a new history and redirect the branch)
4. Stale objects and `git gc`
5. Bare vs full repositories

### Week 3, Lecture 2: Survey of alternative and related tools (VCS 6)

1. "Batteries included" hosting services: GitHub, GitLab, Bitbucket, sourcehut,
   SourceForge
2. Other version control systems (Subversion, Mercurial, rcs, darcs, fossil,
   pijul, perforce, ...) and what they do differently
3. Why does Git have a staging area and other systems do not? Other interesting
   comparisons
4. Other tools: porcelains and UIs (gitk, gitkraken, ...), Gerrit, email patches

### Week 4, Lecture 1: Intro to Linux and the shell (Linux 1)

1. Survey the class to see what people have experienced in previous CS courses
   (What is a shell? What is a server? What is an operating system?)
2. What am I looking at here?
```
utln01@hw06> ls
...
utln01@hw06>
```
3. Poke around the home directory using `cd`, `ls`, and `cat`; show hierarchy
   with `tree` and file explorer GUI
4. What is Linux & how is it organized? `/bin`? `/etc`? `/proc`? `/sys`?
   `/comp`? `/dev`?
5. Permissions by example: what can we read, write, execute, list, etc in the
   above directories?
6. Fast facts for shell navigation (if you forget everything else)
   1. Read-eval-print-loop
   2. Commands take arguments and sometimes input from stdin
   3. You are navigating a hierarchical filesystem (files & folders)
   4. `man TOOL` for help with `TOOL` (including `man man`)
   7. Explain common instructions people have seen ("ssh into the homework
      server")

### Week 4, Lecture 2: Common tools (Linux 2)

1. Talk about argument parsing and flags
2. `grep`: simple text; line numbers and context; regular expressions; inverted
   matching
3. `find`: by name; `-delete`; `xargs`
4. `sed`
5. `man`: `man prog`; sections
6. `ln`: why would you ever want a link; symlinks; hardlinks
7. `top`/`htop`: what does this show you?
8. `tmux`
9. `diff`
10. `which`

### Week 5, Lecture 1: Interactive shell tips & tricks (Linux 3)

1. Tab completion
2. Command history search
3. Executing multiple commands using `;` and `&&` and `||`
4. Job control (`&`, <kbd>Ctrl</kbd>-<kbd>z</kbd>, `bg`, `fg`, `jobs`)
5. <kbd>Ctrl</kbd>-<kbd>r</kbd>
6. Dataflow and pipes and redirection (redirecting to files; redirecting files
   to stdin; redirecting stderr to stdout, aka `2>&1`)
7. Environment variables. `PATH`
8. Wildcards and globs

### Week 5, Lecture 2: The shell as a programming language (Linux 4)

1. Shell variables (and how they differ from environment variables)
2. Loops and control flow
3. Error handling (`set -euo pipefail` is your friend)
4. When NOT to use a shell script (non-textual operations, complex logic that
   can't be delegated to an existing tool, script grows to more than a
   screenful of code)
5. `#!` lines and how the kernel interprets them

### Week 6, Lecture 1: Behind the scenes (Linux 5)

1. How the shell interacts with the operating system (just like any program you
   write! Many shell features map very closely to kernel features, but those
   features aren't available only to shells)
2. How a program gets run (`fork` and `exec` syscalls)
3. How pipes and redirections work (file descriptors, `pipe` syscall)
4. How <kbd>Ctrl</kbd>-<kbd>c</kbd> and <kbd>Ctrl</kbd>-<kbd>z</kbd> work
   (signals)
5. Linux vs POSIX man pages (`man 2` vs `man 3`), and how they differ
   (implementation vs specification)

### Week 6, Lecture 2: Beyond Linux and POSIX (Linux 6)

1. Alternative shells on Linux (Bash, zsh, fish, oilshell, even PowerShell!)
2. Why can these shells run on Linux, BSD, and macOS but not on Windows?
   (Windows isn't POSIX)
3. The Windows command line (DOS shell, PowerShell) and graphical shell
4. Is there anything about the Windows kernel that makes it less suited to a
   command line interface? Anything about the Linux kernel that makes it less
   suited to a graphical interface? (No! That's just how the userspaces
   evolved)
5. Running POSIX environments on Windows with Cygwin and WSL. Running Windows
   apps on Linux and macOS with WINE. (Lesson: APIs are APIs)

### Week 7, Lecture 1: Intro to build systems (Build 1)

1. What problem do build systems solve? (Do you hate typing `g++` repeatedly to
   compile your projects? Do you hate waiting for your entire project to get
   rebuilt every time you make a change? How is a COMP 11 project different
   from another project - what different needs might they have?)
2. How does it solve it? (Specify end results and what their component parts
   are; let the tooling do the repetitive work)
3. Build systems can be closely tied to specific languages (mention `npm`,
   Python setuptools, Cargo, `go build`, Cabal, etc)
4. Why will we focus on Make in this class? (Doesn't assume a specific
   language, although definitely geared towards C; easily applicable to C/C++
   projects in Tufts CS classes; widely used in the real world)
5. Live demo: show how to write a trivial Makefile specifying a binary with .h,
   .cpp dependencies

### Week 7, Lecture 2: Intro to Make (Build 2)

1. Targets and rules
2. Dependency relations
3. The dependency graph (a DAG, just like Git uses!)
4. What happens when you type `make`
5. Why is a Makefile better than a shell script? (Better performance and
   correctness)

### Week 8, Lecture 1: The Make language (Build 3)

1. Variables
2. Special variables and implicit rules (i.e. convenience features for C
   projects)
3. Pattern rules, `.PHONY`, `@`
4. Macros and parse-time vs runtime evaluation (why you should avoid `$(shell)`
   unless you know what you're doing)
5. Imperative logic using macros and shell control flow; why it should be
   avoided if possible

### Week 8, Lecture 2: Large projects using Make (Build 4)

1. Problem: how to split project into multiple Makefiles?
2. Recursive make via submake invocations (read: Recursive Make Considered
   Harmful)
3. Case study: the Linux kernel
4. Whole-project make via include directives
5. Case study: Android

### Week 9, Lecture 1: How does compilation and linking work? (Build 5)

1. Compilation vs linking vs loading (What is a .o file? A .so file? An
   executable?)
2. Why a single `gcc` invocation with multiple C files doesn't scale
3. Separating compilation and linking into separate steps
4. Depending on system libraries (`-l`/`-L` linker flags, `-I` cflag,
   `LD_LIBRARY_PATH`)

### Week 9, Lecture 2: Other build systems and meta-tools (Build 6)

1. Why rebuild files if only their mtime changed? `ccache`
2. What happens if you have enormous amounts of software that take too long to
   compile on one computer? `distcc`/`icecc`, `bazel`, `buck`
3. What about other parts of the operating system that are not the files being
   built? Hermetic and reproducible builds, etc
4. What about building other things than C programs? Distributed rendering;
   package management for other languages like `cargo`, `npm`, `maven`
5. What if I hate writing all these rules by hand? (CMake, SCons, etc)
6. How to choose a build system
7. If your code belongs to a project or company with established tooling, use
   that. The benefits of doing your own thing are almost never worth it.
8. If your language has its own package ecosystem, use whatever the
   currently-recommended build tool for integrating with that ecosystem is.
9. If your project is small and you want it to be buildable on any POSIX system
   under the sun, use plain (read: non-GNU) Make.

### Week 10, Lecture 1: Intro to software correctness (Testing 1)

1. What does it mean for software to be correct? (End on "no bugs")
2. Why are bugs bad? (What is a spec? Is this a deviation from a spec?
   Specifications are implicit. If you and I say "tomorrow", we agree on what
   that means. Software is supposed to help people; it can't help people if it
   doesn't perform the way it's supposed to)
3. How do we minimize the number of bugs in software? (Proofs; types; testing)
4. "Beware of bugs in the above code; I have only proved it correct, not tried
   it." - Knuth
5. Mention throughout: surprising snippets about things people generally assume
   to be true or reliable: math (integer) - mention Gangnam Style view counter
   "overflow"; math (floating point); writing to disk
6. Mention: patriot missile floating point

### Week 10, Lecture 2: Philosophy of software testing (Testing 2)

1. Even simple software has edge cases. Complex software has many more edge
   cases.  Simple software has a few easily enumerable states. Complex software
   has very many more.
2. Have a green main branch: assume there are no bugs. If a change breaks
   something, it was most likely the change that introduced a bug.
   ("Regression")
3. You will write bugs. Even if they aren't bugs in the state-of-the-world at
   time of writing code, the world changes. It's not about how good you are as
   a programmer. Software interacts. Either implicitly (compiler, OS) or
   explicitly (using a library, RPC). Time.
4. Mention: Logan mentioning that recompiling for different computers will
   change his floating point math. Error propagation / AVX / ...
5. Mention: Google's new [CPU failures paper](https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s01-hochschild.pdf)

### Week 11, Lecture 1: Writing unit tests (Testing 3)

1. Write tests for functions, both internal and API.
2. Start with the specification: what should the function do? Test what is
   specified.
3. Write tests for things not mentioned in the specification that you think
   might break the function (big numbers, files that don't exist, etc -
   blackbox testing).
4. Write coverage-based tests for all the conditionals.
5. Write tests for edge cases in the operations inside the function (whitebox
   testing).
6. Test as little code as possible as directly as possible.
7. Avoid "round trips" through layers of software (including many function
   calls, or network requests, or disk I/O, etc).
8. Avoid stateful computation (requiring a file exist on disk, or a network
   request succeed, etc).
9. It's not a test unless you watch it fail.

### Week 11, Lecture 2: Testing interactions of complex systems (Testing 4)

1. What makes software difficult to test? (API surface is I/O heavy and not
   mockable; software is fundamentally nondeterministic; etc)
2. Factoring software for testability. Test from within, and optionally from
   without.
3. When you change your software, do you run the tests of everybody who uses
   your software?

### Week 12, Lecture 1: Continuous integration (Testing 5)

1. Tests should be run on trunk and change requests.
2. Introduction to GitHub Actions and writing manifests. (Survey: SourceHut
   builds?)
3. How can you test CI itself? Continuously monitor? Who watches the watcher?

### Week 12, Lecture 2: Other methods for ensuring software correctness (Testing 6)

1. Tests only make guarantees about the exposed runtime behavior of programs.
   This leaves us wanting for more.
2. Dynamic invariant checks inside software ("asserts"), which are especially
   helpful when they come with messages and context
3. Unit vs integration vs property vs regression vs proofs vs types & static
   analysis
4. What kinds of errors happen in a language like Ruby, Python, or JavaScript
   that do not happen in C? Or OCaml? Haskell? Idris? Agda?
5. What happens if you turn the problem on its head: the program is not
   complete until Coq is satisfied that you have written a correct proof?
6. What other guarantees can static analysis tools make that tests cannot test?
   Taint analysis? Internal NULL dereferences or overflows?
7. What about measuring performance as a feature, where slowdowns are
   regressions?
8. If your program runs at scale, can you collect logs of crashes and determine
   why they happened? Use that to fix bugs?

## Assignments

> Taken from Jeff Foster's COMP 121 syllabus.

Projects must be submitted electronically following the instructions given in
class. Projects may not be submitted by any other means (e.g., please do not
email your projects to us). It is your responsibility to test your program and
verify that it works properly before submitting. All projects are due at
11:59pm on the day indicated on the project assignment, according to the
submission server's internal clock. Your project score will be for the last
version of the project you submit.

You have two late tokens that you can use during the semester. Using one late
token allows you to submit one project up to 24 hours late with no penalty. You
may also use your two late tokens together to submit one project up to 48 hours
late with no penalty. Contact a TA if you need to check the status of your late
tokens.

### Git

We will have two assignments: one investigative ("reading") and one other one
("writing"). These assignments will be problem sets on repositories we provide
or of their own making. We will evaluate the work by examining the commit
history.

LO (reading): Students should be able to...

1. Examine the history and current branches of an existing Git repository using
   subcommands such as `branch` and `log`
2. Figure out who authored some code and in what context using `blame`


LO (writing): Students should be able to...

1. Create a new repository
2. Clone an existing repository
3. Create a commit in a repository
4. Create a branch
5. Merge one branch into another
6. Amend/rebase a commit
7. "Write something you hope to get out of this class in a commit message"

### Linux

Writing: CTF-like assignment like Bandit

Reading: Examine an existing project; Read a man page; Read a shell script and
figure out what it's doing? Track down a bug in a shell script? Extend a shell
script to do something new?

LO: Students should be able to...

1. Navigate a hierarchical filesystem using `cd` and `ls` and `pwd`
2. Explore unfamiliar directory structures using `grep`, `find`, `tree`, `du`
3. String together text processing commands such as `grep`, `wc`, `sed`, `cut`
   using pipes to solve a problem
4. Articulate the differences between types of files (regular, directory, link,
   device node)
5. Enumerate the system directories on a standard Linux installation that are
   likely to be involved when performing common operations (executing a
   program, loading libraries, loading config, compiling a program), including
   `$PATH` resolution
6. Set permissions on a file or directory given a list of who should be able to
   access it
7. Feel at home on the Linux command line

### Make

LO: Students should be able to...

1. Write an idiomatic Makefile to express basic C targets and explicitly list
   their interdependencies
2. Given an existing Makefile and target, determine what commands that target
   runs and what other targets it invokes
3. Use variables (in Makefiles, on the Make command line, and in the
   environment) to abstract behavior over different concrete parameters
4. Produce a shared object and link against it (incl. `LD_LIBRARY_PATH` or
   `DT_RUNPATH`)
5. Download an open source project (like scdoc, masscan, or ripme) and examine
   how the build system is put together.

### Testing

LO: Students should be able to...

1. Read a program and determine some effective coverage-based unit tests
2. Configure a basic GitHub Actions pipeline to build a project and run tests
   for each new commit
3. Write a regression test that fails on a specific piece of buggy code they're
   given, such that it will ensure that same bug does not get introduced again
4. Structure code such that their interfaces are testable and don't have hidden
   dependencies
5. Evaluate an existing project's testing infrastructure:
6. How does this project test itself?
7. How does this project do CI, if at all?

## Grading

Students will be evaluated 100% on homework assignments.

## Contributors

We consulted Ming Chow, Mike Shah, Chris Gregg, and Mark Sheldon while
developing this course.

These similar courses from other institutions inspired elements of this
proposal:

* MIT's [missing semester](https://missing.csail.mit.edu/)
* Berkeley's [EECS201](https://www.eecs.umich.edu/courses/eecs201/)
* Berkeley's [CS9E](https://www2.eecs.berkeley.edu/Courses/CS9E/)

<p style="position:relative;bottom:0; font-size:x-small;">The source of this
page is available <a href="https://github.com/tekknolagi/isdt">here</a>.</p>
