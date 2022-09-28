![Image alt](https://github.com/AshenRain/SberAp/raw/main/Task_2/1.jpg)
![Image alt](https://github.com/AshenRain/SberAp/raw/main/Task_2/2.jpg)

```
class Queue:

    def __init__(self, queue = ''):
        self.queue = list(queue)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 

    def __lt__(self, b):
        ''' < '''
        if self.size() == b.size(): 
            if (self.queue[0]) > (b.queue[0]):
                return True
            else:
                return False
        elif self.size() < b.size():
            return True
        else:
            return False
    
    def __gt__(self, b):
        ''' > '''
        if self.size() == b.size(): 
            if (self.queue[0]) < (b.queue[0]):
                return True
            else:
                return False
        elif self.size() > b.size():
            return True
        else:
            return False
    
    def __eq__(self, b):
        ''' == '''
        if self.size() == b.size() and (self.queue[0]) == (b.queue[0]):
            return True
        else:
            return False
        

def parse_queues(a,b):
    while(a.size() != 0 or b.size() != 0):
        if a > b:
            print(a.dequeue())
        else:
            print(b.dequeue())

a = Queue('AA')
b = Queue('BBB')

print(a > b)
parse_queues(a,b)
```