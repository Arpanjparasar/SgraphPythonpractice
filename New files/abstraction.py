from abc import  ABC,abstractmethod
class panda(ABC):
    @abstractmethod
    def move(self):
        print('Panda are slow, Very slow')

class human:
    def move(self):
        print('Humans are fast ')

obj=panda()
obj.move()
