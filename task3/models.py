class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password
        }

class JobApplication:
    def __init__(self, job_title, company, date_applied, status):
        self.job_title = job_title
        self.company = company
        self.date_applied = date_applied
        self.status = status

    def to_dict(self):
        return {
            "job_title": self.job_title,
            "company": self.company,
            "date_applied": self.date_applied,
            "status": self.status
        }
