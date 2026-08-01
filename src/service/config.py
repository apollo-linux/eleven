from pathlib import Path
import tomllib

from gettext import gettext as _

class ElevenInstallerServiceConfig():
    config_path = Path("/usr/share/apollo/eleven/config.toml")

    def __init__(self,*kwargs, log):
        self.log = log
        
        with open ("/usr/share/apollo/eleven/config.toml", "rb") as config:
            try: 
                data = tomllib.load(config)

                self.os_name = data["info"]["os_name"]
                self.experimental = data["info"]["experimental"]

            except KeyError as e:
                self.log.new_entry(3, _("Configuration has missing parameter: {parameter}").format(parameter=e), 12)

    def check_config_exists(self, *kwargs) -> bool:
        self.log.new_entry(1, "Checking that the configuration is present", 0)

        if self.config_path.exists():
            self.log.new_entry(1, "Configuration is present", 0)
            return True
        else:
            self.log.new_entry(3, "Configuration could not be found at /usr/share/apollo/eleven/config.toml}", 11)
            return False
