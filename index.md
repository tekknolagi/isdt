---
---

<ul class="navbar">
  <li><a href="#administrivia">Administrivia</a></li>
  <li><a href="#schedule">Schedule</a></li>
</ul>

# Home

This is the course website for the inaugural (Fall 2021) semester of *CS 50:
Introduction to Software Development Tooling* at Tufts University. This site
holds the authoritative syllabus, as well as lecture notes and assignments.

*Note:* The course staff reserves the right to change this page at any time
without notice. The [change history][site-commits] is public.

[site-commits]: https://github.com/tekknolagi/isdt/commits/main

## Overview

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

**Instructors:** [Max Bernstein](https://bernsteinbear.com) and [Tom
Hebb](https://tchebb.me/)  
**Teaching Assistants:** Dana Estra, Lexi Galantino, David Gantt  

**Office Hours:** Mondays 6:00p-7:15p ET, Wednesdays 8:00p-9:15p ET; extra
hours to be announced on Piazza (access via Canvas)  
**Discussion board:** [Piazza](https://piazza.com/tufts/fall2021/cs50isdt)  

**Prerequisites:** CS 15 or permission of instructor  
**Equipment:** A computer with SSH access to the Tufts homework server  
**Textbook:** none  

**Lectures:** Tuesday and Thursday 7:30p-8:45p ET via Zoom (access via Canvas)  
**Assignments:** 8 assignments (2 per module), to be submitted with `provide`  
**Exams:** none  

## Schedule

*Note:* We will publish notes for each lecture after it happens, but the lecture
recordings will not be available to students. If you require access to 
recordings for your accommodations, please contact us using a private post on
Piazza.

| Week   | Tuesday | Thursday |
| ----   | ------- | -------- |
|  1     | *Sep 7*<br />*No class* | *Sep 9*<br />Course Administrivia &amp; [CLI 1: Intro to Linux and the shell](lecture-notes/1-cli/#lecture-1) |
|  2     | *Sep 14*<br />[CLI 2: Quoting, common tools, and permissions](lecture-notes/1-cli/#lecture-2)<br/>[Homework 1](assignments/01-cli-investigative/) out | *Sep 16*<br />[CLI 3: Advanced shell features](lecture-notes/1-cli/#lecture-3) |
|  3     | *Sep 21*<br />[CLI 4: The shell as a programming language](lecture-notes/1-cli/#lecture-4) | *Sep 23*<br />CLI 5: Behind the scenes<br />Homework 1 due; [Homework 2 out](assignments/02-cli-constructive/) |
|  4     | *Sep 28*<br />CLI 6: Linux and POSIX | *Sep 30*<br />VCS 1: Intro to version control<br /> Homework 2 due |
|  5     | *Oct 5*<br />VCS 2: Intro to Git and the structure of a repo | *Oct 7*<br />VCS 3: Collaboration with Git<br />Homework 3 out |
|  6     | *Oct 12*<br />VCS 4: Git internals | *Oct 14*<br />VCS 5: Git internals, continued<br />Homework 3 due; Homework 4 out |
|  7     | *Oct 19*<br />VCS 6: Survey of alternative and related tools | *Oct 21*<br />BLD 1: Intro to build systems<br /> Homework 4 due |
|  8     | *Oct 26*<br />BLD 2: Intro to Make | *Oct 28*<br />BLD 3: The Make language<br />Homework 5 out |
|  9     | *Nov 2*<br />BLD 4: Large projects using Make | *Nov 4*<br />BLD 5: Compilation and linking<br />Homework 5 due; Homework 6 out |
| 10     | *Nov 9*<br />BLD 6: Other build systems and meta-tools | *Nov 11*<br />*Veterans' Day; no class* |
| 11     | *Nov 16*<br />COR 1: Intro to software correctness<br />Homework 6 due | *Nov 18*<br />COR 2: Philosophy of software testing<br />Homework 7 out |
| 12     | *Nov 23*<br />COR 3: Writing unit tests | *Nov 25*<br />*Thanksgiving; no class* |
| 13     | *Nov 30*<br />COR 4: Testing interactions of complex systems<br />Homework 7 due; Homework 8 out | *Dec 2*<br />COR 5: Continuous integration |
| 14     | *Dec 7*<br />COR 6: Other methods for ensuring software correctness<br /> Homework 8 due | *Dec 9*<br />TBD |
| 15     | *Dec 14*<br />*No class* | *Dec 16*<br />*No class* |

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

*Note:* This is a new course, written from scratch and being taught for the
first time. Some things might feel rough, slightly out-of-order, or poorly
scheduled. When this happens, please let us know on Piazza. Your feedback will
help us shape future iterations of the course.

## Academic Integrity

You are expected to adhere to [Tufts' Academic Integrity Policy][tufts-policy]
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

[tufts-policy]: https://students.tufts.edu/student-affairs/student-code-conduct/academic-integrity-resources

## Grading

You will be evaluated 100% on homework assignments.

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

<div id="elephant"><img src="jumbo.png" alt="Jumbo on a laptop" /></div>
