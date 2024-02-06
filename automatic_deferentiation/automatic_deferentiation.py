#### Automatic diferentiation need two implementation
# Variable
class Variable:
    def __init__(self, data):
        self.data = data

# initialize class
import numpy as np
data = np.array([[2.1, 2.8], [1.1, 2.2]])
x = Variable(data)
if __name__ == '__main__':
    print(x)
    print(x.data)
    print(x.data[0][0])

