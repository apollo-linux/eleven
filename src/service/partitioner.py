from pathlib import Path

import subprocess, json

class ElevenInstallerServicePartitionerDrive():
    def __init__(self, *kwargs, id, size, model):
        self.id = id
        self.size = size
        self.model = model

class ElevenInstallerServicePartitioner():
    def __init__(self, *kwargs, log):
        self.log = log

    def list_all_drives(self, *kwargs):
        self.drives = []

        drives = dict()

        nvme_drives = subprocess.check_output("lsblk -J -N -b -o NAME,SIZE,MODEL", shell=True)

        if nvme_drives != "":
            nvme_drives = json.loads(
                nvme_drives
            )["blockdevices"]

        scsi_drives = subprocess.check_output("lsblk -J -S -b -o NAME,SIZE,MODEL", shell=True)

        if scsi_drives != "":
            scsi_drives = json.loads(
                scsi_drives
            )["blockdevices"]

        virtio_drives = subprocess.check_output("lsblk -J -v -b -o NAME,SIZE,MODEL", shell=True)

        if virtio_drives != "":
            virtio_drives = json.loads(
                virtio_drives
            )["blockdevices"]

        drives = nvme_drives + scsi_drives + virtio_drives

        for x in drives:
            self.drives.append(
                ElevenInstallerServicePartitionerDrive(
                    id=x['name'],
                    size=x['size'],
                    model=x['model']
                )
            )
        
        for x in self.drives:
            self.log.new_entry(1, f"Found drive: {x.id} [{x.size}B, {x.model}]", 0)