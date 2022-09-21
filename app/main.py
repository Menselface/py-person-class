class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_info = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_list = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            person_list.wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"] is not None:
            person_list.husband = Person.people[person["husband"]]

    return person_info
