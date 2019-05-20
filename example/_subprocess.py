# -*- coding: utf-8 -*-
import multiprocessing as mp
from pydevtoolkit import forkedpdb


def worker():
    foo = 'Hello world!'
    forkedpdb.set_trace()

def main():
    process = mp.Process(target=worker)
    process.start()
    process.join()

if __name__ == '__main__':
    main()
