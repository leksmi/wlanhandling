# Different features to manipulate with wifi_switch
# Support Cisco IOS, Huawei VRP

from baseconnector import DevConnector
from scrapli import Scrapli

platforms = {'cisco': 'cisco_iosxe',
             'huawei': 'huawei_vrp'
             }

class SwConnector(DevConnector):
    def __init__(self, mgmt_ip: str, mgmt_credentials: dict, platforms=platforms) -> None:
        super().__init__(mgmt_ip, mgmt_credentials)

    
