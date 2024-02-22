---
---

# Lecture Notes: Version Control Systems

## Lecture 1

### Module overview
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

### Git is not GitHub
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

### Repositories and commits
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
with directly is called a *commit*. A commit represents the state of a
repository at some point in time: it holds a list of files, the contents of
those files, the date at which it was created, who created it, and a
user-provided description of what changed since the previous commit, which it
also stores a reference to. We'll talk more about commits shortly.

### Creating a repository
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
current state of things is. It shows you a description of what's going on, as
well as some suggested things to do next. When you run it in a new repository,
it helpfully suggests that you make and *track* some files:

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

### Staging files
Tracking a file means asking Git to add it to the *staging area*, also known as
the *index*. The staging area is part of a Git repository that records which
changes from the working tree are ready to be committed. When you create a new
commit, its contents are taken from the staging area.

TODO: Add a diagram showing how changes flow from working tree to staging area
to commits.

Many other version control systems don't have a staging area---commits are
created directly from the changes you make in the working tree. This is a
simpler model, but it can make it harder to work on multiple changes
simultaneously. Programmers disagree on whether the benefits of a staging area
warrant the extra complexity and steeper learning curve.

The subcommand you'll use most often to work with Git's staging area is `git
add`. Let's use it to track a file! While we do so, let's also look at what's
going on behind the scenes in `.git/`! Although you shouldn't directly interact
with `.git/`, knowing how Git represents files and commits internally will make
you a more effective Git user, especially when things go wrong.

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

Git doesn't magically watch as you make changes to a repository. Unlike sync
services such as Dropbox, which continuously run in the background, Git only
does stuff when you ask it to. When you run `git status`, you're asking Git to
take notice of all the changes you've made since your last commit and print a
summary of them. In the snippet above, Git noticed that you have a new and
untracked file named `myfile`. From Git's point of view, untracked files don't
exist: it will tell you about them in `git status`, but it won't include them
in commits, meaning it won't track their history.

To verify this, take a look at the `.git/` directory again and observe that
nothing has changed: no new objects are present, nor have any of the
files---`config`, `description`, `HEAD`, or `info/exclude`---been altered.

To tell Git that the file exists and you plan to commit it, add it to the
staging area with `git add`:

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

Git has created its first object, stored as the file
`.git/objects/d0/3e2425cf1c82616e12cb430c69aaa6cc08ff84`[^storage-limit]. As
you'll soon see, this object represents the contents of `myfile` as of when you
ran `git add`. Every Git object is identified by a *hash*, which is a long (in
Git's case, 40 characters) string of letters and numbers that uniquely
represent the *contents* of that object[^content-addressing]. This latter point
is important: if two objects have exactly the same contents, they are
guaranteed to also have the same hash, meaning that they are the same object
for all intents and purposes.

[^storage-limit]: You may wonder why the first two digits of the object's hash,
    `d0`, are used as a directory name inside `.git/objects/`. This is because
    some (mostly older) filesystems fail or slow down when a single directory
    holds too many files. To prevent the `.git/objects/` directory from
    directly containing tens or hundreds of thousands of files, Git splits the
    objects into subdirectories based on how their hashes happen to start.

[^content-addressing]: The strategy of naming objects based on their contents
    is known as [content-addressable
    storage](https://en.wikipedia.org/wiki/Content-addressable_storage).  Most
    implementations, including Git, use a *cryptographic hash function* like
    [SHA-1](https://en.wikipedia.org/wiki/SHA-1) to derive a fixed-length hash
    from the variable-length contents of a file. The hash depends only on the
    file's contents---not on its filename or anything else.

    Such schemes assume that every hash uniquely identifies the data used to
    calculate it. Unfortunately, this assumption is never true in all cases:
    because hash functions convert a potentially-infinite data stream into a
    fixed-length hash (40 bytes for SHA-1), there always exist multiple data
    streams that "collide" and produce the same hash. (This happens in any
    situation where a function has fewer possible outputs than possible inputs
    and is known as the [pigeonhole
    principle](https://en.wikipedia.org/wiki/Pigeonhole_principle).)

    The good news is that cryptographic hash functions like SHA-1 are
    explicitly designed by very smart number theorists so that collisions are
    hard to find, either intentionally or by accident. The bad news is that
    there are some very smart engineers who spend their time trying to outsmart
    the number theorists and find efficient ways to [produce
    collisions](https://elie.net/talk/how-we-created-the-first-sha1-collision-and-what-it-means-for-hash-security/).

So what's in this object? If you try to read the file directly, using `cat` for
example, you'll see that it contains binary data that can't be meaningfully
interpreted as text[^file-command]. But luckily, since the file is part of
Git's object store, we can use the `git show` subcommand to decode it:

[^file-command]: Tip: the `file` command tries to guess what kind of data a
    file holds. Try it out on the object!

```console
$ git show d03e2425cf1c82616e12cb430c69aaa6cc08ff84
file contents
$ 
```

Cool! It's the contents of your file. The file is now in the staging
area---tracked by Git, but not yet associated with a commit. Each commit you
make records the contents of the staging area, so the next commit will include
your file.

### Creating a commit
To make a commit, run `git commit`. By default, `git commit` opens a text
editor for you to write your commit message and waits until you save and close
the message to make the commit. (The specific editor used depends on the
`$EDITOR` environment variable and often defaults to Vim or Vi.)

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
it tracked by Git, but its contents have been recorded into your project's
history as part of a commit.

Git has printed us a summary of the commit object it created: the commit is on
branch `main`, it's the first commit on that branch (the "root commit"), its
hash starts with `2221050` (the rest is omitted for brevity), its commit
message is "My message", and it contains one new file compared to its parent
(which, in this case, does not exist and so has no files).

This is the point where your output will look different: like all Git objects,
commits are assigned hashes based on their contents, and a commit's contents
include the name and email of its author as well as its creation date. Since
these will be different for you, your commit will have a different hash than
ours even though its file tree and message are identical.

TODO: Side/foot note with command that specifies time, committer, and other
data such that hash is identical.

Let's take a look at the commit object by running `git show`---which when given
no arguments shows the current commit:

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

This tells us some metadata about the commit object: the hash; the author; the
date; the message; what files changed. While `git show` is showing us a *diff*
of the file, it's important to note that Git stores *whole files* with every
commit, not changes. `git show` computes the diff between a commit and its
parent on the fly for your benefit.[^git-stores-trees]

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

If you inspect the `.git/` directory again, you'll see that Git has created
another new object in addition to the commit. This is a *tree* object, and it's
the only type of Git object we haven't discussed yet. Tree objects are
analogous to directories: they're the bridge between blob objects, which
represent a single file's contents, and commit objects, which hold the metadata
of a commit. Each tree object holds a list of filenames, each one referencing
either a blob object or another tree object. By following these references, Git
can reconstruct the complete set of files and directories that the tree
contains. Each commit references a single tree object.

TODO: Diagram showing how a change to a single file propagates up the tree and
eventually results in a different commit hash. (Or maybe just a tree hash?
Since commits have different timestamps by nature.)

### Summary
So what did we learn? We learned that Git repositories contain files and
commits; the general write-add-commit flow; that all Git objects are stored in
`.git/objects/`; that any object can be inspected with `git show`. 

To learn more about a Git subcommand like `git show`, you can use `man
git-<subcommand>`, like `man git-show`.

## Lecture 2

CONTENTS: Git for solo development

### Making good commits
Let's step back from the nitty-gritty of Git's internals and talk about how you
as a developer can use Git to make your life easier. Although Git has a truly
dizzying number of different subcommands, you've already seen most of the ones
you'll use frequently! By running `git add` and `git commit` repeatedly as you
make changes to your code, you build your repository's commit history.

When things go awry or you come back to the project after a while away, you'll
use other subcommands to work with that history (and you'll be grateful for
them!). And when you want to collaborate with others, you'll use even more. All
those subcommands operate on the commit history, though: if you don't make good
commits regularly, they won't be able to help you.

What is a "good" commit? In short, it's one that

1. Represents a single conceptual change to your code
1. Explains why you made that change clearly and concisely

Let's discuss these two properties in detail:

#### One commit per change
You should make each commit as small as you can while keeping it self-contained.
For code, "self-contained" means that a commit leaves the code in at least as
good a state as it found it (e.g. it doesn't break things and rely on a
subsequent commit to fix them) and expresses a complete idea (e.g. it doesn't
add a comment without also adding the code that comment goes with).

There are several reasons to follow this guideline: for one, Git allows you to
move, delete, and/or reorder commits. These operations only make sense if each
commit can stand on its own[^bisect]. If a commit breaks your build unless the
subsequent one is also present, any such operation will have to treat both as a
single unit and so they might as well have just been one to begin with.

[^bisect]: Another subcommand, `git bisect`, takes this to the extreme: it
    attempts to find where a bug was introduced by testing your code at
    arbitrary points along its commit history. If your commits aren't self-
    contained, it's practically impossible to use `git bisect` because commits
    are constantly breaking and fixing things.

    Ensuring each commit stands alone is also known as "keeping the `main`
    branch green," and we'll talk about it more in the final module.

Conversely, if you get in the habit of stuffing several changes into the same
commit, Git also becomes less useful. Subcommands such as `git revert`---which
undoes a commit's changes---work best when commits are as granular as possible.
In fact, Git makes it almost impossible to work with historical changes more
granular than a commit.

As you gain experience with Git, you'll learn how much granularity works best
for you---everyone's workflow is different, and one developer's sweet spot might
feel frustratingly verbose to another. Even for a single developer, the sweet
spot often shifts as a project matures: early commits that add lots of code are
almost universally less granular than later ones that fix bugs or maintain
existing code. Regardless of your preference, it ought to guide Git---not the
other way around.

#### Thoughtful commit messages
Good commits explain the changes they contain. This may sound simple---and
self-contained commits certainly make it simpler---but even so, there's an art
to writing good commit messages that can take some time to master.

A bad commit message might clearly *describe* exactly what the commit does and
yet fail to *explain* the commit. The difference between the two is subtle but
important: it's the difference between

> Use `.equals()` instead of `==` for strings
>
> Replace uses of `a == b`, when a and b are strings, with `a.equals(b)` in
> modules foo, bar, and baz.

and

> Fix false-negative string comparisons
>
> It turns out that `==` in Java compares pointers instead of object contents.
> This has been causing some strings to compare unequal to other strings with
> identical contents, resulting in intermittent failed logins attempts as well
> as other issues. Fix the problem by calling `.equals()` instead.

Even though the second message says less about *what* the commit does, it says
far more about *why*. Messages like that make it far easier for future
maintainers (you included!) to understand the commit's intent.

Beyond their substance, the commit messages above adhere to some stylistic
conventions that are common (but not universal) among projects that use Git.
Those conventions are strongly influenced by the [Linux kernel's commit
guidelines][kernel-commits], since that project is where Git originated. Here
are the basics of that style:

[kernel-commits]: https://www.kernel.org/doc/html/latest/process/submitting-patches.html#describe-your-changes

1. Every commit message begins with a title on its own line, followed optionally
   by a blank line and a longer description. This expectation is baked into Git
   itself, and as such nearly everyone agrees on it.
1. The title is 50 characters or less and written in an imperative style (e.g.
   "Fix foobar" instead of "Fixed foobar" or just "Foobar"). The length limit is
   not typically enforced strictly, but it helps keep titles readable at a
   glance.
1. The body is line-wrapped at 72 characters and organized into paragraphs.
   References to other commits in the body take the form `commit 123456789abc
   ("Fix foobar")`, where `123456789abc` is the first 12 characters of the other
   commit's hash and "Fix foobar" is its title.

Not everyone likes these particular conventions, and many projects set their own
commit message style. Nonetheness, most projects agree that consistent styling
across commits is a good thing, as it makes commit histories easier to read and
makes collaboration easier.

### Staging files partially (`git add -p`)
If you try to follow our advice using the commands we've covered so far, you'll
soon find that it's very difficult to create tidy commits when you can only
stage changes on a file-by-file basis (`git add <file>`). The process of
software development is rarely as organized as a Git history should be: while
working on one change, for example, you might see other issues in the same file
and fix them on the fly.

But doesn't that force you to put both your original change and your quick fix
in the same commit, since `git add` stages every change in the file? You might
already be thinking of clever workarounds---like making a temporary copy of the
file and then undoing one of the changes---but there's a better solution.

`git add -p` is that solution, but Git beginners often don't even know it
exists. Unlike plain `git add` (or worse, `git commit -a`, which commits every
change in every file), `git add -p` lets you partially stage a file. When
invoked, it displays each block of modified lines (called a *hunk*) in sequence
and asks you whether or not to stage it[^add-p-editing]. As usual, a subsequent
`git commit` will include only the staged hunks, letting you quickly and easily
distribute your changes across multiple commits.

[^add-p-editing]: You can also choose to edit a hunk before staging it, which
    will cause `git add -p` to open a text editor where you can modify or delete
    lines. This isn't typically necessary, but it helps when unrelated changes
    are close enough together that Git counts them as a single hunk. (For
    changes that are close but not directly adjacent, you can also ask `git add
    -p` split the hunk into multiple smaller hunks and prompt for each.)

```
TODO: Example of `git add -p` to stage specific hunks that have changed.
Demonstrate committing multiple changes separately with good messages.
```

### Bringing it all together

*Note: this section has a whole lot of commands all in a row. Please skim them,
but don't worry about understanding everything right away. You'll come back to
this section in more manageable portions as you read the rest of the module,
which uses this repository as an example.*

With `git add -p` and some commit guidelines under your belt, you have
everything you need to start tracking a project's history in Git. Here's how
that might look for a simple project (which will look familiar once you begin
Homework 4!). First, you create a repository:

```console?prompt=$
$ mkdir calc
$ cd calc
$ git init
Initialized empty Git repository in /home/you/calc/.git/
$ 
```

Then, you commit some initial code:
```console?prompt=$
$ cat main.c
int main() {
  printf("Hello, world!\n");
  return 0;
}
$ git add main.c
$ git commit -m "Initial commit"
[main (root-commit) 3ba2a93] Initial commit
 1 file changed, 3 insertions(+)
 create mode 100644 main.c
$ 
```

You fix mistakes in the code, using the handy `git diff` subcommand to view your
unstaged changes (think of it like the `diff` command, except it compares files
to Git's staging area instead of to other files).
```console?prompt=$
$ git diff
diff --git a/main.c b/main.c
index fbd71ab..aed773b 100644
--- a/main.c
+++ b/main.c
@@ -1,3 +1,5 @@
+#include <stdio.h>
+
 int main() {
   printf("Hello, world!\n");
   return 0;

$ git add main.c
$ git commit -m "Add #include directives to fix compilation"
[main a83e7a6] Add #include directives to fix compilation
 1 file changed, 2 insertions(+)
$ 
```

...continue working on `main.c`...
```c
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

int calc(int left, char op, int right) {
  <some code>
}

int main(int argc, char **argv) {
  if (argc != 4) {
    fprintf(stderr,
            "Usage: %s <num> <op> <num>\nWhere <op> is one of +, -, *, /.\n",
            argv[0]);
    return EXIT_FAILURE;
  }
  const char *left_str = argv[1];
  const char *op_str = argv[2];
  const char *right_str = argv[3];
  errno = 0;
  int left = strtol(left_str, NULL, 10);
  if (errno != 0) {
    perror(argv[0]);
    return EXIT_FAILURE;
  }

  <some more code>

  int result = calc(left, op_str[0], right);
  fprintf(stdout, "%d\n", result);
  return 0;
}
```

```console?prompt=$
$ git add main.c
$ git commit -m "Make main a simple calculator"
[main 1838eea] Make main a simple calculator
 1 file changed, 45 insertions(+), 2 deletions(-)
$ 
```

...make some smaller edits...
```diff
$ git diff
diff --git a/main.c b/main.c
index 7e2b75d..9407af1 100644
--- a/main.c
+++ b/main.c
@@ -12,6 +12,8 @@ int calc(int left, char op, int right) {
     return left * right;
   case '/':
     return left / right;
+  case  '%':
+    return left % right;
   }
   fprintf(stderr, "Unrecognized op `%c'.\n", op);
   exit(EXIT_FAILURE);
@@ -19,16 +21,21 @@ int calc(int left, char op, int right) {

 int main(int argc, char **argv) {
   if (argc != 4) {
-    fprintf(stderr,
-            "Usage: %s <num> <op> <num>\nWhere <op> is one of +, -, *, /.\n",
-            argv[0]);
+    fprintf(
+        stderr,
+        "Usage: %s <num> <op> <num>\nWhere <op> is one of +, -, *, /, %%.\n",
+        argv[0]);
     return EXIT_FAILURE;
   }
   const char *left_str = argv[1];
   const char *op_str = argv[2];
   const char *right_str = argv[3];
   errno = 0;
-  int left = strtol(left_str, NULL, 10);
+  char *endptr;
+  int left = strtol(left_str, &endptr, 10);
+  if (left_str == endptr) {
+    errno = EINVAL;
+  }
   if (errno != 0) {
     perror(argv[0]);
     return EXIT_FAILURE;
@@ -38,7 +45,10 @@ int main(int argc, char **argv) {
     return EXIT_FAILURE;
   }
   errno = 0;
-  int right = strtol(right_str, NULL, 10);
+  int right = strtol(right_str, &endptr, 10);
+  if (right_str == endptr) {
+    errno = EINVAL;
+  }
   if (errno != 0) {
     perror(argv[0]);
     return EXIT_FAILURE;
```

...and commit each one separately:
```console?prompt=$
$ git add -p
diff --git a/main.c b/main.c
index 7e2b75d..9407af1 100644
--- a/main.c
+++ b/main.c
@@ -12,6 +12,8 @@ int calc(int left, char op, int right) {
     return left * right;
   case '/':
     return left / right;
+  case  '%':
+    return left % right;
   }
   fprintf(stderr, "Unrecognized op `%c'.\n", op);
   exit(EXIT_FAILURE);
(1/3) Stage this hunk [y,n,q,a,d,j,J,g,/,e,?]? ?
y - stage this hunk
n - do not stage this hunk
q - quit; do not stage this hunk or any of the remaining ones
a - stage this hunk and all later hunks in the file
d - do not stage this hunk or any of the later hunks in the file
j - leave this hunk undecided, see next undecided hunk
J - leave this hunk undecided, see next hunk
g - select a hunk to go to
/ - search for a hunk matching the given regex
e - manually edit the current hunk
? - print help
@@ -12,6 +12,8 @@ int calc(int left, char op, int right) {
     return left * right;
   case '/':
     return left / right;
+  case  '%':
+    return left % right;
   }
   fprintf(stderr, "Unrecognized op `%c'.\n", op);
   exit(EXIT_FAILURE);
(1/3) Stage this hunk [y,n,q,a,d,j,J,g,/,e,?]? y
@@ -19,16 +21,21 @@ int calc(int left, char op, int right) {

 int main(int argc, char **argv) {
   if (argc != 4) {
-    fprintf(stderr,
-            "Usage: %s <num> <op> <num>\nWhere <op> is one of +, -, *, /.\n",
-            argv[0]);
+    fprintf(
+        stderr,
+        "Usage: %s <num> <op> <num>\nWhere <op> is one of +, -, *, /, %%.\n",
+        argv[0]);
     return EXIT_FAILURE;
   }
   const char *left_str = argv[1];
   const char *op_str = argv[2];
   const char *right_str = argv[3];
   errno = 0;
-  int left = strtol(left_str, NULL, 10);
+  char *endptr;
+  int left = strtol(left_str, &endptr, 10);
+  if (left_str == endptr) {
+    errno = EINVAL;
+  }
   if (errno != 0) {
     perror(argv[0]);
     return EXIT_FAILURE;
(2/3) Stage this hunk [y,n,q,a,d,K,j,J,g,/,s,e,?]? s
Split into 2 hunks.
@@ -19,12 +21,13 @@ int calc(int left, char op, int right) {

 int main(int argc, char **argv) {
   if (argc != 4) {
-    fprintf(stderr,
-            "Usage: %s <num> <op> <num>\nWhere <op> is one of +, -, *, /.\n",
-            argv[0]);
+    fprintf(
+        stderr,
+        "Usage: %s <num> <op> <num>\nWhere <op> is one of +, -, *, /, %%.\n",
+        argv[0]);
     return EXIT_FAILURE;
   }
   const char *left_str = argv[1];
   const char *op_str = argv[2];
   const char *right_str = argv[3];
   errno = 0;
(2/4) Stage this hunk [y,n,q,a,d,K,j,J,g,/,e,?]? y
@@ -25,10 +28,14 @@
     return EXIT_FAILURE;
   }
   const char *left_str = argv[1];
   const char *op_str = argv[2];
   const char *right_str = argv[3];
   errno = 0;
-  int left = strtol(left_str, NULL, 10);
+  char *endptr;
+  int left = strtol(left_str, &endptr, 10);
+  if (left_str == endptr) {
+    errno = EINVAL;
+  }
   if (errno != 0) {
     perror(argv[0]);
     return EXIT_FAILURE;
(3/4) Stage this hunk [y,n,q,a,d,K,j,J,g,/,e,?]? q

$ git commit -m "Support the modulo operator"
[main 8ad441d] Support the modulo operator
 1 file changed, 6 insertions(+), 3 deletions(-)
$ 
```

```console?prompt=$,quote>
$ git add -p
diff --git a/main.c b/main.c
index 0b5f470..9407af1 100644
--- a/main.c
+++ b/main.c
@@ -31,7 +31,11 @@ int main(int argc, char **argv) {
   const char *op_str = argv[2];
   const char *right_str = argv[3];
   errno = 0;
-  int left = strtol(left_str, NULL, 10);
+  char *endptr;
+  int left = strtol(left_str, &endptr, 10);
+  if (left_str == endptr) {
+    errno = EINVAL;
+  }
   if (errno != 0) {
     perror(argv[0]);
     return EXIT_FAILURE;
(1/2) Stage this hunk [y,n,q,a,d,j,J,g,/,e,?]? y
@@ -41,7 +45,10 @@ int main(int argc, char **argv) {
     return EXIT_FAILURE;
   }
   errno = 0;
-  int right = strtol(right_str, NULL, 10);
+  int right = strtol(right_str, &endptr, 10);
+  if (right_str == endptr) {
+    errno = EINVAL;
+  }
   if (errno != 0) {
     perror(argv[0]);
     return EXIT_FAILURE;
(2/2) Stage this hunk [y,n,q,a,d,K,g,/,e,?]? y

$ git commit -m 'Detect errors when parsing numbers
quote>
quote> strtol can signal error via errno, but it can also report when it
quote> stopped parsing input. This is helpful for determining if the input was
quote> not a number, or at least did not start with a digit.'
[main 6fd624e] Detect errors when parsing numbers
 1 file changed, 9 insertions(+), 2 deletions(-)
$ 
```

### How Git helps you

The example above may have left you confused about the exact commits it actually
made. Although running the commands yourself is generally less confusing than
reading a transcript of them, it can still be hard to remember what you've
committed and when.

Fortunately, the entire purpose of Git is to make it so you don't have to
remember! At long last, it's time to talk about all the Git subcommands that let
you do interesting things based on the commits you've made. The next lecture and
a half will be a whirlwind tour of some of those subcommands.

#### Viewing commits

We already demonstrated `git show` in the last lecture, but there we mainly used
it to inspect various types of Git objects. During normal Git usage, `git show`
almost exclusively operates on commits, and it has several features for doing so
that we haven't yet covered.

With no arguments, `git show` shows the most recent commit. Interestingly, `git
show HEAD` does the exact same thing. `HEAD` is what's known as a *revision
parameter*---an argument to a subcommand that names one or more commits. The
most direct way to name a commit is to specify its hash, like so:

```console
$ git show a83e7a6c4e9844b745a22450b69892d2292d8c7e
commit a83e7a6c4e9844b745a22450b69892d2292d8c7e
Author: Thomas Hebb <tommyhebb@gmail.com>
Date:   Tue Jan 30 22:59:25 2024 -0500

    Add #include directives to fix compilation

diff --git a/main.c b/main.c
index fbd71ab..aed773b 100644
--- a/main.c
+++ b/main.c
@@ -1,3 +1,5 @@
+#include <stdio.h>
+
 int main() {
   printf("Hello, world!\n");
   return 0;
$ 
```

But no one would use Git if the only way to reference a commit was to memorize a
40-digit pseudorandom identifier. Luckily, Git offers several simpler ways to
refer to commits. For example, you can omit the end of a commit hash as long as
the piece you do provide is unambiguous[^ambiguous-hashes]:

[^ambiguous-hashes]: If a prefix matches multiple hashes, you'll see an error
    like this:

    ```console?prompt=$
    $ git log abcde2
    error: short object ID abcde2 is ambiguous
    hint: The candidates are:
    hint:   abcde22a7cfe tree
    hint:   abcde2851321 tree
    hint:   abcde2f236a0 blob
    fatal: ambiguous argument 'abcde2': unknown revision or path not in the working tree.
    ```

    That example is from the Linux kernel's Git repository, where 6-character
    conflicts are incredibly common and many 7+ character ones exist too. Linux
    developers are currently advised to use 12 digits of a commit's hash to
    uniquely identify it, enough to make the probability of a conflict near
    zero.

```console
$ git show a83e7a6
commit a83e7a6c4e9844b745a22450b69892d2292d8c7e
Author: Thomas Hebb <tommyhebb@gmail.com>
Date:   Tue Jan 30 22:59:25 2024 -0500

    Add #include directives to fix compilation

diff --git a/main.c b/main.c
index fbd71ab..aed773b 100644
--- a/main.c
+++ b/main.c
@@ -1,3 +1,5 @@
+#include <stdio.h>
+
 int main() {
   printf("Hello, world!\n");
   return 0;
```

To refer to the current commit, you can use the special name `HEAD`. And to
refer to a commit's parent, you can suffix its hash or name with the character
`^`[^nesting]:

[^nesting]: A revision ending in `^` is still a revision, so you can suffix it
    with another `^` to go to *its* parent, and so forth as many times as you
    like. Git has a shorthand for this: `<commit>^N` means the Nth parent of
    `<commit>`, e.g. `HEAD^5`.

```console
$ git show HEAD^
commit 8ad441d1469c3e23bd7a261f9145f64179364c7c
Author: Thomas Hebb <tommyhebb@gmail.com>
Date:   Wed Jan 31 21:17:45 2024 -0500

    Support the modulo operator

diff --git a/main.c b/main.c
index 7e2b75d..0b5f470 100644
--- a/main.c
+++ b/main.c
@@ -12,6 +12,8 @@ int calc(int left, char op, int right) {
     return left * right;
   case '/':
     return left / right;
+  case  '%':
+    return left % right;
   }
   fprintf(stderr, "Unrecognized op `%c'.\n", op);
   exit(EXIT_FAILURE);
@@ -19,9 +21,10 @@ int calc(int left, char op, int right) {

 int main(int argc, char **argv) {
   if (argc != 4) {
-    fprintf(stderr,
-            "Usage: %s <num> <op> <num>\nWhere <op> is one of +, -, *, /.\n",
-            argv[0]);
+    fprintf(
+        stderr,
+        "Usage: %s <num> <op> <num>\nWhere <op> is one of +, -, *, /, %%.\n",
+        argv[0]);
     return EXIT_FAILURE;
   }
   const char *left_str = argv[1];
$ 
```

You can also reference commits using branch and tag names, which we'll talk
about next lecture, among many other methods. And this syntax isn't specific to
`git show`: revision parameters are accepted by most Git subcommands, including
many of those we're about to cover. To see every form a revision parameter can
take, check out `man gitrevisions`.

With that diversion out of the way, let's get back to `git show`: as you can see
in the examples above, not only does it print a commit's metadata and message,
it also prints the diff between that commit and its parent (`<commit>^`, in our
newly-acquired terminology). In Git, every commit has exactly one
parent[^multiple=children], so such a diff is always well-specified.

[^multiple-children]: Although a commit's parent is unique and unambiguous, the
    same cannot be said of its children. In fact, it would be quite time
    consuming for Git to enumerate a commit's children, so there's no built-in
    primitive to do so.

#### Viewing history

Given that every commit (except the first one) has a parent, which in turn has
its own parent, you might naturally want to view all a commit's ancestors. To do
so, you can use `git log`:

```console?prompt=$
$ git log
commit 6fd624ec083a21b76a0879697974ccc3820e14e8 (HEAD -> main)
Author: Thomas Hebb <tommyhebb@gmail.com>
Date:   Wed Jan 31 21:23:10 2024 -0500

    Detect errors when parsing numbers

    strtol can signal error via errno, but it can also report when it
    stopped parsing input. This is helpful for determining if the input was
    not a number, or at least did not start with a digit.

commit 8ad441d1469c3e23bd7a261f9145f64179364c7c
Author: Thomas Hebb <tommyhebb@gmail.com>
Date:   Wed Jan 31 21:17:45 2024 -0500

    Support the modulo operator

commit 1838eeae89ba4cc4068bff8a1c99c0a9b0853506
Author: Thomas Hebb <tommyhebb@gmail.com>
Date:   Wed Jan 31 21:07:08 2024 -0500

    Make main a simple calculator

commit a83e7a6c4e9844b745a22450b69892d2292d8c7e
Author: Thomas Hebb <tommyhebb@gmail.com>
Date:   Tue Jan 30 22:59:25 2024 -0500

    Add #include directives to fix compilation

commit 3ba2a935126dafc8d4acb96df131bad26cb37396
Author: Thomas Hebb <tommyhebb@gmail.com>
Date:   Tue Jan 30 22:57:04 2024 -0500

    Initial commit
$ 
```

`git log` doesn't show diffs by default. But it does accept several flags to
alter its behavior, including

- **`--patch` (`-p`)**: Show each commit's diff, just like `git show`
- **`--oneline`**: Show each commit in a condensed format on a single line

```console?prompt=$
$ git log --oneline
6fd624e (HEAD -> main) Detect errors when parsing numbers
8ad441d Support the modulo operator
1838eea Make main a simple calculator
a83e7a6 Add #include directives to fix compilation
3ba2a93 Initial commit
$ 
```

Like `git show`, `git log` accepts a revision parameter indicating which
commit's *ancestors* (i.e. commits reachable by recursively following that
commit's parent) to show[^git-log-args]. You'll typically pass it either a
branch name or no argument at all (to show the ancestors of `HEAD`).

[^git-log-args]: Unlike `git show`, `git log` can  take multiple revision
    parameters, which together specify a precise set of commits to show. Here's
    how that works:

    - Each normal revision parameter tells `git log` to show that commit and all
      its ancestors.
    - Revision parameters prefixed with `^` (i.e. `^<commit>`) tell `git log`
      not to show them or their ancestors, even if it otherwise would.
    - The shorthand `<earliest>..<latest>` shows only the ancestors of
      `<latest>` that came after `<earliest>`­---in other words, the range of
      commits between `<earliest>` and `<latest>` It's equivalent to `git log
      <latest> ^<earliest>`.

    For example:

    ```console?prompt=$
    $ git log 1838eeae..HEAD
    commit 6fd624ec083a21b76a0879697974ccc3820e14e8 (HEAD -> main)
    Author: Thomas Hebb <tommyhebb@gmail.com>
    Date:   Wed Jan 31 21:23:10 2024 -0500

        Detect errors when parsing numbers

        strtol can signal error via errno, but it can also report when it
        stopped parsing input. This is helpful for determining if the input was
        not a number, or at least did not start with a digit.

    commit 8ad441d1469c3e23bd7a261f9145f64179364c7c
    Author: Thomas Hebb <tommyhebb@gmail.com>
    Date:   Wed Jan 31 21:17:45 2024 -0500

        Support the modulo operator
    $ 
    ```

    Instead of showing the entire history, this log cuts off right where commit
    1838eeae89ba ("Make main a simple calculator") would appear. 

To further narrow `git log`'s output, you can also pass it one or more file
paths within your repository to see only commits that affect those files. This
is extremely useful in large repositories where changes to a given file or
directory are often interspersed among hundreds of unrelated commits:

```
TODO: our example repo only has one file :( Worth adding one more commit with a
different file, or is it fine to omit this example?
```

There's a pitfall here, though: since `git log` takes multiple revision
parameters (see footnote) and also multiple file paths, it can be ambiguous
where the revision list ends and the file list begins. For example, imagine
running `git log main` to see the history of a file named `main`. If your
repository also has a branch named `main`, that command will show the branch's
history, not the file's!

We mention this case not because it's common but because it's extremely
confusing if you encounter it unawares. Luckily, there's an easy way to ensure
you never encounter it: put `--` before your path list to tell `git log` exactly
where it starts:

```console?prompt=$
$ git log --oneline HEAD ^1838eeae -- main.c
6fd624e (HEAD -> main) Detect errors when parsing numbers
8ad441d Support the modulo operator
$ 
```

In our hypothetical example, you could see the history of `main` the file,
instead of `main` the branch, by running `git log -- main`.

#### Seeing what's changed

We briefly mentioned `git diff` in the example above, but it's worth talking
about the different modes it can run in. By default, `git diff` compares code in
the working tree to the code in the staging area, meaning it shows you unstaged
changes.

But like `git log`, `git diff` can be given a commit as an argument, which
causes it to compare the working tree to that commit. For example, `git diff
HEAD` will show every uncommitted change, even ones you've staged.

TODO: diff between two commits, `--cached`, `--no-index`, filename filtering

#### Undoing mistakes

TODO: Using `git revert` to undo an old change.

#### Going back in time

TODO: Using `git restore` to restore a file to an older version. Mention that
`git checkout` did this in older version of git, but that wasn't its primary
purpose.

#### Saving changes for later

TODO: Using `git stash` to put away and restore changes that you're working on.

#### Seeing who changed a line (`git blame`)

TODO: Introduction to `git blame`. General workflow of `git blame`, `git show`
`git log <rev>^ --`, and repeat until you've found what you want.

#### Finding bugs

TODO: Using `git bisect` to figure out what change broke your program. Only one
or two paragraphs---we don't want to overwhelm them.

TODO: In lecture, let's include an impressive demo to hook them on the
possibilities of Git.

## Lecture 3

CONTENTS: More complex workflows

### Branches

TODO: "What is a branch?" paragraph. A convenient name you can use to reference
a specific variant of your code or set of changes you're working on.

TODO: Examples of what branches might be used for. Classify into long-lived
branches and development/feature branches.

TODO: The concept of main/trunk/master as the main place where you commit new
code and the one long-lived branch you can rely on virtually every project to
have. Discussion of other long-lived branches you might encounter, like release
branches that live for a fixed period and only take bug fixes from master.
Real-world examples of where these are used (e.g. Firefox, Linux) and where a
"main-only" model works instead (e.g. websites).

TODO: Instructions on creating local branches. Demonstration of branching off
points earlier in the history.

TODO: Using "git checkout" to switch branches. Discussion of how checkout is
a very overloaded command, and how to identify this particular mode of it. Also
maybe mention "git checkout -b" to create+checkout a branch in one go. Mention
that you can checkout a commit hash as well.

### Referencing commits

TODO: Talk about refs and how branches are just one type of ref. Explain
`.git/refs/` directory and how different types of refs live in different
subdirectories (which are sometimes inferred for ease of use).

TODO: `HEAD` as a special ref pointing to your current checkout.

TODO: Talk about how either hashes or ref names can be used to refer to a
commit. Hashes are immutable, while refs may change. Say that either method
can be used in nearly every place you see us using one of them.

TODO: There are operators that let you "move around" from a ref. For example,
`^` gets a ref's parent commit. Namedrop `man gitrevisions`.

### Exploring multiple branches

TODO: `git log --graph`. example Demonstrate logging different branches and
logging from a given commit hash (to build on previous section).

### Moving commits between branches ("So You Think You Can Branch?")

TODO: Make sure this section is clear on the three ways to integrate changes:
fast-forwarding, merging, and rebasing.

TODO: `git merge` for pulling in an entire history wholesale without rewriting
it. Talk about fast-forward merges.

TODO: `git cherry-pick` for "replaying" a specific commit from one branch on top
of another.

TODO: `git rebase` for doing lots of charry-picks in a row automatically.

### Rewriting history

TODO: This can mostly come from our existing slide.

TODO: Talk about interactive rebasing for squashing/prettifying.

### Odds and ends

#### Ignoring generated files (`.gitignore`)

#### Seeing a ref's history (`git reflog`)

## Lecture 4

CONTENTS: Collaboration with Git

### Sharing branches with others

TODO: What's a remote? Example of `git remote add` and `git remote -v`. Talk
about different remote protocols.

TODO: Can either `git fetch` from or `git push` to a remote. These update
*remote-tracking branches*, which can then be used to update your local
branches via `git merge --ff-only` or `git rebase`. Mention `git pull` is a
shortcut for fetch+merge but can be unintuitive.

### `git clone` for making a local copy of a remote repo

### Tracking branches

TODO: Ugh, I still don't understand the full semantics of these. Figure it out
and write it down.

## Lecture 5

CONTENTS: Collaboration in practice

### Common development models

TODO: Single "upstream" copy of the repo that's the source of truth.
Maintainers merge changes to it and many "downstreams" maintain changes based
on it.

### Merge/pull requests and patches

TODO: Git has no built-in way to propose a change. So lots of solutions for
proposing and reviewing changes before they're merged upstream have emerged.
Talk about mailing lists, GitHub model, Phabricator model.

### Integrating changes: merging vs squashing vs rebasing

TODO: Take content from my GitHub comment here:
  https://github.com/tekknolagi/isdt/pull/15#issuecomment-920592835

TODO: Examples of prominent projects that use various models.

### Git forges

TODO: Copy from slides. Hosting services and the functionality they provide.

### Aside: bare repositories

TODO: Hosting your own upstream means letting people push to any branch, plus
you don't need a working copy. How to achieve that with bare repos.

## Lecture 6

TODO: Copy in survey stuff from slides
