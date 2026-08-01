from .config import ElevenInstallerServiceConfig
from .log import ElevenInstallerServiceLogging
from .partitioner import ElevenInstallerServicePartitioner

class ElevenInstallerService():
    log = ElevenInstallerServiceLogging()
    
    config = ElevenInstallerServiceConfig(log=log)
    disks = ElevenInstallerServicePartitioner(log=log)

    def __init__(self, *kwargs):
        self.log.new_entry(1, "Starting installer service", 0)

        if self.config.check_config_exists():
            self.config.load_config()

        if self.config.exists and self.config.valid:
            self.log.new_entry(1, "Configuration exists and is valid. Starting installer", 0)

        self.disks.list_all_drives()