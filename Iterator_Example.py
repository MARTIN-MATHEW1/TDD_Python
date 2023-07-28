
class square_function_with_iter:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            # print(self.n, '\n')
            self.n += 1
            return result
        else:
            raise StopIteration



# numbers = square_function_with_iter(-2)
# print(list(numbers))

