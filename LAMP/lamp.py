#!/bin/python3

import os
import logging
from time import sleep

def install_packages():
    os.system("yum install -y --refresh dnf")
    os.system("dnf install -y httpd httpd-tools")
    os.system("dnf install -y mariadb-server mariadb")
    os.system("dnf install -y php php-fpm php-mysqlnd php-opcache php-gd php-xml php-mbstring")

def enable_services():
    os.system("systemctl start httpd")
    os.system("systemctl start mariadb")
    os.system("systemctl start php-fpm")

    os.system("systemctl enable httpd")
    os.system("systemctl enable mariadb")
    os.system("systemctl enable php-fpm")

def restart_services():
    os.system("systemctl restart httpd")
    os.system("systemctl restart mariadb")
    os.system("systemctl restart php-fpm")

def set_access():
    os.system("firewall-cmd --add-service=http")
    #os.system("firewall-cmd --add-service=https")
    os.system("firewall-cmd --reload")
    os.system("setenforce 0")

def set_files():
    print("Starting mysql secure installation in 5 seconds...")
    sleep(5)
    os.system("mysql_secure_installation")

def clean():
    os.system("systemctl stop httpd")
    os.system("systemctl stop mariadb")
    os.system("systemctl stop php-fpm")

    os.system("systemctl disable httpd")
    os.system("systemctl disable mariadb")
    os.system("systemctl disable php-fpm")

    os.system("dnf remove -y httpd httpd-tools mariadb-server mariadb php php-fpm php-mysqlnd php-opcache php-gd php-xml php-mbstring")


def main():
    install_packages()
    set_access()
    set_files()
    restart_services()

if __name__ == '__main__':
    main()
