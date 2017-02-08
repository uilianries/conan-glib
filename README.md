[![Build Status](https://travis-ci.org/uilianries/conan-glib.svg?branch=master)](https://travis-ci.org/uilianries/conan-glib) [![License (LGPL version 2.1)](https://img.shields.io/badge/license-GNU%20LGPL%20version%202.1-blue.svg?style=flat-square)](http://opensource.org/licenses/LGPL-2.1)  

# conan-glib  

#### Gnome library package for [Conan.io](https://conan.io)

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/glib/2.51.1/uilianries/stable).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py
    
## Upload packages to server

    $ conan upload glib/2.51.1@uilianries/stable --all
    
## Reuse the packages

### Basic setup

    $ conan install glib/2.51.1@uilianries/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    glib/2.51.1@uilianries/stable

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.