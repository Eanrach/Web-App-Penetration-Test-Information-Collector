import argparse
import mod

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--whois', dest='domain', help='WhoIs a Domain', type=str)
    parser.add_argument('-n', '--nmap', dest='host', help='Nmap a Domain', type=str)
    args = parser.parse_args()
    if args.domain:
        print(mod.whoisDomain(args.domain))
    else:
        print('you misst argument \'-w\', plese enter a domain')
    if args.host:
        print(mod.scanner(args.host))