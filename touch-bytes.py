#!/usr/bin/env python3
import os
import subprocess

ON_WINDOWS = os.name == "nt"

def show(s):
    if isinstance(s, str) and ON_WINDOWS and not s.isascii():
        # Python on Windows (on GitHub Actions, at least) has issues when
        # trying to print most non-ASCII characters
        return s.encode("utf-8")
    elif isinstance(s, bytes) and not ON_WINDOWS:
        try:
            return s.decode("utf-8", "strict")
        except UnicodeDecodeError:
            pass
    return s

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
        print(f"Failed to touch {show(fname)!r}: {type(e).__name__}: {show(str(e))}")
    else:
        print(f"Created {show(fname)!r}")

print("listdir:")
for fname in os.listdir(b"."):
    print(f"\t{show(fname)!r}")

r = subprocess.run(["git", "status", "--porcelain", "-z"], check=True, stdout=subprocess.PIPE)
print("git status:")
for fname in r.stdout.split(b"\0"):
    if fname:
        print(f"\t{show(fname)!r}")

for gitignore in [
    "f??.txt",
    "f????.txt",
    "f*.txt",
    "snowman-?.txt",
    "snowman-??.txt",
    "snowman-???.txt",
    "snowman-*.txt",
    "goat-?.txt",
    "goat-??.txt",
    "goat-????.txt",
    "goat-*.txt",
    "low-?.txt",
    "low-???.txt",
    "low-*.txt",
]:
    with open(".gitignore", "w") as fp:
        print(gitignore, file=fp)
    r = subprocess.run(["git", "status", "--porcelain", "--ignored=matching", "-z"], check=True, stdout=subprocess.PIPE)
    ignored = [line[3:] for line in r.stdout.split(b"\0") if line.startswith(b"!!") and b"/" not in line]
    print(f"Gitignored by {show(gitignore)!r}:")
    for fname in ignored:
        print(f"\t{show(fname)!r}")
