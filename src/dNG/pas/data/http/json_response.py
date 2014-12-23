# -*- coding: utf-8 -*-
##j## BOF

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

from dNG.data.json_resource import JsonResource
from dNG.data.http.response import Response
from dNG.pas.data.binary import Binary
from dNG.pas.runtime.operation_not_supported_exception import OperationNotSupportedException
from dNG.pas.runtime.value_exception import ValueException

class JsonResponse(Response):
#
	"""
HTTP JSON response object handling decoding in the background.

:author:     direct Netware Group
:copyright:  (C) direct Netware Group - All rights reserved
:package:    pas
:subpackage: json_clients
:since:      v0.1.00
:license:    https://www.direct-netware.de/redirect?licenses;mpl2
             Mozilla Public License, v. 2.0
	"""

	def __init__(self):
	#
		"""
Constructor __init__(JsonResponse)

:since: v0.1.00
		"""

		Response.__init__(self)

		self.json_resource = None
		"""
JSON resource instance
		"""
	#

	def get(self, node_path = None):
	#
		"""
Read a specified node including all children if applicable.

:param node_path: Path to the node - delimiter is space; None for root

:return: (mixed) JSON data; None on error
:since:  v0.1.00
		"""

		if (self.json_resource is None): self.read()
		return (self.json_resource.get() if (node_path is None) else self.json_resource.get_node(node_path))
	#

	def read(self, size = -1):
	#
		"""
Reads data using the given body reader and parse the JSON response. Chunked
transfer-encoded data is handled automatically.

:param size: Bytes to read

:return: (bytes) Data received
:since:  v0.1.00
		"""

		if (size > 0): raise OperationNotSupportedException()

		if (self.json_resource is None):
		#
			_return = Binary.str(self.body_reader())
			self.body_reader = None

			self.json_resource = JsonResource(False)
			if (self.json_resource.json_to_data(_return) is None): raise ValueException("Data received is not a valid JSON encoded response")
		#
		else: _return = Binary.bytes("")

		return _return
	#
#

##j## EOF