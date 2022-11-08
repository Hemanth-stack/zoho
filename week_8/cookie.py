class Jar():
    def __init__(self,capacity):
        self.value = 0
        print(capacity)
        self.capacity = capacity
        #if self.capacity <0:
            #raise ValueError

    def __str__(self,capacity,value):
        return value*'🍪'

    def deposit(self, n):
        if n<=self.capacity:
            self.value = n
        else:
            raise ValueError

    def withdraw(self, n):
        if n <= self.value:
            print('Nom nom nom')
        else:
            raise ValueError

    @property
    def capacity(self):
        return self.capacity
        pass

    @property
    def size(self):
        return self.value


if __name__ == '__main__':
    j = Jar(8)
    j.capacity()
    j.size()