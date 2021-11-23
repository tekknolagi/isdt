---
---
# Homework 7: COR, Investigative

## Fantastic calculators and where to find them

For this assignment, you will be looking at the open-source project
[SuperCalc](https://github.com/cs50isdt/SuperCalc), a command-line
calculator that can evaluate a wide range of mathematical expressions.
Specifically, you will be exploring its source code to answer some questions
about its automated tests.

Note that this assignment is not your typical computer science assignment.
Instead of answering reasonably objective questions about an open source
project or writing code that must pass some tests, you will be offering your
subjective thoughts on the testing philosophy of a project. This may be
intimidating. That's expected and means you're learning. For the more
subjective questions, we will be grading you based on how well your reasoning
justifies your conclusion more than on that conclusion itself; in some cases,
there is no single correct conclusion.

1. What Linux commands are run behind the scenes to build the tests? To run
   them? Look at README.md for a starting point and use your knowledge of
   Makefiles to follow the trail.
2. Would you categorize SuperCalc's tests as unit tests, integration tests, a
   mixture of the two, or some kind of hybrid? Explain your reasoning.
3. Build SuperCalc using the instructions in its README.md and try out some of
   the examples from there. Once you've become familiar with what it can do, go
   back to the tests and name one piece of functionality that has no test.
4. Look at the test names. Can you figure out what each test is testing? Take a
   look at the `orderAdd` test as an arbitrary example of a broader pattern in
   `tests.c`.
   1. We discussed some conventions for naming tests in lecture. With respect
      to those conventions, what's wrong with the name `orderAdd`?
   2. Propose a better name for `orderAdd`.
5. Now, take a look at the `varAssignment` test in the same file.
   1. Do you think this test is a good *unit* test? Which properties of a unit
      test does it have, and which ones does it lack?
   2. What would you change to make this test a better unit test?
6. Which "testing best practices" (below) does this project do well? Which have
   room for improvement? Cite examples of the good and bad practices you
   mention.
7. Look at the project source, like `function.h`. Does the API lend itself to
   testing? Why or why not?
8. In lecture, we defined a *bug* to be a piece of behavior in a program that
   differs from what that program's specification dictates. A specification can
   take many forms, ranging from a formal document spanning hundreds of pages
   (like the ANSI C language standard) to a set of intentions that live only
   inside the original author's head.
   1. Do any written descriptions (i.e. specifications) of SuperCalc's behavior
      exist in the repository? If so, where are they?
   2. Give an example of a piece of SuperCalc's behavior that is not part of
      any textual specification. (By "textual specification," we mean any
      written description of how the code behaves that's separate from the code
      itself.) Justify your answer.

### Best practices

The following is an incomplete list of best practices for writing tests.

* Test small units of code as directly as possible
* Avoid "round trips" through layers of software
* Avoid stateful computation in the functions being tested
* Avoid state in the test harness (writing to disk, database, etc)
* The test should be able to detect if it passed or failed automatically
* Tests should be repeatable (deterministic; non-flaky)
* Tests should be named descriptively (name of system, scenario, expected
  result)
* Tests should be named consistently
* Test input should be as minimal as possible
* Avoid loops and control flow
* Tests should run as part of the automated build (CI) process

## Submitting your work

You should write your answers in a file, `answers.txt`.

Please submit with `provide comp50isdt cor-investigative answers.txt`. You must
be logged into the homework server to use Provide.
