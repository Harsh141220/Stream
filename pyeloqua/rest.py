""" REST API Class """

from __future__ import print_function
from time import sleep
from datetime import datetime
from copy import deepcopy
from json import dumps, dump, load
import requests

from .pyeloqua import Eloqua
from .error_handling import _elq_error_

############################################################################
# Constant definitions
############################################################################

POST_HEADERS = {'Content-Type': 'application/json'}

############################################################################
# REST class
############################################################################

class Rest(Eloqua):
    """ Extension for Bulk API operations """

    def __init__(self, username=None, password=None, company=None, test=False):
        """
        Initialize bulk class:

        Arguments:

        :param string username: Eloqua username
        :param string password: Eloqua password
        :param string company: Eloqua company instance
        :param bool test: Sets up test instance; does not connect to Eloqua
        :return: Bulk object
        """
        Eloqua.__init__(self, username, password, company, test)
        self.page = None
        self.count = None
        self.depth = None

    def reset(self):
        self.page = None
        self.count = None
        self.depth = None
