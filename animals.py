
class LivingThing(object):
    respires = True
    mobile = False

    @property
    def is_alive(self):
        return False

    def is_mobile(self):
        return self.mobile


class Plant(LivingThing):
    pass

class Animal(LivingThing):
    mobile = True
    locale = "ground"
    movement_type = "walks"
    vocalisation = "*static*"

    def move(self):
        return "The {0} {1} along the {2}".format(self.__class__.__name__,self.movement_type, self.locale)

    def speak(self):
        return self.vocalisation

    def walk_and_talk(self):
        print self.move()
        print self.speak()

    def attack(self):
        return "maul"

class Snake(Animal):
    movement_type = "slithers"
    vocalisation = "Hissssssss"

class Dog(Animal):
    movement_type = "runs"
    vocalisation = "Woof"

class Bird(Animal):
    movement_type = "flies"
    locale = "sky"
    vocalisation = "tweet"

if __name__ == "__main__":
    Animal().move()

    Snake().walk_and_talk()
    Dog().walk_and_talk()
