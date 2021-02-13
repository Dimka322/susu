from _collections import deque


# new_stack = deque()
# stack_length = int(input())
# sum = 0
# sum_n = int(input())
# for _ in range(stack_length):
#    new_stack.append(int(input()))
# print(new_stack)
# while new_stack:
#    if len(new_stack)<=2:
#        elem = new_stack.pop()
#        sum += elem
#    else:
#        new_stack.pop()
# print(sum)

# print(new_stack)


class MyStack:
    def __init__(self):
        self.stack, self.quantity_sequence = self.create_stack()
        self.summary = self.get_summary()

        self.new_stack = deque()
        self.new_stack.append(self.summary)

        print(self.new_stack)

    @staticmethod
    def create_stack():
        new_stack = deque()
        stack_size = int(input('размер'))

        for _ in range(stack_size):
            new_stack.append(int(input('жл')))

        quantity_sequence = int(input('n'))

        return new_stack, quantity_sequence

    def get_summary(self):
        summary = 0

        # while len(self.stack)!=0:
        while self.stack:
            # if len(self.stack) <= self.quantity_sequence:
            #    value = self.stack.pop()
            summary += self.stack.pop() if len(self.stack) <= self.quantity_sequence else self.stack.pop()

            return summary


if __name__ == '__main__':
    MyStack()
