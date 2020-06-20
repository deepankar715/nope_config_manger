# nope_config_manger
A non-persistent configuration manager

## Usage:
> ./main.py server_type

Run with root. 
Supported options are NFS, SMB, FTP and LAMP servers

Most of this code was written as a part of homework, so I've organized it into a single thing.
All of this is only tested on CentOS 8. Although it should work on simlar distros like CentOS 7 or Fedora or RHEL.

### Warning:
Although the title says non persistent, a lot of changes that happen in the OS stay the way they are after reboot. Things like shared/exported files and configuration files.
