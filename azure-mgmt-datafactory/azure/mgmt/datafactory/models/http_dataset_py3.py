# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .dataset_py3 import Dataset


class HttpDataset(Dataset):
    """A file in an HTTP web server.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param description: Dataset description.
    :type description: str
    :param structure: Columns that define the structure of the dataset. Type:
     array (or Expression with resultType array), itemType: DatasetDataElement.
    :type structure: object
    :param linked_service_name: Required. Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param parameters: Parameters for dataset.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     Dataset.
    :type annotations: list[object]
    :param folder: The folder that this Dataset is in. If not specified,
     Dataset will appear at the root level.
    :type folder: ~azure.mgmt.datafactory.models.DatasetFolder
    :param type: Required. Constant filled by server.
    :type type: str
    :param relative_url: The relative URL based on the URL in the
     HttpLinkedService refers to an HTTP file Type: string (or Expression with
     resultType string).
    :type relative_url: object
    :param request_method: The HTTP method for the HTTP request. Type: string
     (or Expression with resultType string).
    :type request_method: object
    :param request_body: The body for the HTTP request. Type: string (or
     Expression with resultType string).
    :type request_body: object
    :param additional_headers: The headers for the HTTP Request. e.g.
     request-header-name-1:request-header-value-1
     ...
     request-header-name-n:request-header-value-n Type: string (or Expression
     with resultType string).
    :type additional_headers: object
    :param format: The format of files.
    :type format: ~azure.mgmt.datafactory.models.DatasetStorageFormat
    :param compression: The data compression method used on files.
    :type compression: ~azure.mgmt.datafactory.models.DatasetCompression
    """

    _validation = {
        'linked_service_name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'description': {'key': 'description', 'type': 'str'},
        'structure': {'key': 'structure', 'type': 'object'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'folder': {'key': 'folder', 'type': 'DatasetFolder'},
        'type': {'key': 'type', 'type': 'str'},
        'relative_url': {'key': 'typeProperties.relativeUrl', 'type': 'object'},
        'request_method': {'key': 'typeProperties.requestMethod', 'type': 'object'},
        'request_body': {'key': 'typeProperties.requestBody', 'type': 'object'},
        'additional_headers': {'key': 'typeProperties.additionalHeaders', 'type': 'object'},
        'format': {'key': 'typeProperties.format', 'type': 'DatasetStorageFormat'},
        'compression': {'key': 'typeProperties.compression', 'type': 'DatasetCompression'},
    }

    def __init__(self, *, linked_service_name, additional_properties=None, description: str=None, structure=None, parameters=None, annotations=None, folder=None, relative_url=None, request_method=None, request_body=None, additional_headers=None, format=None, compression=None, **kwargs) -> None:
        super(HttpDataset, self).__init__(additional_properties=additional_properties, description=description, structure=structure, linked_service_name=linked_service_name, parameters=parameters, annotations=annotations, folder=folder, **kwargs)
        self.relative_url = relative_url
        self.request_method = request_method
        self.request_body = request_body
        self.additional_headers = additional_headers
        self.format = format
        self.compression = compression
        self.type = 'HttpFile'
