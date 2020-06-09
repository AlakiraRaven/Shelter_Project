import datetime


class Shelter (object):
    def __init__(self, building, owner):
        self.building = building
        self.owner = owner

        self.animal = {}

    def admission(self, species, name, condition, chip, size, status, race='Mix'):
        '''
        TODO:
            - make sure no animals have the same chip number
        '''
        if race == '':
            race = 'Mix'

        self.animal[chip] = \
            {
            'Species': species,
            'Name': name,
            'Condition': condition,
            'Size': size,
            'Race': race,
            'Status': status,
            'Date': datetime.datetime.now()
        }

    def show_all(self):
        for chip in self.animal:
            for key in self.animal[chip]:

                print(f'{key}: {self.animal[chip][key]}')

    def show(self, chip):
        for key in self.animal[chip]:
            print(f'{key}: {self.animal[chip][key]}')
