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
.navbar {
    list-style-type: none;
    margin: 0;
    padding: 0 !important;
}
.navbar li {
    display: inline;
    padding-right: 16px;
    font-size: 20px;
}
div#elephant img {
  width: 100px;
  position: fixed;
  right: 0;
  bottom: 0;
}
</style>

<ul class="navbar">
  <li><a href="#administrivia">Administrivia</a></li>
  <li><a href="#schedule">Schedule</a></li>
  <li><a href="#assignments">Assignments</a></li>
  <li><a href="#grading">Grading</a></li>
</ul>

# Home

*CS 50: Introduction to Software Development Tooling* is a course being taught
by [Max Bernstein](https://bernsteinbear.com) and [Tom
Hebb](https://tchebb.me/) in the Fall 2021 semester at Tufts University.

*Note:* The course staff reserves the right to change this page at any time
without notice. View the [change
history](https://github.com/tekknolagi/isdt/commits/main).

## Overview

Effective software development requires more than just coding skill: in
industry and academia alike, developers use tools to keep their code
maintainable and reliable. In this course, you will learn four fundamental
categories of tooling: version control, the Linux shell, build systems, and
testing. We’ll dive deep into one industry-standard tool from each category via
hands-on projects and exploration of existing codebases, then survey other
tools in the same category and discuss why you might choose one over another.
By the end of the course, you will have a robust toolset both to manage
complexity in your future projects and to effectively ramp up on software
projects you encounter in the real world.

## Administrivia

**Soft prerequisite:** CS 15 or permission of instructor

**Textbook:** none

**Equipment:** none

**Lectures:** via video call (platform TBD) on Tuesday and Thursday 7:30p-8:45p
ET. Course communication happens primarily on Piazza. Assignments are to be
submitted via TBD.

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

| Week   | Tuesday | Thursday |
| ----   | ------- | -------- |
|  1     | *Sep 7*<br />*No class* | *Sep 9*<br />Course Administrivia &amp; Linux 1: Intro to Linux and the shell |
|  2     | *Sep 14*<br />Linux 2: Common tools<br/>Homework 1 out | *Sep 16*<br />Linux 3: Interactive shell tips &amp; tricks |
|  3     | *Sep 21*<br />Linux 4: The shell as a programming language<br />Homework 1 due; Homework 2 out | *Sep 23*<br />Linux 5: Behind the scenes |
|  4     | *Sep 28*<br />Linux 6: Linux and POSIX<br /> Homework 2 due | *Sep 30*<br />VCS 1: Intro to version control |
|  5     | *Oct 5*<br />VCS 2: Intro to Git and the structure of a repo<br />Homework 3 out | *Oct 7*<br />VCS 3: Collaboration with Git |
|  6     | *Oct 12*<br />VCS 4: Git internals<br />Homework 3 due; Homework 4 out | *Oct 14*<br />VCS 5: Git internals, continued |
|  7     | *Oct 19*<br />VCS 6: Survey of alternative and related tools; Homework 4 due | *Oct 21*<br />Build 1: Intro to build systems |
|  8     | *Oct 26*<br />Build 2: Intro to Make<br />Homework 5 out | *Oct 28*<br />Build 3: The Make language |
|  9     | *Nov 2*<br />Build 4: Large projects using Make<br />Homework 5 due; Homework 6 out | *Nov 4*<br />Build 5: Compilation and linking |
| 10     | *Nov 9*<br />Build 6: Other build systems and meta-tools<br />Homework 6 due | *Nov 11*<br />*Veterans' Day; no class* |
| 11     | *Nov 16*<br />Testing 1: Intro to software correctness | *Nov 18*<br />Testing 2: Philosophy of software testing<br />Homework 7 out |
| 12     | *Nov 23*<br />Testing 3: Writing unit tests | *Nov 25*<br />*Thanksgiving; no class* |
| 13     | *Nov 30*<br />Testing 4: Testing interactions of complex systems<br />Homework 7 due; Homework 8 out | *Dec 2*<br />Testing 5: Continuous integration |
| 14     | *Dec 7*<br />Testing 6: Other methods for ensuring software correctness; Homework 8 due | *Dec 9*<br />TBD |
| 15     | *Dec 14*<br />*No class* | *Dec 16*<br />*No class* |

## Assignments

Assignments will be posted here as they are released. Check back soon...

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

Students will be evaluated 100% on homework assignments.

### Submitting assignments

Projects must be submitted electronically following the instructions given in
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

<p style="position:relative;bottom:0; font-size:x-small;">The source of this
page is available <a href="https://github.com/tekknolagi/isdt">here</a>.</p>
