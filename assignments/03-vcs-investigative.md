---
---

# Homework 3: VCS, Investigative

## Poking around a Git repo: first steps

Jim and Arnold Biscuitson have mostly recovered from that nasty shock of a
dinner party last month. To keep their minds off things, they have been baking.
They track their culinary adventures in a Git repository. This way, they can
collaboratively maintain a history of everything they buy, cook, and bake. We
have obtained this repository with the permission from the Biscuitsons and
stored a copy in `/comp/50ISDT/vcs1-biscuitsons`.

Please answer the following questions about their kitchen journal. For each,
try and come up with a command that produces the answer with the minimum amount
of human interpretation of the output; if a command prints all of the
information about every commit, try and pare down the command so that it
directly produces what you want. Provide *both* the answer and how you arrived
at that answer ("show your work"/"cite your sources"):

1. What is the difference between a commit date and an author date? Please
   explain in your own words.
1. What date did Jim get interested in baking? Please give the full author
   date.
1. How many grocery trips have there been?
1. How many committers are there? Who are they?
1. Who went and bought carrots? In what commit?
1. Which branch did Bridget use to submit her tips?
1. Who took the cookie from the cookie jar?

## Poking around a Git repo: round two

Git is not only used by fictional amateur bakers. Many software projects,
including most open source software, use Git to track code changes. GitHub is
one very popular Git hosting site that also provides additional web-based
features such as *Issues* (for tracking and discussing bugs and feature
requests) and *Pull Requests* (for proposing and reviewing code changes).

One project that does its primary development on GitHub is Visual Studio Code,
an open-source code editor maintained by Microsoft. For this piece of the
assignment, go to the VS Code repository on GitHub at
[microsoft/vscode](https://github.com/microsoft/vscode).

**If you are using the homework server:** You should have enough disk space to
download the repository (it weighs about 500MB), but if you do not, the EECS
staff have requested you email them at
[staff@eecs.tufts.edu](mailto:staff@eecs.tufts.edu) to request a quota
increase. In your email, you should mention this course (CS 50ISDT).

**If you are cloning to another computer:** Go for it, but we cannot guarantee
technical support.

For the following questions, please provide *both* the answer and how you
arrived at that answer ("show your work"/"cite your sources"). You are welcome
to attempt to answer these questions using the GitHub UI, but you may find it
easier to clone and use the CLI.

1. One of the most important things to know about an open-source project you're
   planning to use is whether it's actively maintained. The Git commit history
   can give you an indication of this.
   1. How long ago was the last VS Code commit? (This will change over time;
      it's fine to give your answer as of when you cloned the repo.)
   1. How many commits has it had in the past month, and by how many distinct
      people?
   1. On average, how many commits have been made per day since the project's
      inception?
1. Projects with lots of different contributors need a way to incorporate
   changes made by multiple people in parallel. VS Code is active enough that,
   by the time one contributor finishes their change, the commit they based
   that change on likely won't be the newest one anymore.
   1. What features of Git might you use to incorporate such changes into the
      main branch? Please explain in your own words.
   1. Do you see evidence of any of these features being used in VS Code's
      commit history? Please cite examples if so.
1. It is often useful to do a bit of code archaeology. Maybe you want to know
   what the original team was thinking when they first added a feature, or even
   who the initial team was. Or maybe you are just nosy and want to poke
   around.
   1. What was the first commit? Please provide the hash.
   1. How many files were in it?
   1. Who authored the commit 1aec7078c4d173ff15ca15ce8ffd1a276d9c03b9? What
      GitHub pull request does it belong to? This question requires some use of
      the GitHub UI.
   1. Comment on the quality of the commit message. What would you change about
      it? Why?
1. Reading the code doesn't always answer the questions you have. Often, you
   will have to read a project's documentation to understand why the authors
   designed something the way they did.
   1. Does the project have any documentation?
   1. What kinds of documentation does the project maintain, if more than one?
   1. Where is the documentation located? Is it version controlled?
1. VS Code comes with a number of extensions, located in the `extensions/`
   directory, which provide support for specific languages and tools. New
   extensions are added regularly as people contribute support for their
   favorite language or tool.
   1. What was the last modification to the Git extension (`extensions/git`)?
      Please provide the commit's date and commit message.

## Submitting your work

You should write your answers in a file, `answers.txt`, split into two
sections.

Please submit with `provide comp50isdt vcs-investigative answers.txt`. You must
be logged into the homework server to use Provide.
