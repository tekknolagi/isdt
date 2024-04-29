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

```console?prompt=$
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

```console?prompt=$
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

```console?prompt=$
$ echo 'file contents' >myfile
$ 
```

Now, `git status` has more to tell us:

```console?prompt=$
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

```console?prompt=$
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

```console?prompt=$
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

```console?prompt=$
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

```console?prompt=$
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

```console?prompt=$
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
    
    ```console?prompt=$
    $ git cat-file commit 22210506499fe9e37086d3a5ff1fb8f400facd83
    tree 8a2f7e211356a8551e2e2eed121d2a643208ac6a
    author Max Bernstein <max@thebiscuitsons.net> 1632885282 -0700
    committer Max Bernstein <max@thebiscuitsons.net> 1632885282 -0700
    
    My message
    $ 
    ```
    
    This shows a *tree* called `8a2f7e211356a8551e2e2eed121d2a643208ac6a`
    associated with the commit. And what is that tree?
    
    ```console?prompt=$
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
undoes a commit---work best when each commit holds only one functional change.

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

TODO: expand on what parts of the code snippets to pay attention to

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

...add a Makefile (a sneak peek of module 3!)...

```make
all: main

main: main.c
	gcc main.c -o main

.PHONY: clean
clean:
	rm -f main
```

...commit it...

```console?prompt=$
$ git add Makefile
$ git commit -m "Add a simple Makefile"
[main 01302bc] Add a simple Makefile
 1 file changed, 8 insertions(+)
 create mode 100644 Makefile
$ 
```

...fix some bugs...

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
[main 2d66030] Support the modulo operator
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
[main 221af3e] Detect errors when parsing numbers
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

```console?prompt=$
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
    $ 
    ```

    That example is from the Linux kernel's Git repository, where 6-character
    conflicts are incredibly common and many 7+ character ones exist too. Linux
    developers are currently advised to use 12 digits of a commit's hash to
    uniquely identify it, enough to make the probability of a conflict near
    zero.

```console?prompt=$
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

```console?prompt=$
$ git show HEAD^
commit 2d6603026105b168c126d2ee22c6f4dba8d48437
Author: Thomas Hebb <tommyhebb@gmail.com>
Date:   Wed Feb 21 23:07:15 2024 -0500

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
it also prints what changed between that commit's tree and its parent's
(`<commit>^`, in our newly-acquired terminology). In Git, every commit has
exactly one parent[^multiple=children], so such a diff is always well-specified.

[^multiple-children]: A commit's parent is unique and unambiguous, as its hash
    is stored in the commit. The same is not true of its children, though: the
    only way to enumerate a commit's children is bt checking every other commit
    in the repository. That's quite inefficient, and there's no built-in
    primitive to do it.

#### Viewing history

Given that every commit (except the first one) has a parent, which in turn has
its own parent, you might naturally want to view all a commit's ancestors. To do
so, you can use `git log`:

```console?prompt=$
$ git log
commit 221af3ea46453739392720c56fd44c92124c50fe (HEAD -> main)
Author: Thomas Hebb <tommyhebb@gmail.com>
Date:   Wed Feb 21 23:09:36 2024 -0500

    Detect errors when parsing numbers

    strtol can signal error via errno, but it can also report when it
    stopped parsing input. This is helpful for determining if the input was
    not a number, or at least did not start with a digit.

commit 2d6603026105b168c126d2ee22c6f4dba8d48437
Author: Thomas Hebb <tommyhebb@gmail.com>
Date:   Wed Feb 21 23:07:15 2024 -0500

    Support the modulo operator

commit 01302bc5eb8bbefb9a70366952e478c6af4841e2
Author: Thomas Hebb <tommyhebb@gmail.com>
Date:   Wed Feb 21 23:04:35 2024 -0500

    Add a simple Makefile

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
221af3e (HEAD -> main) Detect errors when parsing numbers
2d66030 Support the modulo operator
01302bc Add a simple Makefile
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
    $ git log 01302bc5..HEAD
    commit 221af3ea46453739392720c56fd44c92124c50fe (HEAD -> main)
    Author: Thomas Hebb <tommyhebb@gmail.com>
    Date:   Wed Feb 21 23:09:36 2024 -0500

        Detect errors when parsing numbers

        strtol can signal error via errno, but it can also report when it
        stopped parsing input. This is helpful for determining if the input was
        not a number, or at least did not start with a digit.

    commit 2d6603026105b168c126d2ee22c6f4dba8d48437
    Author: Thomas Hebb <tommyhebb@gmail.com>
    Date:   Wed Feb 21 23:07:15 2024 -0500

        Support the modulo operator
    $ 
    ```

    Instead of showing the entire history, this log cuts off right where commit
    01302bc5eb8b ("Add a simple Makefile") would appear. 

To further narrow `git log`'s output, you can also pass it one or more file
paths within your repository to see only commits that affect those files. This
is extremely useful in large repositories where changes to a given file or
directory are often interspersed among hundreds of unrelated commits:

```console?prompt=$
$ git log --oneline Makefile
01302bc Add a simple Makefile
$ 
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
$ git log --oneline -- Makefile
01302bc Add a simple Makefile
$ 
```

In our hypothetical example, you could see the history of `main` the file,
instead of `main` the branch, by running `git log -- main`.

#### Seeing what's changed

We briefly mentioned `git diff` in the example above, but it's worth talking
about the different modes it can run in. By default, `git diff` compares code in
the working tree to the code in the staging area, meaning it shows you unstaged
changes.

If you instead want to see staged changes (i.e. what will go in your next
commit), you can run `git diff --cached`. (Apparently Git's developers weren't
satisfied with two terms, "index" and "staging area", for the same thing, as
they sometimes also call it the *cache*.)

For example, let's say we've made two changes to `main.c` but only staged one of
them:

```console?prompt=$
$ git add -p
diff --git a/main.c b/main.c
index 9407af1..ede468c 100644
--- a/main.c
+++ b/main.c
@@ -3,6 +3,7 @@
 #include <stdlib.h>

 int calc(int left, char op, int right) {
+  fprintf(stderr, "DEBUG: op is %c\n", op);
   switch (op) {
   case '+':
     return left + right;
(1/2) Stage this hunk [y,n,q,a,d,j,J,g,/,e,?]? n
@@ -54,6 +55,6 @@ int main(int argc, char **argv) {
     return EXIT_FAILURE;
   }
   int result = calc(left, op_str[0], right);
-  fprintf(stdout, "%d\n", result);
+  printf("%d\n", result);
   return 0;
 }
(2/2) Stage this hunk [y,n,q,a,d,K,g,/,e,?]? y

$ 
```

We can now use `git diff` like this:

```diff
$ git diff
diff --git a/main.c b/main.c
index 2ff8c48..ede468c 100644
--- a/main.c
+++ b/main.c
@@ -3,6 +3,7 @@
 #include <stdlib.h>

 int calc(int left, char op, int right) {
+  fprintf(stderr, "DEBUG: op is %c\n", op);
   switch (op) {
   case '+':
     return left + right;
$ git diff --cached
diff --git a/main.c b/main.c
index 9407af1..2ff8c48 100644
--- a/main.c
+++ b/main.c
@@ -54,6 +54,6 @@ int main(int argc, char **argv) {
     return EXIT_FAILURE;
   }
   int result = calc(left, op_str[0], right);
-  fprintf(stdout, "%d\n", result);
+  printf("%d\n", result);
   return 0;
 }
$ 
```

`git diff` can be given a revision parameter, which causes it to compare the
working tree to that commit. For example, `git diff HEAD` will show every
uncommitted change, even ones you've staged. By adding a second revision
parameter, you can compare two commits directly:

```diff
$ git diff 1838eea HEAD
diff --git a/Makefile b/Makefile
new file mode 100644
index 0000000..6003f4b
--- /dev/null
+++ b/Makefile
@@ -0,0 +1,8 @@
+all: main
+
+main: main.c
+       gcc main.c -o main
+
+.PHONY: clean
+clean:
+       rm -f main
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

Like `git log`, `git diff` can filter its output by file path. The argument
syntax is identical---a list of one or more file paths after all other
arguments, optionally preceded by `--` to eliminate ambiguity:

```diff
$ git diff 1838eea HEAD -- Makefile
diff --git a/Makefile b/Makefile
new file mode 100644
index 0000000..6003f4b
--- /dev/null
+++ b/Makefile
@@ -0,0 +1,8 @@
+all: main
+
+main: main.c
+       gcc main.c -o main
+
+.PHONY: clean
+clean:
+       rm -f main
```

One final note about `git diff`: Git has become so ubiquitous that diffs from
`git diff` are much more widely accepted than those from `diff` itself. Although
`diff` can emulate Git's style with the `-u` flag, it's not a perfect match and
doesn't support some advanced features of `git diff`, such as binary file
diffing. If you want to `git diff` two arbitrary files (like you'd run `diff`),
you can use its `--no-index` flag: `git diff --no-index <file1> <file2>`. This
even works outside a Git repository!

#### Undoing mistakes

Viewing past changes is well and good, and it'll often help you figure out why
the code you've been editing has mysteriously stopped working. But once you've
figured out the problem, what can you do about it? You could hope that your text
editor's undo history is long enough; you could copy and paste individual lines
from the output of `git diff` or `git show`. Or, you could use one of several
Git subcommands, detailed in the next few sections, that use your Git history to
make useful changes to the working tree.

`git revert` is one such command. Given a revision parameter, `git revert`
generates a new commit that undoes the changes of just the specified commit,
preserving changes from other intervening commits:

```console?prompt=$
$ git revert 2d66030
Auto-merging main.c
<editor opens>
<save and quit>
[main 0fb5235] Revert "Support the modulo operator"
 1 file changed, 3 insertions(+), 6 deletions(-)
$ 
```

This results in a new commit, whose changes are immediately reflected in the
working tree:

```console?prompt=$
$ git log --oneline
0fb5235 (HEAD -> main) Revert "Support the modulo operator"
221af3e Detect errors when parsing numbers
2d66030 Support the modulo operator
01302bc Add a simple Makefile
1838eea Make main a simple calculator
a83e7a6 Add #include directives to fix compilation
3ba2a93 Initial commit
$ git show HEAD
commit 0fb52357b6d1c76bda2d33890e1c8d2cd36ec792 (HEAD -> main)
Author: Thomas Hebb <tommyhebb@gmail.com>
Date:   Wed Feb 28 22:35:12 2024 -0500

    Revert "Support the modulo operator"

    This reverts commit 2d6603026105b168c126d2ee22c6f4dba8d48437.

diff --git a/main.c b/main.c
index 9407af1..56ef02d 100644
--- a/main.c
+++ b/main.c
@@ -12,8 +12,6 @@ int calc(int left, char op, int right) {
     return left * right;
   case '/':
     return left / right;
-  case  '%':
-    return left % right;
   }
   fprintf(stderr, "Unrecognized op `%c'.\n", op);
   exit(EXIT_FAILURE);
@@ -21,10 +19,9 @@ int calc(int left, char op, int right) {

 int main(int argc, char **argv) {
   if (argc != 4) {
-    fprintf(
-        stderr,
-        "Usage: %s <num> <op> <num>\nWhere <op> is one of +, -, *, /, %%.\n",
-        argv[0]);
+    fprintf(stderr,
+            "Usage: %s <num> <op> <num>\nWhere <op> is one of +, -, *, /.\n",
+            argv[0]);
     return EXIT_FAILURE;
   }
   const char *left_str = argv[1];
$ head -n 20 main.c
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

int calc(int left, char op, int right) {
  switch (op) {
  case '+':
    return left + right;
  case '-':
    return left - right;
  case '*':
    return left * right;
  case '/':
    return left / right;
  }
  fprintf(stderr, "Unrecognized op `%c'.\n", op);
  exit(EXIT_FAILURE);
}

int main(int argc, char **argv) {
$ 
```

The generated commit removes just the changes introduced in commit 2d6603026105
("Support the modulo operator") but doesn't touch the bug fix from commit
221af3ea4645 ("Detect errors when parsing numbers"), even though that commit
came later.

TODO: resolving merge conflicts

#### Aside: rewriting history

If you find it odd that `git revert` creates a new "undo" commit instead of
deleting the original commit, you're not alone: new users of Git often seek to
delete or edit a commit after it's made, assuming that to be the right way to
fix mistakes. Although the "right" way to use Git, like any tool, is ultimately
up to its user, there are at least two reasons why most collaborative Git
workflows only revise existing commits in very specific situations:

Firstly, Git arguably makes it impossible to edit a commit in the traditional
sense. Git identifies a commit by its hash, but that hash is derived from the
commit's contents: by changing the contents, you change the hash, making the
resulting "edited" commit no different from an entirely new commit that just
happens to have similar contents to the original. To underscore that fact (and
match Git's documentation), from now on we'll say that such commits have been
"*rewritten*" rather than "edited".

The ease of rewriting a commit depends on how many places that commit is
referenced, both implicitly (e.g. by children, branches, and other copies of the
repository) and explicitly (e.g. by commit messages and documentation).
References by child commits pose the biggest problem, as you can only update
children by rewriting them (and all their transitive children) as well!

So, although it's easy to rewrite a commit immediately after you make it (and,
in fact, `git commit --amend` does exactly that), it's difficult and inadvisable
to rewrite a commit with a significant number of references, especially in
projects with multiple collaborators who each have a copy of the repository.
There are Git commands, like `git rebase` and the much riskier `git
filter-repo`, which do so nonetheless, but you should use those judiciously and
only in accordance with what your collaborators on a given project expect.

Hopefully this illustrates the technical reason why `git revert` creates a new
commit instead of rewriting history. But there's also a second reason why, which
is that an accurate history helps us as developers: just because a commit wasn't
perfect doesn't mean it holds no value. Keeping reverted commits in the history
lets us retry them, reproduce the conditions that led to the revert, and see (in
the revert's message) important context about what went wrong. So even if it
were easy to edit commits, `git revert` would likely work just the same.

#### Going back in time

We discussed in Lecture 1 how each commit holds a snapshot of all the files in
your repository. Git has several subcommands that let you inspect those
snapshots or bring back their contents.

To view a file as it was at a given commit, you can use a special form of `git
show`. Imagine that, after reverting the modulo operator from your calculator,
you want to reference its code for use in another project. Instead of trying to
reconstruct the code in your head from diffs, you can run the following
(`2d6603026105` being the "Support the modulo operator" commit):

```console?prompt=$
$ git show 2d6603026105:main.c
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

int calc(int left, char op, int right) {
  switch (op) {
  case '+':
    return left + right;
  case '-':
    return left - right;
  case '*':
    return left * right;
  case '/':
    return left / right;
  case  '%':
    return left % right;
  }
  fprintf(stderr, "Unrecognized op `%c'.\n", op);
  exit(EXIT_FAILURE);
}

int main(int argc, char **argv) {
  if (argc != 4) {
    fprintf(
        stderr,
        "Usage: %s <num> <op> <num>\nWhere <op> is one of +, -, *, /, %%.\n",
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
  if (op_str[1] != '\0') {
    fprintf(stderr, "Op must be one character. Got `%s'.\n", op_str);
    return EXIT_FAILURE;
  }
  errno = 0;
  int right = strtol(right_str, NULL, 10);
  if (errno != 0) {
    perror(argv[0]);
    return EXIT_FAILURE;
  }
  int result = calc(left, op_str[0], right);
  fprintf(stdout, "%d\n", result);
  return 0;
}
$ 
```

By adding a colon and file path to the revision parameter, you tell `git show`
that, instead of showing the commit, it should print the given file from the
tree the commit references. And indeed, the output shows `main.c` as it was when
the modulo operator was first added. Unlike `git revert`, this command neither
makes a commit nor alters the working tree---it just prints to the terminal.

If you want to change the file on disk instead of printing it, you can use `git
restore`:

```console?prompt=$
$ git status
On branch main
nothing to commit, working tree clean
$ git restore --source 2d6603026105 main.c
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   main.c

no changes added to commit (use "git add" and/or "git commit -a")
$ cat main.c
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

int calc(int left, char op, int right) {
  switch (op) {
  case '+':
    return left + right;
  case '-':
    return left - right;
  case '*':
    return left * right;
  case '/':
    return left / right;
  case  '%':
    return left % right;
  }
  fprintf(stderr, "Unrecognized op `%c'.\n", op);
  exit(EXIT_FAILURE);
}
<snip>
$ 
```

This retrieves the same past version of `main.c` from the Git history
but---instead of printing it---writes it directly to the working tree. The
revision to restore is specified using the `-s`/`--source` flag. Unlike `git
revert`, `git restore` does not create a new commit or stage the changes,
meaning they show up in `git status` and `git diff` like if you'd made them
manually.

There's also a third way to go back in history---`git checkout`. Like `git
restore`, `git checkout` changes the working tree. But it doesn't leave those
changes unstaged; instead, it moves `HEAD` to point to the given commit,
resulting in no unstaged *or* staged changes---since Git shows changes relative
to `HEAD`!

```console?prompt=$
$ git checkout 2d6603026105
Note: switching to '2d6603026105'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 2d66030 Support the modulo operator
$ cat main.c
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

int calc(int left, char op, int right) {
  switch (op) {
  case '+':
    return left + right;
  case '-':
    return left - right;
  case '*':
    return left * right;
  case '/':
    return left / right;
  case  '%':
    return left % right;
  }
  fprintf(stderr, "Unrecognized op `%c'.\n", op);
  exit(EXIT_FAILURE);
}
<snip>
$ git status
HEAD detached at 2d66030
nothing to commit, working tree clean
$ 
```

As Git helpfully informs us, checking out a raw commit hash isn't the typical
use of `git checkout`, as it it puts your repository into a state called
"detached HEAD", where new commits aren't tracked as part of a branch. Until we
discuss branches next lecture, don't worry too much about that: just run `git
checkout main` to get back to your latest change before making any new commits.

It's worth noting that, if you pass file paths to `git checkout` after the
revision parameter, it acts like `git restore`: `git checkout 2d6603026105
main.c` does exactly the same thing as `git restore -s 2d6603026105 main.c`,
meaning it doesn't move `HEAD`. Since every other form of `git checkout` does
move `HEAD`, Git's developers eventually identified this one as the odd one out,
decided to give it its own subcommand, and `git restore` was born.

#### Saving changes for later

The development workflow we've depicted so far---where you make a complete,
self-contained change in the working tree, use `git add` to record that change
in the index, and finally use `git commit` to save it to a commit---is sadly
quite idealistic. In reality, you'll often find yourself juggling several tasks
at once. For example, while refactoring some code, you may notice a bug that you
want to investigate by checking out an older commit. But upon using your
newfound `git checkout` skills to do so, you might see something like this:

```console?prompt=$
git checkout 2d6603026105
error: Your local changes to the following files would be overwritten by checkout:
	main.c
Please commit your changes or stash them before you switch branches.
Aborting
$ 
```

The cause of this is your half-finished refactor, which you haven't committed
yet:

```diff
$ git diff
diff --git a/main.c b/main.c
index 56ef02d..6f0fa39 100644
--- a/main.c
+++ b/main.c
@@ -1,6 +1,7 @@
 #include <errno.h>
 #include <stdio.h>
 #include <stdlib.h>
+#include <stdbool.h>

 int calc(int left, char op, int right) {
   switch (op) {
@@ -17,6 +18,23 @@ int calc(int left, char op, int right) {
   exit(EXIT_FAILURE);
 }

+// Converts the string str into an integer using strtol.
+// Returns 1 and stores the result in resultp on success.
+// Returns 0 and sets errno otherwise.
+bool to_int(const char *str, int *resultp) {
+  char *endptr;
+  errno = 0;
+  int result = strtol(str, &endptr, 10);
+  if (str == endptr) {
+    errno = EINVAL;
+  }
+  if (errno != 0) {
+    return false;
+  }
+  *resultp = result;
+  return true;
+}
+
 int main(int argc, char **argv) {
   if (argc != 4) {
     fprintf(stderr,
@@ -29,11 +47,8 @@ int main(int argc, char **argv) {
   const char *right_str = argv[3];
   errno = 0;
   char *endptr;
-  int left = strtol(left_str, &endptr, 10);
-  if (left_str == endptr) {
-    errno = EINVAL;
-  }
-  if (errno != 0) {
+  int left;
+  if (!to_int(left_str, left)) {
     perror(argv[0]);
     return EXIT_FAILURE;
   }
```

Git sees that you've modified `main.c`, so it refuses to check out any other
version of that file for fear of destroying your modifications! Although this is
a nice safety feature, it can be annoying: you're not ready to commit your
refactor---it crashes and introduces a compiler warning---but you have more
important things to do than debug it. So what can you do?

One option is to commit the unfinished change and finish it in a later commit.
Although this violates our rule that each commit should be complete and
self-contained, it can be a viable strategy if the refactoring work is on its
own branch---more on that next lecture. Assuming you don't want to do that,
though, there's another option available to you: `git stash`.

`git stash` is a bit like `git commit` in that it saves changes from the working
tree to a more permanent location. Unlike `git commit`, however, those changes
don't become part of the Git history. Instead, they're saved in a special area
called the *stash*, which unlike the history is neither linear nor shared
between different copies of the repository. The stash is intended to hold
in-progress or experimental changes that you want to temporarily remove from the
working tree.

To create a new stash entry, type `git stash` (which is shorthand for `git stash
push`). That moves all uncommitted changes, staged or not, to the stash and
leaves your working tree clean:

```console?prompt=$
$ git stash
Saved working directory and index state WIP on main: 0fb5235 Revert "Support the modulo operator"
$ git status
On branch main
nothing to commit, working tree clean
$ cat main.c
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

int calc(int left, char op, int right) {
  switch (op) {
  case '+':
    return left + right;
  case '-':
    return left - right;
  case '*':
    return left * right;
  case '/':
    return left / right;
  }
  fprintf(stderr, "Unrecognized op `%c'.\n", op);
  exit(EXIT_FAILURE);
}

int main(int argc, char **argv) {
<snip>
$ 
```

Notice that your changes to `main.c` (like the new `to_int()` function) are no
longer present! Let's see where they've gone:

```console?prompt=$
$ git stash list
stash@{0}: WIP on main: 0fb5235 Revert "Support the modulo operator"
$ git stash show
 main.c | 25 ++++++++++++++++++++-----
 1 file changed, 20 insertions(+), 5 deletions(-)
$ 
```

There's now one stash entry, named `stash@{0}`[^stash-reflog], which contains
your changes. By default, `git stash show` shows a short summary of the most
recent stash entry. You can make it show the full diff with the `--patch`/`-p`
flag, and you can make it show a different stash entry by passing the entry's
name (e.g. `stash@{1}`, `stash@{2}`, etc.) as an argument.

[^stash-reflog]: Stash entries are numbered using the somewhat unwieldy `@{}`
    syntax because, under the hood, stash entries are stored as commits pointed
    to by a ref called `stash`. Once you learn about refs and `git reflog`, try
    running `git reflog stash`. Does the output look familiar? Then look up
    `@{}` in `man gitrevisions` and see how it connects!

`git stash pop` restores a stash entry to the working tree. By default, it
restores the latest one (hence the push/pop terminology---the stash is last-in
first-out, just like a stack), but you can also explicitly specify an earlier
one as an argument. You can restore stash entries even if your working tree has
changed since they were created: that's because `git stash pop` applies the
*diff* from the entry to the current working tree, whatever its contents.

Popping a stash entry removes it from the stash, unless the restored changes
conflict with the current state of the working tree, in which case it's kept in
the stash for extra safety. For the same reason, you cannot pop a change that
would overwrite unstaged working tree changes at all. `git stash apply` is like
`git stash pop`, except it never removes the stash entry.

```console?prompt=$
$ git stash pop
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   main.c
$ git diff
diff --git a/main.c b/main.c
index 56ef02d..6f0fa39 100644
--- a/main.c
+++ b/main.c
@@ -1,6 +1,7 @@
 #include <errno.h>
 #include <stdio.h>
 #include <stdlib.h>
+#include <stdbool.h>

 int calc(int left, char op, int right) {
   switch (op) {
@@ -17,6 +18,23 @@ int calc(int left, char op, int right) {
   exit(EXIT_FAILURE);
 }

+// Converts the string str into an integer using strtol.
+// Returns 1 and stores the result in resultp on success.
+// Returns 0 and sets errno otherwise.
+bool to_int(const char *str, int *resultp) {
+  char *endptr;
+  errno = 0;
+  int result = strtol(str, &endptr, 10);
+  if (str == endptr) {
+    errno = EINVAL;
+  }
+  if (errno != 0) {
+    return false;
+  }
+  *resultp = result;
+  return true;
+}
+
 int main(int argc, char **argv) {
   if (argc != 4) {
     fprintf(stderr,
@@ -29,11 +47,8 @@ int main(int argc, char **argv) {
   const char *right_str = argv[3];
   errno = 0;
   char *endptr;
-  int left = strtol(left_str, &endptr, 10);
-  if (left_str == endptr) {
-    errno = EINVAL;
-  }
-  if (errno != 0) {
+  int left;
+  if (!to_int(left_str, left)) {
     perror(argv[0]);
     return EXIT_FAILURE;
   }

no changes added to commit (use "git add" and/or "git commit -a")
$ 
```

#### Seeing who changed a line (`git blame`)

To wrap up our survey of basic Git commands, let's discuss an alternate way to
view a file's history. Whereas `git log` shows every commit that's changed any
line in a given file, `git blame` shows which commit most recently changed
*each* line of the given file. As its name implies, it's extremely useful when
you want to know who's responsible for a specific piece of code:

```console?prompt=$
$ git blame main.c
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500  1) #include <errno.h>
a83e7a6c (Thomas Hebb 2024-01-30 22:59:25 -0500  2) #include <stdio.h>
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500  3) #include <stdlib.h>
a83e7a6c (Thomas Hebb 2024-01-30 22:59:25 -0500  4)
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500  5) int calc(int left, char op, int right) {
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500  6)   switch (op) {
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500  7)   case '+':
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500  8)     return left + right;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500  9)   case '-':
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 10)     return left - right;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 11)   case '*':
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 12)     return left * right;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 13)   case '/':
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 14)     return left / right;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 15)   }
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 16)   fprintf(stderr, "Unrecognized op `%c'.\n", op);
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 17)   exit(EXIT_FAILURE);
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 18) }
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 19)
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 20) int main(int argc, char **argv) {
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 21)   if (argc != 4) {
0fb52357 (Thomas Hebb 2024-02-28 22:35:12 -0500 22)     fprintf(stderr,
0fb52357 (Thomas Hebb 2024-02-28 22:35:12 -0500 23)             "Usage: %s <num> <op> <num>\nWhere <op> is one of +, -, *, /.\n",
0fb52357 (Thomas Hebb 2024-02-28 22:35:12 -0500 24)             argv[0]);
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 25)     return EXIT_FAILURE;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 26)   }
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 27)   const char *left_str = argv[1];
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 28)   const char *op_str = argv[2];
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 29)   const char *right_str = argv[3];
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 30)   errno = 0;
221af3ea (Thomas Hebb 2024-02-21 23:09:36 -0500 31)   char *endptr;
221af3ea (Thomas Hebb 2024-02-21 23:09:36 -0500 32)   int left = strtol(left_str, &endptr, 10);
221af3ea (Thomas Hebb 2024-02-21 23:09:36 -0500 33)   if (left_str == endptr) {
221af3ea (Thomas Hebb 2024-02-21 23:09:36 -0500 34)     errno = EINVAL;
221af3ea (Thomas Hebb 2024-02-21 23:09:36 -0500 35)   }
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 36)   if (errno != 0) {
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 37)     perror(argv[0]);
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 38)     return EXIT_FAILURE;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 39)   }
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 40)   if (op_str[1] != '\0') {
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 41)     fprintf(stderr, "Op must be one character. Got `%s'.\n", op_str);
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 42)     return EXIT_FAILURE;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 43)   }
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 44)   errno = 0;
221af3ea (Thomas Hebb 2024-02-21 23:09:36 -0500 45)   int right = strtol(right_str, &endptr, 10);
221af3ea (Thomas Hebb 2024-02-21 23:09:36 -0500 46)   if (right_str == endptr) {
221af3ea (Thomas Hebb 2024-02-21 23:09:36 -0500 47)     errno = EINVAL;
221af3ea (Thomas Hebb 2024-02-21 23:09:36 -0500 48)   }
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 49)   if (errno != 0) {
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 50)     perror(argv[0]);
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 51)     return EXIT_FAILURE;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 52)   }
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 53)   int result = calc(left, op_str[0], right);
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 54)   fprintf(stdout, "%d\n", result);
^3ba2a93 (Thomas Hebb 2024-01-30 22:57:04 -0500 55)   return 0;
^3ba2a93 (Thomas Hebb 2024-01-30 22:57:04 -0500 56) }
$ 
```

As you can see, each line has been annotated with a commit hash (the first
column), as well as basic metadata about that commit (`^` at the beginning of a
hash indicates a commit with no parent---generally the first commit ever made).
To see more details of a commit, you can use `git show` as usual.

By default, `git blame` blames a file as it exists in the working tree, but like
`git log` it can take a commit hash to change that. This lets you "skip past" an
irrelevant commit in the blame and instead see the second-most (or third-most,
etc) recent commit to change a line. To do so, pass `git blame` the parent of
the commit you don't care about. For example, we can check what commit prior to
`221af3ea` touched line 32:

```console?prompt=$
$ git blame 221af3ea^ -- main.c
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500  1) #include <errno.h>
a83e7a6c (Thomas Hebb 2024-01-30 22:59:25 -0500  2) #include <stdio.h>
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500  3) #include <stdlib.h>
a83e7a6c (Thomas Hebb 2024-01-30 22:59:25 -0500  4)
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500  5) int calc(int left, char op, int right) {
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500  6)   switch (op) {
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500  7)   case '+':
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500  8)     return left + right;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500  9)   case '-':
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 10)     return left - right;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 11)   case '*':
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 12)     return left * right;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 13)   case '/':
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 14)     return left / right;
2d660302 (Thomas Hebb 2024-02-21 23:07:15 -0500 15)   case  '%':
2d660302 (Thomas Hebb 2024-02-21 23:07:15 -0500 16)     return left % right;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 17)   }
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 18)   fprintf(stderr, "Unrecognized op `%c'.\n", op);
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 19)   exit(EXIT_FAILURE);
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 20) }
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 21)
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 22) int main(int argc, char **argv) {
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 23)   if (argc != 4) {
2d660302 (Thomas Hebb 2024-02-21 23:07:15 -0500 24)     fprintf(
2d660302 (Thomas Hebb 2024-02-21 23:07:15 -0500 25)         stderr,
2d660302 (Thomas Hebb 2024-02-21 23:07:15 -0500 26)         "Usage: %s <num> <op> <num>\nWhere <op> is one of +, -, *, /, %%.\n",
2d660302 (Thomas Hebb 2024-02-21 23:07:15 -0500 27)         argv[0]);
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 28)     return EXIT_FAILURE;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 29)   }
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 30)   const char *left_str = argv[1];
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 31)   const char *op_str = argv[2];
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 32)   const char *right_str = argv[3];
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 33)   errno = 0;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 34)   int left = strtol(left_str, NULL, 10);
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 35)   if (errno != 0) {
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 36)     perror(argv[0]);
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 37)     return EXIT_FAILURE;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 38)   }
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 39)   if (op_str[1] != '\0') {
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 40)     fprintf(stderr, "Op must be one character. Got `%s'.\n", op_str);
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 41)     return EXIT_FAILURE;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 42)   }
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 43)   errno = 0;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 44)   int right = strtol(right_str, NULL, 10);
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 45)   if (errno != 0) {
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 46)     perror(argv[0]);
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 47)     return EXIT_FAILURE;
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 48)   }
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 49)   int result = calc(left, op_str[0], right);
1838eeae (Thomas Hebb 2024-01-31 21:07:08 -0500 50)   fprintf(stdout, "%d\n", result);
^3ba2a93 (Thomas Hebb 2024-01-30 22:57:04 -0500 51)   return 0;
^3ba2a93 (Thomas Hebb 2024-01-30 22:57:04 -0500 52) }
$ 
```

(Despite its name, please don't use the results of `git blame` to shame anyone
for the code they've written!)

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

TODO: `git commit --amend` for quick fixes

TODO: `git rebase` for doing lots of charry-picks in a row automatically.

### Rewriting history

TODO: This can mostly come from our existing slide.

TODO: Talk about interactive rebasing for squashing/prettifying.

#### Finding bugs

TODO: Using `git bisect` to figure out what change broke your program. Only one
or two paragraphs---we don't want to overwhelm them.

TODO: In lecture, let's include an impressive demo to hook them on the
possibilities of Git.

### Odds and ends

#### Ignoring generated files (`.gitignore`)

#### Seeing a ref's history (`git reflog`)

## Lecture 4

CONTENTS: Collaboration with Git

You've done enough solo development. It's now time to learn to work with your
groupmates on projects. In order to do that, you need to know how to make your
repository accessible to the others somehow.

Git is pretty flexible about how repositories can be shared---after all, they
are "just files"---but the easiest and most common way to share is via a code
forge such as GitHub, SourceHut, or GitLab. These Git forges do a bunch of
stuff but the most important part is hosting a copy of your `.git` folder and
managing permissions. It's totally possible to DIY this with your own server
and software such as Gitolite (I used to do that for years), but these forges
*also* provide issue tracking and pull requests and other niceties.

So you go ahead and make a repository on GitHub. Now you're in this weird
situation where you have a repository locally and GitHub has this blank
repository somewhere in San Francisco and you have to find a way to get your
code across the country. (To be clear, *all* forges will create blank repos
when you click the "New Repository" button on the website. This is expected.)
To do this, you need to add a *remote*.

### Sharing branches with others

A *remote* is a copy of your repository that is... somewhere else. It could be
the directory next door, it could be a big binary file called a
*bundle*[^bundle], or---most commonly---it could be on someone else's
computer[^xkcd908] accessible over the network. Network remotes are referenced
using URLs: common types are HTTPS
(`https://server.com/myusername/myreponame`), SSH
(`git@server.com:myusername/myreponame.git`) and (less commonly) Git's native
protocol (`git://server.com/myusername/myreponame.git`)[^protocols]. These
days, `server.com` is often `github.com` or one of the other forges. These URLs
specify the location and protocol for how your local Git installation should
make network requests to the remote repository.

[^bundle]: A [bundle](https://git-scm.com/docs/git-bundle) is a snapshot of an
    entire Git repository using *packfiles*. This gets pretty into the weeds of
    Git, but feel free to read and learn more on your own.

[^xkcd908]: See [XKCD 908](https://xkcd.com/908/).

[^protocols]: Now, SSH is just one way to share Git objects over the network.
    We prefer it because it is the most convenient once set up and does not
    require typing in your password or using an additional HTTPS authentication
    token on GitHub. You should feel free to use whatever protocol you like.

A repository on your local machine can have zero or more remotes, though having
one remote is probably the most common. To go from zero to one, you need to add
the remote:

```console?prompt=$
$ git remote
$ git remote add origin git@github.com:myusername/myreponame.git
$ git remote
origin
$
```

(The name `origin` is convention and the default Git remote name; you could
call it `fred` or `lemonade` if you prefer.)

All this has done is make a little entry in your `.git/config` telling Git
where the remote called `origin` points. It does not make any network requests
or anything:

```console?prompt=$
$ cat .git/config
...
[remote "origin"]
	url = git@github.com:myusername/myreponame.git
	fetch = +refs/heads/*:refs/remotes/origin/*
...
$
```

To see this information without digging into the configuration, you can use
`git remote -v`:

```console?prompt=$
$ git remote -v
origin	git@github.com:myusername/myreponame.git (fetch)
origin	git@github.com:myusername/myreponame.git (push)
$
```

If you had more remotes, they would also show up both in the configuration file
and in the output of `git remote -v`.

> As another aside, this convention of the path being `username/projectname` is
> just that---convention. The server name and path name could be anything that
> the server chooses. In GitHub's case, though, separating out by username
> gives nice namespacing (same for the other forges).

So you have a remote now. You can tell Git to copy a local ref (in this case,
the `main` branch and the commits it points to) to the remote (in this case,
`origin`) by using the `push` subcommand:

```console?prompt=$
$ git push origin main
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 7 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 367 bytes | 367.00 KiB/s, done.
Total 4 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To github.com:tekknolagi/isdt.git
   d509779..7cc7fb1  mb-vcs-4 -> mb-vcs-4
$
```

TODO: describe above output

TODO: Deleting branches with `git push :foo`

To reduce the amount of typing, you can also use `--set-upstream`/`-u` one time
to mark `origin/main` as the default destination for the local ref `origin`.
This adds an entry in the `.git/config` file:

```console?prompt=$
$ git push -u origin main
...
Branch 'main' set up to track remote branch 'main' from 'origin'.
$ cat .git/config
...
[branch "main"]
	remote = origin
	merge = refs/heads/main
...
$ # Now you can do `git push`
```

#### Remote tracking branches

Time for a light detour. Another side effect of a `git push` is updating
*remote tracking branches*. These are local refs that cache the last known
state of refs on the remotes you've added. For example, if you `git push origin
main`, you know (for a little while at least) exactly what ref the remote's
`main` branch points to: you just pushed it! You can inspect (but not manually
update) this ref by (for example) the name `origin/main`. The remote state may
change while you are disconnected from it, but that is okay.

These remote tracking branches share similar names to your local branches. Your
local `main` branch, for example, has a counterpart called `origin/main`. When
you make a commit, `origin/main` is left alone; it falls behind your local
`main`. For example, it might look like this:

```
* a879406 (HEAD -> main) My second new commit
* 5e72155 My first new commit
* 2187cc4 (origin/main) The last shared commit
.
.
.
```

In the diagram above, the topmost commit `a879406` is the most recent, whereas
the bottom commit `2187cc4` is the least recent. Commits are also labeled with
what branches have that commit as their most recent commit.

In order to update `origin/main`, you would need to push your changes again.
But what if someone else has updated (pushed to) the remote in the meantime?
Well, you'll need to download their changes. You can do that with `git fetch`.

#### Fetch

Running `git fetch` will update all of your remote tracking branches. For
example, if someone updated `main` on the remote, you can see their changes
(update your local `origin/main`) by fetching.

```console?prompt=$
$ git fetch
remote: Enumerating objects: 22, done.
remote: Counting objects: 100% (22/22), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 16 (delta 12), reused 9 (delta 6), pack-reused 0
Unpacking objects: 100% (16/16), 7.74 KiB | 792.00 KiB/s, done.
From github.com:tekknolagi/isdt
   b357867..d573c7f  mb-vcs-4         -> origin/mb-vcs-4
 * [new branch]      tom-vcs-lecture2 -> origin/tom-vcs-lecture2
$
```

In this output, we can see that the server has printed some messages for us to
see (the lines starting with `remote:`). Then, Git unpacks the objects---this
can take a long time in large repositories---and shows a summary of what refs
have changed. We can see that the remote has updates on its `origin/mb-vcs-4`
branch and on its (new to us!) `origin/tom-vcs-lecture2` branch.

I use fetch a lot. Right before I go offline---say, for a plane or train
trip---I'll fetch all of the changes to the upstream repo so that I have them
available when I'm offline.

Again: fetch *only* updates remote tracking branches. It does **not** update
normal local branches. My `mb-vcs-4` branch will remain untouched until I
manually incorporate the changes from upstream using `rebase` or (less
commonly) `merge`.

#### Rebase

You learned about rebase earlier, but for the sake of completeness and
repetition in learning, I'll show how I might incorporate the remote changes
into my local branches using `rebase`. First, we'll take stock of the situation
and reflexively type `git status` to see what's going on:

```console?prompt=$
$ git status
On branch mb-vcs-4
Your branch is behind 'origin/mb-vcs-4' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)
$
```

As expected, the remote has updates that we do not, so our local branch is
*behind*. The status message also notes that our local branch can be
*fast-forwarded*, which we talked about earlier as well. This is the easiest
case and is illustrated by the below diagram:

```
* a879406 (origin/mb-vcs-4) A shiny new thing, freshly downloaded
* 5e72155 (mb-vcs-4) My most recent local commit
* 2187cc4 My previous local commit
.
.
.
```

It's not the *only* situation we could be in, though. We could also have a
situation where the remote tracking branch has a new commit **and** the local
branch has a *different* new commit. In that case, Git will note that the
branches have "diverged"[^needs-all-info].

[^needs-all-info]: If you have fetched all the new commits from the remote, Git
    may be able to let you know about this in the output of `git status`; it
    has the information available locally. But sometimes you might not have
    fetched, and might find this out when you tried to `git push`. In this
    case, it is the Git software *on the remote* that is preventing you from
    pushing to the remote branch:

    ```console?prompt=$
    $ git push
    To github.com:tekknolagi/isdt.git
     ! [rejected]        mb-vcs-4 -> mb-vcs-4 (non-fast-forward)
    error: failed to push some refs to 'github.com:tekknolagi/isdt.git'
    hint: Updates were rejected because the tip of your current branch is behind
    hint: its remote counterpart. Integrate the remote changes (e.g.
    hint: 'git pull ...') before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.
    $
    ```

    That is, unless your remote is a local file-based remote or something, in
    which case it is still your local Git. But you should still think of it as
    the remote Git.

Now, divergence only means that one ref is not strictly behind or in front of
the other; it does not imply anything about the commit contents or whether the
commits will textually conflict with one another. (For now, we'll assume *no
conflicts*, because it's not the point of this section. The same principles
from earlier still apply.)

In either case, we can use rebase to bring in the remote changes. For example:

```console?prompt=$
$ git rebase origin/mb-vcs-4
Successfully rebased and updated refs/heads/mb-vcs-4.
$
```

This rebase command finds the *fork point* between the local `mb-vcs-4` and the
remote `origin/mb-vcs-4`. Then, it applies (cherry-picks) all of the remote
commits to the fork point. Last, it applies all of the local commits on top.

If there are no local commits, Git will choose to automatically fast-forward
the local branch to get it up to date with the remote branch. Otherwise, it
will go through the full rigamarole of applying commits one by one (making new
commits along the way!).

After you have rebased, you can safely push your (renewed) local commits to the
remote. That is, unless someone else has beaten you to the punch and pushed
even more commits to the remote. In that case, keep fetching and rebasing.

<!-- TODO(max): Figure out whether to keep this, delete it, or move it to
lecture 5
> Note that this re-applying of local commits on top of remote changes
> constitutes *rewriting history*. As we have discussed before, some people
> find this very distasteful and even ban it in their projects, preferring
> merge commits exclusively. The course staff has a more moderate view of
> things: rewriting history is fine if it's a private, short-lived development
> branch. Otherwise, merge.
-->

#### Merge

It's also possible to use `git merge` to reconcile local and remote changes.
Like rebase, merge also comes with ability to fast-forward, and this will
happen automatically unless disabled with `--no-ff`.

We'll talk about `--ff-only` first because it's the most similar to what you
have seen so far. If you run `git merge --ff-only origin/branch-name`, the
merge will only succeed if it need not create a merge commit. That is, if the
local branch can be fast-forwarded to the remote, great. If not, noisily fail.

In the case where the two branches diverge (`--ff-only` would fail), you can
use `git merge origin/branch-name` to make a merge commit between your local
branch and the remote-tracking branch.

A middle ground is `git merge --ff`, which will try to fast-forward if it can,
and otherwise fall back to creating a merge commit.

#### Pull

We've talked about running `git fetch` and then either `git rebase` or
`git merge` to reconcile differences between local and remote commits. Running
two commands each time can be cumbersome, so Git provides a shortcut. We
mention the shortcut last for two reasons:

1. We want you to understand what is going behind the scenes; this combo
   command is not magical
2. The combo command can behave in unexpected ways, especially if you don't
   understand the underlying concepts

The command is `git pull`. Now, directly from the man page:

> Incorporates changes from a remote repository into the current branch. If the
> current branch is behind the remote, then by default it will fast-forward the
> current branch to match the remote. If the current branch and the remote have
> diverged, the user needs to specify how to reconcile the divergent branches
> with `--rebase` or `--no-rebase` [...].
>
> More precisely, `git pull` runs `git fetch` with the given parameters and
> then depending on configuration options or command line flags, will call
> either `git rebase` or `git merge` to reconcile diverging branches.

Now that you have both learned about remote tracking branches and refreshed
your memory about rebase/merge, this may make perfect sense. Of
course that's what it does, right? Why would it do anything else?

Unfortunately, many people learn `pull` (and `push`) only as a black box that
magically synchronizes a local branch to a remote one (or vice versa). Since
much of the commands' behavior can only be explained by knowing the separate
steps they take, those people risk an unpleasant surprise in all but the most
simple branch states. Now you know, and hopefully can avoid future confusion.

### `git clone` for making a local copy of a remote repo

You don't always start off making a local repo and then pushing it to a forge.
Sometimes, the project already exists and you want to contribute. To work
locally, you will need to download the repository using `git clone`:

```console?prompt=$
$ ls -dl isdt
ls: cannot access 'isdt': No such file or directory
$ git clone git@github.com:tekknolagi/isdt.git
Cloning into 'isdt'...
remote: Enumerating objects: 2103, done.
remote: Counting objects: 100% (907/907), done.
remote: Compressing objects: 100% (274/274), done.
remote: Total 2103 (delta 685), reused 818 (delta 627), pack-reused 1196
Receiving objects: 100% (2103/2103), 4.08 MiB | 20.98 MiB/s, done.
Resolving deltas: 100% (1334/1334), done.
$ ls -dl isdt
drwxrwxr-x 13 max max 4096 Apr 29 18:47 isdt
$
```

By default, `git clone` will create a new directory with the same name as the
repository[^clone-repo-name]. Then it downloads all of the objects from the
remote repository, and checks out the default branch.

[^clone-repo-name]: It comes with a heuristic to determine what that is, but
    you can think of it as the last piece of the URL, minus a trailing `.git` or `/.git` if present.

Now that you know a bunch of new terms from the first part of this lecture, you
can digest the man page:

> Clones a repository into a newly created directory, creates remote-tracking
> branches for each branch in the cloned repository (visible using `git branch
> --remotes`), and creates and checks out an initial branch that is forked from
> the cloned repository's currently active branch.
>
> After the clone, a plain `git fetch` without arguments will update all the
> remote-tracking branches, and a `git pull` without arguments will in addition
> merge the remote `master` branch into the current `master` branch, if any
> [...].

## Lecture 5

CONTENTS: Collaboration in practice

### Common development models

TODO: Single "upstream" copy of the repo that's the source of truth.
Maintainers merge changes to it and many "downstreams" maintain changes based
on it.

TODO: Add a section about incorporating main branch changes into feature
branches and all associated problems. Tom covers it a bit earlier in the VCS
notes but it would be good to elaborate here.

### Merge/pull requests and patches

TODO: Git has no built-in way to propose a change. So lots of solutions for
proposing and reviewing changes before they're merged upstream have emerged.
Talk about mailing lists, GitHub model, Phabricator model.

TODO: mention https://github.com/vim/vim/pull/8859 since that came up during
ISDT notes

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
