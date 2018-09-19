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

from msrest.serialization import Model


class AzureTimeSeriesData(Model):
    """AzureTimeSeriesData.

    All required parameters must be populated in order to send to Azure.

    :param dim_values: Gets or sets dimension values
    :type dim_values: list[str]
    :param min: Required. Gets or sets Min value
    :type min: float
    :param max: Required. Gets or sets Max value
    :type max: float
    :param sum: Required. Gets or sets Sum value
    :type sum: float
    :param count: Required. Gets or sets Count value
    :type count: int
    """

    _validation = {
        'min': {'required': True},
        'max': {'required': True},
        'sum': {'required': True},
        'count': {'required': True},
    }

    _attribute_map = {
        'dim_values': {'key': 'dimValues', 'type': '[str]'},
        'min': {'key': 'min', 'type': 'float'},
        'max': {'key': 'max', 'type': 'float'},
        'sum': {'key': 'sum', 'type': 'float'},
        'count': {'key': 'count', 'type': 'int'},
    }

    def __init__(self, *, min: float, max: float, sum: float, count: int, dim_values=None, **kwargs) -> None:
        super(AzureTimeSeriesData, self).__init__(**kwargs)
        self.dim_values = dim_values
        self.min = min
        self.max = max
        self.sum = sum
        self.count = count
