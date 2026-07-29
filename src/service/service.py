from .config import ElevenInstallerServiceConfig
from .log import ElevenInstallerServiceLogging

class ElevenInstallerService():
    log = ElevenInstallerServiceLogging()

    config = ElevenInstallerServiceConfig(log=log)