class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    for one_people in people:
        Person(one_people["name"], one_people["age"])

    for one_people in people:
        if one_people.get("wife"):
            Person.people[one_people["name"]].wife \
                = Person.people[one_people["wife"]]
        if one_people.get("husband"):
            Person.people[one_people["name"]].husband \
                = Person.people[one_people["husband"]]

    result = [Person.people[d["name"]] for d in people]

    return result
