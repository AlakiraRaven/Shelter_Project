import csv
import random
import shelter

ListOfShelters = \
    [
        shelter.Shelter('333 Main Street', 'Bella Goth'),
        shelter.Shelter('34 Pleasant View', 'Kassandra Goth'),
        shelter.Shelter('76 Growth Way', 'Lilith Pleasant'),
    ]


def print_shelters():
    for i in range(len(ListOfShelters)):
        print(
            f'{i}: Location: {ListOfShelters[i].building}, owner: {ListOfShelters[i].owner}')


def interface():
    x = 0

    while x != 'Q':

        x = input('''
        Hello! Welcome to the Little Monsters shelter database :D
        What do you want to do today?

        Write 1 if you want to admit an animal.
        Write 2 if you want to register an adoption
        Write 3 to hear a joke
        Write 4 to create a new shelter
        Write 5 to see a list of all shelters


        Write Q to quit
        ''')

        if x == '1':
            admit()
        elif x == '2':
            adopt()
        elif x == '3':
            joke()
        elif x == '4':
            create_shelter()
        elif x == '5':
            print_shelters()

    return 0


def create_shelter():

    building = input('Where is the new shelter?')
    owner = input('Who is the owner?')

    shell = shelter.Shelter(building, owner)
    ListOfShelters.append(shell)

    return shell


def admit():
    print('''
    Which shelter do you want to admit an animal to?

    Choose one from the list below:
    ''')
    print_shelters()
    s = int(input(''))

    shell = ListOfShelters[s]

    species = input('What is the species? ')
    name = input('What is the name? ')
    condition = input('What is the condition of the animal? ')
    chip = int(input('Provide the chip number: '))
    size = input('How big is the animal? ')
    race = input('What race is the animal (optional, to skip press enter)? ')
    status = input('What is the status of that animal?')

    shell.admission(species, name, condition, chip, size, status, race)

    print('\nHere is the new member of our small family:')
    shell.show(chip)


def adopt():
    pass


def joke():
    with open('Static\shortjokes.csv', mode='r') as infile:
        reader = csv.reader(infile, delimiter=',')
        jokes = {}
        for row in reader:
            jokes[row[0]] = row[1]
        jokes.pop('ID')
    a = 1
    b = 231657
    r = random.randint(a, b)

    print(jokes[str(r)])


if __name__ == "__main__":

    interface()
