---
---

# Lecture Notes: Correctness

## Lecture 1

### Module overview
Welcome to the final module! So far, you have spent a great deal of time
learning about concrete tools to help you build software. In this module, we
will look first at some philosophical tools---ways of thinking---and then one
sample concrete tool, [UTest](https://github.com/sheredom/utest.h).

This module will be discussion-based.

### What does it mean for software to be correct?
Possible meanings for software correctness (as discussed in class):

* It does what I want it to
* It follows the specification
* It doesn't crash
* I wrote a proof about it
* The PR/diff/CL was reviewed and accepted by my coworkers
* ...
* It doesn't have any bugs

(By the way, here's some [interesting reading](https://tildesites.bowdoin.edu/~allen/courses/cs260/readings/ch12.pdf) that we won't assign.)

The broadest and also vaguest possible definition of software correctness is
"it does what I mean", or "it has no bugs". But it's hard to talk about this if
we haven't defined the term *bug*, so let's talk about that.

### What is a bug?
Wikipedia has a fine definition.

> A software bug is an error, flaw or fault in a computer program or system
> that causes it to produce an incorrect or unexpected result, or to behave in
> unintended ways.

The interesting parts of this definition are "unexpected results" or
"unintended behaviors". These hint at, but do not explicitly call out, the
existence of a specification for the behavior of a given program. This
specification need not be a three-hundred page tome handed down from management
for a software engineering team to implement. It may be less formal, like a
homework assignment, or even just a vague notion in your mind of what you want
your program to do. If your program deviates from this specification, it has a
bug.

You might ask why software correctness matters at all. In what will later be
described as a crime against Nature, we taught rocks to think and forced them
to run our programs. All those rocks can do are move and compute numbers. So
who really cares if a program doesn't precisely conform to its specification
and the numbers are wrong? Well...

### Why are bugs bad?
A cop-out answer is that the professor of your computer science course has told
you that buggy code will cause you to lose points. For a couple years of your
life, this will suffice.

More broadly, though, software is supposed to help people, and it can’t help
people if it doesn’t perform the way it’s supposed to. Billions of people rely
on software every day for everything from critical infrastructure to medical
equipment to silly games. If there's a one in a million chance that your cancer
radiation therapy machine[^therac25] has a bug that kills you---well, you might
care. Or if the facial recognition software The State employs has a bug that
lands you in a prison cell, you might care.

[^therac25]: The Therac-25 radiation therapy machine is a case study often used
    in engineering ethics courses. Due to a race condition, the machine
    occasionally dosed people with hundreds of times the radiation they should
    have received, injuring several people and killing several people.

On a less serious note, bugs can lead to data loss, or revenue loss, or wasting people's
time. For personal projects, bugs might be inconsequential, like Bob Ross's
happy little accidents. You won't always be writing code for small projects,
though. You might be writing video game software and [accidentally delete
people's home
directories](https://github.com/valvesoftware/steam-for-linux/issues/3671).
That would be a huge problem.

So let's assume we want to reduce the quantity of bugs as much as possible. The
logical next step is figuring out how to do that.

### How do we minimize the number of bugs in software?
Different classes of bugs can be mitigated or outright prevented with different
software and people practices.

For example, *segmentation faults* and *memory corruption*, which you may have
experienced while writing C++ code, result from a class of bug that is very
unlikely to happen in other programming languages like Python or Java. These
higher-level languages have different *memory models* that outright preclude
these kinds of memory bugs.

Another class of bug, *logic errors*, are easy to introduce when writing
complex code with lots of edge cases like string processing algorithms. Higher
level languages often provide more library functions than lower level ones, and
such functions often provide battle-tested implementations of such algorithms.
Library functions are frequently more correct than a from-scratch
implementation because they have been written and revised by many people.

<!-- TODO: Rename Coq to Rocq? -->

Other logic errors are preventable by employing *mathematical proofs*. Tools
like [Coq](https://coq.inria.fr/) and [Isabelle](https://isabelle.in.tum.de/)
make it possible for programmers to write proofs about properties of the
systems they are building and have them automatically checked. Coq can then
generate a program for you that has been proven correct[^specification-errors].

[^specification-errors]: Formal verification is sometimes cited as a way to
    eliminate bugs altogether. After all, if your program has been
    mathematically proven to be correct, and if we have defined "correct" to
    mean "no bugs," it by definition cannot have bugs. But there's a flaw in
    this reasoning: proofs like those generated by Coq and Isabelle only prove
    that a program confirms to a specification that you---the person using
    them---provide. For example, if you write a program that returns the number
    4, and you tell Coq that your program ought to return 4, there's a pretty
    good chance it can prove it "correct." But if this specification is itself
    inaccurate---the customer wanted the program to return the number 2, for
    example---or incomplete, the proof is worthless.

When proving a program correct is impossible or intractable, it's almost always
possible to fall back on *testing*. These days, testing usually refers to
*automated tests*, or snippets of code that exercise your program and check its
output against expected known-correct output.

A good test suite on a software project is often a mark of high attention to
detail and a reasonable proxy for correctness[^evidence-of-bugs]. Tests also
have one advantage over proofs: since they exercise the code in a real
environment, they validate the environment as well as the code. For example, if
you accidentally rely on undefined behavior from your code and then upgrade
your compiler to one that produces a different result, your test suite will let
you know. As Donald Knuth once said, "Beware of bugs in the above code; I have
only proved it correct, not tried it."

[^evidence-of-bugs]: Unfortunately, test suites are only cable of showing
    evidence of a bug existing. They are not capable of showing that no bugs
    exist in the system. Yes, even if you have "full test coverage".

Lastly, software development practices can help. For a multi-person software
project, having a required code review step in the development process can help
catch bugs and otherwise raise the bar. People reviewing code may notice edge
cases that the original author did not think of, request that the author write
tests for those edge cases, and improve the quality of the proposed code
change.

In this module, we're going to focus primarily on writing tests as a means for
ensuring software correctness. Tests are not the only way to make your software
more correct, but they are the easiest to immediately apply and reason about.

### Common classes of bugs

Some time ago, Patrick McKenzie wrote a blog post called [Falsehoods
Programmers Believe About
Names](https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/).
In it, he lists common but false assumptions about names that lead to bugs in
software. Bad name handling is especially tricky because it can disenfranchise
entire classes of people. Imagine not being able to sign up for a service
because your last name is "too short", for example.

It inspired [a rash of follow-on
posts](https://github.com/kdeldycke/awesome-falsehood) in the form "Falsehoods
Programmers Believe About XYZ", all of which give perspective about a variety
of domains and common problems in software. While they are probably not all
worth reading and understanding in totality, it is certainly worth becoming
more mindful about the assumptions you bring to the table and accidentally bake
into software.

### "Best practices"
While we intend for everything we teach to be helpful, our advice won't always
apply in every situation. Use your best judgement. Read
[this tweet](https://twitter.com/garybernhardt/status/1433474928024735748) by
Gary Bernhardt.

## Lecture 2

Even simple software has edge cases. In a data structures course, for example,
one assignment might involve writing a `remove` function to remove an element
from a binary search tree and maintain the BST invariant.


```c++
Node* BST::remove(Node* root, int value) {
  // ...
}
```

This function alone had several cases: the node is `NULL`; the root has the
expected value (and you're deleting the root); the root does not have the
expected value; the node has no children; the node has one child; the node has
two children. Even though you probably should write unit tests, that's a
manageable number of cases to test manually... for now. Are you going to
remember to continue testing it as your software grows and changes? And this
BST is still considered fairly simple, too.

Complex software has many more edge cases. Business requirements often have to
take into account the Real World, which is much messier than a binary search
tree. Even if you "just" have to consider the BST interacting with other
software, that is complex on its own. You might need to think about interacting
with the disk, a database, the network, the operating system, Unicode, and all
the layers that have to work in between for anything to get done.

And it's not just writing code all day, either. In one day, you might have to
think about software performance, adding a new feature, complying with internal
guidelines, complying with a new law passed by the state, and complying with a
new law passed in a different country. There are so many cases to consider. In
isolation, they are tricky problems to keep correct. When combined, the cross
product can swiftly become completely and utterly unmanageable to keep correct.

The point here is not to make you stop, shudder, and forever put down your
keyboard. We would not be overwhelming you with a huge mess of stuff if we were
not also going to give you hope. The good news is that there *are* reasonably
well-established software practices to untangle this huge mess of code. Writing
tests is helpful, yes, but there are some other auxiliary practices that can
help make your tests even more effective.

### Automated tests

If you, the programmer, have to run tests manually after every change you make,
you will probably not run them very often. And, worse, if the test suite takes
a long time to run, you may run them even less often. Automating this process
is instrumental to both ensuring that the tests run and reducing cognitive
load.

If you think back to our source control module, where we introduced a Pull
Request-based collaborative workflow, there is a great place to insert an
automated test run: run tests on each commit in a pull request. Collaborative
version control providers often expose an API surface for building and running
tests. Having a green checkmark per change is a good signal to you, the
programmer, and your colleagues, that you have not broken anything, and also
pass your new tests.

Tests are also one possible encoding of a specification for your program. Tests
are not formal[^formal-semantics] and they do not form the complete set of
expected behavior, but they do document and enforce a contract.

[^formal-semantics]: <!-- TODO --> term of art

### Invariant of the green main branch

There's a bit of an implicit assumption that makes automated tests useful:
expecting the main branch to always be passing tests (to be "green", as in a
green checkmark symbol). If you maintain the invariant that the main branch
always passes tests, it's straightforward to tell if your changes break
anything.

If tests fail on your change, then it is most likely that the change introduced
a bug---a *regression*. It's also possible that the change exposed a bug that
already existed elsewhere and was not tested, in which case the signal is still
useful to the person submitting the change.

If the tests are failing or flaky on the main branch, though, the signal is
much less useful to anyone submitting a change to the project. It's very
difficult to use the test failure to a particular root cause[^test-bisect].

[^test-bisect]: It's especially difficult if you are going to use a test to
    programmatically track down what revision introduced buggy behavior. <!--
    TODO talk more about this -->

If you want to get really nitpicky about this, having tests run with every
change *still* is not enough. Consider a case where multiple engineers are
writing and landing changes concurrently. Generally, tests run for each change:

```
change A        (pass)
change B        (pass)
```

But this does not account for concurrent landing of A and B. If A and B both
land at the same time, there will be a "land race" and they will land in some
non deterministic order. It may happen that A and B conflict with one another
and one change causes the other to fail to build or fail to pass tests.

```
change A    *before*    change B        (fail)
change B    *before*    change A        (build fail)
```

This is a common reason that projects also enable "land-time" tests, ensuring
that the linearization of concurrent landing commits still passes tests.
Land-time tests build and run the project before every commit to the main
branch.

Most of the time this is done automatically by a kind of software known as
"continuous integration" software, and we'll talk more about that later.

<!-- TODO(max): Do we want to integrate the GitHub Actions activity I wrote for
the NEU software class? -->

### The real world and pebbles in a stream

As much as some people might wish, you are not writing code in a spherical
vacuum fixed in time. Even if you manage to write perfect bug-free code, which
is extraordinarily unlikely, your code will at some point interact with other
software and with hardware. This code is also extraordinarily unlikely to be
bug-free.

You will have bugs. Even if they aren’t bugs in the state-of-the-world at time
of writing code, the world changes. Time passes, bits rot, and people die, no
matter how much we try to stop it. Take a moment to call your loved ones and
tell them how much they mean to you.

It’s not about how good you are as a programmer. Your code interacts with the
toolchain of the programming language in which it's written: the compiler or
the runtime. It interacts with the operating system. With the filesystem. With
the network. Your code may run well when compiled with Clang but crash when
compiled with GCC, and the reason may be that your code implicitly took
advantage of a subtle clause in the C standard that allows the two compilers to
implement a behavior differently.

The third-party library you use might also have bugs. Or if it does not have
bugs, something changed with the last version. Perhaps the email software *du
jour* has an upgrade that changes a timeout and causes delivery
failures[^email]. Or perhaps part of the code literally changes behavior over
time, because it relies on the current date to do something.

[^email]: This is a fun, if apocryphal, story underscoring the point.
    https://web.mit.edu/jemorris/humor/500-miles

In all of these cases, writing tests, frequently running tests, and ensuring
that the test environment is the same as the "production" environment (whatever
that may be), will ease your pain.

<!-- TODO(max): expound -->

Google’s new CPU failures [paper](https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s01-hochschild.pdf)

Facebook hardware failure
[paper 1](https://research.fb.com/wp-content/uploads/2020/03/Optimizing-Interrupt-Handling-Performance-for-Memory-Failures-in-Large-Scale-Data-Centers.pdf)
and [paper 2](https://arxiv.org/pdf/2102.11245.pdf)

## Lecture 3

In this lecture, we will focus a bit more on one approach for software
correctness---unit tests---and explore a method for writing useful tests for
software.

### Where to start

Starting can be a little intimidating. You're sitting there, staring at the
blank text editor window before you, vaguely humming Natasha Bedingfield songs
to yourself. It's especially tricky when you haven't written any code yet *at
all*[^tdd-orthodoxy]. What do you type first?

[^tdd-orthodoxy]: This is what the Test Driven Development orthodoxy preaches.
    I have my personal opinions about that---I think starting test first
    always can lead to paralysis, and experimenting with the implementation
    first can help. But I do in general agree that you should be testing pretty
    rigorously as you go.

Start with the specification, even if you have never written it down: what
should the function do?

### What even is a specification?

We're probably going to start some fights by saying this, but a *specification*
is the document that describes the intended behavior of a piece of (potentially
imaginary) software. While the word "document" calls to mind a very formal
paper to be submitted to IEEE or the IETF or similar, it can also be
interpreted very loosely to mean something like a sketchy Google Doc written en
route to a meeting.

In an ideal world, it would describe all of the following: **purpose**,
**inferfaces**, **constraints**, **assumptions**, **dependencies**, and
**requirements**.

That begs the question: is a website casually describing the behavior of your
software project a spec? Is a comprehensive test suite? Do code comments
constitute a specification?

<!-- TODO -->

<!--
Can they be turned into documentation (Doxygen, JavaDoc)?
Do they explain the audience-facing behavior?
Do they explain *why* a decision was made?




All this to say... it depends. Let's get back to tests.
-->

Either way, the specification should guide your tests.

### Write some tests

Test what is specified, on paper or in your head. Call your imaginary function
or API a couple times to see what it feels like.

Imagine a function `isEven` that must return `true` if the number given was
even, and `false` otherwise:

```c
bool isEven(int num);
```

In order to pick good test cases for this function, we should consider the
cases mentioned in the specification: an even number; an odd number. Let's
write some tests.

```c
#include "utest.h"
#include "is-even.h"

TEST(MySoftwareModule, IsEvenWithOddNumberReturnsFalse) {
  EXPECT_FALSE(isEven(7));
}

TEST(MySoftwareModule, IsEvenWithEvenNumberReturnsTrue) {
  EXPECT_TRUE(isEven(8));
}

UTEST_MAIN();
```

and run them:

```console?prompt=$
$ cc test.c
$ ./a.out
[==========] Running 2 test cases.
[ RUN      ] MySoftwareModule.IsEvenWithOddNumberReturnsFalse
[       OK ] MySoftwareModule.IsEvenWithOddNumberReturnsFalse (631ns)
[ RUN      ] MySoftwareModule.IsEvenWithEvenNumberReturnsTrue
[       OK ] MySoftwareModule.IsEvenWithEvenNumberReturnsTrue (631ns)
[==========] 2 test cases ran.
[  PASSED  ] 2 tests.
$
```

Neat. The tests passed. But what does that *mean*?

Ignore the particulars of the syntax and the names of things for a moment.
Focus on the function calls to `isEven`.

These tests exercise a small sample of the very large space of even and odd
numbers (about two billion each) that could be passed into this function. The
tests assume a "regular" implementation, as opposed to a "silly"
implementation. For example, these tests would not do a very good job checking
the correctness of the following implementation of `isEven`:

```c
bool isEven(int num) {
  switch (num) {
    case 0: case 2: case 4: case 6: case 8: return true;
    case 1: case 3: case 5: case 7: case 9: return false;
    // TODO: add the rest of the numbers
    default: return false;
  }
}
```

This is a somewhat reductive example, but such "stub" functions are not
uncommon in production codebases. The band-aid solution to this is generally to
make the unimplemented case abort the program, and have a unit test checking
for an abort when passing in unimplemented input.

> **Pause for a moment.** Can you think of a testing strategy that might do
> better at detecting "bugs" such as the stub implementation above? Try and
> think outside the box. There is very little objective "right" and "wrong"
> here and we'll come back to this thought later in the module.

Sometimes your programming environment might change how you think about unit
testing your code. In the above C environment, there are no run-time exceptions
to handle and types are decided at compile time. There is no need to test that
you will always get a `bool` back from `isEven`---it is guaranteed. In general,
there is no need to test infrastructure guarantees[^bernhardt-stripe]. In other
programming environments, you might have fewer things guaranteed by the
compiler or runtime. Let us consider a Python language equivalent of `isEven`:

[^bernhard-stripe]: Again, *usually*. Refer back to renowned software engineer
    and speaker Gary Bernhardt's
    [tweet](https://twitter.com/garybernhardt/status/1433474928024735748) for
    an argument in favor of testing outside infrastructure.

```python
def is_even(num):
  if num in (0, 2, 4, 6, 8): return True
  if num in (1, 3, 5, 7, 9): return False
  # TODO: add the rest of the numbers
  return False
```

There is one big difference in Python compared to C: you will notice that there
are no types to be found! This is because Python is a dynamically typed
language. It does not require you to annotate your variables or function
signatures with types. This means that it's possible to pass other types such
as a string, or a floating point number, or something else entirely to
`is_even`, and it won't be a compile-time error. It won't be a run-time error
either, in this case; `is_even` will return `False`.

So what *should* it do, given a non-integer? That's to be written in the
specification, and tested in the unit tests. In this case, appropriate tests
might ensure that the code raises an exception, or that it returns some
sentinel value.

### Other things to test

<!-- TODO(max): review 4350 notes for more detail here. perhaps it's more
useful to instead of splitting it by approach, describe different attributes of
test strategies? -->

When testing a function, there are two main approaches: blackbox testing, and
whitebox testing.

When writing blackbox unit tests, assume the function definition is hidden. All
you get is the signature. What inputs can you think of to break the function?
Let's look at `isEven` again.

```c
bool isEven(int num);
```

Some interesting values come to mind: what happens if you pass zero? A negative
number? A very large number? Integers in C are bound to some platform-dependent
size. What happens if you pass `INT_MIN` or `INT_MAX` to the function? Without
looking at the body of this function in particular, there is not much else to
test in this style. Other signatures and other programming languagea may leave
room for more interesting test cases---maybe they operate on strings or
floating point numbers or something more complicated (see for example
JavaScript's number type).

When writing whitebox unit tests, on the other hand, assume you have access to
the current function definition. What test cases might break it? One common
strategy is coverage-based testing---ensuring that all code paths through the
function are tested. This requires figuring out values that pass and fail
various conditionals, exercise behaviors of loops, and so on. Some of the
conditionals may be implicit, if they happen in functions called inside the
function you are testing. <!-- TODO(max): This takes more care -->

<!-- TODO: example of coverage based testing -->

Although coverage is a good way to find code paths you haven't tested, you
should be wary about blindly chasing 100% coverage. There are plenty of cases
where a code path just isn't that interesting or error-prone; writing tests for
such paths purely to improve your coverage metric can waste time and hide the
few tests that actually matter among lots that don't.

<!-- TODO(max): it also gets "invalidated" if you change the implementation
significantly -->

### Naming tests

You may notice that the unit tests for the `isEven` function have very verbose
names. This is not because the course staff are enthusiastic Java
programmers---we are not---but instead because the names serve as
documentation.  Imagine writing a test case with the name `IsEvenTests`, that
expects different results with a bunch of different numbers. With your current
implementation of `isEven` and with your current context, that may be fine. But
you will likely come back to these tests in a year or three, with the
implementation of `isEven` having completely changed, and wonder what made
these numbers so special. Or perhaps your coworker will wonder about these
things, because they did not write the code in the first place.

<!-- TODO(max): Add examples of bad test names and critique them -->

Having descriptive test names also separates concerns for the testing harness.
If only part of the `isEven` function breaks, it would be nice to know at a
glance *which* part broke. `IsEvenWithOddNumberReturnsFalse` failed? Well. Now
you know what to take a look at.

### Which functions to test

Write tests for code you write. Sometimes when writing tests for a function *f*
that calls another function *g*, it is tempting to write tests that directly or
indirectly check the output of *g*. Assuming that *g* is independently well
tested (by you or by its author), this is unnecessary[^mocking].

[^mocking]: Some people take extra care to avoid this by using a technique
    called *dependency injection* and *mocking* the third-party functions, but
    the community is divided on its merits. We will talk more about this later.

Sometimes the software you are building is meant to be consumed by other
programmers, either in the form of a library, or a service. Either way, your
software will provide an Application Programming Interface---an API. Because
this is the primary way your users will be interacting with your software, it
is imperative these API functions be well-tested. You will likely also write
smaller building blocks---internal functions, classes, or other services. Test
these, too.

### Maxims

**Test small units of code as directly as possible.** Ideally, your functions
should be small and have simple lives. And ideally tests should call the
functions they are testing directly. That's the simplest way to make sure that
you're actually calling the intended function, that you're actually calling
with the variant you intended to test, and that something else did not affect
your results.

**Avoid "round trips" through layers of software.** Round trips, including
nested function calls, or network requests, or disk I/O, or other things,
increase the amount of noise in your testing. Noise in this context refers to
potential unexpected failures that are unrelated to the code you wrote.

<!-- TODO(max): if your software involves layers, test each layer independently
and also working together; coupling -->

**Avoid stateful computation.** If your test requires some setup, such as
creating a file on the disk, or adding a table to a database, you will likely
run into issues with concurrency. Tests that have shared mutable state may
break when run concurrently, leading to a slow, sequential test suite.
Additionally, this violates the "round trips" maxim above.

**It’s not a test unless you watch it fail.** Make sure your tests are running!
If they have never failed, it's entirely possible that you are testing the
wrong function, or not running your tests, or something somewhere is very, very
broken.

<!-- TODO(max): unit vs integration; "continuum of tests" -->

Few real tests perfectly fit into one category:

* Units often depend on other units
* Your language or architecture can prevent isolated testing of such units
* Many unit tests, therefore, end up "seeing" other units indirectly

But your intent still matters:

* Unit and integration tests serve different purposes
* Don't let technical constraints blind you to that fact
* Write both unit and integration tests, and keep them separate
  * Your unit tests may end up testing multiple units, and that's okay
  * Your integration tests might not cover certain units, and that's okay too

## Lecture 4

The function we wrote above is fairly straightforward to test. If you wanted
to, it is not difficult to enumerate the entire space of inputs for `isEven`
and check their results. On a modern computer, this would take no more than a
second. So what makes software difficult to test? And, implicitly, should we
factor software to be easier to test?

In the previous lecture, we alluded to parts of this difficulty with the
testing maxims: test small units of code; avoid round trips; avoid state. Let's
break those down.

### Test small units of code

With any luck, you will have been advised to write code with single-purpose,
easily-understandable, composable units. While there is always some discourse
about how big functions should be and where to divide them, it's easier to test
smaller chunks than bigger chunks. Consider the case of coverage-based testing
from before: the more conditionals you have to reason about, the harder your
test cases get. If your function has multiple conditional early returns, some
large `if` statements, and a loop, you're in for a rough time.

Consider also the case where you have a "compound" function that does two
things. Maybe `void setAgeAndHeight(int age, int height)`. It's not clear how
to test this function---do you write one test that tests two of its behaviors?
Write two tests, each testing one behavior? What about the complex behavior
space for valid and invalid inputs? It would be easier to test if it were split
into two functions that could be tested independently: `void setAge(int age)`
and `void setHeight(int height)`. Then it is reasonably straightforward to
write:

```c
TEST(PeopleSoft, SetAgeSetsAge) {
  Person person;
  person.setAge(50);
  EXPECT_EQ(person.age(), 50);
}

TEST(PeopleSoft, SetHeightSetsHeight) {
  Person person;
  person.setHeight(70);
  EXPECT_EQ(person.height(), 70);
}
```

And, as before, if you have a test failure in the future, the failing test
should clearly point to the function that broke.

### Avoid round trips

Often it is tempting to test the internals of a bit of code indirectly by
calling it via another function. Maybe this is because the top-level function
requires fewer parameters, or less state setup, or neatly packages up its
results---whatever the reason may be, try to resist this temptation. If at all
possible, call the function directly by name.

As an example, we can look at the unfortunate `setAgeAndHeight` function from
earlier. Pretend it is implemented as follows:

```c
void setAgeAndHeight(int age, int height) {
  setAge(age);
  setHeight(height);
}
```

Instead of testing `setAge` by calling `setAgeAndHeight` and then reading the
age in the test, call `setAge` directly! This can be tricky when writing
private methods. There are several ways around this, of which we recommend two.
The first is to make the method public. This is not always an option; some
methods should stay private. The second, which is not always available either,
is to use the language-specific feature that exposes private methods to tests.
C++, for example, has `friend` declarations.

We don't mean to discourage you from writing *integration tests*---tests that
run a whole suite of software as one unit to ensure that it works
together---but instead encourage you to keep your unit tests unit-y.

* Avoid state
* I/O
* Randomness
* Filesystem / network

`void computeAndPrintResult()`

That function does not return anything and only produces its output as an I/O
side effect. It would be easier to test if it were split into two functions
`int computeResult()` and `void printResult(int)`.

(API surface is I/O heavy and not mockable; software is fundamentally
nondeterministic; etc)

Factor software for testability. Test from within, and optionally from without.

### Parting thoughts

When you change your software, do you run the tests of everybody who uses your
software?

There is a programming language called Rust and software tooling for Rust
programmers to publish package their software into units called *crates*. With
every release of the Rust compiler, the Rust team runs the compiler on many
crates to check for regressions[^crater].

[^crater]: https://github.com/rust-lang/crater

Software engineers who write programming language infrastructure at large
companies (Clang at Google and Facebook, Go at Google, HHVM at Facebook, etc)
are not doing so in a vacuum; most of the time, they have an internal customer
that uses their compiler or language runtime. These teams tend to also test
their releases against their customers' tests.

What do you do if you find breaking behavior surfaced by a large integration
test written by your client?

## Lecture 4.5

### Strategies for isolating units

Abstraction is wonderful. It helps you paper over the nasty stuff while you
write your elegant software. It helps you replace components without getting
into the weeds in every single other component of your software. There's a
reason they teach it in introductory computer science courses.

Abstraction is terrible. It leads to code bloat. People pick the wrong
abstractions too frequently. It hides details that are important for
correctness, security, or performance. There's a reason that you learn some of
the gnarly details in the introductory computer science course.

<style>
/* https://stackoverflow.com/a/43691462/569183 */
img[src*='#left'] {
    float: left;
}
img[src*='#right'] {
    float: right;
}
img[src*='#center'] {
    display: block;
    margin: auto;
}
</style>

![]({{site.baseurl}}/assets/images/layers.jpg#right "Shrek saying 'Layers!' angrily to Donkey. You can feel the Scottish accent in your bones.")

Abstraction leads to layers.

Imagine you're writing a web application that multiple people will use, and
that each person needs a profile page. This sounds like it needs a database, so
you install your favorite database management system (DBMS) and make some
tables.

You then start writing the application part of it. You scaffold some web
routes: the index page, `/`; `/signup`, `/login`, `/page/:user`, etc. Right
now they all return "hello, world" but soon they will do Real Stuff.

You start writing raw SQL queries inside your application endpoints to fetch
and filter users, but then you sit back and think *hmm, maybe I would like to
migrate databases one day... I should use an ORM*. Maybe you also want to avoid
SQL injections, (which happen oh-so-frequently due to mixing code and data).
Totally valid reasons. You install the ORM du jour and use that instead.

Life is good. The techno music is thumping[^cake]. Your foot is tapping and the
code is flowing. You blow through several albums and finish a workable
prototype. You're all ready to ship.

[^cake]: At the time of writing, I'm actually listening to CAKE.

Then, suddenly, with a sinking feeling and growing horror, you realize that you
don't have any tests and you have no idea how to test your application. You
see, it kind of looks like this imagined code:

```python
# app.py
from flask import Flask, request, render_template
from dbstuff import create_db
from mailer import send_email

@app.post("/signup")
def do_signup():
    email = request.form.get("email")
    password = request.form.get("password")
    if len(password) < 7:
        return "<p>Pick a longer password, silly</p>", 400
    hashed = bcrypt(password)
    code = new_uuid()
    send_email(email, subject="Confirm your email", body="Code is {code}")
    with db.session() as session:
        user = db.User(email, hashed, code)
        session.commit(user)
    return f"<p>Success! Thanks for joining, {user.fullname}.</p>"

@app.get("/users")
def list_users():
    return render_template("users.html", db=db)

db = create_db("sqlite://")
app = Flask(__name__)
app.run("localhost", 8080)
```

```html
{% raw %}
<!-- users.html -->
<html>
    <head></head>
    <body>
        <ul>
        {% for user in db.User.all() %}
        <li><a href="/{{ user.username }}">{{ user.fullname }}</a></li>
        {% endfor %}
        </ul>
    </body>
</html>
{% endraw %}
```

I am not picking on Flask or Python or any specific technology here. Flask is
just fairly ubiquitous and Python is fairly readable. I am picking on some of
the other software design choices. So pause and think about it this microcosm
of larger issues: what's going on? Take a moment to think about how you woud
test it.

...alright, welcome back. I hope you came to the conclusion that it's just not
obvious. What are you going to do in your tests, start up your HTTP server and
fire requests at it? Infer if the process succeeded from the HTML? That's the
core of the problem: there is only one way for data to flow in (request
parameters), the control-flow graph is very deep (call, call, call, call,
return, return, return, return), and half of the logic has a bunch of side
effects, such as writing to the database or sending an email. We'll learn more
about why side effects are bad news later, but for now you can trust us.

The core problem in this example is not actually the layers or the
abstraction---we've misled you---but the entanglement *between* the
hypothetical layers and differing amounts of abstraction. <!-- TODO(max): Hm,
rewrite -->

Here's a diagram to illustrate what we mean. We've used boxes to indicate
entire units that can be called. Dashed boxes represent library code we did not
write, whereas solid boxes represent our code:

<object class="svg" type="image/svg+xml" data="{{site.baseurl}}/assets/images/modularization-bad.excalidraw.svg">
  If you're seeing this text, it means your browser cannot render SVG.
</object>

There's one way into a monolithic unit of code, which means no way to test the
middle bits without testing the rest, too.

Let's take a look at a different imagining of the same application:

```python
# lib.py
def validate_password(password):
    if len(password) < 7:
        raise InvalidPassword("Password too short")

def create_validation_email(code):
    return {"subject": "Confirm your email", "body": "Code is {code}"}
```

```python
# app.py
from flask import Flask, request, render_template
from dbstuff import create_db
from mailer import send_email
from lib import validate_password, create_validation_email

@app.post("/signup")
def do_signup():
    email = request.form.get("email")
    password = request.form.get("password")
    validate_password(password)
    hashed = bcrypt(password)
    code = new_uuid()
    send_email(email, **create_validation_email(code))
    with db.session() as session:
        user = db.User(email, hashed)
        session.commit(user)
    return f"<p>Success! Thanks for joining, {user.fullname}.</p>"

@app.get("/users")
def list_users():
    all_users = db.User.all()
    return render_template("users.html", all_users=all_users)

db = create_db("sqlite://...")
app = Flask(__name__)
app.run("localhost", 8080)
```

```html
{% raw %}
<!-- users.html -->
<html>
    <head></head>
    <body>
        <ul>
        {% for user in all_users %}
        <li><a href="/{{ user.username }}">{{ user.fullname }}</a></li>
        {% endfor %}
        </ul>
    </body>
</html>
{% endraw %}
```

Now you can test individual elements, such as `validate_password` without
needing to be connected to the internet and sending an email. Imagine not being
able to test password validation because you're on a train...

And now you can test `create_validation_email` and notice that there has been a
bug in there the entire time: you don't use the proper string formatting syntax
(`f"{xyz}"`, note the leading `f`), so the desired confirmation code never gets
embedded in the actual email to your real, frustrated, human customers.

Likewise, you can test the HTML rendering of the users page---if you
like---without connecting to the database; you can create temporary `User`
objects without needing to commit (write) and then fetch them.

Here's a new diagram to illustrate the new architecture. Because we have
extracted `validate_password` and `create_validation_email` into their own
stateless functions, they can be more easily tested in isolation:

<object class="svg" type="image/svg+xml" data="{{site.baseurl}}/assets/images/modularization-good.excalidraw.svg">
  If you're seeing this text, it means your browser cannot render SVG.
</object>

We've also indicated that these can now be considered "unit" tests instead of
"integration" tests because they test one small feature at a time.

### Maxim: avoid round trips
### The Database interface
### Self-contained units
### Maxim: avoid state
### Writing integration tests
### Testing at scale
### Doxygen

## Lecture 5

You write tests for a project, but they keep breaking because no one runs them.
How would you fix this?

### Continuous integration
### Popular CI tools
### GitHub Actions
This section could go out of date fast.
### Continuous integration vs build systems
### Security considerations for CI
### Testing CI

## Lecture 6

### Limitations of tests
### Coding practices for bug reduction
### Adversarial mindset
### Other ways to check runtime behavior
### What constitutes "behavior"?
### The parable of the intern
### Checking behavior statically
Types and static analysis; proofs
### Proof engineering
### Adversarial situations
You have been assuming you have normal coworkers

Sometimes they are silly and paste large chunks untested from LLMs. You need a
totally different mindset for this

Or, worse, your coworkers are secretly working for a nation-state
### Machine learning generating tests
Speaking of LLMs, ...
