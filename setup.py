# -*- coding: utf-8 -*-

"""
direct PAS
Python Application Services
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
https://www.direct-netware.de/redirect?pas;json_clients

This Source Code Form is subject to the terms of the Mozilla Public License,
v. 2.0. If a copy of the MPL was not distributed with this file, You can
obtain one at http://mozilla.org/MPL/2.0/.
----------------------------------------------------------------------------
https://www.direct-netware.de/redirect?licenses;mpl2
----------------------------------------------------------------------------
setup.py
"""

from distutils.core import setup
from os import path

from dNG.distutils.command.build_py import BuildPy
from dNG.distutils.command.install_data import InstallData
from dNG.distutils.temporary_directory import TemporaryDirectory

def get_version():
    """
Returns the version currently in development.

:return: (str) Version string
:since:  v0.1.2
    """

    return "v1.0.0"
#

with TemporaryDirectory(dir = ".") as build_directory:
    parameters = { "pasJsonClientsVersion": get_version() }

    InstallData.set_build_target_path(build_directory)
    InstallData.set_build_target_parameters(parameters)

    _build_path = path.join(build_directory, "src")

    setup(name = "pas_json_clients",
          version = get_version(),
          description = "Python Application Services",
          long_description = """"pas_json_clients" provide HTTP clients based on the JavaScript Object Notation.""",
          author = "direct Netware Group et al.",
          author_email = "web@direct-netware.de",
          license = "MPL2",
          url = "https://www.direct-netware.de/redirect?pas;json_clients",

          platforms = [ "any" ],

          package_dir = { "": _build_path },
          packages = [ "dNG" ],

          data_files = [ ( "docs", [ "LICENSE", "README" ]) ],

          # Override build_py to first run builder.py over all PAS modules
          cmdclass = { "build_py": BuildPy,
                       "install_data": InstallData
                     }
         )
#
