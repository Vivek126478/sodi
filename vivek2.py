class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()

    def menu(self):
        user_input = input("Welcome to Chatbook! How would you proceed?\n " \
        "1. Press to Signup\n" \
        " 2. Press to Login\n" \
        "3. Press 3 to write a post\n" \
        "4. Press 4 to message a friend\n" \
        "5. Press any other key to exit")
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass