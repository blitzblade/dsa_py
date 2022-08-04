def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

## handling collision
# chaining: storing a list at each location instead of one value

if __name__ == "__main__":
    t = HashTable()
    t['march 6'] = 130

    print(t['march 6'])