class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        # each index record the latest log change this index
        self.cntr = 0
        self.log = {}
        self.dct = {}
    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.log[index] = val

    def snap(self):
        """
        :rtype: int
        """
        self.dct[self.cntr] = self.log
        self.log = {}
        self.cntr += 1
        return self.cntr-1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        while snap_id >= 0 and index not in self.dct[snap_id]:
            snap_id -= 1
        if snap_id < 0:
            return 0
        return self.dct[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)