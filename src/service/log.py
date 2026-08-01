from enum import Enum
import datetime as dt

class ElevenInstallerServiceLogging:
    def __init__(self):
        self.types = Enum(
            'ElevenInstallerServiceLoggingType', [
                ('INFO', 1),
                ('WARNING', 2),
                ('ERROR', 3)
            ]
        )

    def new_entry(self, type, message, error_code):
        error_msg = ""
        
        if error_code != 0:
            error_msg = "error {error_code}"

        print(f"{self.types(type)}: {message} [{dt.datetime.now()}] {error_msg}")
