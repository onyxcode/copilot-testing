# check if a given website is up or down
def main():
    import requests
    import sys
    import time
    import argparse
    import socket
    import re
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    parser = argparse.ArgumentParser(description='Check if a website is up or down')
    parser.add_argument('-w', '--website', help='Website to check', required=True)
    parser.add_argument('-t', '--timeout', help='Timeout in seconds', required=False)
    parser.add_argument('-p', '--port', help='Port to check', required=False)
    args = parser.parse_args()

    if args.timeout:
        timeout = int(args.timeout)
    else:
        timeout = 5

    if args.port:
        port = int(args.port)
    else:
        port = 80

    try:
        response = requests.get(args.website, timeout=timeout, verify=False)
    except requests.exceptions.ConnectionError:
        print('Connection error')
        sys.exit(1)
    except requests.exceptions.ReadTimeout:
        print('Read timeout')
        sys.exit(1)
    except requests.exceptions.TooManyRedirects:
        print('Too many redirects')
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

    if response.status_code == 200:
        print('Website is up')
        sys.exit(0)
    elif response.status_code == 404:
        print('Website is down')
        sys.exit(1)
    else:
        print('Website is down')
        sys.exit(1)
# run the main function
if __name__ == '__main__':
    main()