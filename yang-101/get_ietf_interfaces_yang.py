#!/usr/bin/env python

import logging
from ncclient import manager
import sys
from ncclient.xml_ import *
from lxml import etree


rootLogger = logging.getLogger('ncclient.transport.session')
rootLogger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
rootLogger.addHandler(handler)


# the variables below assume the user is requesting
# access to a Nexus device running in VIRL in the
# DevNet Always On SandBox
# use the IP address or hostname of your Nexus device
HOST = '172.16.126.250'
# use the NETCONF port for your Nexus device
PORT = 2022
# use the user credentials for your Nexus device
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
        # print(m.dispatch('get-schema xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring"'))
        xsd_fetch = new_ele('get-xnm-information')
        sub_ele(xsd_fetch, 'type').text="xml-schema"
        sub_ele(xsd_fetch, 'namespace').text="junos-configuration"
        # dispatch(xsd_fetch)
        print xsd_fetch

if __name__ == '__main__':
    sys.exit(main())
