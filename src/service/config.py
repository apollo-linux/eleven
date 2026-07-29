from pathlib import Path

class ElevenInstallerServiceConfig():
    config_path = Path("/usr/share/apollo/eleven/config.toml")

    # TODO: use real values and data here
    os_name = ""

    def __init__(self,*kwargs):
        self.os_name = "Apollo"

    def check_config_exists(self, *kwargs) -> bool:
        if self.config_path.exists():
            return True
        else:
            return False
