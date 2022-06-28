class HashTable:
    def __init__(self):
        self.size = 99999999
        self.slots = [None] * self.size
        self.data = [None] * self.size 

    def put(self, key, data):
        hash_value = self.hash_function(key,len(self.slots))
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data #replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
        
            if self.slots[next_slot] == None:
                self.slots[next_slot] = key
                self.data[next_slot] = data
            else:
                self.data[next_slot] = data #replace
    def getdata(self,key):
        hash_value = self.hash_function(key,len(self.slots))
        return self.data[hash_value]
    def hash_function(self, key, size):
        return key % size
    
    def rehash(self, old_hash, size):

        return (old_hash + (size*2)) 

    def delete1(self, key):
        hash_value = self.hash_function(key,len(self.slots))
        key_exist= False
        if self.slots[hash_value] == None:
            print('item does not exist')

        else:
            if self.slots[hash_value] == key:
                key_exist = True
            else:
                next_slot= self.rehash(hash_value,len(self.slots))
                while self.slots[next_slot] != None and \
                    self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] == None:
                    print('item does not exist')
                else:
                    key_exist=True
            if key_exist:
                #del self.slots[key]
                self.slots[hash_value] ='Deleted'
                self.data[hash_value]='Deleted'
                # print('key',key,'deleted')
            else:
                print('key',key,'not found')
    
    def delete2(self,key):
        hash_value = self.hash_function(key,len(self.slots))
        keyb=False
        if self.slots[hash_value] == None:
            print('item does not exist')
        else:
            if self.slots[hash_value]==key:
                keyb=True
            else:
                next_slot=self.rehash(hash_value,len(self.slots))
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot=self.rehash(next_slot,len(self.slots))
                if self.slots[next_slot]== None:
                    print ('Item not found')
                else:
                    keyb= True
            if keyb == True:
                self.slots[hash_value] = None
                self.data[hash_value]= None
                next_slot=self.rehash(hash_value,len(self.slots))
                while self.data[next_slot] != None:
                    Data = self.data[next_slot]
                    KEY = self.slots[next_slot]
                    self.data[next_slot] = None
                    self.slots[next_slot] = None
                    self.put(KEY, Data)
                    hash_value = next_slot
                    next_slot=self.rehash(next_slot,len(self.slots))



c = HashTable()
c.put(0,'cat')
c.put(1,'cat')
c.put(2,'cat')
c.put(3,'cat')
c.put(4,'cat')
c.put(5,'cat')
c.put(6,'cat')
c.put(7,'cat')
c.put(8,'cat')
c.put(9,'cat')

