"""Conan test receipt

Validates GLib Conan Package
"""
import os
from conans import ConanFile, CMake


_USERNAME = os.getenv('CONAN_USERNAME', 'uilianries')
_CHANNEL = os.getenv('CONAN_CHANNEL', 'testing')


class GLibTestConan(ConanFile):
    """Build and Execute a unit test

    This test ensure the package dependency
    """
    settings = "os", "compiler", "build_type", "arch"
    requires = "glib/2.51.1@%s/%s" % (_USERNAME, _CHANNEL)
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' %
                 (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def imports(self):
        self.copy("*.so*", "bin", "lib")
        self.copy("*.a", "lib", "lib")

    def test(self):
        self.run("cmake --build . --target check")
