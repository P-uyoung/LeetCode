# Doubly linked list

class Node(object):
    def __init__(self, url=0, prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory(object):
    def __init__(self, homepage):
        self.head = self.cur = Node(homepage)   # 여기서, head는 형식상 포인텅ㅇㅇㅇㅇ
    
    def visit(self, url):
        new_node = Node(url=url, prev=self.cur)
        self.cur.next = new_node
        self.cur = new_node
        
    def back(self, steps):
        while steps>0 and self.cur.prev is not None:
            steps -= 1
            self.cur = self.cur.prev
        return self.cur.url         
        
    def forward(self, steps):
        while steps > 0 and self.cur.next is not None:
            steps -= 1
            self.cur = self.cur.next
        return self.cur.url
