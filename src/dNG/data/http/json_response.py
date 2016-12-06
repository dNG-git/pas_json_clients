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

from dNG.data.binary import Binary
from dNG.data.json_resource import JsonResource
from dNG.runtime.operation_not_supported_exception import OperationNotSupportedException
from dNG.runtime.value_exception import ValueException

from .response import Response

class JsonResponse(Response):
    """
HTTP JSON response object handling decoding in the background.

:author:     direct Netware Group et al.
:copyright:  (C) direct Netware Group - All rights reserved
:package:    pas
:subpackage: json_clients
:since:      v0.2.00
:license:    https://www.direct-netware.de/redirect?licenses;mpl2
             Mozilla Public License, v. 2.0
    """

    # pylint: disable=invalid-name

    def __init__(self):
        """
Constructor __init__(JsonResponse)

:since: v0.2.00
        """

        Response.__init__(self)

        self.json_resource = None
        """
JSON resource instance
        """
    #

    def get(self, node_path = None):
        """
Read a specified node including all children if applicable.

:param node_path: Path to the node - delimiter is space; None for root

:return: (mixed) JSON data; None on error
:since:  v0.2.00
        """

        if (self.json_resource is None): self.read()
        return (self.json_resource.get() if (node_path is None) else self.json_resource.get_node(node_path))
    #

    def read(self, n = 0):
        """
Reads data using the given body reader and parse the JSON response. Chunked
transfer-encoded data is handled automatically.

:param n: Bytes to read

:return: (bytes) Data received
:since:  v0.2.00
        """

        # pylint: disable=access-member-before-definition, attribute-defined-outside-init, not-callable, used-before-assignment

        if (n > 0): raise OperationNotSupportedException()

        if (self.json_resource is None):
            _return = Binary.str(self.body_reader())
            self.body_reader = None

            self.json_resource = JsonResource(False)
            if (self.json_resource.json_to_data(_return) is None): raise ValueException("Data received is not a valid JSON encoded response")
        else: _return = Binary.bytes("")

        return _return
    #
#
