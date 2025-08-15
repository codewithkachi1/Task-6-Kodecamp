class Student:
    def __init__(self, username, password, grades):
        self.username = username
        self.password = password
        self.grades = grades

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "grades": self.grades
        }
