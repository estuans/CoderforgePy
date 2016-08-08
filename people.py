from store import Storable

class Person(object):

    first_name = ""
    last_name = ""
    age = 0

    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def print_name(self):
        print self.full_name

class AddressBook(Storable):

    def enumerate_all_entries():
        return enumerate(self.__register)
