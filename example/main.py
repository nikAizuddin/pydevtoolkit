# -*- coding: utf-8 -*-
import subprocess as sp


def main():
    process = sp.Popen(['python', '_subprocess.py'])
    process.wait()

if __name__ == '__main__':
    main()
