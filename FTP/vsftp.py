#!/bin/python3

import os
import logging

def install_packages():
    os.system("yum install -y --refresh dnf")
    os.system("dnf install -y vsftpd")

def enable_services():
    os.system("systemctl start vsftpd")
    os.system("systemctl enable vsftpd")

def restart_services():
    os.system("systemctl restart vsftpd")

def set_access():
    os.system("firewall-cmd --add-service=ftp")
    os.system("firewall-cmd --reload")
    os.system("setenforce 0")

def clean():
    os.system("systemctl stop vsftpd")
    os.system("systemctl disable vsftpd")
    os.system("dnf remove -y vsftpd")

def main():
    install_packages()    
    set_access()
    restart_services()

if __name__ == '__main__':
    main()
