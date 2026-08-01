# Configuring Eleven
Eleven gets its configuration from a toml file stored in the system root at `/usr/share/apollo/eleven/config.toml`. This file contains important information on how installations should be performed by Eleven. If the file is missing, or some required values are missing, Eleven will quit with an error to prevent broken installs.

## Configuration values
*\* indicates a setting is required, and Eleven will **quit** without a value*

### `info`
- `os_name`* - used as the display name for the OS
- `experimental` - Eleven will show a message if this is true

### `disks`
- `filesystem`* - what filesystem to use, this should be one compatible with bootc and the target image
- `efi_size`* - how big the efi system partition should be, we recommend 2GB

### `bootc`
- `target_image`* - which container image should be deployed to the drive
- `source`* - whether to install a local container image (`container-storage`), or from an online container (`registry`)
- `use_composefs` - whether to use bootc's [experimental composefs backend](https://bootc.dev/bootc/experimental-composefs.html), this may be needed for non-Fedora based distros