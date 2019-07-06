import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):

        if not 0 <= k < self.n:
            return IndexError("K is out of bonds")

        return self.A[k]


    def append(self, element):

        if self.n == self.capacity:
            self._resize(2*self.capacity)

        self.A[self.n] = element
        self.n += 1


    def _resize(self, new_capacity):
        B = self.make_array(new_capacity)

        for i in range(0, self.n):
            B[i] = self.A[i]

        self.A = B
        self.capacity = new_capacity


    def make_array(self, new_capacity):

        return(new_capacity * ctypes.py_object)()

arr = DynamicArray()
arr.append(1)
print(len(arr))