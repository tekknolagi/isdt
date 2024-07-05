#!/usr/bin/env python3

"""psh: a simple shell written in Python"""

import io
import mmap
import os
import subprocess
import shlex
import sys

# https://xiayingp.gitbook.io/build_a_os/os-interfaces/pipes

# TODO(max): Define shell variables and add them to environment variables
# TODO(max): Pass env to Popen
# TODO(max): Read shell/environment variables


def main():
    toplevel_stdin = sys.stdin
    toplevel_stdout = sys.stdout
    toplevel_stderr = sys.stderr
    while True:
        try:
            inp = input("psh> ")
        except EOFError:
            inp = "exit"
        pipeline = inp.split("|")
        stdin = toplevel_stdin
        stdout = toplevel_stdout
        stderr = toplevel_stderr
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
                print("Peel!")
                continue
            if tokens == ["exit"]:
                print("Goodbye.")
                return
            result = subprocess.Popen(
                tokens, stdin=stdin, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            toplevel_stderr.write(result.stderr.read().decode("utf-8"))
            stdin = result.stdout
        toplevel_stdout.write(result.stdout.read().decode("utf-8"))


if "__main__" == __name__:
    main()
