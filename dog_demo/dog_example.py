#!/usr/bin/env python3
# coding: utf8

class Dog:
    """Base class for all dogs. Dogs have the properties 'name' and 'max_speed' and can 'say_name()'. """

    def __init__(self, name, max_speed):
        """Init, the constructor creates an instance of a dog. It requires the argument name and max_speed."""
        self._name = name
        self._max_speed = max_speed

    def say_name(self):
        """Lets the dog say its name."""
        print(f"My name is '{self._name}'")

    def get_name(self):
        """Returns the name of the dog."""
        return self._name
    
    def get_max_speed(self):
        """returns the max. speed this dog can reach."""
        return self._max_speed
    

class ShepherdDog(Dog):
    """A ShepherdDog is a specialization of a dog. It can do the same as each dog can, plus 'collect_herd()'"""

    def __init__(self, name, max_speed):
        """The constructor creates an instance of a shepherd dog."""
        super().__init__(name, max_speed)

    def collect_herd(self):
        """'collect_herd()' is abstract: It is defined, but does not really do something."""
        pass
    

class BorderCollie(ShepherdDog):
    """Border Collies are a special type of shepherd dogs."""

    def __init__(self, name, max_speed):
        """Creates/initializes/constructs a border collie."""
        super().__init__(name, max_speed)

    def collect_herd(self):
        """BorderCollie.collect_herd() does a little bit more...."""
        print(f"{self._name} is collecting the herd")


if __name__ == '__main__':
    # instantiate to dogs
    bello = Dog("Bello", 15)
    sira = BorderCollie("Sira", 25)

    all_dogs = [bello, sira]

    # print the name and the type of each dog
    for dog in all_dogs:
        print(f"'{dog.get_name()}' is {type(dog)}")

    # let all dogs say its name
    for dog in all_dogs:
        dog.say_name()

    # try to let all dogs collect their herd
    for dog in all_dogs:
        try:
            dog.collect_herd()
        except AttributeError:
            print(f"ERROR: Dog '{dog.get_name()}' can't collect a herd")
   