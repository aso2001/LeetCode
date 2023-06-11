class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.hh = [[(0,0)] for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        self.hh[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        
    def get(self, index: int, snap_id: int) -> int:
        # snap_idx = bisect.bisect_right(self.hh[index], [snap_id,10**9])
        # return self.hh[index][snap_idx - 1][1]
        his = self.hh[index]
        L, R = 0, len(his) - 1
        while L <= R:
            mid = (L + R)//2
            if his[mid][0] <= snap_id:
                L = mid + 1
            else:
                R = mid - 1
        return his[R][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)