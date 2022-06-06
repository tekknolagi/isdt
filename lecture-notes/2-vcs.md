---
layout: spec
---

# Lecture Notes: Version Control Systems

# Lecture 1

## Module overview
Welcome to the second module of the course! This module is all about *version
control* systems. Version control (also known as *VCS* or *source control*)
tools record how your code has changed over time. Version control adds another
dimension to the files and directories you're used to: in a codebase tracked by
version control, you can not only ask "what are the contents of this file?" or
"what's in this directory?" but also "what version of this file am I looking
at?", "what was the last change made to this directory?", and other similar
questions.

Have you ever had a piece of code mysteriously break during development and
spent hours trying to figure out what changed? Or commented out a piece of code
instead of deleting it because you're afraid you'll eventually need it back? Or
copied your entire project directory before doing a big refactor in case
something goes wrong? Or accidentally deleted a file and lost days of work?
Scenarios like these are commonplace in codebases without version control, and
they only get worse as more code and collaborators are added.

With version control, every one of these scenarios can be resolved in a matter
of minutes by running one or two commands. Version control lets you develop
your code fearlessly, safe in the knowledge that every change you make is
recorded and reversible. Additionally, it brings those same guarantees to
changes made by others: each person working on your project can make changes to
their own copy without worrying that their hard work will be overwritten by
someone else.

The version control system we'll use in this course is called *Git*. Git is a
source control system originally written by Linus Torvalds to track the Linux
kernel's source code. Since its inception, it's emerged as the de facto source
control system for open-source projects across all platforms and fields of
software engineering[^github]. Git does not hold quite the same monopoly over
proprietary codebases you'll find at jobs and internships, but it's still very
common, especially at smaller companies that don't have the need or the
resources to develop their own source control systems.

We have chosen Git because it is ubiquitous. One of the main purposes of source
control is to collaborate with others, so it's especially important to learn a
system that potential collaborators will already know. Git is a mature and
fully-featured VCS, but it can be frustrating to learn at times: much like
Linux and POSIX, it was not architected but rather grew into what it is through
countless incremental changes. As such, its interface has warts and
inconsistencies that take some time to get used to. We'll try to point these
out as we encounter them; if you're ever in doubt, man pages are your friend!

[^github]: Git won the source control wars thanks in no small part to GitHub, a
    company that provides free centralized hosting of Git repositories. When
    GitHub launched in 2008, many found it to provide a user experience and
    feature set superior to more well-established competitors like SourceForge.
    As a result, open-source projects that may have otherwise picked a more
    mature VCS like Subversion instead chose Git so they could be on GitHub.
    However, make no mistake: GitHub and Git are *not* the same.

## Git is not GitHub
Before diving into Git, we'd like to take a moment to clear up a common
misconception among new Git users: *sites like GitHub, GitLab, Bitbucket, and
sourcehut are not part of Git and are not required to use Git*. These sites are
Git *hosts*, meaning they provide server space where you can upload copies of
repositories that you want to be easily available to anyone in the world. They
also provide friendly UIs for portions of Git's functionality, allowing you to
browse and even make commits to repositories straight from the web.

But everything these UIs do is simply a wrapper around what Git itself does.
Git is a (primarily) command-line tool that tracks the history of a directory
on your local computer. It requires no internet connection and no centralized
server[^dvcs]. Every copy (or *clone*) of a Git repository contains that
repository's entire history and allows the full set of operations that Git is
capable of.

This isn't to say that GitHub and the like aren't useful services: it's common
for the authoritative copy of a repository to live on GitHub, where it's
accessible to everyone and easy to browse without making a clone. But don't be
fooled into thinking that you need to make a GitHub account (or share your
project with the world) in order to use Git. Everything we're about to discuss
is just as applicable to a personal project that never leaves your personal
computer as it is to a project on GitHub with thousands of contributors.

[^dvcs]: The lack of a centralized server is a hallmark of *distributed*
    version control systems (DVCSes), of which Git is one. Most other modern
    source control systems (like Mercurial, Darcs, Fossil, and Pijul) are also
    distributed. Older source control systems (like Subversion, Perforce, and
    CVS) do require a central server by contrast.

## Repositories and commits
Before you can use Git to keep track of a directory, you have to create a
*repository* at that directory. A repository tracks a single project or group
of related files. It must be rooted at a directory, and it generally keeps
track of everything inside that directory, including subdirectories and their
contents. You can't make multiple repositories at the same directory, so you'll
want to create a separate directory for each of your projects---even those
which consist of only a single file.

When you create a repository at a directory, Git creates a directory named
`.git/` (note the dot, which prevents it from showing up in `ls`) in that
directory. `.git/` is what distinguishes a Git repository from a normal,
untracked directory. It's where Git stores metadata about old versions of your
files, and it's what the `git` command-line tool interacts with whenever you
perform a Git operation.

Apart from `.git/`, a Git repository looks and acts just like any other
directory: you can create and edit files using whatever tools you like, move
and copy them with `mv` and `cp`, search them with `grep`, and so
on[^check-out]. But, once you've made a change, you can ask Git to record that
change. If you decide you don't like the change, you can ask Git to restore the
affected file(s) to an earlier version. If you can't remember what you did
last, you can ask Git to show you all the changes a file has undergone. And
much more.

[^check-out]: Some older version control systems required you to manually
    "check out" a file before working on it, then manually "check it in" once
    you'd finished. This is moderately evocative of a library book or a shared
    notebook. Git does not require this: your code is considered permanently
    checked out, and it's only checked in when you take a snapshot of it by
    creating a commit.

In Git parlance, all the files outside `.git/` are called your *working tree*.
These files are the only things it expects you to work with directly. Under the
hood, it represents old versions of your files, as well as changes to those
files, using numerous *objects*, stored as binary files inside `.git/`. These
files are managed by Git, and you shouldn't modify them directly.

There are several types of object, but the only one you'll generally interact
directly with is called a *commit*. A commit represents the state of a
repository at some point in time: it holds a list of files, the contents of
those files, the date at which it was created, who created it, and a
user-provided description of what changed since the previous commit, which it
also stores a reference to. We'll talk more about commits shortly.

## Creating a repository
There are two main ways to make a repository, both of which use the Git
*subcommand* `git init`. If you want to make a new, empty repository, run `git
init myrepo` to make a directory called `myrepo/` with a `.git/` directory
inside it. If you want to track the files in an existing directory with Git,
you can navigate there and run `git init` to create a `.git/` directory
alongside your existing files.

Once you have a repository, you can run all sorts of other Git subcommands.
Each subcommand is basically its own command---they just all happen to be
implemented inside a single program, `git`. Each subcommand has its own man
page, whose name is prefixed with `git-`. For example, `man git-init`.

Try out the `git status` subcommand! `git status` tells you what Git thinks the
current state of things is. It shows you a helpful description of what's going
on, as well as some suggested things to do next. When you run it in a new
repository, it helpfully suggests that you make and *track* some
files:

```console
$ git status
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
$
```

(The "On branch main" message may be different for you, depending on both your
global Git configuration and your version of Git. Recent versions of Git have
moved away from the old default branch name of "master" in favor of "main".
We'll talk more about branches later.)

## Creating a commit
Let's follow Git's advice and track some files, which is the first step to
creating a commit. While we do so, let's also look at what's going on behind
the scenes in `.git/`! Although you shouldn't directly interact with `.git/`,
knowing how Git represents files and commits internally will make you a more
effective Git user, especially when things go wrong.

Start by taking a look at `.git/` in your new, empty repository. It has 8
directories and 16 files, but we'll focus on just a few:

```console
$ tree .git/
.git/
├── branches
├── config
├── description
├── HEAD
├── hooks
│   ├── <these template files have been omitted for brevity>
├── info
│   └── exclude
├── objects
│   ├── info
│   └── pack
└── refs
    ├── heads
    └── tags

9 directories, 16 files
$ 
```

The main thing to notice here is that the `objects` directory is empty, save
for a couple child directories that are also empty. As we mentioned before,
commits are objects. Commits also reference other objects, namely *trees* and
*blobs*, both of which we'll discuss shortly. But in this brand-new repository
with no commits, no objects exist yet.

Git won't let you make a commit unless something in your repository has
changed[^empty-commit]. So make a change by adding a new file:

[^empty-commit]: You can override this behavior with the `--allow-empty` flag,
    but the occasions you'll want to are few and far between.

```console
$ echo 'file contents' >myfile
$ 
```

Now, `git status` has more to tell us:

```console
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
    myfile

nothing added to commit but untracked files present (use "git add" to track)
$
```

Git doesn't magically watch as you make changes to a repository. In fact, Git
only does anything when you type `git`: unlike sync services such as Dropbox,
Git doesn't run in the background. When you run `git status`, you're asking Git
to take notice of all the changes you've made since your last commit and print
a summary of them. In the snippet above, Git noticed that you have a new and
untracked file named `myfile`. From Git's point of view, untracked files don't
exist: it will tell you about them in `git status`, but it won't include them
in commits, meaning it won't track their history.

To verify this, take a look at the `.git/` directory again and observe that
nothing has changed: no new objects are present, nor have any of the
files---`config`, `description`, `HEAD`, or `info/exclude`---been altered.

To track an untracked file, use the *git add* subcommand:

```console
$ git add myfile
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
    new file:   myfile

$
```

After running this, you'll finally see a change in your `.git/` directory!

```console
$ tree .git
.git
├── branches
├── config
├── description
├── HEAD
├── hooks
├── index
├── info
│   └── exclude
├── objects
│   ├── d0
│   │   └── 3e2425cf1c82616e12cb430c69aaa6cc08ff84
│   ├── info
│   └── pack
└── refs
    ├── heads
    └── tags

10 directories, 6 files

$
```
{: data-highlight="11-13" }

Git has created its first object, stored as the file
`.git/objects/d0/3e2425cf1c82616e12cb430c69aaa6cc08ff84`. As you'll soon see,
this object represents the contents of `myfile` as of when you ran `git add`.
Every Git object is identified by a *hash*, which is a long (in Git's case, 40
characters) string of letters and numbers that uniquely represent the
*contents* of that object[^content-addressing]. This latter point is important:
if two objects have exactly the same contents, they are guaranteed to also have
the same hash, meaning that they are the same object for all intents and
purposes.

[^content-addressing]: The strategy of naming objects based on their contents
    is known as [content-addressable
    storage](https://en.wikipedia.org/wiki/Content-addressable_storage). In
    most implementations, including Git's, a *cryptographic hash function* like
    [SHA-1](https://en.wikipedia.org/wiki/SHA-1) is used to produce a
    fixed-length hash derived entirely from the variable-length contents of a
    file---no filename involved. Such schemes assume that every hash value
    corresponds to exactly one file. Unfortunately, this assumption can never
    be entirely true because hash functions attempt to represent a
    potentially-infinite piece of data as a mere 40-byte hash. As such, there
    must be multiple files that produce the same hash, also known as
    collisions.  (This is called the pigeonhole principle.) The good news is
    that cryptographic hash functions are explicitly designed by very smart
    number theorists to make collisions hard to find, either intentionally or
    by accident. The bad news is that there are some very smart engineers who
    work on [breaking hash
    functions](https://elie.net/talk/how-we-created-the-first-sha1-collision-and-what-it-means-for-hash-security/).

We now have this mysterious thing in the `objects` subdirectory. At this point,
you should have the same file names. What is in that file, though? It's a
binary file (check it out with `file .git/objects/...`) but it's owned by Git
so we can take a look with `git show`. To do that, concatenate the directory
name (`d0`) with the filename `(e324...`)[^storage-limit]:

[^storage-limit]: Because of a limit to the number of files in a directory, Git
    breaks up long hash filenames. If every hashed object were in the top-level
    directory, we could end up with a huge number of files in `.git/objects/`.

```console
$ git show d03e2425cf1c82616e12cb430c69aaa6cc08ff84
file contents
$ 
```

Cool! It's the contents of our file. This file is in what's called the *staging
area*---tracked by Git, but not yet associated with any one commit. Let's
commit it. The following command by default opens up your editor---depending on
the environment variable `$EDITOR`, this could be Nano, Vim, Emacs, or
something else entirely.

```console
$ git commit
<editor opens>
<save and quit>
[main (root-commit) 2221050] My message
 1 file changed, 1 insertion(+)
 create mode 100644 myfile
$ 
```

Now you can consider your file well and truly version controlled. Not only is
it tracked by Git, but a version of it has also been checked in.

Git has printed us a summary of the commit object it has just created: it is on
branch `main`; it is the first commit on the branch (the "root commit"); it has
the hash `2221050`; the commit message is "My message"; it modified some files,
including a summary of the changes.

This is the point where your output might look different; the Git hashes
objects based on their contents, and Git includes the date and author name in
the commit. We will talk more about hashing later.

Let's take a look at the commit object `2221050` by running `git show`---which
defaults to showing our current commit:

```console
$ git show
commit 22210506499fe9e37086d3a5ff1fb8f400facd83 (HEAD -> main)
Author: Max Bernstein <max@thebiscuitsons.net>
Date:   Tue Sep 28 20:14:42 2021 -0700

    My message

diff --git a/myfile b/myfile
new file mode 100644
index 0000000..d03e242
--- /dev/null
+++ b/myfile
@@ -0,0 +1 @@
+file contents
$
```

This tells us some metadata about the commit object: the ID; the author; the
date; the message; what files changed. While `git show` is showing us a *diff*
of the file, it's important to note that Git stores *whole files* with every
commit, not changes. The output to `git show` computes these change
descriptions on the fly for your benefit.[^git-stores-trees]

[^git-stores-trees]: To verify this, look at the output of `git cat-file`:
    
    ```console
    $ git cat-file commit 22210506499fe9e37086d3a5ff1fb8f400facd83
    tree 8a2f7e211356a8551e2e2eed121d2a643208ac6a
    author Max Bernstein <max@thebiscuitsons.net> 1632885282 -0700
    committer Max Bernstein <max@thebiscuitsons.net> 1632885282 -0700
    
    My message
    $
    ```
    
    This shows a *tree* called `8a2f7e211356a8551e2e2eed121d2a643208ac6a`
    associated with the commit. And what is that tree?
    
    ```console
    $ git ls-tree 8a2f7e211356a8551e2e2eed121d2a643208ac6a
    100644 blob d03e2425cf1c82616e12cb430c69aaa6cc08ff84    myfile
    $
    ```
    
    Aha! It contains our whole file (`d03e`...) and associated metadata.

Feel free to take a look at the `.git/` directory again and see what the
objects are. You should be able to inspect any of them by using `git show`.

## Summary
So what did we learn? We learned that Git repositories contain files and
commits; the general write-add-commit flow; that all Git objects are stored in
`.git/objects/`; that any object can be inspected with `git show`. 

To learn more about a Git subcommand like `git show`, you can use `man
git-<subcommand>`, like `man git-show`.

# Subsequent lectures

Unfortunately, we have not been able to write lecture notes at the pace we
expected. No notes currently exist for lectures 2-6. We sincerely apologize for
this. We have made slide decks available for these lectures instead, which you
can access from the calendar on the main page. Note that the examples in the
slides reference the example Git repository at
`/comp/50ISDT/examples/git-zoo/`.
