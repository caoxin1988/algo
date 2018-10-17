
class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class ListQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data) -> bool:
        node = ListNode(data)

        if self.tail is None and self.head is None:
            self.head = node
            self.tail = node
            return True

        self.tail.next = node
        self.tail = node

        return True

    def dequeue(self) -> int:
        if self.head is None:
            print('    -> queue is empyt, dequeue fail')
            return None

        node = self.head
        if node.next is None:
            self.head = self.tail = None
        else:
            self.head = node.next

        node.next = None

        return node.data

def main():
    queue = ListQueue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print('data : %s' % queue.dequeue())
    print('data : %s' % queue.dequeue())
    print('data : %s' % queue.dequeue())
    print('data : %s' % queue.dequeue())
    print('data : %s' % queue.dequeue())

    print('\n' + '*==' * 10 + '*\n')
    queue.enqueue(10)
    print('data : %s' % queue.dequeue())
    print('data : %s' % queue.dequeue())

if __name__ == '__main__':
    main()