class Node:
    def __init__(self,itemdata):
        self.data = itemdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext

class OrderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count+=1
            currrent = current.getNext()
        return count