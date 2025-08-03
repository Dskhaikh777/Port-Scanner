import socket
import argparse
import sys
from datetime import datetime


def scan_port(host, port):
    try:
        # create a new socket obj
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # timeout for the connection attempt
        socket.setdefaulttimeout(0.5)

        # attempt to connect
        result = s.connect_ex((host, port))
        if result == 0:
            return True
        s.close()
    except (socket.error, KeyboardInterrupt):
        print("\nExiting program.")
        sys.exit()
    return False



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
    
    
    print("-" * 50)
    print(f"Scanning target: {target_ip}")
    print(f"Time started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    try:
        for port in ports_to_scan:
            if scan_port(target_ip, port):
                try:
                    service = socket.getservbyport(port, 'tcp')
                    print(f"Port {port}: \033[92mOpen\033[0m   Service: {service}")
                except OSError:
                    # If the service is not found, just print that it's open
                    print(f"Port {port}: \033[92mOpen\033[0m")
    except KeyboardInterrupt:
        print("\nScan stopped by user.")
        sys.exit()
    
    print("-" * 50)
    print("Scan finished.")


if __name__ == "__main__":
    main()