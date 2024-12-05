"""
The admins module uses the users module to generate
an admin user.
"""
from users import Users

class Privileges:
    def __init__(self):
        self.privileges = ["Add post", "Delete post", "Ban user"]
    
    
    def show_privileges(self):
        print(self.privileges)
    
    def add_privileges(self):
        if "Delete post" in self.privileges:
            # If user can delete, he should be able to read
            self.privileges.append("Read post")

class Admin(Users):
    def __init__(self, first_name, last_name, home_dir, phone_number, manager):
        super().__init__(first_name, last_name, home_dir, phone_number, manager)
        self.privileges = Privileges()
        self.manager = "Self"