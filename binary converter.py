import os
from time import sleep

width = os.get_terminal_size().columns
functionDict = {
    1: "bin2den",
    2: "den2bin",
    3: "den2hex",
    4: "hex2den",
    5: "filesize",
}  #
hexstr = "ABCDEF"
# invalid selection function
def invalid():
    print("Invalid selection. Try again.")
    sleep(1)
    menu(headstring)


# binary to denary function
def bin2den():
    print("Selection: Binary to Denary")
    binlist = []
    placevlist = []
    binin = str(input("Please enter binary value to convert: ")).replace(" ", "")
    denout = []
    placev = len(binin) - 1
    for char in binin:
        binlist.append(int(char))
        placevlist.append(placev)
        placev -= 1
    for i in range(0, len(placevlist), 1):
        denout.append(int((binlist[i] * (2 ** placevlist[i]))))
    print("Your binary number converted is: {}! ".format(sum(denout)))


# denary to binary function
def den2bin():
    print("Selection: Denary to Binary")
    # recursive function to convert to base 2
    def d2b(num):
        global binarylist
        binarylist = []
        if num >= 1:
            d2b(num // 2)
            binarylist.append(num % 2)

    denin = int(input("Please enter denary value to convert: "))
    d2b(denin)
    convertlist = [str(i) for i in binarylist]
    finalout = "0" * (8 - len(binarylist)) + "".join(convertlist)
    print("Your denary value in binary is: {}".format(finalout))


# denary to hex function
def den2hex():
    print("Selection: Denary to Hex")
    global hexlist
    hexlist = []
    # recursive function, similar to the binary converter, useful to convert different base number systems, although not as useful as just hex(number)
    def d2h(num):
        if num >= 1:
            d2h(num // 16)
            hexlist.append(num % 16)

    decin = int(
        input("Please enter the base 10 integer you would like to be converted: ")
    )
    d2h(decin)
    convertlist = [hexstr[x - 10] if x >= 10 else x for x in hexlist]
    finallist = [str(i) for i in convertlist]
    finalout = "".join(finallist)
    print("Your denary value in hex is: {}".format(finalout))


# hex to denary function, nice and easy
def hex2den():
    print("Selection: Hexadecimal to Denary")
    hex = str(input("Please enter the hex value you would like converted: "))
    print("Your converted value is: {}".format(int(hex, 16)))


# filesize calculator function
def filesize():
    print("Selection: Image File Size Calculator")
    bitdepth = int(input("Please enter bit depth of the image e.g. 1, 8, 16 bit: "))
    width = int(input("Please enter the width of the image(px): "))
    height = int(input("Please enter the height of the image(px): "))
    print("Thank You. Processing...")
    res = width * height
    bitrate = res * bitdepth
    btes = bitrate / 8
    kb = btes / 1000
    mb = btes / 1000000
    sleep(1)
    print(
        "COMPLETE! IMAGE STATS:\n Resolution: {} \n Bitrate: {} \n Size in Bytes: {}B \n Size in KiloBytes: {}KB\n Size in MegaBytes: {}MB".format(
            res, bitrate, btes, kb, mb
        )
    )


headstring = (
    "=" * 20 + "Binary, Hexadecimal, Image File Size Calculator".upper() + "=" * 20
)

# header and menu function
def menu(header):
    print(header.center(width))
    sleep(2)
    print("Getting available functions... ")
    sleep(1)
    print(
        "\nBinary To Denary Conversion {}1 \nDenary to Binary Conversion {}2 \nDenary to Hexadecimal Conversion {}3 \nHexadecimal to Denary Conversion {}4 \nImage file size calculator{}5".format(
            "." * 11, "." * 11, "." * 6, "." * 6, "." * 13
        )
    )
    function = int(input("Please select an option [1-5] "))
    if function >= 1 and function <= 5:
        eval(functionDict.get(function) + "()")
    else:
        invalid()


menu(headstring)
