def myb64encode(plain):
    table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopgrstuvwxyz0123456789+/'
    assert len(table) == 64
    #transform str to asciicode
    asc_plain = ''
    for i in range(len(plain)):
        temp = bin(ord(plain[i])).split('b')[1]
        while len(temp) < 8:
            temp = '0' + temp
        asc_plain += temp

    padLen = 24 - (len(asc_plain) % 24)
    if padLen != 24:
        asc_plain = asc_plain + (padLen*'0')

    cipher = ''
    for i in range(0,len(asc_plain),6):
        temp = ''
        for j in range(0,6):
            temp += asc_plain[j+i]
        temp = int(('0b' + temp),2)
        cipher += table[temp]

    check = int(padLen / 8)
    if check == 3:
        return (cipher)
    elif check == 2 and cipher[-1] == cipher[len(cipher) - 2]:
        cipher = cipher[:-2] + '=='
        return (cipher)
    elif check == 1 and cipher[-1] == 'A':
        cipher = cipher[:-1] + '='
        return (cipher)
    else :
        raise BaseException("Error")

if __name__ == '__main__':
    plain = 'Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure.'
    # wiki example:https://zh.wikipedia.org/wiki/Base64
    print(myb64encode(plain=plain))