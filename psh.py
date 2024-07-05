#!/usr/bin/env python3

"""psh: a simple shell written in Python"""

import os
import subprocess
import shlex
import sys

# https://xiayingp.gitbook.io/build_a_os/os-interfaces/pipes

# TODO(max): Define shell variables and add them to environment variables
# TODO(max): Pass env to Popen
# TODO(max): Read shell/environment variables


def memfd(output: bytes):
    fd = os.memfd_create("tmp")
    result = open(fd, "w+b")
    result.write(output)
    result.seek(0)
    return result


def main():
    while True:
        try:
            inp = input("psh> ")
        except EOFError:
            inp = "exit"
        pipeline = inp.split("|")
        stdin = sys.stdin
        stdout = sys.stdout
        stderr = sys.stderr
        for idx, command in enumerate(pipeline):
            # TODO(max): Figure out how to do I/O pipes and stuff for built-in
            # commands.
            tokens = shlex.split(command)
            # TODO(max): Ask students why cd needs to be a builtin
            if tokens[0] == "cd":
                os.chdir(os.path.abspath(tokens[1]))
                continue
            # TODO(max): Ask students why it is fine to comment out pwd "builtin"
            # if tokens == ["pwd"]:
            #     print(os.getcwd())
            #     continue
            if tokens[0] == "banana":
                stdin = memfd(b"Peel!\n")
                continue
            if tokens == ["exit"]:
                print("Goodbye.")
                return
            result = subprocess.Popen(
                tokens, stdin=stdin, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            sys.stderr.write(result.stderr.read().decode("utf-8"))
            stdin = result.stdout
        # Write the last command's stdout to shell stdout
        sys.stdout.write(stdin.read().decode("utf-8"))


if "__main__" == __name__:
    main()
