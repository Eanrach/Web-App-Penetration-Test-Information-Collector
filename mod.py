import whois
import os
import nmap


def whoisDomain(domain):
    domain = domain
    whois_domain = whois.whois(domain)
    whois_domain_file_name = './whois_' + domain + '.json'
    return (whois_domain_file_name, whois_domain)

def nslookup(domain):
    result = str(os.popen('nslookup ' + domain).read())
    fileName = 'nslookup_' + domain +'.json'
    fileCotent = result
    return fileName, fileCotent

def scanner(host):
    nm = nmap.PortScanner()
    result = nm.scan(host, ports='1-65535', arguments="-sS")
    nmap_domain_file_name = './nmap_' + host + '.json'
    return(nmap_domain_file_name, result)

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

