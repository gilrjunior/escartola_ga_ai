class Team:

    def __init__(self, athletes):
        self.athletes = athletes

    def add_athlete(self, athlete):
        self.athletes.append(athlete)

    def get_athletes(self):
        return self.athletes
    
    def get_athlete_by_position(self, position):
        return [athlete for athlete in self.athletes if athlete.position == position]
    
    def get_total_price(self):
        return sum([athlete.price for athlete in self.athletes])
    
    def get_total_score(self):
        return sum([athlete.score for athlete in self.athletes])
    
    def check_if_athlete_is_in_team(self, athlete):
        return athlete in self.athletes
    
    def __str__(self):
        for athlete in self.athletes:
            print(f"{athlete.__str__()}\n")