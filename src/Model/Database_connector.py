import mysql.connector
import json

class Database_conector:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="db",
            user="root",
            password="PASSWORD", # Password ommited for obvious reasons
            database="chore_chart"
        )
        self.cursor = self.db.cursor()

    # Create Location
    def add_location(self, location_info):
        pass

    # Edit Location
    def edit_location(self, location_info):
        pass

    # Delete Location
    def delete_location(self, location_info):
        pass

    # Create Chore
    def add_chore(self, chore_info):
        pass

    # Edit Chore
    def edit_chore(self, chore_info):
        pass

    # Delete Chore
    def delete_chore(self, chore_info):
        pass


    # Create Chore Assignment
    def add_chore_assignment(self, assignment_info):
        pass

    # Edit Chore Assignment
    def edit_chore_assignment(self, assignment_info):
        pass

    # Delete Chore Assignment
    def delete_chore_assignemnt(self, assignment_info):
        pass