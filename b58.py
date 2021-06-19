# example: https://oranwind.org/post-post-7/
def myb58encode(plain):
    table = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopgrstuvwxyz'
    assert len(table) == 58

    asc_result = 0
    for i in range(len(plain)):
        temp = ord(plain[i]) * (2**(8*(len(plain) - i - 1)))
        asc_result += temp

    out_str = ''
    while True:
        num1 = asc_result // 58
        num2 = asc_result % 58
        #print(num1,num2)
        out_str += table[num2]
        asc_result = num1
        if num1 == 0:
            break
    return (''.join(reversed(out_str)))

if __name__ == '__main__':
    plain = 'Hellow'
    print(myb58encode(plain=plain))