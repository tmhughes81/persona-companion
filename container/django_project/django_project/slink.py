class SLink:
    def __init__(self):
        self.details = {}
        self.details['game'] = 'None'
        self.details['name'] = 'None'
        
        self.details['school'] = False
        self.details['night'] = False

        self.details['available_days'] = {
            'Monday': False,
            'Tuesday': False,
            'Wednesday': False,
            'Thursday': False,
            'Friday': False,
            'Saturday': False,
            'Sunday': False,
            'unk': False # Should never be used
        }
        
        # Initialize Link Conversations
        self.details['stages'] = {}
        
        for i in range(1,11):
            self.details['stages'][i] = "None"

    # Always use the full name of the day
    def format_day(self, day:str):
        days = {
            "Mon": "Monday",
            "M": "Monday",
            "Mo": "Monday",
            "Monday": "Monday",
            
            "Tues": "Tuesday",
            "Tu": "Tuesday",
            "Tue": "Tuesday",
            "Tuesday": "Tuesday",

            "Wed": "Wednesday",
            "W": "Wednesday",
            "We": "Wednesday",
            "Wednesday": "Wednesday",

            "Thur": "Thursday",
            "Thu": "Thursday",
            "Th": "Thursday",
            "Thursday": "Thursday",

            "Fri": "Friday",
            "F": "Friday",
            "Fr": "Friday",
            "Friday": "Friday",

            "Sat": "Saturday",
            "Sa": "Saturday",
            "Saturday": "Saturday",

            "Sun": "Sunday",
            "Su": "Sunday",
            "Sunday": "Sunday"
        }

        try:
            formatted_day = format_day[day]
        except:
            print("Unknown day submitted to format_day: {}".format(day))
            print("Returning 'unk'")
            formatted_day = 'unk'

        return formatted_day
            
    # Export the details of this link to a string in yaml format
    def export_yamls(self):
        return yaml.dump(self.details)

    # Import the details of this link from a yaml formatted string
    def import_yamls(self, yamls:str):
        self.details = yaml.safe_load(yamls)
        return self

    # Get the name of this link (e.g., Fool, Empress, etc)
    def get_name(self):
        return self.details['name']

    # Set the name of this link (e.g., Fool, Empress, etc)
    def set_name(self, name:str):
        self.details['name'] = name

    # Get the game this link belongs to, e.g., P3P-Male, P5R, etc)
    def get_game(self):
        return self.details['game']

    # Set the game this link belongs to, e.g., P3PM, P5R, etc)
    def set_game(self, game:str):
        self.details['game'] = game

    # Get the best answers for a given rank of this link (e.g., a/1/a/2, a/a/a, etc) 
    def get_ans_stage(self, rank:int):
        return self.details['stages'][rank]

    # Set the best answers for a given rank of this link (e.g., a/1/a/2, a/a/a, etc)
    def set_ans_stage(self, rank:int, ans:str):
        self.details['stages'][rank] = ans

    #get weekday availability
    def get_weekday_avail(self, day:str):
        return self.details['availabile_days'][format_day(day)]
    
    # Set weekday availability
    def set_weekday_avail(self, day:str, avail:bool):
        self.details['available_days'][format_day(day)] = avail

    # Get school status (e.g., is this link only available on school days)
    def get_school(self):
        return self.details['school']

    # Set school status
    def set_school(self, school:bool):
        self.details['school'] = school

    # Get night status
    def get_night(self):
        return self.details['night']

    # Set night details
    def set_night(self, night:bool):
        self.details['night'] = night

