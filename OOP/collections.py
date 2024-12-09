from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

def demo_counter():
    some_text = "sadadsafdsaxxxxxxxx"
    my_counter = Counter(some_text)
    print("Counter Example:")
    print(my_counter)
    print(list(my_counter.items()))
    print(list(my_counter.values()))
    print(f"Most common character: {my_counter.most_common(1)[0][0]} with count {my_counter.most_common(1)[0][1]}")
    print(f"Elements as list: {list(my_counter.elements())}")
    print("-" * 30)

def demo_namedtuple():
    Point = namedtuple('Point', 'x,y')
    pt = Point(7, -8)
    print("Namedtuple Example:")
    print(pt)
    print(f"x = {pt.x}, y = {pt.y}")
    print("-" * 30)

def demo_ordered_dict():
    ordered_dict = OrderedDict()
    ordered_dict['b'] = 2
    ordered_dict['c'] = 3
    ordered_dict['d'] = 4
    ordered_dict['a'] = 1
    print("OrderedDict Example:")
    print(ordered_dict)
    print("-" * 30)

def demo_defaultdict():
    print("Defaultdict Example:")
    d = defaultdict(int)
    d['f'] = 1
    d['g'] = 2
    print(d)
    print(f"Accessing existing key: {d['f']}")
    # default dict will return 0, as int was specified as default, it would be [] for list, or 0.0 for float
    # standard dict would raise KeyError exception if would attempt to access missing key
    print(f"Accessing missing key: {d['z']} (default value)")
    d2 = defaultdict(list)
    d2['h'] = [1]
    d2['j'] = [2]
    print(d2)
    print("-" * 30)

def demo_deque():
    dec = deque()
    print("Deque Example:")
    dec.append(1)
    dec.append(2)
    dec.appendleft(3)
    print(f"After appending: {dec}")
    dec.pop()
    print(f"After popping: {dec}")
    dec.popleft()
    print(f"After popping left: {dec}")
    dec.extend([4, 5, 6])
    print(f"After extending: {dec}")
    dec.extendleft([-9, -7, -5])
    print(f"After extending left: {dec}")
    dec.rotate(1)
    print(f"After rotating right: {dec}")
    dec.rotate(-2)
    print(f"After rotating left: {dec}")
    print("-" * 30)

if __name__ == "__main__":
    demo_counter()
    demo_namedtuple()
    demo_ordered_dict()
    demo_defaultdict()
    demo_deque()
