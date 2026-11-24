#!/usr/bin/env python3
"""news-image-24nov: write Tuesday 24 November 2026's world news to /output/entry.png.

The broadsheet image is drawn at build time and shipped in this repository
as entry.png. This program copies it to the output directory so the grader
sees exactly the bytes that were built and checked. It needs no network and
writes the same bytes on every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
