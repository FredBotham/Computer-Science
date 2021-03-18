def d2b(num):
    global binarylist
    binarylist = []
    if num >= 1:
        d2b(num//2)
        binarylist.append(num % 2)
denin = int(input("Please enter denary value to convert: "))
d2b(denin)
convertlist = [str(i) for i in binarylist]
finalout = "0"*(8 - len(binarylist)) + "".join(convertlist)
print(finalout)