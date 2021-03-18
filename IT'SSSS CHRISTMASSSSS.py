# MERRY CHRISTMAS! HAVE FUN WITH THE TWELVE DAYS OF CHRISTMAS!
daystuple = (
    ("1st", "A Partridge in a Pear Tree"),
    ("2nd", "Two Turtle Doves"),
    ("3rd", "Three French Hens"),
    ("4th", "Four Calling Birds"),
    ("5th", "Five Golden Rings"),
    ("6th", "Six Geese a Laying"),
    ("7th", "Seven Swans a Swimming"),
    ("8th", "Eight Maids a Milking"),
    ("9th", "Nine Ladies Dancing"),
    ("10th", "Ten Lords a Leaping"),
    ("11th", "Eleven Pipers Piping"),
    ("12th", "12 Drummers Drumming"),
)


def printdays():
    daynum = 1
    for _ in range(daynum, 12):
        for i in range(daynum - 1, -1, -1):
            if i == daynum - 1:
                print(
                    "On the {} day of christmas my true love gave to me:".format(
                        daystuple[i][0]
                    )
                )
            if i == 0 and daynum != 1:
                print("And ", end=" ")
            print(daystuple[i][1])
    daynum += 1


printdays()
