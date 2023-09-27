class dog:
    " dog activities "
    def __init__(self, bark, eat, sleep, drink):
        print(" inside  constructor (its for my reference only)")
        self.bark= bark
        self.eat= eat
        self.sleep= sleep
        self.drink= drink


    def display_dog_activity(self):
        print(" inside a method")
        print(self.bark)
        print(self.eat)
        print(self.sleep)
        print(self.drink)



    def add_dog(self):
        print("inside class")

s=dog(" it should drink"," it should sleep"," it should bark"," it should eat")
s.add_dog()

#dog.display_dog_activity(self)

