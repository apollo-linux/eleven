from dataclasses import dataclass
import subprocess, json

@dataclass
class ElevenDiskPartitionerDrive():
    id: str
    size: str
    model: str

# Command itself might fail, make sure to follow handle exceptions from subprocess.run
def _get_lsblk_output(args: list[str]) -> list[dict[str,str]]:
    return json.loads(subprocess.run(args, capture_output=True).stdout)["blockdevices"]

class ElevenInstallerServicePartitioner():
    def __init__(self, *kwargs, log):
        self.log = log

    scan_ran: bool = False
    drives: list[ElevenDiskPartitionerDrive] = []

    # Do not overuse this function, we do not want to keep probing devices all the time due to things like old disk drives spinning up
    def scan_drives(self):
        scan_ran = True # Initial drive scanning tag, no more automated runs after that
        nvme_drives = _get_lsblk_output(["lsblk","-J","-p","-N","-o","NAME,SIZE,MODEL"])
        scsi_drives = _get_lsblk_output(["lsblk","-J","-p","-S","-o","NAME,SIZE,MODEL"])
        virtio_drives = _get_lsblk_output(["lsblk","-J","-p","-v","-o","NAME,SIZE,MODEL"])

        drives_raw = nvme_drives + scsi_drives + virtio_drives

        self.drives = list(map(lambda x: ElevenDiskPartitionerDrive(id=x['name'], size=x['size'], model=x['model']), drives_raw))

    # Will scan drives if no drives were found previously
    def get_drives(self) -> list[ElevenDiskPartitionerDrive]:
        if not self.scan_ran:
            self.scan_drives()
        return self.drives

    def list_all_drives(self, *kwargs):
        self.drives = []

        drives = dict()

        nvme_drives = subprocess.check_output("lsblk -J -p -N -b -o NAME,SIZE,MODEL", shell=True)

        if nvme_drives != "":
            nvme_drives = json.loads(
                nvme_drives
            )["blockdevices"]

        scsi_drives = subprocess.check_output("lsblk -J -p -S -b -o NAME,SIZE,MODEL", shell=True)

        if scsi_drives != "":
            scsi_drives = json.loads(
                scsi_drives
            )["blockdevices"]

        virtio_drives = subprocess.check_output("lsblk -J -p -v -b -o NAME,SIZE,MODEL", shell=True)

        if virtio_drives != "":
            virtio_drives = json.loads(
                virtio_drives
            )["blockdevices"]

        drives = nvme_drives + scsi_drives + virtio_drives

        for x in drives:
            self.drives.append(
                ElevenDiskPartitionerDrive(
                    id=x['name'],
                    size=x['size'],
                    model=x['model']
                )
            )
        
        for x in self.drives:
            self.log.new_entry(1, f"Found drive: {x.id} [{x.size}B, {x.model}]", 0)
