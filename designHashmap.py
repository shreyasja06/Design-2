# leetcode username: shreyagoyal06
# put, get, remove have worst case complexity: O(n), average case complexity: O(1)


class MyHashMap(object):

    def __init__(self):
        # Array of 10000 buckets, each bucket is a list for collision handling(separate chaining)
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]
        
    def put(self, key, value):
        # Hash key to find bucket, update if exists, otherwise append new [key, value] pair
        bucket_index = key % self.size
        for pair in self.buckets[bucket_index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.buckets[bucket_index].append([key, value])

    def get(self, key):
        # Search bucket for key, return value if found, otherwise return -1
        bucket_index = key % self.size
        for pair in self.buckets[bucket_index]:
            if pair[0] == key:
                return pair[1]
        return -1


    def remove(self, key):
        bucket_index = key % self.size
        bucket = self.buckets[bucket_index]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return
