#!/bin/python3

import argparse

def parse_argvs():
    '''Parse command line arguments, offer help messages and overall make the program more intuitive to use.'''

    help = """
    Configure different types of servers.
    For now, NFS, SMB, FTP (VSFTP), LAMP servers are supported.
    Very limited testing done.
    """

    parser = argparse.ArgumentParser(description=help)

    help = "Type of server to configure. (nfs, ftp, smb, lamp)"
    parser.add_argument("server", type=str, help=help, metavar="Server")

    return parser


def main():
    arg_parser = parse_argvs()
    args = arg_parser.parse_args()
    

    if args.server.lower() == "nfs":
        from NFS import nfs
        nfs.main()
    elif args.server.lower() == "smb":
        from SMB import smb
        smb.main()
    elif args.server.lower() == "ftp":
        from FTP import vsftp
        vsftp.main()
    elif args.server.lower() == "lamp":
        from LAMP import lamp
        lamp.main()
    else:
        arg_parser.print_usage()
        

if __name__ == "__main__":
    main()










