#!/bin/python3

import os
import logging
import configparser

def install_packages():
    os.system("yum install -y --refresh dnf")
    os.system("dnf install -y samba samba-client samba-common")

def enable_services():
    os.system("systemctl enable smb")
    os.system("systemctl enable nmb")

    os.system("systemctl start smb")
    os.system("systemctl start nmb")

def restart_services():
    os.system("systemctl restart smb")
    os.system("systemctl restart nmb")

def set_access():
    os.system("firewall-cmd --add-service=samba")
    os.system("firewall-cmd --reload")
    os.system("setenforce 0")

def set_dirs():
    os.system("mkdir -p /srv/samba/anonymous")
    os.system("chmod -R 0777 /srv/samba/anonymous")
    os.system("chown -R nobody:nobody /srv/samba/anonymous")
    os.system("chcon -t samba_share_t /srv/samba/anonymous")

    os.system("groupadd smbgrp")
    os.system("usermod deep -aG smbgrp")
    os.system("smbpasswd -a deep")
    os.system("mkdir -p /srv/samba/secure")
    os.system("chmod -R 0770 /srv/samba/secure")
    os.system("chown -R root:smbgrp /srv/samba/secure")
    os.system("chcon -t samba_share_t /srv/samba/secure")
    os.system("setenforce 1")

def set_files():
    if not os.path.isfile('/etc/samba/smb.conf.orig'):
        os.system("cp /etc/samba/smb.conf /etc/samba/smb.conf.orig")
    os.system("cp /etc/samba/smb.conf /etc/samba/smb.conf.bak")
    os.system("cp /etc/samba/smb.conf.bak /etc/samba/smb.conf")

    smb_config_file = "/etc/samba/smb.conf"
    smb_config = configparser.ConfigParser()
    smb_config.read(smb_config_file)

    smb_config['Anonymous'] = {
        'comment': 'Anonymous File Server Share',
        'path': '/srv/samba/anonymous',
        'browsable': 'yes',
        'writable': 'yes',
        'guest ok': 'yes',
        'read only': 'no',
        'force user': 'nobody'
    }
    smb_config['Secure'] = {
        'comment': 'Secure File Server Share',
        'path':  '/srv/samba/secure',
        'valid users': '@smbgrp',
        'guest ok': 'no',
        'writable': 'yes',
        'browsable': 'yes'
    }

    with open(smb_config_file, "a") as file:
        smb_config.write(file)

def clean():
    os.system("cp /etc/samba/smb.conf.orig /etc/samba/smb.conf")
    os.system("systemctl stop smb")
    os.system("systemctl stop nmb")
    os.system("systemctl disable smb")
    os.system("systemctl disable nmb")
    os.system("dnf remove -y samba samba-client samba-common")


    
def main():
    install_packages()
    set_access()
    set_dirs()
    set_files()
    restart_services()

if __name__ == '__main__':
    main()
