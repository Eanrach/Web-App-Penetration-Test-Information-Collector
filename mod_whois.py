import whois
import os


def whoisDomain(domain):
    domain = domain
    whois_domain = whois.whois(domain)
    whois_domain_file_name = './whois_' + domain + '.json'
    return (whois_domain_file_name, whois_domain)

def writeFile(*args):
    #print(len(args))
    fileName = args[0][0]
    fileContent = args[0][1]
    # if not os.path.isfile(str(fileName)):
    #     return str(fileName)
    # else:
    #     return 'F'
    if not os.path.isfile(fileName):
        f = open(fileName, 'a+')
        f.write(str(fileContent))
        f.close()
        return (fileName + 'is already completed', fileContent)
    else:
        return (fileName + 'is already exist', fileContent)

# if __name__ == '__main__':
#     print(writeFile(whoisDomain('google.com')))

# import mod_whois
# import argparse
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-w', '--whois', dest='domain', help='WhoIs a Domain', type=str, default='baidu.com')
#     args = parser.parse_args()
#     print(mod_whois.whoisDomain(args.domain))