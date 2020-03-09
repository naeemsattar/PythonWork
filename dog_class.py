class Dog():
    def __init__(self, bread, name, spots):
        self.bread = bread
        self.name = name
        self.spots = spots

# Methods
    def bark(self):
        print("Wooo! My name is {}, I am {} have spots:{}".format(self.name,self.bread,self.spots))


my_dog = Dog(bread="Lab",name="SAMMY",spots=False)
print(my_dog.name,my_dog.bread,my_dog.spots)
my_dog.bark()