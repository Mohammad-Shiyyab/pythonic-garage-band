
from abc import ABC
from typing import ClassVar


class Musician(ABC):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    
    def __repr__(self) :
        pass

    
    def get_instrument(self) :
        pass

    
    def play_solo(self) :
        pass


class Guitarist(Musician):

    def __init__(self, name):
        super().__init__(name)

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):

    def __init__(self, name):
        super().__init__(name)

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):

    def __init__(self, name):
        super().__init__(name)

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"
    
class Band:

    instances = []

    def __init__(self, name, members = []):
        self.name = name
        self.members = members

        Band.instances.append(self)

    def play_solos(self):
        new_list = []

        for member in self.members:
            new_list.append(member.play_solo())
        return new_list
        

    def __str__(self):
        return f"Band {self.name} has {len(self.members)} members"

    def __repr__(self):
        return f"Band('{self.name}', {self.members})"

    @classmethod
    def to_list(cls):
        return cls.instances    

