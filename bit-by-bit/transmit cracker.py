
content = ""
with open("out.txt") as f:
    content = f.read()

a_file = open("analyse.txt", "w")
a2_file = open("analyse2.txt", "w")
res_file = open("res.txt", "w")

content = content.strip('\n').strip('\n')


l32_blocks = [content[i:i+32] for i in range(0, len(content), 32)]


def decode(dec):
    start = 1
    decodedstring = ""
    while dec > 0:
        mask = (1 << 8*start) - 1
        charbyte = dec & mask
        decodedstring = chr(charbyte) + decodedstring
        dec = dec>>8
    return decodedstring


# k6 is
# 174 205 75 19 144 69
# key = "ae" + "cd" + "4b" + "13" + "90" + "45" + "23" + "ea" + "69" + "ba" + "fe" + "0e"


a3_file = open("analyse3.txt", "w")
for i in range(len(l32_blocks)-255):
    dec1 = int("0x" + l32_blocks[i][:8], 16)
    dec1 = decode(dec1)

    dec1 = dec1 + decode(int("0x" + l32_blocks[i][8:32], 16) ^ int("0xaecd4b13904523ea69bafe0e", 16))


    dec2 = int("0x" + l32_blocks[i+255][:8], 16)
    dec2 = decode(dec2)
    dec2 = dec2 + decode(int("0x" + l32_blocks[i+255][8:32], 16) ^ int("0xaecd4b13904523ea69bafe0e", 16))

    p3 = int("0x" + l32_blocks[i][8:], 16)^int("0x" + l32_blocks[i+255][8:], 16) 


    try:
        a2_file.write(dec1 + "|"  + dec2 + "   " + hex(p3)+ "\n" )
    except:
        print("Errors")


keyfound = 0xaecd4b13904523ea69bafe00

iv = 0
for i in range(len(l32_blocks)):
    iv = (iv + 1)%255
    curr_key = keyfound + iv
    

    dec1 = decode(int("0x" + l32_blocks[i], 16) ^ curr_key)


    try:
        res_file.write(dec1)

    except Exception as e:
        pass






