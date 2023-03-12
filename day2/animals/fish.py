class Fish:
    def __init__(self) -> None:
        self.members = ['Fish1', 'Fish2', 'Fish3']

    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print('\t%s' % (member))