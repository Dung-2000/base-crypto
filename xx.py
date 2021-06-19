def myxxencode(plain):
    table = '+-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    assert len(table) == 64

    asc_plain = ''
    for i in range(len(plain)):
        temp = bin(ord(plain[i])).split('b')[1]
        while len(temp) < 8:
            temp = '0' + temp
        asc_plain += temp

    padLen = 24 - (len(asc_plain) % 24)
    if padLen == 24:
        pass
    elif padLen == 16 or padLen == 8:
        asc_plain += '0' * padLen
    else:
        raise BaseException('Error')

    res_str = ''
    for i in range(0,len(asc_plain), 6):
        temp = ''
        for j in range(6):
            temp += asc_plain[i+j]
        temp = int(('0b' + temp), 2)
        res_str += table[temp]

    out_str = ''
    for i in range(0,len(res_str)//60):
        out_str += 'h' + res_str[(i*60):((i+1)*60)] + '\n'
    out_str += table[len(plain) % 45] + res_str[-(len(res_str) % 60):]
    return (out_str)

if __name__ == '__main__':
    plain = 'Cat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat CatCat Cat'
    #plain = 'Cat Cat'
    #plain = 'http://www.wikipedia.org'
    # wiki example: https://en.wikipedia.org/wiki/Xxencoding http://cryptowikis.com/EncodeDecode/XXencode/
    print(myxxencode(plain=plain))