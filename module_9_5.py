class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        else:
            self.start = start
            self.stop = stop
            self.step = step
            self.i = 0

    def __iter__(self):
        self.pointer = self.start
        self.i = 0
        return self

    def __next__ (self):
        self.i += 1
        if self.i > 1:
            self.pointer += self.step
        if (self.step > 0 and self.pointer > self.stop)\
                or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration()
        return self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print('- iter2')
for i in iter3:
    print(i, end=' ')
print('- iter3')
for i in iter4:
    print(i, end=' ')
print('- iter 4')
for i in iter5:
    print(i, end=' ')
print('- iter 5')