import subprocess
import re
from prettytable import PrettyTable
import pyasn


def get_path(hostname):
    tracer = subprocess.Popen(['tracer', '-w', '30', hostname], stdout=subprocess.PIPE)
    re_ip = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    n = 0
    result = PrettyTable()
    result.field = ['№ по порядку', 'IP', 'AS']
    i = 0
    for line in iter(tracer.stdout.readline, ""):
        if i < 4:
            i += 1
            continue
        line = line.decode('windows-1251')
        if "*        *        *" in line:
            print(result)
            break
        else:
            ip = re.search(re_ip, line)[0]
            Asn = pyasn.pyasn('IpAsn.dat')
            lookup = Asn.lookup(ip)
            if lookup[0] is None:
                asn = ''
            else:
                asn = lookup[0]
            result.add_row(n, ip, asn)
            n += 1
