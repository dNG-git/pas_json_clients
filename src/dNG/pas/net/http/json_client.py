# -*- coding: utf-8 -*-
##j## BOF

"""
direct PAS
Python Application Services
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
http://www.direct-netware.de/redirect.py?pas;http;json_client

This Source Code Form is subject to the terms of the Mozilla Public License,
v. 2.0. If a copy of the MPL was not distributed with this file, You can
obtain one at http://mozilla.org/MPL/2.0/.
----------------------------------------------------------------------------
http://www.direct-netware.de/redirect.py?licenses;mpl2
----------------------------------------------------------------------------
#echo(pasHttpJsonClientsVersion)#
#echo(__FILEPATH__)#
"""

from dNG.net.http.client import Client
from dNG.pas.data.http.json_response import JsonResponse
from dNG.pas.runtime.io_exception import IOException

class JsonClient(Client):
#
	"""
"JsonClient" provides an HTTP client that expects "Content-Type" to be
"application/json".

:author:     direct Netware Group
:copyright:  (C) direct Netware Group - All rights reserved
:package:    pas.http
:subpackage: json_clients
:since:      v0.1.00
:license:    http://www.direct-netware.de/redirect.py?licenses;mpl2
             Mozilla Public License, v. 2.0
	"""

	def _get_connection(self):
	#
		"""
Returns a connection to the HTTP server.

:return: (mixed) Response data; Exception on error
:since:  v0.1.00
		"""

		_return = Client._get_connection(self)

		if (self.headers == None): self.headers = { }
		if ("ACCEPT" not in self.headers): self.set_header("Accept", "application/json")
		if ("CONTENT-TYPE" not in self.headers): self.set_header("Content-Type", "application/json")

		return _return
	#

	def _init_response(self, raw_response):
	#
		"""
Initializes an HTTP response object based on the received raw data.

:param raw_response: Raw response dict

:return: (object) Response object
:since:  v0.1.00
		"""

		_return = JsonResponse()
		_return._set_code(raw_response['code'])
		_return._set_headers(raw_response['headers'])

		if (isinstance(raw_response['body'], Exception)): _return._set_exception(raw_response['body'])
		elif ("body_reader" in raw_response):
		#
			content_type = raw_response['headers'].get("content_type")
			if (content_type != None and content_type.lower() != "application/json"): raise IOException("Response content is not of type JSON")
			_return._set_body_reader(raw_response['body_reader'])
		#

		return _return
	#
#

##j## EOF