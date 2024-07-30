# Homework 6: BLD, Constructive

## Build me up, buttercup

In this assignment, you'll be adding a build system to an existing software
project written in C. The project is based on a real open-source project, but
we've modified it to be more conducive to the task at hand.

The project in question, called *jvm*, has gotten to the point where manually
rebuilding every file by hand is frustrating and error-prone. To make its
developers' lives easier, you'll write a Makefile to build it automatically.

Start by cloning the repository from `https://github.com/cs50isdt/jvm`.

### Step 1: determine the build graph

Before you write a Makefile to automate the build process, however, you need to
figure out what that build process is. The following questions will help you
discern the proper way to build the code you've been given. We designed the
questions to help you, but you do not have to provide us the answers. Skip
them at your own peril.

1. How many executable files is this project designed to have? What are they
   called? How do you know? (*Hint*: there are multiple ways to determine this,
   but it may help to think about what piece of code every C or C++ program
   must have.)
1. Starting from the main `.c` file for each executable, list all the other
   `.c` files needed for that executable to compile and run. (*Hint*: follow
   the `#include`s.)
1. Assume that, during the build, every `.c` file will be compiled into a
   matching `.o` file then those `.o` files will be linked together as
   appropriate to create the final executable(s). Draw a graph showing the
   compile-time[^compile-time-vs-run-time] dependencies between the
   executable(s), the `.o` files, and the source (`.c` and `.h`) files. Your
   answer to the previous question will be useful here. Do not use wildcards or
   globs---each file should be its own node in the graph.
   1. You may hand draw this on paper or use a free online service like
      [Excalidraw](https://excalidraw.com/) to draw it digitally.
   1. We recommend that you organize the graph with the executable(s)
      horizontally across the top, the object files below them, and the source
      files below those. For each `.o` file an executable depends on, draw an
      arrow pointing from the executable to the `.o` file. Likewise, for each
      source file a `.o` file depends on, draw an arrow pointing from the `.o`
      file to the source file.
   1. If you're unsure of your drawing, feel free to make a private post on
      Piazza and we can let you know if you're headed in the right direction!

[^compile-time-vs-run-time]: Technically, there is compile-time, link-time,
    load-time, and run-time. In C, the *compile-time dependencies* for a `.o`
    file almost always consist of a single C file and one or more header files.
    Header files contain enough information for the resulting `.o` file to know
    how to call the functions they declare (the *interfaces*), but they don't
    contain the actual *implementations* of those functions. Those
    implementations live in their own `.o` files, and they're only needed while
    linking the final executable, which has link-time dependencies on all of
    the implementations. This particular kind of interface is known as an
    *application binary interface*, or ABI, and the compile-time dependency is
    why interfaces are specified in header files.

### Step 2: express the graph in a Makefile

Now that you've drawn out the different files involved in the build and the
dependencies between them, it's time to start on a Makefile! **Please create a
file called `Makefile` at the root of the repository that builds the
executable(s) as described above.**

When writing your Makefile, you must do the following:
1. If an [implicit
   rule](https://www.gnu.org/software/make/manual/html_node/Implicit-Rules.html#Implicit-Rules)
   exists to do what you want, use it instead of writing your own recipe.
   (*Hint*: remember that most implicit rules are customizable by setting
   specially-named variables.)
1. Ensure that *both* `make` and `make all` cause all executables to be built.
1. Ensure that any individual `.o` or executable file can be built by passing
   its filename to Make as a target.
1. Specify the minimal correct set of prerequisites for each target (i.e.
   rebuild each target only when strictly needed).
1. Use a C compiler such as `gcc` or `clang` for compilation and linking. The
   choice of which is up to you, except the default of `cc`, which you must not
   use.
1. Include the following flags in the compiler invocation: `-Wall -Wextra
   -std=gnu99`.
1. Include the following flags at the *very end* of the linker invocation:
   `-lm`. (Without this, the linker will fail. *Hint*: take a look at Make's
   [documentation](https://www.gnu.org/software/make/manual/html_node/Catalogue-of-Rules.html#Catalogue-of-Rules)
   for the "Linking a single object file" implicit rule.)
1. Ensure that running `make clean` removes all generated files.
1. Ensure that the `clean` and `all` rules do their jobs even if files named
   `clean` or `all` are present on disk.

Apart from these requirements, you may use your discretion about how to
implement things. Please try to follow the general practices set out in lecture
and the [GNU Make
manual](https://www.gnu.org/software/make/manual/html_node/index.html), though.

Once you've fulfilled these requirements to the best of your ability, test out
your Makefile. Try building various targets. Does Make do what you expect?
Next, try updating various source files (you can use `touch` to indicate to
Make that file has changed without actually altering it), rerunning `make`
along the way. Do the right targets get rebuilt? Does anything get rebuilt that
shouldn't?

### Step 3: teach an old DAG new tricks

C code isn't the only thing in this repository that can be compiled. As you
have hopefully seen by now, one of the executables you've built is named `java`
and implements a small Java Virtual Machine (JVM) capable of running a subset
of valid Java programs. Inside the `tests/` directory are a number of Java
programs, intended to test out this JVM.

Before you can run the Java programs, however, you have to compile the `.java`
source you've been given into Java *bytecode*, which is what the JVM knows how
to read. Java bytecode is stored in files with the extension `.class`. You can
use the standard Java compiler, `javac` (which is installed on the homework
server), to perform this compilation.

**Add a pattern rule to your Makefile that can compile any given `.java` file
inside `tests/` into a matching `.class` file.** (The `.class` files must also
reside in `tests/` and have an identical name save for the changed extension).
In your recipe for this rule, please use [automatic
variables](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html#Automatic-Variables)
wherever possible. The rule should build only the given `.class` file, and it
should rebuild that file if the source changes. **Update your `clean` rule as
appropriate.**

Take a look inside the `tests/` directory for a suite of sample Java programs.
Try running the HelloWorld program using your interpreter: first build
HelloWorld and the interpreter with `make java tests/HelloWorld.class`, then
run HelloWorld with `./java -cp tests HelloWorld`! (Note how you must provide
the directory and class name separately instead of as a single path.)

### Step 4: classy tests

Makefiles can do more than just compile code; since recipes can consist of
arbitrary commands, developers often create special rules to perform common
tasks, even if those tasks don't produce files on disk. Like running unit
tests, for example.

**Add a pattern rule to your Makefile that can run any given test.** The rule
must have targets of the form `run-ClassName`. To run a test, use `./java -cp
tests ClassName`. You may find the automatic variable `$*` helpful here. When
you invoke such a target, it should run successfully even if you haven't
explicitly built *anything* else yet. There is no need to make this rule phony,
but you get an imaginary gold star if you make it work.[^phony]

[^phony]: It's not as simple as you might think. Test out your hypothesis by
    running, for example, `touch run-HelloWorld` and seeing if Make will still
    run your Java program with `make run-HelloWorld`.

**Add a rule, `test`, that runs all the tests.** This rule should rely on the
`run-*` rules you just created to actually perform its work. This rule should
be phony, as it needs to run even if a file called `test` exists on disk.

## Submitting your work

To submit, submit your Git repository to Gradescope.

This is a good opportunity to exercise your Git skills from last
module---you're free to make your changes using as many commits as you want!
