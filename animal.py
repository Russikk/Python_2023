class Animal:
    def __repr__(self):
        return f'{self.__class__.__name}()'


class Human(Animal):
    pass


class Person(Human):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(name={self.name!r})'


class Pet(Animal):
    def __init__(self, owner):
        self.change_owner(owner)

    def change_owner(self, new_owner):
        self.owner = new_owner

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if isinstance(value, Person):
            self.__owner = value
        else:
            err = f'{value!r} must be an instance or subclass of Person.'
            raise ValueError(err)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f'{clsname}(owner={self.owner!r})'


class Enterprise:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def __repr__(self):
        return f'Enterprise(name={self.name!r}, pets={self.pets!r})'


class Vaccine:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'Vaccine(name={self.name!r}, description={self.description!r})'


class Chip:
    def __init__(self, chip_id):
        self.chip_id = chip_id

    def __repr__(self):
        return f'Chip(chip_id={self.chip_id!r})'


class DogIDChip(Chip):
    def __init__(self, chip_id, breed):
        super().__init__(chip_id)
        self.breed = breed

    def __repr__(self):
        return f'DogIDChip(chip_id={self.chip_id!r}, breed={self.breed!r})'


if __name__ == '__main__':
    person = Person(name="John")
    pet = Pet(owner=person)

    enterprise = Enterprise(name="Pet Enterprises")
    enterprise.add_pet(pet)

    vaccine = Vaccine(name="Rabies Vaccine", description="Protects against rabies")
    dog_chip = DogIDChip(chip_id="1234", breed="Labrador")

    print(person)
    print(pet)
    print(enterprise)
    print(vaccine)
    print(dog_chip)