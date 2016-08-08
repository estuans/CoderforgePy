from cPickle import pickle


class Storable(object):
    __register = []
    path = ""

    @property
    def file_path(self):
        pass

    def save(self):
        pass

    def load(self):
        pass
