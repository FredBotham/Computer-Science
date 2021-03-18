from time import sleep


def convert(bitdepth, w, h):
    global res, bitrate, btes, kb, mb
    res = w * h
    bitrate = res * bitdepth
    btes = bitrate / 8
    kb = btes / 1000
    mb = btes / 1000000


def gui():
    print("{} WELCOME TO IMAGE FILE SIZE CALCULATOR {}".format("*" * 30, "*" * 30))
    depth = int(input("Please enter bit depth of the image e.g. 1, 8, 16 bit: "))
    width = int(input("Please enter the width of the image(px): "))
    height = int(input("Please enter the height of the image(px): "))
    res = width * height
    print("Thank You. Processing...")
    sleep(1)
    convert(depth, width, height)
    print(
        "COMPLETE! IMAGE STATS:\n Resolution: {} \n Bitrate: {} \n Size in Bytes: {}B \n Size in KiloBytes: {}KB\n Size in MegaBytes: {}MB".format(
            res, bitrate, btes, kb, mb
        )
    )


again = "y"
while again.lower() != "n":
    gui()
    again = str(input("Convert Again?(y/n): "))
