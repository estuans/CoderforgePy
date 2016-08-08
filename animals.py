
class LivingThing(object):
    respires = True
    mobile = False
    species = ""

    @property
    def is_alive(self):
        return False

    def is_mobile(self):
        return self.mobile

    def __init__(self, *args, **kwargs):
        self.species = kwargs.get("species", None)
        print "========="
        print "LivingThing Init - Darwin was here :3"
        print vars()
        print "========="

class Plant(LivingThing):
    pass

class Animal(LivingThing):
    mobile = True
    locale = "ground"
    movement_type = "walks"
    vocalisation = "*static*"
    blood_type = "Warm"
    name = ""

    def __init__(self, *args, **kwargs):
        print "Hello Init -- %s" % self.__class__.__name__
        self.name = kwargs.get("name", None)
        if self.name:
            print "My name is %s" % self.name

        super(Animal, self).__init__(*args, **kwargs)

    def move(self):
        return "The {0} {1} along the {2}".format(self.__class__.__name__,self.movement_type, self.locale)

    def get_name(self):
        if self.name:
            return self.name
        else:
            return self.__class__.__name__

    def speak(self):
        return "{0} says {1}".format(self.get_name(), self.vocalisation)

    def walk_and_talk(self):
        print self.move()
        print self.speak()

    def attack(self):
        return "maul"

class Snake(Animal):
    movement_type = "slithers"
    vocalisation = "Hissssssss"
    blood_type = "Cold"

class Dog(Animal):
    movement_type = "runs"
    vocalisation = "Woof"

class Bird(Animal):
    movement_type = "flies"
    locale = "sky"
    vocalisation = "tweet"

def demo_animals():
    print "\n\n"
    Animal().walk_and_talk()
    print "\n\n************\n\n"
    Snake(species="Pythonidae Morelia Spilota Sp.").walk_and_talk()
    print "************\n\n"
    Dog(name="Steve").walk_and_talk()

if __name__ == "__main__":
    demo_animals()
