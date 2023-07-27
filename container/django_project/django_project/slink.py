class SLink:
    def __init__(self):
        self.details = {}
        self.details['game'] = 'None'
        self.details['name'] = 'None'
        
        self.details['school'] = False
        
        self.details['available_days'] = {
            'Monday': False,
            'Tuesday': False,
            'Wednesday': False,
            'Thursday': False,
            'Friday': False,
            'Saturday': False,
            'Sunday': False
        }
        
        # Initialize Link Conversations
        self.details['stages'] = {}
        
        for i in range(1,11):
            self.details['stages'][i] = "None"

    def export_yamls(self):
        return yaml.dump(self.details)

    def import_yamls(self, yamls:str):
        self.details = yaml.safe_load(yamls)
        return self
    
    def get_name(self):
        return self.details['name']
    
    def set_name(self, name):
        self.details['name'] = name
    
    def get_game(self):
        return self.details['game']
    
    def set_game(self, game):
        self.details['game'] = game
