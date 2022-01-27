class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)


def hotPotato(listval,numval):
    q = Queue()
    for name in listval:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(numval):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()

listinfo = ["Mary","Jane","John","Mike","Jake","Gillian","Fred","Nolan","Chris","Dueck"]
numinfo = 7

print(hotPotato(listinfo,numinfo))