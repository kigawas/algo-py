from algo.data_structures.bag import PriorityQueue
from algo.data_structures.bag import Queue
from algo.data_structures.bag import Stack


def test_bag():
    s = Stack()
    s.push(1).push(2)
    assert s.pop() == 2
    assert s.pop() == 1

    q = Queue()
    q.push(1).push(2)
    assert q.pop() == 1
    assert q.pop() == 2

    pq = PriorityQueue()

    pq.push((3, "b"))
    pq.push((1, "a"))
    pq.push((2, "c"))
    assert pq.pop() == (1, "a")
