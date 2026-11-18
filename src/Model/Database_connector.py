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
    