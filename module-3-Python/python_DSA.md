# Python DSA:


## Contents

1. [Quick Comparison of All 4](#quick-comparison-of-all-4)
2. [List](#part-1-list)
3. [Tuple](#part-2-tuple)
4. [Set](#part-3-set)
5. [Dictionary](#part-4-dictionary)

---

# Quick Comparison of All 4

| | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Brackets | `[ ]` | `( )` | `{ }` | `{ key: value }` |
| Ordered | Yes | Yes | No | Yes (insertion order, 3.7+) |
| Indexing | Yes | Yes | No | By key |
| **Slicing** | **Yes** | **Yes** | **No** | **No** |
| Duplicates | Allowed | Allowed | Not allowed | Keys unique, values can repeat |
| Mutable | Yes | No | Yes | Yes |
| Number of methods | 11 | 2 | 17 | 11 |
| Best for | Ordered, changeable data | Fixed data, dictionary keys | Unique values, fast lookup, set math | Lookups, counting, grouping |

---

# Part 1: List

## What is a List?

A **list** is a container that stores multiple values in one variable, in a specific order.

```python
marks = [85, 90, 78]
names = ["Kalpit", "Rahul", "Amit"]
mixed = [1, "hello", 3.5, True]   # different types are allowed
```

## Key Features

| Feature | Meaning |
|---|---|
| **Ordered** | Items keep their position (`marks[0]` is always 85) |
| **Indexed** | Access by position, starting from 0 (`marks[-1]` is the last) |
| **Mutable** | You can change, add or remove items after creating it |
| **Allows duplicates** | `[1, 2, 2, 3]` is valid |
| **Any data type** | Numbers, strings, even other lists |
| **Written with `[ ]`** | Items are separated by commas |

```python
marks = [85, 90, 78]
marks[1] = 95        # change an item
print(marks)         # [85, 95, 78]
```

## Types of List Methods (11 methods, 5 groups)

| Type | Purpose | Methods |
|---|---|---|
| **1. Adding** | Put new items in | `append()`, `extend()`, `insert()` |
| **2. Removing** | Take items out | `remove()`, `pop()`, `clear()` |
| **3. Searching** | Find or count items | `index()`, `count()` |
| **4. Ordering** | Change the order | `sort()`, `reverse()` |
| **5. Copying** | Make a duplicate | `copy()` |

### 1. Adding

**`append(x)`** adds one item at the end.
```python
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)   # ['apple', 'banana', 'mango']
```

**`extend(iterable)`** adds all items of another list (or any iterable) at the end.
```python
a = [1, 2]
a.extend([3, 4])
print(a)        # [1, 2, 3, 4]
```

**`insert(i, x)`** adds `x` at position `i`.
```python
a = [10, 30, 40]
a.insert(1, 20)
print(a)        # [10, 20, 30, 40]
```

### 2. Removing

**`remove(x)`** removes the first matching value. It raises an error if the value isn't found.
```python
a = [5, 8, 5, 9]
a.remove(5)
print(a)        # [8, 5, 9]
```

**`pop(i)`** removes the item at index `i` and returns it. With no index, it removes the last item.
```python
a = [10, 20, 30]
x = a.pop()     # x = 30
y = a.pop(0)    # y = 10
print(a)        # [20]
```

**`clear()`** removes everything.
```python
a = [1, 2, 3]
a.clear()
print(a)        # []
```

### 3. Searching

**`index(x)`** returns the position of the first match. It raises an error if the value isn't found.
```python
a = ["a", "b", "c", "b"]
print(a.index("b"))      # 1
print(a.index("b", 2))   # 3 (search starts from index 2)
```

**`count(x)`** returns how many times `x` appears.
```python
a = [1, 2, 2, 3, 2]
print(a.count(2))   # 3
```

### 4. Ordering

**`sort()`** sorts the list in place.
```python
a = [30, 10, 20]
a.sort()
print(a)                    # [10, 20, 30]
a.sort(reverse=True)
print(a)                    # [30, 20, 10]

words = ["pear", "fig", "banana"]
words.sort(key=len)
print(words)                # ['fig', 'pear', 'banana']
```

**`reverse()`** reverses the order in place.
```python
a = [1, 2, 3]
a.reverse()
print(a)        # [3, 2, 1]
```

### 5. Copying

**`copy()`** returns a new list with the same items.
```python
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)        # [1, 2, 3] (unchanged)
print(b)        # [1, 2, 3, 4]
```

## Common List Mistakes

```python
a = [3, 1, 2]
a = a.sort()
print(a)        # None, because sort() changes the list and returns nothing
```

```python
a = [1, 2]
a.append([3, 4])   # [1, 2, [3, 4]]   (one nested list)
a.extend([5, 6])   # [1, 2, [3, 4], 5, 6]
```

```python
b = a              # not a copy, both names point to the same list
b = a.copy()       # use this (or a[:]) for a real copy
```

## Remember the List Methods

- **Add:** `append`, `extend`, `insert`
- **Remove:** `remove`, `pop`, `clear`
- **Find:** `index`, `count`
- **Arrange:** `sort`, `reverse`
- **Duplicate:** `copy`

---

# Part 2: Tuple

## What is a Tuple?

A **tuple** is like a list, but **immutable**: once created, its items cannot be changed, added or removed.

```python
point = (10, 20)
days = ("Mon", "Tue", "Wed")
mixed = (1, "hello", 3.5, True)
```

## Key Features

| Feature | Meaning |
|---|---|
| **Ordered** | Items keep their position |
| **Indexed** | Access by position, starting from 0 (`days[0]`, `days[-1]`) |
| **Immutable** | You cannot change, add or remove items after creating it |
| **Allows duplicates** | `(1, 2, 2, 3)` is valid |
| **Any data type** | Numbers, strings, even lists |
| **Written with `( )`** | Items are separated by commas |
| **Hashable** | A tuple of immutable items can be a dictionary key or a set item |

```python
days = ("Mon", "Tue", "Wed")
print(days[1])        # Tue
print(days[-1])       # Wed
days[0] = "Sun"       # TypeError: tuple does not support item assignment
```

**Single-item tuple needs a comma:**
```python
a = (5,)     # tuple
b = (5)      # just the integer 5
print(type(a), type(b))   # <class 'tuple'> <class 'int'>
```

## Packing and Unpacking

```python
person = ("Kalpit", 21, "Porbandar")   # packing
name, age, city = person               # unpacking
print(name, age, city)                 # Kalpit 21 Porbandar

a, b = 1, 2
a, b = b, a                            # swap values
print(a, b)                            # 2 1

first, *rest = (1, 2, 3, 4)
print(first, rest)                     # 1 [2, 3, 4]
```

## Types of Tuple Methods (only 2 methods)

Because tuples cannot change, they have just two methods, both for **searching**:

| Type | Purpose | Methods |
|---|---|---|
| **Searching** | Find or count items | `count()`, `index()` |

**`count(x)`** returns how many times `x` appears.
```python
t = (1, 2, 2, 3, 2)
print(t.count(2))    # 3
```

**`index(x)`** returns the position of the first match. It raises an error if the value isn't found.
```python
t = ("a", "b", "c", "b")
print(t.index("b"))       # 1
print(t.index("b", 2))    # 3
```

## Useful Built-ins with Tuples

```python
t = (30, 10, 20)
len(t)          # 3
min(t)          # 10
max(t)          # 30
sum(t)          # 60
sorted(t)       # [10, 20, 30]  (returns a LIST, original tuple unchanged)
20 in t         # True
t + (40, 50)    # (30, 10, 20, 40, 50)  (new tuple)
t * 2           # (30, 10, 20, 30, 10, 20)
```

## How to "Change" a Tuple

Convert to a list, change it, convert back:
```python
t = (1, 2, 3)
temp = list(t)
temp.append(4)
t = tuple(temp)
print(t)        # (1, 2, 3, 4)
```

## Common Tuple Mistakes

```python
t = (1, 2, 3)
t.append(4)          # AttributeError, tuples have no append()
```

```python
t = (1, [2, 3])
t[1].append(4)       # works! the list INSIDE can change
print(t)             # (1, [2, 3, 4])
```

## Why Use a Tuple?

- **Safe data:** values that should never change (coordinates, RGB colors, dates).
- **Faster and lighter** than a list.
- **Dictionary keys:** `{(1, 2): "A"}` works, but a list key does not.
- **Returning multiple values** from a function.

---

# Part 3: Set

## What is a Set?

A **set** is an **unordered** collection of **unique** items. Duplicates are removed automatically.

```python
nums = {1, 2, 3, 3, 2}
print(nums)          # {1, 2, 3}

teams = {"RCB", "MI", "CSK"}
```

## Key Features

| Feature | Meaning |
|---|---|
| **Unordered** | No fixed position, so no indexing (`s[0]` is an error) |
| **Unique items** | Duplicates are removed automatically |
| **Mutable** | You can add and remove items |
| **Items must be hashable** | Numbers, strings and tuples are fine. Lists and dicts are not |
| **Fast lookup** | `x in s` is O(1) on average |
| **Written with `{ }`** | Items are separated by commas |

**Empty set trap:**
```python
a = {}          # this is an empty DICTIONARY
b = set()       # this is an empty SET
print(type(a), type(b))   # <class 'dict'> <class 'set'>
```

**Remove duplicates from a list:**
```python
data = [1, 2, 2, 3, 3, 3]
unique = list(set(data))
print(unique)   # [1, 2, 3]
```

## Types of Set Methods (17 methods, 6 groups)

| Type | Purpose | Methods |
|---|---|---|
| **1. Adding** | Put new items in | `add()`, `update()` |
| **2. Removing** | Take items out | `remove()`, `discard()`, `pop()`, `clear()` |
| **3. Set operations (new set)** | Combine sets, return a new set | `union()`, `intersection()`, `difference()`, `symmetric_difference()` |
| **4. Set operations (in place)** | Same as above but change the original set | `intersection_update()`, `difference_update()`, `symmetric_difference_update()` |
| **5. Checking** | Compare two sets, return True/False | `issubset()`, `issuperset()`, `isdisjoint()` |
| **6. Copying** | Make a duplicate | `copy()` |

### 1. Adding

**`add(x)`** adds one item. If it already exists, nothing happens.
```python
s = {1, 2}
s.add(3)
s.add(2)
print(s)        # {1, 2, 3}
```

**`update(iterable)`** adds many items at once.
```python
s = {1, 2}
s.update([3, 4], {5})
print(s)        # {1, 2, 3, 4, 5}
```

### 2. Removing

**`remove(x)`** removes the item. It raises `KeyError` if the item is missing.
```python
s = {1, 2, 3}
s.remove(2)
print(s)        # {1, 3}
```

**`discard(x)`** removes the item. It raises no error if the item is missing.
```python
s = {1, 2, 3}
s.discard(99)   # no error
print(s)        # {1, 2, 3}
```

**`pop()`** removes and returns a random item (sets are unordered).
```python
s = {10, 20, 30}
x = s.pop()
print(x, s)
```

**`clear()`** removes everything.
```python
s = {1, 2, 3}
s.clear()
print(s)        # set()
```

### 3. Set Operations (return a new set)

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

**`union(b)`** (or `a | b`) has all items from both.
```python
print(a.union(b))                  # {1, 2, 3, 4, 5, 6}
```

**`intersection(b)`** (or `a & b`) has only the common items.
```python
print(a.intersection(b))           # {3, 4}
```

**`difference(b)`** (or `a - b`) has items in `a` but not in `b`.
```python
print(a.difference(b))             # {1, 2}
```

**`symmetric_difference(b)`** (or `a ^ b`) has items in either set but not in both.
```python
print(a.symmetric_difference(b))   # {1, 2, 5, 6}
```

### 4. Set Operations (in place)

These do the same jobs, but change the original set and return `None`.

```python
a = {1, 2, 3, 4}
a.intersection_update({3, 4, 5})
print(a)        # {3, 4}

a = {1, 2, 3, 4}
a.difference_update({3, 4})
print(a)        # {1, 2}

a = {1, 2, 3, 4}
a.symmetric_difference_update({3, 4, 5})
print(a)        # {1, 2, 5}
```

### 5. Checking

```python
a = {1, 2}
b = {1, 2, 3, 4}
c = {8, 9}
```

**`issubset(x)`** is True if every item of `a` is in `x`.
```python
print(a.issubset(b))      # True
```

**`issuperset(x)`** is True if `a` contains every item of `x`.
```python
print(b.issuperset(a))    # True
```

**`isdisjoint(x)`** is True if the two sets have nothing in common.
```python
print(a.isdisjoint(c))    # True
print(a.isdisjoint(b))    # False
```

### 6. Copying

**`copy()`** returns a shallow copy.
```python
a = {1, 2, 3}
b = a.copy()
b.add(4)
print(a)        # {1, 2, 3} (unchanged)
print(b)        # {1, 2, 3, 4}
```

## Common Set Mistakes

```python
s = {1, 2, 3}
print(s[0])             # TypeError, sets have no index
```

```python
s = {[1, 2], 3}         # TypeError, a list is not hashable
s = {(1, 2), 3}         # works, a tuple is hashable
```

```python
s = {3, 1, 2}
s.add(4)
print(s)                # order is not guaranteed, so never rely on it
```

## Frozenset (immutable set)

```python
fs = frozenset([1, 2, 3])
# fs.add(4) -> AttributeError
```
Use it when you need a set that can be a dictionary key or a set item.

## Remember the Set Methods

- **Add:** `add`, `update`
- **Remove:** `remove`, `discard`, `pop`, `clear`
- **Combine (new set):** `union`, `intersection`, `difference`, `symmetric_difference`
- **Combine (in place):** `intersection_update`, `difference_update`, `symmetric_difference_update`
- **Check:** `issubset`, `issuperset`, `isdisjoint`
- **Duplicate:** `copy`

---

# Part 4: Dictionary

## What is a Dictionary?

A **dictionary** stores data as **key → value pairs**. You look up a value by its key, not by position.

```python
student = {"name": "Kalpit", "age": 21, "city": "Porbandar"}
print(student["name"])   # Kalpit
```

## Key Features

| Feature | Meaning |
|---|---|
| **Key-value pairs** | Each item is `key: value` |
| **Keys are unique** | A repeated key overwrites the old value |
| **Keys must be immutable** | Strings, numbers and tuples work. Lists and dicts can't be keys |
| **Values can be anything** | Numbers, strings, lists, even other dicts |
| **Mutable** | You can add, change or remove pairs |
| **Ordered** | Keeps insertion order (Python 3.7+) |
| **Written with `{ }`** | Pairs separated by commas, `key: value` |

```python
student["age"] = 22          # change a value
student["marks"] = 88        # add a new pair
del student["city"]          # delete a pair
print(student)               # {'name': 'Kalpit', 'age': 22, 'marks': 88}
```

## Types of Dictionary Methods (11 methods, 4 groups)

| Type | Purpose | Methods |
|---|---|---|
| **1. Accessing** | Read keys and values | `get()`, `keys()`, `values()`, `items()` |
| **2. Adding / Updating** | Put in new pairs or change them | `update()`, `setdefault()`, `fromkeys()` |
| **3. Removing** | Take pairs out | `pop()`, `popitem()`, `clear()` |
| **4. Copying** | Make a duplicate | `copy()` |

### 1. Accessing

**`get(key, default)`** returns the value, or the default if the key is missing. It never raises an error.
```python
d = {"name": "Kalpit", "age": 21}
print(d.get("name"))          # Kalpit
print(d.get("city"))          # None
print(d.get("city", "N/A"))   # N/A
# d["city"] would raise KeyError
```

**`keys()`** returns all keys.
```python
print(d.keys())     # dict_keys(['name', 'age'])
```

**`values()`** returns all values.
```python
print(d.values())   # dict_values(['Kalpit', 21])
```

**`items()`** returns all (key, value) pairs, mostly used in loops.
```python
for k, v in d.items():
    print(k, "->", v)
# name -> Kalpit
# age -> 21
```

### 2. Adding / Updating

**`update(other)`** merges another dict in. Existing keys are overwritten, new keys are added.
```python
d = {"a": 1, "b": 2}
d.update({"b": 20, "c": 3})
print(d)            # {'a': 1, 'b': 20, 'c': 3}
```

**`setdefault(key, default)`** returns the value if the key exists. If not, it adds the key with the default and returns that.
```python
d = {"a": 1}
d.setdefault("a", 99)   # 1 (unchanged)
d.setdefault("b", 2)    # adds 'b': 2
print(d)                # {'a': 1, 'b': 2}

groups = {}
groups.setdefault("RCB", []).append("Kohli")   # handy for grouping
```

**`fromkeys(keys, value)`** creates a new dict from a list of keys, all with the same value.
```python
d = dict.fromkeys(["x", "y", "z"], 0)
print(d)            # {'x': 0, 'y': 0, 'z': 0}
```

### 3. Removing

**`pop(key)`** removes the key and returns its value. You can give a default to avoid an error.
```python
d = {"a": 1, "b": 2}
x = d.pop("a")          # x = 1
d.pop("zzz", None)      # no error because a default was given
print(d)                # {'b': 2}
```

**`popitem()`** removes and returns the last inserted pair as a tuple.
```python
d = {"a": 1, "b": 2, "c": 3}
print(d.popitem())      # ('c', 3)
print(d)                # {'a': 1, 'b': 2}
```

**`clear()`** removes everything.
```python
d.clear()
print(d)                # {}
```

### 4. Copying

**`copy()`** returns a shallow copy.
```python
a = {"x": 1}
b = a.copy()
b["x"] = 100
print(a)    # {'x': 1} (unchanged)
```

## Common Dictionary Mistakes

```python
d = {"a": 1}
print(d["b"])         # KeyError, so use d.get("b") instead
```

```python
d = {"a": 1}
e = d                 # not a copy, both names point to the same dict
e["a"] = 5
print(d)              # {'a': 5}, so use d.copy()
```

## Remember the Dictionary Methods

- **Read:** `get`, `keys`, `values`, `items`
- **Add or change:** `update`, `setdefault`, `fromkeys`
- **Remove:** `pop`, `popitem`, `clear`
- **Duplicate:** `copy`
