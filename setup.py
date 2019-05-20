# -*- coding: utf-8 -*-
from os import path
from setuptools import setup, find_packages

def get_version():
    versionfile = path.join(path.dirname(path.abspath(__file__)), 'VERSION.txt')
    with open(versionfile) as f:
        version = f.read().strip()
    return version

def setup_package():
    setup(
        name='pydevtoolkit',
        version=get_version(),
        description='Python 3.x developer toolkit',
        long_description='Python 3.x developer toolkit',
        keywords='python development debug',
        author='Nik Mohamad Aizuddin bin Nik Azmi',
        author_email='nik-mohamad-aizuddin@yandex.com',
        maintainer='Nik Mohamad Aizuddin bin Nik Azmi',
        maintainer_email='nik-mohamad-aizuddin@yandex.com',
        url='https://github.com/nikAizuddin/pydevtoolkit',
        license='MIT',
        packages=find_packages(exclude=('example',)),
        install_requires=[],
        classifiers=[
            'Intended Audience :: Developers',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3.6',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )

def write_version_py():
    pyfile = path.join('pydevtoolkit', 'version.py')

    content = "# THIS FILE IS GENERATED FROM PYDEVTOOLKIT SETUP.PY\n"
    content += "version = '{version}'\n"

    with open(pyfile, 'w') as f:
        f.write(content.format(version=get_version()))

if __name__ == '__main__':
    setup_package()
    write_version_py()

