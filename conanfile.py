"""Gnome library package for conan.io

This receipt build GLib under Conan context
"""
import os
from tempfile import mkdtemp
from conans import ConanFile
from conans.tools import download
from conans.tools import untargz


class GLibConan(ConanFile):
    """Download glib source files and build

    All artifacts are installed and exported
    """
    name = "glib"
    version = "2.51.1"
    url = "http://github.com/uilianries/conan-glib"
    license = "https://github.com/GNOME/glib/blob/master/COPYING"
    author = "Uilian Ries <uilianries@gmail.com>"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "txt"
    description = "Gnome library package for conan.io"
    temp_dir = mkdtemp('conan-glib')

    def source(self):
        package_name = 'glib-%s.tar.xz' % self.version
        url = 'https://ftp.gnome.org/pub/gnome/sources/glib/2.51/' + package_name
        download(url, package_name)
        untargz(package_name)
        os.unlink(package_name)

    def build(self):
        if self.settings.os == "Linux":
            self.run("configure --prefix=%s && make && make install" %
                     self.temp_dir)
        else:
            raise AssertionError("Only Linux is supported.")

    def package(self):
        self.copy("*", dst="lib", src=self.temp_dir.join('lib'))
        self.copy("*", dst="bin", src=self.temp_dir.join('bin'))
        self.copy("*", dst="include", src=self.temp_dir.join('include'))
        self.copy("*", dst="share", src=self.temp_dir.join('share'))

    def package_info(self):
        self.cpp_info.libs = ["glib"]
