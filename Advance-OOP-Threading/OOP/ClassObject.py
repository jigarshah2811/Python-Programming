"""
This is valid, self takes up the arg!
"""
# class Robot:
#     def introduce(self):
#         print("My name is {}".format(self.name))
#
# r1 = Robot()
# r1.name = "Krups"
# #r1.namee = "Krups"         # Error: Because now self.name wouldn't be defined!
# r1.introduce()
#
# r2 = Robot()
# r2.name = "Pasi"
# r2.introduce()

""" OOP
Class constructor
"""
class Robot:
    def __init__(self, name, color, weight):
        self.name, self.color, self.weight = name, color, weight

    def introduce(self):
        print("My name: {}, color: {}, weight: {}".format(self.name, self.color, self.weight))


r1 = Robot(name="Google", color="Pink", weight=10)
r2 = Robot(name="Alexa", color="Purple", weight=60)
r1.introduce()
r2.introduce()

class Person:
    def __init__(self, name, personality, isSitting=True):
        self.name, self.personality, self.isSitting = name, personality, isSitting

    def introduce(self):
        print("Person name: {}, personality: {}, isSitting: {}".format(self.name, self.personality, self.isSitting))


krups = Person(name="Krups", personality="Talkative", isSitting=False)
pasi = Person(name="pasi", personality="Singing", isSitting=True)

""" OOP: Relationship between objects
"""
krups.robot_owned = r1      # A class member can be defined "Run-Time"!. This will be self.robot_owned in "krups" object
pasi.robot_owned = r2
krups.robot_owned.introduce()
pasi.robot_owned.introduce()
