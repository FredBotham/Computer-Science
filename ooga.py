passlength = 0
lowcase = 0
upcase = 0
number = 0
strengths = ['weak', 'stronger, but vulnerable', 'strong']
def strength(l,u,n):
    return strengths[(l+u+n)-1]
while passlength < 6:
    password = str(input("Please enter new password: "))
    passlength = len(password)
    for x in range(0, passlength- 1,1):
        if password[x] == password[x].lower():
            lowcase = 1
        if password[x] in password[x].upper():
            upcase = 1
        if password[x] in ["1","2","3","4","5","6","7","8","9"]:
            number = 1
    if passlength < 6 or passlength > 12:
        print("Invalid. Password doesn't match length requirement.")
    elif passlength >= 6 and passlength <= 12:
        print("Password meets length requirement: {} characters, strength is: {}".format(passlength, strength(lowcase, upcase, number)))