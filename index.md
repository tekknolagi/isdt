---
---

<ul class="navbar">
  <li><a href="#administrivia">Administrivia</a></li>
  <li><a href="#schedule">Schedule</a></li>
</ul>

# Home

This is the course website for *CS 4973: Introduction to Software Development
Tooling* at Northeastern University, Summer 2 2024. This site holds the
authoritative syllabus, as well as lecture notes and assignments.

*Note:* The course staff reserves the right to change this page at any time
without notice. The [change history][site-commits] is public. **It is being
actively changed right now as we update it for Summer 2024.**

[site-commits]: https://github.com/tekknolagi/isdt/commits/main

## Overview

Learn tools you'll be expected to know as a working software engineer, which will
help you write better code, collaborate with others, and tackle problems you
previously thought impossible.

Effective software development requires more than just coding skill: in
industry and academia alike, developers use tools to keep their code
maintainable and reliable. In this course, you will learn four fundamental
categories of tooling: the command line, version control, build systems, and
correctness. We’ll dive deep into one industry-standard tool from each category
via hands-on projects and exploration of existing codebases, then survey other
tools in the same category and discuss why you might choose one over another.
By the end of the course, you will have a robust toolset both to manage
complexity in your future projects and to effectively ramp up on software
projects you encounter in the real world.

We are teaching this course as a series of four modules. The first, Command
Line, will give you an overview of the operating system and tools available to
you to make your life as a software engineer easier. The second, VCS, will
teach you about how to version control your software with Git, so that you may
maintain a history of your changes and collaborate with others. The third,
Build, will teach you about how to reliably build your software with Make. The
fourth and final module, Correctness, will introduce you to testing and other
tools for ensuring that your software meets quality standards.

## Administrivia

**Instructor:** [Max Bernstein](https://bernsteinbear.com)  
**Teaching Assistants:** TBD

**Office Hours:** TBD; extra hours to be announced on Piazza  
**Discussion board:** Piazza (access via Canvas)

**Prerequisites:** An introductory computer science class and the willingness
to learn a little C  
**Equipment:** A computer with a POSIX shell  
**Textbook:** none  

**Lectures:** Mo-Tu-We-Thu, 9:50am-11:30am, in person (location TBD)
**Assignments:** 8 assignments (2 per module), to be submitted on Gradescope  
**Exams:** none  

## Schedule (to be updated!)

*Note:* We will publish notes or slides for each lecture after it happens, but
the lecture recordings will not be available to students. If you require access
to recordings for your accommodations, please contact us using a private post
on Piazza.

<!-- from gensched.py -->
{% include cal.md %}

## Course philosophy

This course will consist of 25 lectures (unplanned cancellations
notwithstanding) and 8 assignments, spaced evenly throughout the semester.
There will be no exams. We'll use the lectures (accompanied by written lecture
notes, assigned readings, and other media) to introduce new material, and we'll
use the assignments to reinforce that material and evaluate your progress.

While we hope you enjoy this course, we will only be present for a small
minority of your lifelong learning. Therefore, we have done our best to build
assignments and lectures that show you how to find documentation, read code,
and carry out small experiments on your own so that you can continue to broaden
your knowledge long after this course has ended. We believe this ability is
just as important to your success as anything we can teach you directly.

*Note:* This is a relatively new course, written from scratch and being taught
for the second time. Some things might feel rough, slightly out-of-order, or
poorly scheduled. When this happens, please let us know on Piazza. Your
feedback will help us shape future iterations of the course.

## Academic Integrity

**TL;DR: Do all of your own work. This course will necessarily involve a lot of
searching and reading. Skipping the work will only make your life easier in the
short term. Don't use LLMs such as ChatGPT.**

You are expected to adhere to [NEU's Academic Integrity Policy][neu-policy]
in this course. Plagiarism of code or answers to assignments is strictly
prohibited, as is sharing answers with or accepting answers from others.

You are allowed to reference Linux man pages and any open source projects while
completing assignments. You are also allowed to read any internet resource,
with the exception of material outside this website that explicitly pertains to
this course (e.g. assignment solutions accidentally shared by a former
student).  However, no matter what resources you reference, you must not
plagiarise or complete a substantial part of an assignment using someone else's
work, even if you credit that work.

You are, however, allowed to base your answers on information you find online.
The purpose of this course is to learn, so if you find a useful resource that
clarifies a misunderstanding or explains a tricky topic and in doing so gives
you the knowledge you need to complete an assignment, you are welcome to read
it (and share it with other students)! You may even copy short snippets of code
from examples you find online, given that either 1) you cite your source, or 2)
the snippet is something that couldn't reasonably be implemented any other way
(e.g. a call to a Linux API function that we have asked you to use).

To cite your source, leave a reference to it that is enough for the reader to
easily find the resource. If the source is a webpage, give the full URL. If the
source is a print book, give the title, author, and edition. Use your common
sense here.

As a rule of thumb, it's okay to look for resources to answer specific
questions that come up while you are working on an assignment, but it's not
okay to look for resources to avoid having to work on the assignment at all.

In the former case, you may end up copying or retyping small snippets of code
from the resources you find. If what you copy has no originality (e.g. if you
look up the name of a specific function or command-line flag) and so serves
only as an expression of thoughts you already had, no attribution is needed.
However, if what you copy affected your thinking about how to go about solving
the problem (e.g. by using a command in a way you hadn't considered before),
you should cite your source. Either way, things like this are generally okay
and won't affect your grade.

What's not okay is copying a function, program, or command that solves a
substantial portion of the problem we've given you, regardless of whether you
attribute it. You are graded on what *you* bring to the course, and if the
course staff believes that you did not bring your own originality and
problem-solving skills to an assignment, you will receive a failing grade for
that assignment. Additionally, if you don't attribute the unoriginal code, you
will be guilty of plagiarism and the extra consequences that entails.

[neu-policy]: https://osccr.sites.northeastern.edu/academic-integrity-policy/

## Grading

You will be evaluated 100% on homework assignments. Your final percentage grade
will be the average (mean) of your individual grades for each of the 8
assignments. We may decide to adjust (i.e. curve) the grades of any individual
assignment if we deem it necessary, and in that case the curved value is what
will go into the average. A curve will never decrease your grade for an
assignment.

Your final letter grade will be computed from your final percentage grade using
the cutoffs outlined [here](https://math.tufts.edu/resources/grading-schemes).
(We know that's a Tufts math department page, but their scheme closely matches
that which most students expect, and the computer science department doesn't
have a recommended set of cutoffs documented anywhere.)

Often on homework assignments we will ask you questions as part of an
"investigative" assignment. The purpose of these questions is to guide you
through a learning process and teach you how to find things out for yourself.
You should explain "why" or "how" in your answers to demonstrate your process.
This is similar to "showing your work" for math. For example, if a question
asks, "how many files are in the directory?", we would expect you to say "42. I
found the answer with `ls -l | wc -l`" or similar. Just responding "42" would
not be enough.

### Submitting assignments

You must submit projects electronically following the instructions given in
class. Projects may not be submitted by any other means (e.g., please do not
email your projects to us). It is your responsibility to test your program and
verify that it works properly before submitting. All projects are due at
11:59pm on the day indicated on the project assignment, according to the
submission server's internal clock. Your project score will be for the last
version of the project you submit.

### Late policy

You have two late tokens that you can use during the semester. Using one late
token allows you to submit one project up to 24 hours late with no penalty. You
may also use your two late tokens together to submit one project up to 48 hours
late with no penalty. Contact a TA if you need to check the status of your late
tokens.

## Contributors

We consulted Ming Chow, Mike Shah, Chris Gregg, Mark Sheldon, Tyler Lubeck, and
Lexi Galantino while developing this course.

We borrowed the "Assignments" submission guidelines from Jeff Foster's CS 121
syllabus.

These similar courses from other institutions inspired elements of this
course:

* MIT's [missing semester](https://missing.csail.mit.edu/)
* Berkeley's [EECS201](https://www.eecs.umich.edu/courses/eecs201/)
* Berkeley's [CS9E](https://www2.eecs.berkeley.edu/Courses/CS9E/)

<div id="elephant"><img src="assets/images/jumbo.png" alt="Jumbo on a laptop" /></div>
