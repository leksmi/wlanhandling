# Base class to connect to wifi devices


class DevConnector:
    """ 
    :param mgmt_ip: management device ip address
    :param mgmt_credentials: dict with username and password to login
    :returns: None
    :raises keyError: raises an exception
    """

    def __init__(self, mgmt_ip: str, mgmt_credentials: dict) -> None:
        self.mgmt_ip = mgmt_ip
        self.mgmt_credential = mgmt_credentials
