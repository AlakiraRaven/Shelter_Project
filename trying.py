import shelter
# from shelter import Shelter


def try_Shelter_init():
    monster = shelter.Shelter('333 Main Street', 'Bella Goth')
    print('Address of the shelter: ',
          monster.building, '\nOwner: ', monster.owner, '\n')
    return monster


def try_Shelter_admission(shelt):
    shelt.admission(species='Cat', name='Beetle',
                    condition='Good; hungry', chip=1234, size='Medium', status='Admitted')
    # shelt.admission('Cat', 'Beetle', 'Good; hungry', 1234, 'Medium')
    
    for chip in shelt.animal:
        for key in shelt.animal[chip]:
            # print(key, ': ' ,end='')
            # print(shelt.animal[chip][key]) # another way of printing it, but the one used is faster to write
            print(f'{key}: {shelt.animal[chip][key]}')


if __name__ == "__main__":
    s = try_Shelter_init()  # s means shelter here
    try_Shelter_admission(s)