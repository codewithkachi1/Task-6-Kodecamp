class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password
        }

class Note:
    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "date": self.date
        }
