#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=None, **kwargs):
        self._name = None
        self._breed = None
        if name is not None:
            self.name = name
        elif 'name' in kwargs:
            self.name = kwargs['name']
        if breed is not None:
            self.breed = breed
        elif 'breed' in kwargs:
            self.breed = kwargs['breed']

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 25:
            self._name = new_name
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, new_breed):
        if new_breed in APPROVED_BREEDS:
            self._breed = new_breed
        else:
            print("Breed must be in list of approved breeds.")
