# ░░░░░░░░░░░░░░ LeetCode 295 —— 数据流的中位数 ░░░░░░░░░░░░░░
class MedianFinder:
    """
    对顶堆维护动态中位数, 使用两个堆将数据分成两半:
        - 左堆(大根堆)：存储较小的一半，堆顶是最大值
        - 右堆(小根堆)：存储较大的一半，堆顶是最小值
    维护两个不变量：
        1. 平衡性：len(left) - len(right) ∈ {0, 1}
        2. 有序性：max(left) ≤ min(right)
    """
    def __init__(self):
        self.left = []   # 大根堆（存负数），保存较小的一半
        self.right = []  # 小根堆，保存较大的一半
    
    def addNum(self, num: int) -> None:
        """ 添加数字的核心逻辑: 不能直接插入目标堆！必须先经过另一个堆"过滤" """
        if len(self.left) == len(self.right):
            # 两堆相等，新元素要进左堆
            # num先进右堆，弹出最小值，该值 ≤ 右堆所有元素
            heappush(self.left, -heappushpop(self.right, num))
        else:
            # 左堆多一个，新元素要进右堆
            # -num先进左堆，弹出最大值的负数，还原后 ≥ 左堆所有元素
            heappush(self.right, -heappushpop(self.left, -num))
    
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (self.right[0] - self.left[0]) / 2


# ░░░░░░░░░░░░░░ LeetCode 347 - 前K个高频元素 ░░░░░░░░░░░░░░
@staticmethod
def topKFrequent(nums: List[int], k: int) -> List[int]:"
    freq_map = Counter(nums)
    heap = []
    for num, freq in freq_map.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, num))
        else:
            if freq > heap[0][0]:
                heapq.heapreplace(heap, (freq, num))
    return [num for _, num in heap]
