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

    # resolve the hostname to an ip address
    try:
        target_ip = socket.gethostbyname(args.host)
    except socket.gaierror:
        print(f"Error: Hostname '{args.host}' could not be resolved.")
        sys.exit()

    # parse the port range
    ports_to_scan = []
    if '-' in args.ports:
        start_port, end_port = map(int, args.ports.split('-'))
        ports_to_scan = range(start_port, end_port + 1)
    else:
        ports_to_scan = [int(p.strip()) for p in args.ports.split(',')]
    print(f"Scanning {target_ip}...")


if __name__ == "__main__":
    main()