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

    pq.push("b", 3)
    pq.push("a", 1)
    pq.push("c", 2)

    pq.decrease_key("b", 0)
    assert pq.pop() == ("b", 0)

    pq.decrease_key("a", 0)
    assert pq.pop() == ("a", 0)
