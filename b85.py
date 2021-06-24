def myb85encode(plain):
    padLen = (4 - (len(plain) % 4))
    if padLen == 4:
        pass
    else:
        plain += '\0' * padLen

    ct = ''
    for i in range(0,len(plain),4):
        trans_plain = ''
        for j in range(i,i + 4):
            temp = bin(ord(plain[j])).split('b')[1]
            while len(temp) < 8:
                temp = '0' + temp
            trans_plain += temp

        trans_plain = int(('0b' + trans_plain),2)

        res_plain = ''
        for j in range(4,0,-1):
            a = trans_plain // (85**j)
            trans_plain = trans_plain % (85**j)
            res_plain += chr(a + 33)
        res_plain += chr(trans_plain + 33)
        ct += res_plain
    res = '<~' + ct[:-padLen] + '~>'

    result = ''
    for i in range(0,len(res),75):
        temp = res[i:i+75] + '\n'
        result += temp
    result = result[:-1]
    return (result)

if __name__ == '__main__':
    plain = 'Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure.'
    print(myb85encode(plain=plain))
