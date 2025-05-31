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
        "5. Press any other key to exit\n")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.login()
        elif user_input == "3":
            self.write_post()
        elif user_input == "4":
            self.send_message()
        else:
            exit("Thank you for using Chatbook. Goodbye!")


    def signup(self):
        email = input("Enter your email: ")
        pwd = input("Enter your password: ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully!\n")
        self.menu()

    def login(self):
        if self.username ==  "" and self.password == "":
            print("You need to sign up first!")
        else:
            email = input("Enter your email: ")
            pwd = input("Enter your password: ")
            if email == self.username and pwd == self.password:
                print("You have logged in successfully!\n")
                self.logged_in = True
            else:
                print("Invalid credentials. Please try again.\n")
        self.menu()

    def write_post(self):
        if not self.logged_in:
            print("You need to log in first!")
            return
        elif self.logged_in:
            post_content = input("Write your post: ")
            print(f"Your post has been created: {post_content}\n")
        self.menu()

    def send_message(self):
        if not self.logged_in:
            print("You need to log in first!")
            return
        elif self.logged_in:
            friend = input("Enter the name of your friend: ")
            message = input("Enter your message: ")
            print(f"Your message to {friend} has been sent: {message}\n")
        self.menu()


obj = chatbook()
