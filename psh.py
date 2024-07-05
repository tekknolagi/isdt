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


class FakeProcess:
    def __init__(self, output: bytes):
        self.fd = fd = os.memfd_create("tmp")
        self.stdout = stdout = open(fd, "w+b")
        stdout.write(output)
        stdout.seek(0)

    def close(self):
        self.stdout.close()
        os.close(self.fd)


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
                result = FakeProcess(b"Peel!\n")
                stdin = result.stdout
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
        sys.stdout.write(result.stdout.read().decode("utf-8"))


if "__main__" == __name__:
    main()
