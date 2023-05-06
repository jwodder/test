#!/usr/bin/env python3
import os
import subprocess

for fname in [
    "foo",
    "föö.txt",
    "snowman-\u2603.txt",
    "goat-\U0001F410.txt",
    b"eighty-\x80.txt",
    b"low-\xED\xB0\x80.txt",
]:
    try:
        with open(fname, "w"):
            pass
    except Exception as e:
        print(f"Failed to touch {fname!r}: {type(e).__name__}: {e}")
    else:
        print(f"Created {fname!r}")

print("listdir:")
for fname in os.listdir(b"."):
    try:
        fname = fname.decode("utf-8", "strict")
    except UnicodeDecodeError:
        pass
    print(f"\t{fname!r}")

r = subprocess.run(["git", "status", "--porcelain", "-z"], check=True, stdout=subprocess.PIPE)
print("git status:")
for fname in r.stdout.split(b"\0"):
    if fname:
        try:
            fname = fname.decode("utf-8", "strict")
        except UnicodeDecodeError:
            pass
        print(f"\t{fname!r}")
