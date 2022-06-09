import os
import math
import site
import sys
import requests
import importlib
import subprocess

from typing import Optional
import c4d
from c4d import gui
from c4d import storage

class PN_pip:
    def __init__(self):
        if PN_pip.check_pip() == False:
            self.install_pip()
        try:
            globals()["_pip"] = importlib.import_module("pip._internal")
            self.is_pip_import_successful = True
        except ImportError:
            print("pip not found.")
            self.is_pip_import_successful = False

    @staticmethod
    def check_pip():
        # Checks if pip is installed.
        if importlib.util.find_spec("pip") is None:
            return False
        else:
            return True

    @staticmethod
    def get_3rd_party_module_path():
        return site.USER_SITE

    def install_pip(self):
        installer_url = "https://bootstrap.pypa.io/get-pip.py"
        installer = requests.get(installer_url).content
        installer_path = os.path.join(os.path.dirname(__file__), "get-pip.py")
        with open(installer_path, "wb") as f:
            result = f.write(installer)
        getpip = importlib.import_module("get-pip")
        getpip.main()
        os.remove(installer_path)

    def install_module(self, module_name: str):
        # Installs a module.
        if self.is_pip_import_successful == True:
            globals()["_pip"].main(["install", module_name])
        else:
            print("pip not found.")

    def uninstall_module(self, module_name: str):
        # Uninstalls a module.
        if self.is_pip_import_successful == True:
            globals()["_pip"].main(["uninstall", module_name])
        else:
            print("pip not found.")

    def update_module(self, module_name: str):
        # Updates a module.
        if self.is_pip_import_successful == True:
            globals()["_pip"].main(["install", "--upgrade", module_name])
        else:
            print("pip not found.")

    def get_pip_version(self):
        # Returns the version of pip.
        if self.is_pip_import_successful == True:
            return globals()["_pip"].__version__
        else:
            print("pip not found.")

if __name__ == '__main__':
    if PN_pip.check_pip() == False:
        if gui.QuestionDialog("pip not found.\nDo you want to install pip?"):
            PN_pip()
    else:
        gui.MessageDialog("pip already installed.\n3rd party modules path: " + PN_pip.get_3rd_party_module_path())