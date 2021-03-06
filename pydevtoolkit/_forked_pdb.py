#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pdb


class ForkedPdb(pdb.Pdb):
    """A Pdb subclass that only be used from a forked multiprocessing child.
    """

    def interaction(self, *args, **kwargs):
        _stdin = sys.stdin
        try:
            sys.stdin = open(0)
            pdb.Pdb.interaction(self, *args, **kwargs)
        finally:
            sys.stdin = _stdin
