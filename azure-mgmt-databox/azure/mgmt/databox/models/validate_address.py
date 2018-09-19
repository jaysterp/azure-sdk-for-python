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


class ValidateAddress(Model):
    """The requirements to validate customer address where the device needs to be
    shipped.

    All required parameters must be populated in order to send to Azure.

    :param shipping_address: Required. Shipping address of the customer.
    :type shipping_address: ~azure.mgmt.databox.models.ShippingAddress
    :param device_type: Required. Device type to be used for the job. Possible
     values include: 'DataBox', 'DataBoxDisk', 'DataBoxHeavy'
    :type device_type: str or ~azure.mgmt.databox.models.SkuName
    """

    _validation = {
        'shipping_address': {'required': True},
        'device_type': {'required': True},
    }

    _attribute_map = {
        'shipping_address': {'key': 'shippingAddress', 'type': 'ShippingAddress'},
        'device_type': {'key': 'deviceType', 'type': 'SkuName'},
    }

    def __init__(self, **kwargs):
        super(ValidateAddress, self).__init__(**kwargs)
        self.shipping_address = kwargs.get('shipping_address', None)
        self.device_type = kwargs.get('device_type', None)
