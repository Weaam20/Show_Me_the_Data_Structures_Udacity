import heapq


class PriorityQueue:
    def __init__(self):
        self._data = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._data, (priority, self._index, item))
        self._index += 1

    def pop(self):
        if len(self._data) > 0:
            return heapq.heappop(self._data)[-1]
        else:
            return None

    def Print(self):
        for i in range(len(self._data)):
            item = self._data[i][-1]
            if len(self._data) > 0:
                print('Data: ', item.data, 'Freq: ', 'Right: ', item.frequency, item.right, 'Left: ', item.left)
            else:
                print('Data: ', item.data, 'Freq: ', item.frequency)

    def size(self):
        return len(self._data)
