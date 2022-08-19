#!/usr/bin/env python
# encoding: utf-8

import cactus
import sys

from cactus.cli import main

print("Using: %s" % cactus.__file__)

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)