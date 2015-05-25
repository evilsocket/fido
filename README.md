FIDO
==

Fido is a minimalistic C/C++ project generator supporting various templates.

Installation
==

    python setup.py build
    sudo python setup.py install

Usage
==

    Usage: fido <action> [template] (path)

    Available actions:

                       help : Print the usage menu.
                     create : Create a project with the specified template, requires a template and a path.
                        add : Add one or multiple files to the proper folders by their extensions.
                      build : Build the current project.
                      clean : Clean built files for the current project.
                      reset : Available only for certain templates, remote every build generated file.

    Available templates:

             android-make-c : Create a native Android C project based on Makefile.
           android-make-cpp : Create a native Android C++ project based on Makefile.
        android-ndk-build-c : Create a native Android C project based on the ndk-build utility.
                    cmake-c : Create a C project based on CMake.
                  cmake-cpp : Create a C++ project based on CMake.
                     make-c : Create a C project based on Makefile.
                   make-cpp : Create a C++ project based on Makefile.

Example
==

    $ fido create make-c sample-project

    [I] Creating project 'sample-project' with template 'make-c' ...
    [D]   Creating project '.fido' file ...
    [D]   Updating variable '#PROJECT_NAME#' in sample-project/Makefile ...
    [D]   Updating variable '#PROJECT_NAME#' in sample-project/.gitignore ...
    [D]   Updating variable '#PROJECT_NAME#' in sample-project/README.md ...
    [D]   Updating variable '#PROJECT_NAME#' in sample-project/src/main.c ...
    [I] DONE

    $ cd sample-project
    $ fido add io.h io.c networking.h networking.c

    [I] Creating 'include/io.h' ...
    [I] Creating 'src/io.c' ...
    [I] Creating 'include/networking.h' ...
    [I] Creating 'src/networking.c' ...

    $ fido build
    $ ./sample-project

    Hello World from sample-project !

Video Example
==

[![asciicast](https://asciinema.org/a/8te8gnp36ii7iypj2j1eg5b6m.png)](https://asciinema.org/a/8te8gnp36ii7iypj2j1eg5b6m)

License
==

This project is copyleft of [Simone Margaritelli](http://www.evilsocket.net/) and released under the GPL 3 license.