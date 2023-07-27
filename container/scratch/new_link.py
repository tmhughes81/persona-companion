from slink import SLink

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

    link.set_game(game)

    name = input("S. Link Name: ")
    if (name == ""):
        print("Name is required! Exiting...")
        exit(1)

    link.set_name(name)

    night = input("Is this a 'nighttime' link? [N]: ")

    if (night == "" or lower(night) == "n"):
        night = False
    elif (lower(night) == "y"):
        night = True
    else:
        print("Only valid options are 'Y' or 'N'.")
        exit(1)

    link.set_night(night)

    school = input("Is this a 'school' link? [N]: ")

    if (school == "" or lower(school) == "n"):
        school = False
    elif (lower(school) == "y"):
        school = True
    else:
        print("Only valid options are 'Y' or 'N'.")
        exit(1)

    link.set_school(night)

    avails = input("Set avails (e.g., MoTuWeThFrSaSu): ")

    if (avails == ""):
        print("At least one day must be set available!")
        exit(1)

    i = 0
    for i in range(i, len(avails)):
        print(avails[i:i+2])
        i += 2
