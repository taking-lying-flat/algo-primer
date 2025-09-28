# https://docs.python.org/3/library/collections.abc.html
# https://docs.python.org/3/library/collections.html
# https://docs.python.org/3/library/heapq.html
# https://grantjenks.com/docs/sortedcontainers/

"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.1 将序列分解为单独变量 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────────────
⭐ 适用对象 : 所有可迭代对象 (元组 / 列表 / 字符串 / 文件对象 / 迭代器 / 生成器 …)
⭐ 数量匹配 : 变量数量必须与序列元素数量一致，否则抛 ValueError
⭐ 结构匹配 : 支持嵌套结构解包，例如 (year, mon, day) = date_tuple
⭐ 占位符   : 使用下划线 _ 忽略不需要的值
⭐ 部分解包 : Python 无专门语法，必须为每个元素提供变量名 (或占位符)
♻️ 可迭代判定 : 对象只需实现 __iter__() 即视作 Iterable
────────────────────────────────────────────────────────────────────────────────────────────
万物皆对象  Everything is an Object (identity / type / value)
🔥🔥🔥 Python 运行期把任何东西（数字、字符串、函数、类、模块、None …）都视作 object 的一个实例
每个对象自带三块核心元信息
⭐ identity  — id(obj) 返回的整数，通常映射到对象在内存中的地址；在对象的生命周期内保持不变
⭐ type — type(obj) 返回对象所属的 class，决定它支持哪些操作、方法与运算符
⭐ value  — 对象存储的数据本体
   - 不可变对象 (int, str, tuple, frozenset …) 一旦创建其值不可修改；“修改” 会得到新对象，身份改变
   - 可变对象 (list, dict, set, bytearray …) 可在原身份上原地修改其值
────────────────────────────────────────────────────────────────────────────────────────────
"""
# 基本解包
x, y = (4, 5)
# 列表 + 嵌套元组
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, mon, day) = data  # 嵌套解包
# 使用占位符 _ 忽略不需要的值
_, shares, price, _ = data
# ❌ 解包数量不匹配示例 (抛 ValueError)
try:
    a, b, c = (1, 2)
except ValueError as err:
    print("ValueError:", err)


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.2 解压可迭代对象赋值给多个变量 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────────────
⭐ 适用场景 : 当可迭代对象元素多于变量时，用 *var 接收剩余元素
⭐ 收集类型 : *var 永远是 list（即便为空）
⭐ 位置灵活 : *var 可在开头、中间、结尾（*head, last / first, *mid, last / first, *tail）
⭐ 占位符   : 若仅想丢弃余下元素，用 *_ 或其他占位名
────────────────────────────────────────────────────────────────────────────────────────────
"""
def drop_first_last(grades):                     # grades = [10, 9, 8, 7, 6]
    first, *middle, last = grades
    return sum(middle) / len(middle)             # → 8.0

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phones = record  # name='Dave', email='dave@example.com', phones=['773-555-1212','847-555-1212']
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *_, homedir, shell = line.split(':')       # uname='nobody', homedir='/var/empty', shell='/usr/bin/false'


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.3 保留最后 N 个元素 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────────────
⭐ 问题     : 迭代或其他操作中，仅需保留最近 N 条记录
⭐ 解决方案 : 使用 collections.deque(maxlen=N) 自动丢弃最老元素
⭐ 特点     : append 操作 O(1)，满时自动剔除队首；appendleft, pop, popleft 同样高效
────────────────────────────────────────────────────────────────────────────────────────────
⭐ 容器 (Container)
   • 定义 : 实现 __contains__(self, item) 或支持 in 运算的对象，可存放其他对象的盒子
   • 典型 : list, tuple, set, dict, str, deque, 自定义类实现 __iter__/__len__/__contains__ 亦可视为容器
   • 特性 : 可配合 len(), in, 迭代等操作; 多数容器同样是 Iterable / Collection
⭐ 生成器 (Generator)
   • 定义 : 含有 yield 的函数调用结果，返回一个延迟计算的迭代器；或 (expr for x in iterable) 推导式产生
   • 协议 : 同时实现 __iter__() 和 __next__()，每次 next() 产出一个值，直至抛 StopIteration
   • 优势 : 惰性、节省内存，可无限序列或大数据流; 可配合 send() /throw() /close() 做协程
────────────────────────────────────────────────────────────────────────────────────────────
"""
def search(lines: Iterable[str], pattern: str, history: int = 3) -> Generator[Tuple[str, List[str]], None, None]:
    prev: deque[str] = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, list(prev)
        prev.append(line)

logs = ['a','python error','b','c','python ok','d']
for match, prev in search(logs, 'python', history=2):
    print(match, prev)                          # → 'python error', ['a']
                                                # → 'python ok', ['b', 'c']


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.4 查找最大或最小的 N 个元素 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────────────
⭐ 场景     : 从序列或可迭代对象中快速获得最大 / 最小的前 N 个元素
⭐ 核心 API : heapq.nlargest(N, data, key=...) / heapq.nsmallest(...)
⭐ 性能优势 : 当 N ≪ 数据量时，复杂度 ~ O(len(data) · log N)，优于整体排序
• N == 1          → 直接用 min() / max() 更快
• N 接近数据量     → 直接排序后切片; sorted(data)[:N] / [-N:]
• N 远小于数据量   → heapq.nlargest/nsmallest 优势最大
────────────────────────────────────────────────────────────────────────────────────────────
常用堆操作 API（heapq 模块）
⭐ heapq.heapify(seq)
   • 将任意序列原地转成最小堆；时间复杂度 O(len(seq))
⭐ heapq.heappush(heap, item)
   • 向堆插入新元素并保持堆性质
⭐ heapq.heappop(heap)
   • 弹出并返回最小元素（堆顶）
⭐ heapq.heappushpop(heap, item)
   • 先 push 再 pop，但只做一次平衡；比先 push 再 pop 更快
⭐ heapq.heapreplace(heap, item)
   • 先 pop 最小元素，再 push 新元素；与 heappushpop 作用相反
⭐ heapq.merge(*iterables)
   • 多个已排序输入按顺序合并生成器，节省内存；适合外排序
⏩ 记忆要点：heap[0] 永远是最小值，所有操作都围绕维护这一不变式
────────────────────────────────────────────────────────────────────────────────────────────
"""
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.nlargest(3, nums)   # → [42, 37, 23]
heapq.nsmallest(3, nums)  # → [-4, 1, 2]
portfolio = [
    {'name': 'IBM',  'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50,  'price': 543.22},
    {'name': 'FB',   'shares': 200, 'price': 21.09},
    {'name': 'HPQ',  'shares': 35,  'price': 31.75},
    {'name': 'YHOO', 'shares': 45,  'price': 16.35},
    {'name': 'ACME', 'shares': 75,  'price': 115.65},
]
cheap      = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive  = heapq.nlargest(3,  portfolio, key=lambda s: s['price'])


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.5 实现一个优先级队列 (Priority Queue) ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────────────
⭐ 场景     : 需要按优先级（权重）依次取元素，最高优先级先出队
⭐ 数据结构 : heapq + 元组 (-priority, index, item) 形成稳定的最大堆
⭐ 复杂度   : push / pop 均为 O(log n)，适合海量数据
⭐ index   : 避免同优先级元素不可比较，并确保 FIFO 顺序
────────────────────────────────────────────────────────────────────────────────────────────
"""
class PriorityQueue:
    """最大堆优先级队列，支持同优先级 FIFO。"""
    def __init__(self):
        self._queue: list[tuple[int, int, object]] = []  # (-priority, index, item)
        self._index: int = 0

    def push(self, item, priority: int) -> None:
        # -priority ↔ 最大堆；index 保证同优先级按插入顺序 (稳定)
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        """弹出优先级最高且最早插入的元素"""
        return heapq.heappop(self._queue)[-1]


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.6 字典中的键映射多个值 (Multi‑Dict) ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
──────────────────────────────────────────────
⭐ 场景     : 需要让同一个键关联多个值（如日志归类、倒排索引）
⭐ 推荐做法 : collections.defaultdict( list / set ) —— 自动初始化容器
⭐ 何时用哪种容器
   • list  → 保留插入顺序，允许重复
   • set   → 去重且不关心顺序
"""
list_map: defaultdict[str, list[int]] = defaultdict(list)
list_map['a'].append(1)
list_map['a'].append(2)
list_map['b'].append(4)
# list_map == {'a': [1, 2], 'b': [4]}

set_map: defaultdict[str, set[int]] = defaultdict(set)
set_map['a'].add(1)
set_map['a'].add(2)
set_map['a'].add(2)  # 重复被忽略
set_map['b'].add(4)
# set_map == {'a': {1, 2}, 'b': {4}}


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.7 字典排序 (OrderedDict) ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────────────
⭐ 场景     : 构建将来需要保持键插入顺序的映射（迭代/序列化时稳定顺序）
⭐ 数据结构 :  collections.OrderedDict —— 基于双向链表维护插入顺序。
⭐ 复杂度   : 与普通 dict 相当，内存开销略高（额外链表指针）
────────────────────────────────────────────────────────────────────────────────────────────
"""
d = OrderedDict()        # 插入新键时置于末尾；对已有键赋值不改变顺序
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print(key, d[key])   # foo 1  bar 2  spam 3  grok 4
json.dumps(d)            # {"foo": 1, "bar": 2, "spam": 3, "grok": 4}


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.8 字典的运算 (Dict Computations) ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────────────
⭐ 问题     : 在字典中进行最小/最大值查找与排序，同时获取对应的键和值
⭐ 核心技术 : 利用 zip() 交换 (value, key) 或使用 min()/max() 的 key 参数
⭐ 核心技巧 : zip(dict.values(), dict.keys()) 反转为 (值, 键) 元组
⭐ 原理     : 元组比较时先比值再比键；zip() 返回迭代器只能用一次
────────────────────────────────────────────────────────────────────────────────────────────
"""
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
min_val_key = min(zip(prices.values(), prices.keys()))  # → (10.75, 'FB')
max_val_key = max(zip(prices.values(), prices.keys()))  # → (612.78, 'AAPL')
# 排序所有项
sorted_by_price = sorted(zip(prices.values(), prices.keys()))  # → [(10.75,'FB'), (37.2,'HPQ'), ...]
# 使用 key 参数直接在键上查找
min_key = min(prices, key=lambda k: prices[k])          # → 'FB'
max_key = max(prices, key=lambda k: prices[k])          # → 'AAPL'
min_value = prices[min_key]                             # → 10.75


"""
░░░░░░░░░░░░░░ 1.9 查找两字典的相同点 (Dict Comparisons) ░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────────────
⭐ 问题     : 查找两个字典的共同键、共同值对、差异等
⭐ 核心技术 : 字典的 keys() 和 items() 返回的视图对象直接支持集合操作（交集、并集、差集等），无需转换为 set
⭐ 注意     : values() 不支持集合操作（值可能重复）
⭐ 视图对象特性: 视图对象是字典的「动态窗口」，永远映射字典当前状态
  - 动态性: 持有原字典弱引用，实时反映字典最新状态，任何修改立即可见
  - 惰性计算: 不缓存数据，每次操作都直接访问原字典（len/iter/contains）
  - 轻量级: 只是包装对象，不复制数据，内存开销极小
  - 只读接口: 不能通过视图修改字典，只能通过原字典修改
────────────────────────────────────────────────────────────────────────────────────────────
"""
a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}
common_keys = a.keys() & b.keys()            # → {'x', 'y'}
unique_in_a = a.keys() - b.keys()            # → {'z'}
common_items = a.items() & b.items()         # → {('y', 2)}
c = {key: a[key] for key in a.keys() - {'z', 'w'}}  # → {'x': 1, 'y': 2}


"""
░░░░░░░░░░░░░░ 1.10 删除序列相同元素并保持顺序 (Dedupe with Order) ░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────
⭐ 问题     : 去除序列中的重复元素，同时保持原始顺序
⭐ 核心技术 : 使用 set 记录已见元素 + 生成器惰性返回
  - set 提供 O(1) 的查重性能
  - 生成器避免创建新列表，节省内存
  - key 函数处理不可哈希类型（如 dict）
⭐ 对比     : set(items) 会去重但破坏顺序，本方案保持顺序
────────────────────────────────────────────────────────────────────────────────────
⭐ 什么是可哈希
  - 可哈希对象必须有 __hash__() 方法，返回整数哈希值
  - 生命周期内哈希值不变，且相等的对象哈希值必须相同
  - 可作为 dict 的键或 set 的元素
⭐ 为什么可变类型不可哈希
  - 如果对象内容改变，哈希值也应该改变
  - 但这会破坏 dict/set 的内部结构（基于哈希表）
  - 所以 Python 禁止可变类型作为 dict 键或 set 元素
⭐ 可哈希 vs 不可哈希：
  - hashable: int, float, str, tuple, frozenset, bool, None
  - unhashable: list, dict, set, bytearray（所有可变类型）
  - 规则: 不可变类型通常可哈希，可变类型不可哈希
────────────────────────────────────────────────────────────────────────────────────
"""
def dedupe(items, key=None):
   seen = set()
   for item in items:
       val = item if key is None else key(item)
       if val not in seen:
           yield item
           seen.add(val)

a = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
list(dedupe(a, key=lambda d: (d['x'],d['y'])))
list(dedupe(a, key=lambda d: d['x']))


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.11 命名切片 (Named Slices) ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────
⭐ 问题     : 代码中存在大量硬编码切片下标，降低可读性
⭐ 核心技术 : 使用 slice() 创建命名切片对象
  - 提高代码可读性和可维护性
  - 切片对象可重用
  - 支持所有切片操作（读取、赋值、删除）
⭐ 高级特性 : indices(size) 方法自动调整边界，避免 IndexError
────────────────────────────────────────────────────────────────────────────────────
"""
record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])

a = slice(2, 4)
items[a] = [10,11]  # 等价于 items[2:4] = [10,11]

# indices() 避免越界
a = slice(5, 50, 2)
a.indices(10)  # → (5, 10, 2)


"""
░░░░░░░░░░░░░░ 1.12 序列中出现次数最多的元素 (Most Common Elements) ░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────
⭐ 问题     : 找出序列中出现频率最高的元素
⭐ 核心技术 : collections.Counter 类
  - Counter(iterable) 创建计数器
  - most_common(n) 返回出现频率最高的 n 个元素
  - update() 批量更新计数
⭐ 高级特性 : 支持数学运算 +  -  &  |
⭐ 比较运算符：
  == / != : 判断两个计数器在「正计数元素」上的计数是否完全一致。等价于 dict(c1) == dict(c2)（自动忽略计数≤0的元素）
  < / <=  : 判断真子集/子集关系  all(c1[x] <= c2[x] for x in c1∪c2) ;  < 还需至少一个元素严格小于
  > / >=  : 判断真超集/超集关系  all(c1[x] >= c2[x] for x in c1∪c2);  还需至少一个元素严格大于
────────────────────────────────────────────────────────────────────────────────────
"""
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words)
top_three = word_counts.most_common(3)  # → [('eyes', 8), ('the', 5), ('look', 4)]

# 访问计数
word_counts['eyes']  # → 8

# 更新计数
word_counts['new'] += 1
word_counts.update(['more', 'words'])

# 数学运算
a = Counter(words1)
b = Counter(words2)
c = a + b  # 合并计数
d = a - b  # 差集计数
e = a & b  # 交集（取最小）
f = a | b  # 并集（取最大）


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.13 通过某个关键字排序字典列表 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────
⭐ 问题     : 根据字典的某个或某几个字段排序字典列表
⭐ 核心技术 : operator.itemgetter()
 - itemgetter('key') 创建获取单个键的函数
 - itemgetter('key1', 'key2') 创建获取多个键的函数
 - 比 lambda 表达式更快
⭐ 适用场景 : sorted(), min(), max() 等需要 key 函数的场合
────────────────────────────────────────────────────────────────────────────────────
"""
rows = [
   {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
   {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
   {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
   {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))

# 用于 min/max
min_uid = min(rows, key=itemgetter('uid'))  # uid 最小的记录
max_uid = max(rows, key=itemgetter('uid'))  # uid 最大的记录

# lambda 替代方案（稍慢）
rows_by_fname_lambda = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname_lambda = sorted(rows, key=lambda r: (r['lname'], r['fname']))


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.14 排序不支持原生比较的对象 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────
⭐ 问题     : 排序没有实现比较方法的自定义对象
⭐ 核心技术 : operator.attrgetter()
 - attrgetter('attr') 创建获取单个属性的函数
 - attrgetter('attr1', 'attr2') 创建获取多个属性的函数
 - 比 lambda 表达式更快
⭐ 适用场景 : sorted(), min(), max() 等需要 key 函数的场合
────────────────────────────────────────────────────────────────────────────────────
"""
class User:
   def __init__(self, user_id, first_name='', last_name=''):
       self.user_id = user_id
       self.first_name = first_name
       self.last_name = last_name
   
   def __repr__(self):
       return f'User({self.user_id})'

users = [User(23), User(3), User(99)]
sorted_by_name = sorted(users, key=attrgetter('last_name', 'first_name'))

# 用于 min/max
min_user = min(users, key=attrgetter('user_id'))  # user_id 最小的对象
max_user = max(users, key=attrgetter('user_id'))  # user_id 最大的对象
sorted_by_name_lambda = sorted(users, key=lambda u: (u.last_name, u.first_name))


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.15 通过某个字段将记录分组 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────
⭐ 问题     : 根据某个字段对字典或对象序列进行分组迭代
⭐ 核心技术 : itertools.groupby()
 - 必须先排序: groupby只检查连续相同的元素
 - 返回 (key, group_iterator) 元组
 - group_iterator 是一次性迭代器
⭐ 替代方案 : defaultdict(list) 构建多值字典（无需排序）
────────────────────────────────────────────────────────────────────────────────────
"""
rows = [
   {'address': '5412 N CLARK', 'date': '07/01/2012'},
   {'address': '5148 N CLARK', 'date': '07/04/2012'},
   {'address': '5800 E 58TH', 'date': '07/02/2012'},
   {'address': '2122 N CLARK', 'date': '07/03/2012'},
   {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
   {'address': '1060 W ADDISON', 'date': '07/02/2012'},
   {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
   {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.16 过滤序列元素 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────
⭐ 问题     : 根据条件从序列中提取元素
⭐ 核心技术 : 
 - 列表推导：[x for x in seq if condition]
 - 生成器表达式：(x for x in seq if condition) - 省内存
 - filter(func, seq) - 复杂条件过滤
 - itertools.compress(data, selectors) - 根据布尔序列过滤
⭐ 高级技巧 : 条件表达式替换不符合条件的值
────────────────────────────────────────────────────────────────────────────────────
"""
# filter() - 复杂条件
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
   try:
       int(val)
       return True
   except ValueError:
       return False

ivals = list(filter(is_int, values))  # ['1', '2', '-3', '4', '5']

# compress() - 根据另一个序列过滤
from itertools import compress
addresses = ['5412 N CLARK', '5148 N CLARK', '5800 E 58TH', '2122 N CLARK']
counts = [0, 3, 10, 4]
more5 = [n > 5 for n in counts]  # [False, False, True, False]
result = list(compress(addresses, more5))  # ['5800 E 58TH']


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.17 从字典中提取子集 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────
⭐ 问题     : 根据条件从字典中提取部分键值对，构造新字典
⭐ 核心技术 : 
- 字典推导：{k:v for k,v in dict.items() if condition}
- 键集合操作：dict.keys() & set 获取交集
- dict()构造函数：dict((k,v) for k,v in items if condition)
⭐ 性能对比 : 字典推导 > dict()函数
────────────────────────────────────────────────────────────────────────────────────
"""
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}

# 1. 按值过滤 - 价格 > 200
p1 = {k: v for k, v in prices.items() if v > 200}  
# 2. 按键过滤 - 在指定集合中
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {k: v for k, v in prices.items() if k in tech_names}
# 3. 键集合操作方式（更优雅）
p3 = {k: prices[k] for k in prices.keys() & tech_names}
# 4. 多条件过滤
p4 = {k: v for k, v in prices.items() if v > 50 and k.startswith('A')}


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.18 映射名称到序列元素 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────
⭐ 问题     : 通过名称而非下标访问序列元素，提高代码可读性
⭐ 核心技术 : 
 - namedtuple('类名', ['字段1', '字段2'])：创建具名元组类
 - 实例._replace(**kwargs)：创建修改后的新实例（不可变）
 - 兼容元组：支持索引、解包、len()等操作
⭐ 优势     : 比字典省内存，比元组可读性高，适合只读数据结构
────────────────────────────────────────────────────────────────────────────────────
"""
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
# 更新字段（返回新实例）
s = s._replace(shares=75)

# 缺失字段处理 - 原型模式
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)
   
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
dict_to_stock(a)  # Stock(name='ACME', shares=100, price=123.45, date=None, time=None)


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.19 转换并同时计算数据 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────
⭐ 问题     : 在聚集函数中同时进行数据转换或过滤
⭐ 核心技术 : 
- 生成器表达式作参数
- 避免创建临时列表：生成器迭代处理，节省内存
- 配合any()/all()/min()/max()等聚集函数使用
⭐ 性能优势 : 不创建中间列表，适合大数据集
────────────────────────────────────────────────────────────────────────────────────
"""
# 过滤并判断 - 是否存在.py文件
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
   print('There be python!')

# 提取并聚集 - 最小股份数
portfolio = [
   {'name':'GOOG', 'shares': 50},
   {'name':'YHOO', 'shares': 75},
   {'name':'AOL', 'shares': 20},
   {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
min_item = min(portfolio, key=lambda s: s['shares'])  


"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 1.20 合并多个字典或映射 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────────────────────────
⭐ 问题     : 逻辑上合并多个字典，执行查找等操作
⭐ 核心技术 : 
- ChainMap(dict1, dict2, ...)：创建字典链视图
- 查找顺序：从左到右，返回第一个找到的值
- 修改操作：只影响第一个字典
- new_child()/parents：创建/移除作用域层级
⭐ 优势     : 不创建新字典，原字典修改实时反映
────────────────────────────────────────────────────────────────────────────────────
"""
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
c['z']  # 3 (from a, not b)

values = ChainMap()
values['x'] = 1
values = values.new_child()  # 新作用域
values['x'] = 2
values = values.new_child()  # 再新作用域
values['x'] = 3
# ChainMap({'x': 3}, {'x': 2}, {'x': 1})
values = values.parents  # 退出作用域
# values['x'] = 2

# 4. 对比update() - ChainMap是视图，不是拷贝
# update(): 创建数据的副本，之后相互独立
# ChainMap: 创建视图/引用，始终反映原字典的最新状态
merged = dict(b)
merged.update(a)
a['x'] = 42 # merged['x'] 仍是 1
