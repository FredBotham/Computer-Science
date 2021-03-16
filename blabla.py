import os
import datetime
from time import sleep
keys = {1: 0, 2: 1, 3: 5, 4: 3}
terms = {1: "Country Name", 2: "Team Captain", 3: "Total Medals", 4: "Minimum Golds"}
#events dictionary with date and time assigned for each
events = {
    "Opening Ceremony": datetime.datetime(2020,7,24,20,00), 
"Men\'s 100m Final": datetime.datetime(2020,8,2,19), 
"Women\'s 4 x 400m Relay Final": datetime.datetime(2020,8,7,19,00), 
"Closing Ceremony": datetime.datetime(2020,8,9,20,00)
}
#random strings that are needed, easier if declared here.
current = os.getcwd()
accesslog = os.path.join(current, 'logs/accessLog.txt')
countrylog = os.path.join(current, 'logs/countryLog.txt')
h = f'{"-"*10}Tokyo 2020 Olympic Games{"-"*10}'
h2 = f'{"*"*6}File Handling{"*"*6} \n'
h3 = '--   Version 1.2   --'
#gets width of the window for centering the strings later
width = os.get_terminal_size().columns
#returns the full accesslog.txt file as string.
def readaccesslog():
    with open(accesslog,mode='r',encoding = 'utf-8') as f:
        return f.read()
#writes username and current time information to log file
def writeaccesslog(u):
    try:
        os.mkdir(os.path.join(current, "logs"))
    except FileExistsError:
        sleep(1)
        print("Log folder found, creation cancelled.")
    else:
        sleep(1)
        print("No log folder found, creating /logs...")
    with open(accesslog, mode="a", encoding="UTF-8") as f:
        f.write(f'Access at time: {datetime.datetime.now():%Y-%m-%d %H:%M:%S} by user: {u}\n')
#allows input for country data and sets default medals
def addcountrylog():
    #assigning variables
    countryName = input("Enter competing country name: ")
    teamCaptain = input("Enter Team Captain name: ")
    medals = {
        "gold":0,
        "silver":0,
        "bronze":0
    }
    totalMedals = sum(medals.values())
    varList = [countryName, teamCaptain, str(medals.get("gold")), str(medals.get("silver")), str(medals.get("bronze")), str(totalMedals) + "\n"]
    with open(countrylog, mode="a",encoding="UTF-8" ) as f:
        f.write("|".join(varList))
#prints log of all countries in countryLog.txt
def viewcountrylog():
    with open(countrylog, "r") as f:
        for line in f:
            print(line, end="")
#allows user to search for countries by different data types in countryLog.txt
def searchcountrylog():
    try:
        search = int(input(f"What would you like to search by: \n1: {'Country Name':}\n 2: {'Current Team Captain':}\n 3: {'Total Medals':}\n 4: {'Minimum gold medals ':}\n Enter no. selection: "))
        keyword = str(input(f"Your Selection: {terms.get(search)}, please enter the {terms.get(search)} to search for: "))
        Found = False
    except:
        print("You've entered something wrong, sorry.")
    with open(countrylog, mode="r", encoding="UTF-8") as f:
        for line in f:
            data = line.split("|")
            if data[keys[search]] in keyword and search != 4: 
                print(f"Selected country name: {data[0]}, current team captain: {data[1]} \n Medals: gold:{data[2]:>5}, silver: {data[3]:>5}, bronze: {data[4]:>5}\n total medals: {data[5]:>5}")
                Found = True
            elif search == 4:
                if int(data[keys[search]]) >= int(keyword):
                    print(f"Selected country name: {data[0]}, current team captain: {data[1]} \n Medals: gold:{data[2]:>5}, silver: {data[3]:>5}, bronze: {data[4]:>5}\n total medals: {data[5]:>5}")
            if Found == False:
                print(f'No countries matched your criteria: {search:>30}')
#user can edit stats for countries in countryLog.txt
def editcountrylog():
    print("Now printing countries currently available for edits: ")
    fcontents = []
    sleep(2)
    viewcountrylog()
    select = input("Please enter the name of the country you would like to edit: ")
    with open(countrylog, mode="r") as f:
        for line in f:
            data = line.split('|')
            if data[0] == select:
                print(f"Country selected: {data[0]}, Current Data:\n Team Captain: {data[1]} \n Medals: {data[2]} Gold{data[3]} Silver {data[4]} Bronze \n Total Medals: {data[5]}")
                editselect = "y"
                while editselect != "n":
                    editselect = int(input(f"Available fields to edit: \n1: {"Country Name":>20}\n2: {"Team Captain":>20}\n3: {"Gold Medals":>20}\n4: {"Silver Medals":>20}\n5: {"Bronze Medals":>20}"))- 1                    
            else:
                line.append(fcontents)
    with open()
intro subroutine
def intro():
    repeat = "y"
    print(h.center(width))
    sleep(1)
    print(h2.center(width))
    print(h3.center(width))
    sleep(1)
    #display name for log
    currentUname = input("Please enter a username to identify yourself in the log: ")
    #using function to write name and time to log file
    writeaccesslog(currentUname)
    print("Thank you, logged successfully.\n")
    sleep(2)
    repeat = input("Would you like to ADD, SEARCH, EDIT or VIEW a country(type as shown, n to skip)? ")
    sleep(1)
    while repeat != "n":
        print(f"Your selection: {repeat}.")
        sleep(1)
        eval(repeat.lower() + "countrylog" + "()")
        repeat = input("Would you like to ADD, SEARCH, EDIT or VIEW another country(type as shown, n to skip)? ")
    sleep(1)
    #printing table of events using the datetime()s from earlier to print the date and time seperately requiring only one variable in dictionary
    print(f'{"Event":<30} {"Date":<14} {"Time (JST)":>20}')
    for i in events.keys():
        print(f'{i:<30} {events.get(i).strftime("%Y-%m-%d"):<14} {events.get(i).strftime("%H:%M"):>20}')
    sleep(1)
    print("Now printing current log: ")
    sleep(1)
    #prints accesslog.txt
    print(f'\nCurrent log to date: \n {readaccesslog()}')

intro()
