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
#echo(pasJsonClientsVersion)#
#echo(__FILEPATH__)#
"""

# pylint: disable=import-error, no-name-in-module

from dNG.data.http.json_response import JsonResponse
from dNG.runtime.io_exception import IOException

from .client import Client

class JsonClient(Client):
    """
"JsonClient" provides an HTTP client that expects "Content-Type" to be
"application/json".

:author:     direct Netware Group et al.
:copyright:  (C) direct Netware Group - All rights reserved
:package:    pas
:subpackage: json_clients
:since:      v1.0.0
:license:    https://www.direct-netware.de/redirect?licenses;mpl2
             Mozilla Public License, v. 2.0
    """

    def request(self, method, separator = ";", params = None, data = None):
        """
Call a given request method on the connected HTTP server.

:param method: HTTP method
:param separator: Query parameter separator
:param params: Parsed query parameters as str
:param data: HTTP body

:return: (dict) Response data; 'body' may contain the catched exception
:since:  v1.0.0
        """

        # pylint: disable=attribute-defined-outside-init

        if (self.headers is None): self.headers = { }
        if ("ACCEPT" not in self.headers): self.set_header("Accept", "application/json")

        return Client.request(self, method, separator, params, data)
    #

    def _init_response(self, raw_response):
        """
Initializes an HTTP response object based on the received raw data.

:param raw_response: Raw response dict

:return: (object) Response object
:since:  v1.0.0
        """

        # pylint: disable=protected-access

        _return = JsonResponse()
        _return._set_code(raw_response['code'])
        _return._set_headers(raw_response['headers'])

        if (isinstance(raw_response['body'], Exception)): _return._set_exception(raw_response['body'])
        elif ("body_reader" in raw_response):
            content_type = raw_response['headers'].get("content_type")

            if (content_type is not None
                and content_type.split(";", 1)[0].lower() != "application/json"
               ): raise IOException("Response content is not of type JSON")

            _return._set_body_reader(raw_response['body_reader'])
        #

        return _return
    #
#
