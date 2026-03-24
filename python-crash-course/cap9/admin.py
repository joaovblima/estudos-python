import user


class Admin(user.User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


# admin = Admin("joao", "lima", ["can add post", "can delete post"])
# admin.privileges.show_privileges()
