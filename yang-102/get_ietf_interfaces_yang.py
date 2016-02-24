#!/usr/bin/env python

import logging
from lxml import etree
from ncclient import manager
from ncclient.xml_ import *
import sys


# the variables below assume the user is requesting
# access to a CSR1000V device running in the DevNet
# Always On SandBox
# use the IP address or hostname of your CSR1000V device
HOST = '172.16.126.250'
# use the NETCONF port for your CSR1000V device
PORT = 2022
# use the user credentials for your CSR1000V device
USER = 'cisco'
PASS = 'cisco'


# create a main() method
def main():
    """Main method that prints netconf capabilities of remote device."""
    with manager.connect(host=HOST, port=PORT, username=USER, password=PASS,
                         hostkey_verify=False, device_params={'name': 'default'},
                         look_for_keys=False, allow_agent=False) as m:

        # print YANG module
        print('***Here is the YANG Module***')
        data = m.get_schema('ietf-interfaces')
        print(data.xml)


if __name__ == '__main__':
    sys.exit(main())
