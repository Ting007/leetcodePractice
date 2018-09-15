class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._len= capacity
        self._caches = {}
        self._priority = []
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self._caches.keys():
                self._priority.remove(key)
                self._priority.append(key)
        try:
            return self._caches[key]
        except:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if len(self._caches) < self._len:
            self._caches[key] = value
        else:
            self._caches.pop(self._priority[0])
            self._caches[key] = value
        self._priority.append(key)

if __name__ == '__main__':
    foo = LRUCache(2)
    foo.get(1)
    foo.put(1, 1)
    foo.put(2,2)
    foo.get(1)
    foo.put(3,3)

