import json

class Chore:
    def __init__(self, name, description, time_interval):
        self.name = name
        self.description = description
        self.time_interval = time_interval

    # Getters 
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_time_interval(self):
        return self.time_interval

    # This assumes that it has been set already
    # Chore ID is assigned by the database, so after the entry is made, this gets set
    def get_chore_id(self):
        return self.chore_id

    # Setters
    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def set_time_interval(self, time_interval):
        self.time_interval = time_interval

    # This needs to be called after a db entry is made
    def set_chore_id(self, chore_id):
        self.chore_id = chore_id

    # serialize to json - Everything but the chore ID since it is unknown
    # This function is intended to be used for the entry creation
    def as_json_no_id(self):
        return {
            'name' : self.name,
            'description' : self.description,
            'time_interval' : self.time_interval
        }

    # this is everything including the id for the other operations
    def as_json(self):
        return {
            'name' : self.name,
            'description' : self.description,
            'time_interval' : self.time_interval,
            'chore_id' : self.chore_id
        }
    
