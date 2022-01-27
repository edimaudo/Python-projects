class Node:
    def __init__(self,inputitem):
        self.data = inputitem
        self.next = None
    def getNext(self):
        return self.next
    def getData(self):
        return self.data
    def setNext(self,newnext):
        self.next = newnext
    def setData(self,newdata):
        self.data = newdata

class UnorderedLinkedList():
    def __init__(self):
        self.head = None
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def isEmpty(self):
        return self.head == None
    def size(self):
        countval = 0
        current = self.head
        while current != None:
            countval += 1
            current.getNext()
        return countval
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        countval = 0
        while not found:
            if self.size() == countval:
                break
            elif current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
            countval+=1
        if previous == None:
            self.head = current.getNext()
        elif self.size() == countval:
            previous = None
        else:
            previous.setNext(current.getNext())
    def search(self,item):
        found = False
        current = self.head
        countval = 0
        while current != None:
            if current.getData() == item:
                found = True
                break
            current = current.getNext()
        print(found)
    def append(self,item):
        current = self.head
        found = False
        countval = 0
        temp = Node(item)
        while not found:
            if current.getNext() == None:
                current.setNext(temp)
                found = True
                break
            current = current.getNext()
    def index(self,item):
        current = self.head
        countval = 1
        outputval = 0
        found = False
        while not found:
            if current.getNext() == None:
                outputval = -1
                break
            elif current.getData() == item:
                outputval = countval
                break
            countval+=1
            current = current.getNext()
        print (str(outputval))       
    def insert(self,pos,item):
        current = self.head
        found = False
        countval = 0
        while not found:
            if pos > self.size() or pos < 1:
                found = True
            elif pos == 1:
                self.add(item)
                found = True
            elif pos == self.size():
                self.append(item)
                found = True
            elif countval == pos:
                previous = current
                temp = Node(item)
                previous.setNext(temp)
                temp.setNext(current.getNext())
                found = True
            current = current.getNext()
            countval+=1                         
    def pop():
        current = self.head
        found = False
        while not found:
            if current.getNext() == None:
                outputval = current.getData()
                self.remove(current.getData())
                found = True
                break
            current=current.getNext()
        return outputval       
    def pop_pos(self,pos):
        current = self.head
        found = False
        countval = 0
        while not found:
            if pos > self.size or pos < 1:
                outputval = "-1"
                found = True
                break
            elif countval == pos:
                outputval = current.getData()
                self.remove(outputval)
                found = True
                break
            current = current.getNext()
            countval+=1               
        return outputval
                
        


def main():
    s = UnorderedLinkedList()
    s.add(1)
    s.add(2)
    s.add(3)
    print(s.size())
    #s.insert(4,5)

    
    
main()
