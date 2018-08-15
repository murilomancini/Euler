def t(n):
    results = 0
    for i in range(1, 10**n):
        if checkStringFriendly(str(i)):
            results += 1
            print(i)
    return results

def checkStringFriendly(myString):
    digits = [int(d) for d in str(myString)]
    boolFactor = False
    if len(digits) > 1:
         d =0
         while d < len(digits)-1:
            soma = 0
            size = 2
            boolFactor = False
            while soma < 10:
                soma = checkString(digits, size, d)
                if soma == 10:
                    boolFactor = True
                    break
                if d + size >= len(digits):
                    break
                size += 1
            d += size - 1
            if soma > 10:
                break
    return boolFactor

def checkString(mySequence, size, initial):
    soma = 0
    for i in range(0,size):
         soma += mySequence[i+initial]
    return soma

print(t(3))
