class String:

    def __init__(self):
        self.string = " "

    def get_string(self):
        self.string = str(input())

    def print_string(self):
        print(self.string)


string1 = String()
string1.get_string()
string1.print_string()


