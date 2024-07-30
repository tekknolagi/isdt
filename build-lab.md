---
---

# Graph lab

Build system targets are often modeled as a directed acyclic graph (DAG).
Each node in the graph represents a build target and each edge represents a
dependency on another target. A correct build order is a topological sort: an
order in which each target is only built after all of its dependencies have
been built.

We're not going to make a whole build system from scratch, but we will
implement one of the core components in your preferred programming language: a
topological sort.

## Graph representation

Write a class that satisfies this interface (it need not be Python; that's just
the syntax for the interface sketch pseudocode):

```python
class Target:
    def name(self) -> str: ...
    def recipe(self) -> str: ...
    def dependencies(self) -> list[Target]: ...
```

The `name` method should return the name of the target. The `recipe` method
should return the command executed to build the target. The `dependencies`
method should return a list of the target's dependencies.

## A small graph

Now, manually create a small graph of targets and dependencies. Try modeling
the C example from `build.sh`:

```make
foo: foo.o rng.o
	cc -o foo foo.o rng.o

foo.o: foo.c rng.h
	cc -c foo.c

rng.o: rng.c rng.h
	cc -c rng.c

myls.o: myls.c
	cc -c myls.c

myls: myls.o
	cc -o myls myls.o
```

You may need to change around the order (bottom-up) to get your
manually-created `Target` objects to make sense.

## Topological sort

Start by writing a function `execute` that, given a target with no
dependencies, prints the recipe and adds the target's name to the `output`
list.

```python
def execute(target: Target, output: list[str]): ...
```

Then, add another case: if the target has dependencies, `execute` them first.

Now you have a problem: if targets `A` and `B` both depend on `C`, it will
execute (print recipe and append to the output) the recipe for `C` twice. To
fix this, add a `set` parameter called `visited` to `execute`. Before executing
a target, check if its name is in the visited set.

```python
def execute(target: Target, output: list[str], visited: set[str]): ...
```

Check that this works by writing some tests...

## Tests

What are the core properties of your program that you want to test?

Write tests for your topological sort. You can use the example above from
`build.sh`, but you should also think smaller, and be more targeted. What is
your specific test case trying to "break" in your implementation? We'll talk
more about this next module.

## Cycles?

If you have a cycle in your graph, your topological sort will not work. How
might you detect cycles?

## Reading a 'real' Makefile

Now let's try running your topological sort on a real Makefile.

If you want to write your own parser, go for it. If you want to use this nasty
hacked-up thing that accepts a very limited subset of Make syntax, you can use
this too.

```python
name_to_target = {}

first_target = None

with open("Makefile", "r") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        target, dependencies = line.split(":")
        if not first_target:
            first_target = target
        target = target.strip()
        dependencies = dependencies.split()
        recipe = next(f).strip()
        for dependency in dependencies:
            if dependency not in name_to_target:
                name_to_target[dependency] = Target(dependency)
        dependencies = [name_to_target[dependency] for dependency in dependencies]
        if target not in name_to_target:
            name_to_target[target] = Target(target, recipe, dependencies)
        else:
            name_to_target[target]._dependencies = dependencies
            name_to_target[target]._recipe = recipe

first_target = name_to_target[first_target]

output = []
execute(first_target, output)
print(output)
```

It assumes every target has a recipe, and that the recipe is one line and on
the next line.
