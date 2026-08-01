from .config import ElevenInstallerServiceConfig
from .log import ElevenInstallerServiceLogging

class ElevenInstallerService():
    log = ElevenInstallerServiceLogging()

    config = ElevenInstallerServiceConfig(log=log)

    def __init__(self, *kwargs):
        if self.config.check_config_exists():
            self.config.load_config()