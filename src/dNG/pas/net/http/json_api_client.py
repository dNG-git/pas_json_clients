# -*- coding: utf-8 -*-
##j## BOF

"""
direct PAS
Python Application Services
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
http://www.direct-netware.de/redirect.py?pas;json_clients

This Source Code Form is subject to the terms of the Mozilla Public License,
v. 2.0. If a copy of the MPL was not distributed with this file, You can
obtain one at http://mozilla.org/MPL/2.0/.
----------------------------------------------------------------------------
http://www.direct-netware.de/redirect.py?licenses;mpl2
----------------------------------------------------------------------------
#echo(pasJsonClientsVersion)#
#echo(__FILEPATH__)#
"""

from dNG.data.json_resource import JsonResource
from .json_client import JsonClient

class JsonApiClient(JsonClient):
#
	"""
"JsonApiClient" is used to communicate with JSON aware endpoint URLs.

:author:     direct Netware Group
:copyright:  (C) direct Netware Group - All rights reserved
:package:    pas
:subpackage: json_clients
:since:      v0.1.00
:license:    http://www.direct-netware.de/redirect.py?licenses;mpl2
             Mozilla Public License, v. 2.0
	"""

	def request(self, method, separator = ";", params = None, data = None):
	#
		"""
Call a given request method on the connected HTTP server.

:param method: HTTP method
:param separator: Query parameter separator
:param params: Parsed query parameters as str
:param data: HTTP body

:return: (dict) Response data; 'body' may contain the catched exception
:since:  v0.1.01
		"""

		if (self.headers == None): self.headers = { }
		if ("CONTENT-TYPE" not in self.headers): self.set_header("Content-Type", "application/json; charset=utf-8")

		return JsonClient.request(self, method, separator, params, data)
	#

	def _json_encode(self, data):
	#
		"""
Encodes the given data dict as JSON.

:param data: Request data dict

:return: (str) JSON representation
:since:  v0.1.00
		"""

		return JsonResource().data_to_json(data)
	#

	def request_delete(self, params = None, separator = ";", data = None):
	#
		"""
Do a DELETE request on the connected HTTP server.

:param params: Query parameters as dict
:param separator: Query parameter separator
:param data: HTTP body

:return: (mixed) Response data; Exception on error
:since:  v0.1.00
		"""

		if (isinstance(data, dict)): data = self._json_encode(data)
		return JsonClient.request_delete(self, params, separator, data)
	#

	def request_patch(self, data = None, params = None, separator = ";"):
	#
		"""
Do a PATCH request on the connected HTTP server.

:param data: HTTP body
:param params: Query parameters as dict
:param separator: Query parameter separator

:return: (mixed) Response data; Exception on error
:since:  v0.1.00
		"""

		if (isinstance(data, dict)): data = self._json_encode(data)
		return JsonClient.request_patch(self, data, params, separator)
	#

	def request_post(self, data = None, params = None, separator = ";"):
	#
		"""
Do a POST request on the connected HTTP server.

:param data: HTTP body
:param params: Query parameters as dict
:param separator: Query parameter separator

:return: (mixed) Response data; Exception on error
:since:  v0.1.00
		"""

		if (isinstance(data, dict)): data = self._json_encode(data)
		return JsonClient.request_post(self, data, params, separator)
	#

	def request_put(self, data = None, params = None, separator = ";"):
	#
		"""
Do a PUT request on the connected HTTP server.

:param data: HTTP body
:param params: Query parameters as dict
:param separator: Query parameter separator

:return: (mixed) Response data; Exception on error
:since:  v0.1.00
		"""

		if (isinstance(data, dict)): data = self._json_encode(data)
		return JsonClient.request_put(self, data, params, separator)
	#

	def request_options(self, params = None, separator = ";", data = None):
	#
		"""
Do a OPTIONS request on the connected HTTP server.

:param params: Query parameters as dict
:param separator: Query parameter separator
:param data: HTTP body

:return: (mixed) Response data; Exception on error
:since:  v0.1.00
		"""

		if (isinstance(data, dict)): data = self._json_encode(data)
		return JsonClient.request_options(self, params, separator, data)
	#
#

##j## EOF