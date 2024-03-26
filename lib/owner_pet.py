class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self._pets.append(pet)
            pet.set_owner(self)
        else:
            raise Exception("Invalid pet type")

    def get_sorted_pets(self):
        sorted_pets = sorted(self._pets, key=lambda x: x.name)
        return sorted_pets


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type
        self.owner = owner
        self.all_pets.append(self)

    def set_owner(self, owner):
        if isinstance(owner, Owner):
            self.owner = owner
        else:
            raise Exception("Invalid owner type")