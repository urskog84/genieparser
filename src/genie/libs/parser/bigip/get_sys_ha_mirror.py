# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/ha-mirror' resources
# =============================================


class SysHamirrorSchema(MetaParser):

    schema = {}


class SysHamirror(SysHamirrorSchema):
    """ To F5 resource for /mgmt/tm/sys/ha-mirror
    """

    cli_command = "/mgmt/tm/sys/ha-mirror"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
