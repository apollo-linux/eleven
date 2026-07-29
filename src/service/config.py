from pathlib import Path

class ElevenInstallerServiceConfig():
    config_path = Path("/usr/share/apollo/eleven/config.toml")

    # TODO: use real values and data here
    os_name = ""

    def __init__(self,*kwargs, log):
        self.os_name = "Apollo"
        self.log = log

    def check_config_exists(self, *kwargs) -> bool:
        self.log.new_entry(1, "Checking that the configuration is present")

        if self.config_path.exists():
            self.log.new_entry(1, "Configuration is present")
            return True
        else:
            self.log.new_entry(3, "Configuration could not be found at /usr/share/apollo/eleven/config.toml")
            return False
