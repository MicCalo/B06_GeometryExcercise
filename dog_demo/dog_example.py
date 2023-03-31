#!/usr/bin/env python3
# coding: utf8

class Dog:
    """Base class for all dogs. Dogs have the properties 'name' and 'max_speed' and can 'do_bark()'. """

    def __init__(self, name, max_speed):
        """Init, the constructor creates an instance of a dog. It requires the argument name and max_speed."""
        self._name = name
        self._max_speed = max_speed

    def do_bark(self):
        """Lets the dog bark."""
        print("Wuff")

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
        print("Collecting herd")
   