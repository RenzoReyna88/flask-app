from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, Username) -> None:
        super().__init__()
        self.id= id
        self.Username= Username