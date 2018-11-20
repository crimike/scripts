import commands
import sys

output = commands.getstatusoutput("snmpwalk -v2c -c " + sys.argv[2] + " " + sys.argv[1] + " 1.3.6.1.2.1.4.34.1.3")
lines = output[1].split('\n')
for line in lines:
    numbers = line.split(' ')[0].split('.')
    ip_numbers = numbers[12:]
    if len(ip_numbers) != 16:
        continue
    ipv6 = ""
    for i in range(0, 16, 2):
        a = hex(int(ip_numbers[i])).split('x')[1]
        b = hex(int(ip_numbers[i+1])).split('x')[1]
        ipv6+= a
        ipv6+= b
        ipv6+= ':'

    print ipv6[:-1]

