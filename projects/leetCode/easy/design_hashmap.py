class Hashmap:

    def __init__(self):
        self.map = dict()

    def put(self,key,value):
        self.map[key] = value
        print(self.map)

    def get(self,key):
        try :
            return self.map[key]
        except:
            return -1

    def remove(self,key):
        if key in self.map:
            del self.map[key]

if __name__  == '__main__':
    a = Hashmap()
    a.put(1,1)
    a.put(2,2)
    a.put(1,3)
    a.remove(2)
    print(a)
