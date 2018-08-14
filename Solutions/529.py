def t(n):
    results = 0
    #for i in range(1, 10**n):
    if checkStringFriendly(str(919)):
            results += 1
            #print(i)
    return results

def checkStringFriendly(myString):
    digits = [int(d) for d in str(myString)]
    boolFactor = False
    if len(digits) > 1:
         d =0
         while d < len(digits):
            soma = 0
            size = 1
            boolFactor = False
            while soma <= 10:
                if soma == 10:
                    boolFactor = True
                if d + size >= len(digits):
                    break
                soma = checkString(digits, size)
                size +=1
            d += 1
    return boolFactor

def checkString(mySequence, size):
    soma = 0
    for i in range(0,size):
         soma += mySequence[i]
    return soma

print(t(3))