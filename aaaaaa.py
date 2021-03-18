sentence = str(input("Please enter sentence to have 'a's counted: "))
noas = 0
for char in sentence:
    if "a" in char:
       noas += 1
print("No. As in the sentence: {} ".format(noas))