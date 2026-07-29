from pathlib import Path
import tomllib

class ElevenInstallerServiceConfig():
    config_path = Path("/usr/share/apollo/eleven/config.toml")

    def __init__(self,*kwargs, log):
        self.log = log
        
        with open ("/usr/share/apollo/eleven/config.toml", "rb") as config:
            data = tomllib.load(config)

            self.os_name = data["info"]["os_name"]
            self.experimental = data["info"]["experimental"]

    def check_config_exists(self, *kwargs) -> bool:
        self.log.new_entry(1, "Checking that the configuration is present")

        if self.config_path.exists():
            self.log.new_entry(1, "Configuration is present")
            return True
        else:
            self.log.new_entry(3, "Configuration could not be found at /usr/share/apollo/eleven/config.toml")
            return False
