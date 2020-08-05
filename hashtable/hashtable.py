class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f'Node({repr(self.value)})'

class LinkList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "[Empty List]"

        cur = self.head
        s = ""

        while cur != None:
            s += f'({cur.value})'

            if cur.next is not None:
                s += '-->'

            cur = cur.next
        return s

    def find(self, value):
        cur = self.head

        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next

        return None

    def delete(self, value):
        cur = self.head

        if cur.value == value:
            self.head = cur.next
            return cur
        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.value == value:
                prev.next = cur.next
                return cur
            prev = cur
            cur = cur.next
        
        return None

    def addToHead(self, node):
        node.next = self.head
        self.head = node
    
    def insert_overwrite(self, key, value):
        node = self.find(value)

        if node is None:
            self.addToHead(Node(key, value))
        node.value = value

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        return len(HashTable)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this. --> number of items in hash / total number of slots
        """
        # Your code here
        return self.count / len(self.capacity)

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (( hash << 5 ) + hash ) + ord(x)
        return hash & 0xffffffff

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        #figure out index
        index = self.hash_index(key)
        curNode = self.storage[index]
        #search LL if key is there
        if curNode is not None:
            #if current key is there, overwrite
            if curNode.key == key:
                self.storage[index] = HashTableEntry(key, value)
                self.count += 1
        #if not, HashTableEntry and insert to list
        # self.storage.insert_overwrite(value)
        self.storage[index] = HashTableEntry(key, value)
        self.count += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        #Figure out index
        #Search for HTE that match keys
            #if found, delete entry form linked list, return value
            #return None
        index = self.hash_index(key)
        # hash_data[index] = None
        self.count -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        #Figure out index for the key
        index = self.hash_index(key)
        curNode = self.storage[index]
        #Search LL for HashTableEntry that matches key
        if curNode is not None:
            #Return value for entry, and None if not found
            return curNode
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
