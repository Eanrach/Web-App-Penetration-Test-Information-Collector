import os
from mod_whois import writeFile


def nslookup(domain):
    result = str(os.popen('nslookup ' + domain).read())
    fileName = 'nslookup_' + domain +'.json'
    fileCotent = result
    return fileName, fileCotent

if __name__ == '__main__':
    print(writeFile(nslookup('baidu.com')))