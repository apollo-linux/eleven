from .config import ElevenInstallerServiceConfig
from .log import ElevenInstallerServiceLogging
from .partitioner import ElevenInstallerServicePartitioner

class ElevenInstallerService():
    log = ElevenInstallerServiceLogging()

    config = ElevenInstallerServiceConfig(log=log)
    disks = ElevenInstallerServicePartitioner(log=log)

    def __init__(self, *kwargs):
        if self.config.check_config_exists():
            self.config.load_config()

        self.disks.list_all_drives()