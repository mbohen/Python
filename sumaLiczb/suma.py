def findSum(str1, str2):
    if (len(str1) > len(str2)):
        t = str1
        str1 = str2
        str2 = t
    str = ""
    n1 = len(str1)
    n2 = len(str2)
    str1 = str1[::-1]
    str2 = str2[::-1]

    reszta = 0
    for i in range(n1):
        sum = ((ord(str1[i]) - 48) +
               ((ord(str2[i]) - 48) + reszta))
        str += chr(sum % 10 + 48)

        reszta = int(sum / 10)

    for i in range(n1, n2):
        sum = ((ord(str2[i]) - 48) + reszta)
        str += chr(sum % 10 + 48)
        reszta = (int)(sum / 10)

    if (reszta):
        str += chr(reszta + 48)

    str = str[::-1]

    return str

str1 = input("Podaj liczbe 1: ")
str2 = input("Podaj liczbe 2: ")
c= input("Podaj którą cyfrę sumy podać: ")

suma = findSum(str1, str2)
print(suma)
print(suma[int(c)-1])