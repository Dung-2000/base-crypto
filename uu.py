def myuuencode(plain):
    asc_plain = ''
    for i in range(len(plain)):
        temp = str((bin(ord(plain[i])).split('b')[1]))
        while len(temp) < 8:
            temp = '0' + temp
        asc_plain += temp

    padLen = 24 - (len(asc_plain) % 24)
    if padLen == 16:
        #asc_plain += '00000001' * (padLen // 8)
        asc_plain += '00000000' * (padLen // 8)
    elif padLen == 8:
        #asc_plain += '00000010' * (padLen // 8)
        asc_plain += '00000000' * (padLen // 8)
    elif padLen == 24:
        pass
    else :
        raise BaseException('Error')

    res_str = ''
    for i in range(0,len(asc_plain),6):
        temp = ''
        for j in range(0,6):
            temp += asc_plain[i+j]
        temp = chr(int(('0b' + temp), 2) + 32)
        res_str += temp

    out_str = ''
    res_str = res_str.replace(' ','`')
    for i in range(0,(len(res_str) // 60)):
        out_str += 'M' + res_str[(i*60):(i+1)*60] + '\n'
    out_str += chr((len(plain) % 45) + 32)
    a = len(res_str) % 60
    out_str += res_str[-a:] + '\n' + '`'
    return (out_str)
if __name__ == '__main__':
    # wiki(use zero padding) example: https://zh.wikipedia.org/wiki/Uuencode http://www.herongyang.com/Encoding/UUEncode-Algorithm.html
    #plain = 'Cat'
    plain = '''Each group of sixty output characters (corresponding to 45 input bytes) is output as a separate line preceded by an encoded character giving the number of encoded bytes on that line. For all lines except the last, this will be the character 'M' (ASCII code 77 = 32+45). If the input is not evenly divisible by 45, the last line will contain the remaining N output characters, preceded by the character whose code is 32 + the number of remaining input bytes. Finally, a line containing just a single space (or grave character) is output, followed by one line containing the string "end".'''
    print(myuuencode(plain=plain))