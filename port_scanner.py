import socket
import argparse
import sys

def main():
    # parser object
    parser = argparse.ArgumentParser(description="A simple network port scanner")

    # arguments
    parser.add_argument("host", type=str, help="The IP address or hostname to scan")
    parser.add_argument("-p", "--ports", type=str, default="1-1024", help="Port range to scan (e.g., 1-1024, 80, 22)")

    #parsing the argument from cmd line
    args = parser.parse_args()

    print(f"Target:{args.host}, Port: {args.ports}")


if __name__ == "__main__":
    main()