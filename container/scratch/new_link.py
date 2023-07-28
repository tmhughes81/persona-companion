from slink import SLink

def valid_day(day:str):
    days = set(["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"])

    if day in days:
        return True

    return False

if __name__ == "__main__":
    link = SLink()
    
    print("Set Game...")
    print(" 1. Persona 3 Portable Female (P3PF)")
    print(" 2. Persona 3 Portable Male (P3PM)")
    print(" 3. Persona 3 FES (P3F)")
    print(" 4. Persona 4 (P4)")
    print(" 5. Persona 4 Golden (P4G)")
    print(" 6. Persona 5 (P5)")
    print(" 7. Persona 5 Royal (P5R)")
    print("")
    game = input("Your choice? [1]: ")
    
    if (game == ""):
        game = "1"

    try:
        game = int(game)
        assert game > 0
        assert game < 8
    except:
        print("Valid entries are from 1 to 7.")

    games = {
        1: "P3PF",
        2: "P3PM",
        3: "P3F",
        4: "P4",
        5: "P4G",
        6: "P5",
        7: "P5R"
    }

    link.set_game(games[game])

    name = input("S. Link Name: ")
    if (name == ""):
        print("Name is required! Exiting...")
        exit(1)

    link.set_name(name)

    night = input("Is this a 'nighttime' link? [N]: ")

    if (night == "" or night.lower() == "n"):
        night = False
    elif (night.lower() == "y"):
        night = True
    else:
        print("Only valid options are 'Y' or 'N'.")
        exit(1)

    link.set_night(night)

    school = input("Is this a 'school' link? [N]: ")

    if (school == "" or school.lower() == "n"):
        school = False
    elif (school.lower() == "y"):
        school = True
    else:
        print("Only valid options are 'Y' or 'N'.")
        exit(1)

    link.set_school(night)

    avails = input("Set avails (e.g., MoTuWeThFrSaSu): ")

    if (avails == ""):
        print("At least one day must be set available!")
        exit(1)

    for i in range(0, len(avails), 2):
        day = avails[i:i+2]
        if (not valid_day(day)):
            print("String contains invalid day!")
            exit(1)

        link.set_weekday_avail(day, True)

    for i in range(1,11):
        link.set_ans_stage(i, input("Correct answers for stage {}: ".format(i)))
    
    with open("{}.yaml".format(link.get_name()), "w") as f:
        f.write(link.export_yamls())

