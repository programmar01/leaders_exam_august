#Basic subclasses - Adam and Eve

class Human():
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        self.name = name
        
class Woman(Human):
    def __init__(self, name):
        self.name = name
        
def God():
    return [Man("adam"), Woman("eve")]