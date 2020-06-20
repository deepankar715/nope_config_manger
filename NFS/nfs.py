#!/bin/python3


import os
import logging

nfs_dir = "/srv/NFS"
server_ip = "10.0.0.11"

def install_packages():
    os.system("yum install -y --refresh dnf")
    os.system("dnf install -y nfs-utils nfs-utils-lib")

def enable_services():
    os.system("systemctl start nfs-server")
    os.system("systemctl enable nfs-server")

def restart_services():
    os.system("systemctl restart nfs-server")

def set_access():
    os.system("firewall-cmd --add-service=nfs")
    os.system("firewall-cmd --reload")
    os.system("setenforce 0")

def set_dirs():
    os.system(f"mkdir -P {nfs_dir}")
    os.system(f"chmod -R 755 {nfs_dir}")
    os.system(f"chown nobody:nobody {nfs_dir}")

def set_files():
    exports = "/etc/exports"
    with open(exports, "w") as file:
        file.write(f"{nfs_dir}    {server_ip}(rw)")

def finalize():
    os.system("exportfs -rav")

def clean():
    exports = "/etc/exports"
    with open(exports, "w") as file:
        file.write()
    finalize()
    os.system("systemctl stop nfs-server")
    os.system("systemctl disable nfs-server")
    os.system("dnf remove -y nfs-utils nfs-utils-lib")

    


def main():
    install_packages()    
    set_access()
    set_dirs()
    set_files()
    finalize()
    restart_services()


if __name__ == '__main__':
    main()
