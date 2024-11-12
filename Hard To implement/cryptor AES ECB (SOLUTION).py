from pwn import *
from Crypto.Util.Padding import pad
import codecs
target = remote("chal.competitivecyber.club", 6001)

flagarr = []

for j in range(14):
    ts = b''.join([chr(c).encode() for c in flagarr])
    print(ts)
    for i in range(256):
        target.recvuntil("Send challenge >")
        pt = b'0'*(15 - len(flagarr)) + ts + chr(i).encode() + b'0'*(15 - len(flagarr))  

        target.sendline(pt)
        target.recvuntil("Response > ")
        ct = target.recvline()
        
        ct = ct.strip(b'\n')
        ct = ct.decode()
        ct = codecs.decode(ct, "hex")

        if len(ct[:16]) != len(ct[32:]):
            print(i, "---->", ct)
            print(ct[:32], ct[32:], ct[64:])
        if(ct[:16] == ct[16:32]):
            print(ct[:16], ct[16:32])
            print("this is it!")
            flagarr.append(i)
            break

ans = "".join([chr(c) for c in flagarr])
print(ans)
    # target.interactive()