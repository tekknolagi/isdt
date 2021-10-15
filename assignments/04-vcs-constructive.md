---
---
# Homework 4: VCS, Constructive

## Tracking changes with Git: maintainer for a day

You co-maintain a software project with your mustachioed friend Tommaso. You
normally split your maintainer duties evenly, but he has taken a well-deserved
two week vacation to a beach in France and left you completely in charge.
Throughout this week, a number of situations have come up and it is your duty
to deal with them! In this assignment, we will have you modify a Git repository
with several sequential steps that you must translate to Git commands.

Many of these questions are graded solely by the final state of the repository
you submit to us. For the ones that aren't, we expect you to tell us what
commands you ran and why, as in prior assignments. See the first question for
instructions on how to submit your answers to such questions.

Expect to make good use of `git reflog` in this assignment as you make errors.

Start by cloning the initial repository from `/comp/50ISDT/vcs2-constructive`.
We suggest you work on the homework server, but you are also free to work on a
personal computer (make sure you have `clang-format` installed if so).

1. A number of the following questions ask you to tell us what commands you
   used. Start out by making a place to put your answers! **Create a new branch
   with no history (meaning the first commit you make to it will be parentless)
   named `answers` by running `git checkout --orphan answers`.** As you answer
   our questions, update a file called `answers.txt` in that branch. You may
   commit your answers either one-by-one or all at once, but make sure you've
   committed them before you submit!
1. A user named Gianna opened a GitHub issue pointing out that the project has
   no LICENSE file, meaning she doesn't know if she's allowed to use the
   software in the way she wants. You did some research and found that the [MIT
   license](https://choosealicense.com/licenses/mit/) is appropriate for the
   project. **Add a new file called LICENSE containing the license text from
   that link (with appropriate placeholders filled in), then commit the
   addition to the `main` branch with a descriptive commit message.**
1. Encouraged by your prompt addition of a license, Gianna has done some work
   to adapt the project to her needs. She has sent you a pull request, asking
   you to review the changes in `gianna-increase-int-size` and add them to the
   `main` branch if possible. You review the changes and they look great--no
   revision needed! **Create a merge commit on `main` that merges the tip of
   `gianna-increase-int-size` with the previous tip of `main`.**
1. You receive another pull request, this one from a person named Dr.
   Garbarini. You don't know him, but the changes look reasonable to you.
   Unfortunately, Garbarini doesn't seem to care about making his commit
   history look nice: the branch he wants you to merge, `garbarini-branch`, is
   full of commits with titles like "doc" and no further description. You
   decide that it's best to add all his changes to `main` as a single commit to
   cut down on the noise. **Create a new commit on `main` consisting of all the
   changes from `logan-branch` since it diverged from `main`. Tell us how you
   did so.** Note that it is possible to do this without manually copying any
   files or code--if you find yourself re-entering things, there's probably a
   better way.
1. Massimo has been working on fixing a nasty bug for quite some time, and he
   finally posted his changes to the `fix-parsing-bug` branch right before
   leaving. Unlike Dr. Garbarini, his commits are masterfully documented, and
   you want to add them to `main` as-is. But you notice that the commit titled
   "Fix parsing of left hand side" has some formatting errors. You can run
   `clang-format -i` to automatically fix those errors, but you want to include
   the fix as part of the original commit instead of putting it in a separate
   one.
   1. **Change the `fix-some-bug` branch to point to an updated version of the
      same set of commits (with matching commit messages, titles, and diffs)
      with fixed formatting in the problematic change. Tell us how you did
      so.**
   1. **Now that the commits are ready, add them to `main` by rebasing them.**
      This is different from merging, like you did with Gianna's branch: in
      this case, you should make no new merge commits.
1. Uh oh! You just noticed that Dr. Garbarini's branch included a commit that
   deleted some tests from `main-tests.sh`. You ask him why and learn that it
   was an accident--he always creates his commits using `git commit -a`, and so
   he didn't notice that one of them included a local change meant for
   debugging. Since you've already pushed his changes to the public, it's too
   late to amend them. **Create a new commit on `main` that restores
   `main-tests.sh` back to how it was before Dr. Garbarini's change. Tell us
   how you did so.**
1. Alessia is a disgruntled user of your open source project. She opened [an
   issue](04-vcs-constructive-issue.txt) maligning the project and its esteemed
   maintainers. Make an appropriately cool and collected comment on the issue
   before the discussion gets too spicy.

## Submitting your work

To submit, first join our [GitHub Classroom
instance](https://classroom.github.com/a/GJz9jQnu). You will need a GitHub
account to do this. Once you've joined, you should be able to find yourself on
the class roster, after which you will see a repository belonging to you for
the "vcs-constructive" assignment. Add this repository as a remote to the local
repository where you've been working, then push your `main` and `answers`
branches to that remote. If you do this correctly, you'll see both branches
shown in GitHub's web UI.
