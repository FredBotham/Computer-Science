from time import sleep

print(
    "PLEASE ENSURE 'topteams.txt' IS IN THE SAME FOLDER AS THIS FILE FOR PROGRAM TO FUNCTION."
)
sleep(2)
keywords = {1: "Team Name", 2: "Stadium", 3: "Team Captain", 4: "Nickname"}
teamlog = "TopTeamsSearch/topteams.txt"


def TeamSearch():
    with open(teamlog, mode="r", encoding="UTF-8") as f:
        found = False
        filter = int(
            input(
                "Please enter the variable you'd like to search for: \r\n 1: Team Name \r\n 2: Stadium \r\n 3: Team Captain \r\n 4: Nickname \r\n 5: Min. stadium capacity \r\n enter number: "
            )
        )
        if filter != 5:
            keyword = input(f"Enter search keyword for: {keywords.get(filter)} ")
            for line in f:
                data = line.split(",")
                if keyword in data[filter - 1]:
                    found = True
                    print(f"Team Found: ")
                    print(line)
        elif filter == 5:
            keyword = int(input("Please enter minimum capacity of stadium to show."))
            results = []
            for line in f:
                stadiumCapacity = line.split(",")[4]
                if stadiumCapacity >= keyword:
                    results.append(line)
                    found = True
            if found == True:
                print(
                    f'Stadiums found, sorted by capacity(ascending): {sorted(results, key=lambda line: float(line.split(",")[4]), reverse=True)}'
                )
        if found == False:
            print(f"No entry for '{keyword}' found. Try again.")


def run():
    repeat = "y"
    while repeat.lower() != "n":
        TeamSearch()
        repeat = input("Would you like to search again? (y/n): ")


run()
