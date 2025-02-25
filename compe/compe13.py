# Welcome Message: Develop a function called welcome_message that takes in a 
# parameter name and returns a greeting message: "Hello (name)! We hope that you will enjoy this course. :)".

class Greetings:
    
    def __init__(self, name):
        # Did this so you can know any self.VAR_NAME will do but self.name is better...
        self.name_testing = name
        
    def greet(self):
        print(f"Hello {self.name_testing}! We hope that you will enjoy this course. :)")
    
    
user = Greetings("nash")
# user.greet()



