import time

first = "\nOn the "
second = " day of Christmas \nMy true love gave to me, "
day = [
    "first",
    "second",
    "third",
    "forth",
    "fith",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelth",
]
item = [
    "",
    "\nTwo turtle doves,",
    "\nThree French hens,",
    "\nFour calling birds,",
    "\nFive golden rings,",
    "\nSix geese a-laying,",
    "\nSeven swans a-swimming,",
    "\nEight maids a-milking,",
    "\nNine ladies dancing,",
    "\nTen lords a-leaping,",
    "\nEleven pipers piping,",
    "\nTwelve drummers drumming,",
]
third = ["\nA", "\nAnd a"]
ending = " partridge in a pear tree."
newItems = ""
for i in range(12):
    newItems = item[i] + newItems
    final = first + day[i] + second + newItems
    if i > 0:
        final = final + third[1] + ending
    else:
        final = final + third[0] + ending
    print(final)
    time.sleep(4)
