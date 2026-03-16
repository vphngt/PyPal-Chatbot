import tkinter as tk
import re

# ── Categories ─────────────────────────────────────────────────────────────────
# When a user types a category name, show this overview (no code examples).
categories = {
    "data types": {
        "title": "Data Types",
        "overview": "Python has 4 basic data types. Type the specific one to see details + example.",
        "items": [
            ("int",   "  Whole numbers."),
            ("float", " Decimal numbers."),
            ("str",   "  Text in quotes."),
            ("bool",  "True or False."),
        ]
    },
    "control flow": {
        "title": "Control Flow",
        "overview": "Control flow decides the order your code runs. Type the specific one to see details + example.",
        "items": [
            ("if",         "       Run code only when a condition is True."),
            ("for loop",   "  Repeat for each item in a sequence."),
            ("while loop", "Repeat while a condition stays True."),
        ]
    },
    "searching algorithms": {
        "title": "Searching Algorithms",
        "overview": "Used to find a value inside a list. Type the specific one to see details + example.",
        "items": [
            ("linear search", " O(n), check every item. Works on unsorted data."),
            ("binary search", "O(log n), check middle, discard half. List MUST be sorted."),
        ]
    },
    "sorting algorithms": {
        "title": "Sorting Algorithms",
        "overview": "Used to arrange a list in order. All three below are O(n²). Type the specific one to see details + example.",
        "items": [
            ("bubble sort",    " Swap adjacent pairs, largest bubbles to the end."),
            ("selection sort", "Find minimum, move it to front. 1 swap per pass."),
            ("insertion sort", " Insert one item at a time into sorted position. Best for almost-sorted data."),
        ]
    },
    "data structures": {
        "title": "Data Structures",
        "overview": "Ways to organize and store data. Type the specific one to see details + example.",
        "items": [
            ("list",       "      Ordered, mutable sequence.  [ ]"),
            ("tuple",      "   Ordered, immutable sequence. ( )"),
            ("dictionary", "Key-value pairs. O(1) lookup. { 'key': value }"),
            ("set",        "     Unique unordered elements.   { }"),
            ("stack",      "   LIFO (Last In, First Out)."),
            ("queue",      " FIFO (First In, First Out)."),
        ]
    },
    "oop": {
        "title": "Object-Oriented Programming (OOP)",
        "overview": "OOP organizes code using classes and objects. Type the specific one to see details + example.",
        "items": [
            ("classes",       "      Blueprint for creating objects. Uses __init__ and __str__."),
            ("inheritance",   "   Child class reuses code from a parent class."),
            ("encapsulation", " Hide data inside a class using __ (private)."),
            ("polymorphism",  "Same method name, different behaviour per class."),
        ]
    },
    "user defined": {
        "title": "User-defined Functions",
        "overview": "Reusable blocks of code created by user. Type the specific one to see details + example.",
        "items": [
            ("functions", "Define a function with def, pass params, return values, use defaults."),
            ("scope",     "  Local variables die with the function. Global variables persist."),
            ("recursion", "A function that calls itself. Needs a base case to stop."),
        ]
    },
    "libraries": {
        "title": "Libraries",
        "overview": "Built-in modules you can import. Type 'libraries' to see all at once, or type the module name.",
        "items": [
            ("math",   "sqrt(), ceil(), floor(), pi"),
            ("random", "randint(a,b), choice(list), shuffle(list)"),
            ("numpy",  "Fast arrays and vectorized math operations."),
        ]
    },
}

# ── Concepts (specific topics — show summary + code example) ──────────────────
concepts = {

    "variables": {
        "title": "Variables",
        "summary": "Containers that store values. Python figures out the type automatically.",
        "example": (
            "x = 10          # int\n"
            "pi = 3.14       # float\n"
            "name = 'Alice'  # str\n"
            "passed = True   # bool"
        )
    },

    # Data types
    "int": {
        "title": "Integer",
        "summary": "Whole numbers with no decimal point.",
        "example": (
            "age = 17\n"
            "score = -5\n"
            "print(age + score)   # 12\n"
            "print(type(age))     # <class 'int'>\n"
            "print(10 // 3)       # 3  (floor division)\n"
            "print(10 % 3)        # 1  (remainder)"
        )
    },
    "float": {
        "title": "Float",
        "summary": "Numbers with a decimal point. Used for precision (averages, measurements).",
        "example": (
            "gpa = 3.85\n"
            "pi  = 3.14159\n"
            "print(type(gpa))      # <class 'float'>\n"
            "print(round(pi, 2))   # 3.14\n"
            "print(int(3.9))       # 3   (truncates, does NOT round)\n"
            "print(float(5))       # 5.0"
        )
    },
    "str": {
        "title": "String",
        "summary": "Text enclosed in quotes. Strings are immutable, meaning you can't change a character directly.",
        "example": (
            "name = 'Alice'\n"
            "print(name.upper())           # ALICE   (capital)\n"
            "print(name[0])                # A       (indexing)\n"
            "print(name[1:4])              # lic     (slicing)\n"
            "print(len(name))              # 5\n"
            "# f-string formatting\n"
            "print(f'My name is {name}.')  # My name is Alice."
        )
    },
    "bool": {
        "title": "Boolean",
        "summary": "True or False. Result of comparisons and logical operations.",
        "example": (
            "is_passing = True\n"
            "is_absent = False\n"
            "print(is_passing and is_absent)  # False\n"
            "print(is_passing or is_absent)   # True\n"
            "print(not is_passing)            # False\n"
            "print(10 > 5)                    # True\n"
            "print(10 == 10)                  # True\n"
            "print(10 != 5)                   # True"
        )
    },

    # Operators
    "operators": {
        "title": "Operators",
        "summary": "Arithmetic: + - * / // % **   |   Comparison: == != < > <= >=   |   Logical: and or not",
        "example": (
            "print(10 // 3)             # 3   (floor division)\n"
            "print(10 % 3)              # 1   (remainder)\n"
            "print(2 ** 8)              # 256 (exponent)\n"
            "print(5 == 5)              # True\n"
            "print(5 != 3 and 2 < 4)    # True"
        )
    },

    # Control flow
    "if": {
        "title": "If statement",
        "summary": "Conditional statement. Use if / elif / else.",
        "example": (
            "age = 17\n"
            "if age >= 18:\n"
            "    print('Adult')\n"
            "elif age > 12:\n"
            "    print('Teen')\n"
            "else:\n"
            "    print('Child')"
        )
    },
    "for loop": {
        "title": "For loop",
        "summary": "Repeats for each item in a sequence. Use when you know how many times to loop.",
        "example": (
            "for i in range(5):  # 0 to 4\n"
            "    print(i)\n\n"
            "fruits = ['apple', 'banana']\n"
            "for fruit in fruits:\n"
            "    print(fruit)"
        )
    },
    "while loop": {
        "title": "While loop",
        "summary": "Repeats while a condition is True. Use when you don't know how many times to loop.",
        "example": (
            "count = 0\n"
            "while count < 5:\n"
            "    print(count)\n"
            "    count += 1   # don't forget this or it loops forever!"
        )
    },

    # Functions
    "functions": {
        "title": "Function",
        "summary": "Reusable blocks of code. Define with def, return a value, set defaults in params.",
        "example": (
            "def add(a, b=10):       # b has a default value\n"
            "    return a + b\n\n"
            "print(add(5))           # 15  (uses default b=10)\n"
            "print(add(5, 3))        # 8\n\n"
            "# Keyword argument, order doesn't matter!\n"
            "print(add(b=2, a=3))    # 5"
        )
    },
    "scope": {
        "title": "Scope",
        "summary": "Local: created inside a function, dies when it ends. Global: lives for the whole script.",
        "example": (
            "x = 100       # global\n\n"
            "def show():\n"
            "    y = 5     # local y only exists here\n"
            "    print(x)  # can read global x\n"
            "    print(y)\n\n"
            "show()\n"
            "# print(y)  <-- ERROR! y doesn't exist outside"
        )
    },
    "recursion": {
        "title": "Recursion",
        "summary": "A function that calls itself. MUST have a base case (stopping condition) or it loops forever!",
        "example": (
            "def factorial(n):\n"
            "    if n <= 1: return 1        # base case\n"
            "    return n * factorial(n-1)  # recursive step\n\n"
            "print(factorial(5))            # 120\n\n"
            "def fibonacci(n):\n"
            "    if n <= 1: return n\n"
            "    return fibonacci(n-1) + fibonacci(n-2)\n\n"
            "print(fibonacci(7))            # 13"
        )
    },

    # Libraries
    "libraries": {
        "title": "Libraries",
        "summary": "Built-in modules you can import. Key ones for this class: math, random, numpy.",
        "example": (
            "# STYLE 1: Merged into Local\n"
            "from math import *\n"
            "print(sqrt(25))                  # 5.0\n"
            "print(ceil(4.2))                 # 5\n"
            "print(floor(4.9))                # 4\n\n"
            "# STYLE 2: Reference by dot notation (Safe)\n"
            "import random\n"
            "print(random.randint(1,10))      # random int 1-10\n"
            "print(random.choice(['a','b']))  # random item\n\n"
            "# STYLE 3: Alias import (Efficient)\n"
            "import numpy as np\n"
            "arr = np.array([1, 2, 3])\n"
            "print(arr * 2)                   # [2 4 6]  (vectorized!)"
        )
    },

    # Searching
    "linear search": {
        "title": "Linear Search",
        "summary": "Check every item one by one. Works on unsorted data. O(n), slow for large lists.",
        "example": (
            "def linear_search(lst, target):\n"
            "    for i in range(len(lst)):\n"
            "        if lst[i] == target:\n"
            "            return i             # found at index i\n"
            "    return -1                    # not found\n\n"
            "nums = [4, 2, 7, 1, 9]\n"
            "print(linear_search(nums, 7))    # 2\n"
            "print(linear_search(nums, 99))   # -1"
        )
    },
    "binary search": {
        "title": "Binary Search",
        "summary": "Divide and Conquer: check middle, discard half. O(log n), LIST MUST BE SORTED first!",
        "example": (
            "def binary_search(lst, target):\n"
            "    low, high = 0, len(lst) - 1\n"
            "    while low <= high:\n"
            "        mid = (low + high) // 2\n"
            "        if lst[mid] == target:\n"
            "            return mid\n"
            "        elif lst[mid] < target:\n"
            "            low = mid + 1        # search right half\n"
            "        else:\n"
            "            high = mid - 1       # search left half\n"
            "    return -1\n\n"
            "nums = [1, 3, 5, 7, 9, 11]\n"
            "print(binary_search(nums, 7))    # 3\n"
            "print(binary_search(nums, 6))    # -1"
        )
    },

    # Sorting
    "bubble sort": {
        "title": "Bubble Sort",
        "summary": "Compares adjacent pairs and swaps. Largest value 'bubbles' to the end each pass. O(n²).",
        "example": (
            "def bubble_sort(lst):\n"
            "    n = len(lst)\n"
            "    for i in range(n):\n"
            "        for j in range(n - i - 1):\n"
            "            if lst[j] > lst[j+1]:\n"
            "                lst[j], lst[j+1] = lst[j+1], lst[j]\n"
            "    return lst\n\n"
            "print(bubble_sort([64, 34, 25, 12, 22]))\n"
            "# [12, 22, 25, 34, 64]"
        )
    },
    "selection sort": {
        "title": "Selection Sort",
        "summary": "Finds the minimum in the unsorted part and moves it to the front. Exactly 1 swap per pass. O(n²).",
        "example": (
            "def selection_sort(lst):\n"
            "    for i in range(len(lst)):\n"
            "        min_i = i\n"
            "        for j in range(i+1, len(lst)):\n"
            "            if lst[j] < lst[min_i]:\n"
            "                min_i = j\n"
            "        lst[i], lst[min_i] = lst[min_i], lst[i]\n"
            "    return lst\n\n"
            "print(selection_sort([64, 25, 12, 22, 11]))\n"
            "# [11, 12, 22, 25, 64]"
        )
    },
    "insertion sort": {
        "title": "Insertion Sort",
        "summary": "Picks one item and inserts it into the correct spot. Best for almost-sorted data. O(n²) worst, O(n) best.",
        "example": (
            "def insertion_sort(lst):\n"
            "    for i in range(1, len(lst)):\n"
            "        key = lst[i]\n"
            "        j = i - 1\n"
            "        while j >= 0 and lst[j] > key:\n"
            "            lst[j+1] = lst[j]\n"
            "            j -= 1\n"
            "        lst[j+1] = key\n"
            "    return lst\n\n"
            "print(insertion_sort([12, 11, 13, 5, 6]))\n"
            "# [5, 6, 11, 12, 13]"
        )
    },

    # Data structures
    "list": {
        "title": "List",
        "summary": "Ordered, mutable (changeable) sequence. Index starts at 0.",
        "example": (
            "fruits = ['apple', 'banana', 'cherry']\n"
            "fruits.append('mango')      # add to end\n"
            "fruits.remove('banana')     # remove by value\n"
            "print(fruits[0])            # apple\n"
            "print(fruits[-1])           # last item\n"
            "print(len(fruits))          # 3"
        )
    },
    "tuple": {
        "title": "Tuple",
        "summary": "Similar to a list but immutable (cannot change after creation). Use () instead of [].",
        "example": (
            "point = (10, 20)\n"
            "print(point[0])    # 10\n\n"
            "x, y = point       # unpacking\n"
            "print(x, y)        # 10 20\n\n"
            "# point[0] = 99   <-- TypeError! Tuples can't be changed"
        )
    },
    "dictionary": {
        "title": "Dictionary",
        "summary": "Key-value pairs. O(1) lookup. Keys must be unique and immutable.",
        "example": (
            "student = {'name': 'Alice', 'age': 17}\n\n"
            "print(student['name'])     # Alice\n"
            "student['grade'] = 12      # add new key\n"
            "del student['age']         # remove a key\n\n"
            "for key, val in student.items():\n"
            "    print(key, ':', val)"
        )
    },
    "set": {
        "title": "Set",
        "summary": "Unordered collection of unique elements. Duplicates are removed automatically.",
        "example": (
            "nums = {1, 2, 2, 3, 3}\n"
            "print(nums)    # {1, 2, 3}  duplicates gone!\n\n"
            "a = {1, 2, 3, 4}\n"
            "b = {3, 4, 5, 6}\n"
            "print(a | b)   # Union: {1,2,3,4,5,6}\n"
            "print(a & b)   # Intersection: {3, 4}\n"
            "print(a - b)   # Difference: {1, 2}"
        )
    },
    "stack": {
        "title": "Stack",
        "summary": "LIFO — Last In, First Out. Like a stack of books. .append() to push, .pop() to remove top.",
        "example": (
            "stack = []\n"
            "stack.append('a')      # push\n"
            "stack.append('b')\n"
            "stack.append('c')\n"
            "print(stack.pop())     # 'c' (last in, first out)\n"
            "print(stack)           # ['a', 'b']"
        )
    },
    "queue": {
        "title": "Queue",
        "summary": "FIFO — First In, First Out. Like a checkout line. .append() to add, .pop(0) to remove front.",
        "example": (
            "queue = []\n"
            "queue.append('Alice')    # enqueue\n"
            "queue.append('Bob')\n"
            "queue.append('Charlie')\n"
            "print(queue.pop(0))      # 'Alice' (first in, first out)\n"
            "print(queue)             # ['Bob', 'Charlie']"
        )
    },

    # OOP
    "classes": {
        "title": "Class",
        "summary": "A class is a blueprint. An object is an instance. Use __init__ to set up, __str__ to print nicely.",
        "example": (
            "class Student:\n"
            "    def __init__(self, name, grade):\n"
            "        self.name  = name\n"
            "        self.grade = grade\n\n"
            "    def __str__(self):\n"
            "        return f'{self.name}: {self.grade}%'\n\n"
            "s = Student('Alice', 85)\n"
            "print(s)          # Alice: 85%\n"
            "print(s.name)     # Alice"
        )
    },
    "inheritance": {
        "title": "Inheritance",
        "summary": "Child class gets all attributes and methods from a parent class. Use super() to call the parent's __init__.",
        "example": (
            "class Animal:\n"
            "    def __init__(self, name):\n"
            "        self.name = name\n"
            "    def speak(self): return '...'\n\n"
            "class Dog(Animal):           # inherits Animal\n"
            "    def speak(self):         # overrides speak\n"
            "        return f'{self.name}: Woof!'\n\n"
            "d = Dog('Rex')\n"
            "print(d.speak())             # Rex: Woof!"
        )
    },
    "encapsulation": {
        "title": "Encapsulation",
        "summary": "Hide internal data using __ (private). Only allow access through methods.",
        "example": (
            "class Account:\n"
            "    def __init__(self, balance):\n"
            "        self.__balance = balance   # private\n\n"
            "    def deposit(self, amt):\n"
            "        self.__balance += amt\n\n"
            "    def get_balance(self):\n"
            "        return self.__balance\n\n"
            "acc = Account(1000)\n"
            "acc.deposit(500)\n"
            "print(acc.get_balance())           # 1500\n"
            "# acc.__balance  <-- AttributeError!"
        )
    },
    "polymorphism": {
        "title": "Polymorphism",
        "summary": "Same method name, different behaviour depending on which object calls it.",
        "example": (
            "class Cat:\n"
            "    def speak(self): return 'Meow'\n\n"
            "class Dog:\n"
            "    def speak(self): return 'Woof'\n\n"
            "animals = [Cat(), Dog()]\n"
            "for a in animals:\n"
            "    print(a.speak())   # Meow, then Woof"
        )
    },

    # Big O
    "big o": {
        "title": "Time Complexity",
        "summary": "Measures how runtime grows with input size n (worst case).\nO(1) < O(log n) < O(n) < O(n log n) < O(n²)",
        "example": (
            "O(1)       — dict lookup:    d['key']\n"
            "O(log n)   — binary search\n"
            "O(n)       — linear search, simple loop\n"
            "O(n log n) — merge sort, quick sort\n"
            "O(n²)      — bubble / selection / insertion sort\n\n"
            "# Nested loop = O(n²)\n"
            "for i in lst:\n"
            "    for j in lst:\n"
            "        print(i, j)"
        )
    },
}

# ── Category aliases (these trigger the overview, not a concept) ───────────────
category_aliases = {
    "data type":           "data types",
    "types":               "data types",
    "type":                "data types",
    "basic types":         "data types",
    "search":              "searching algorithms",
    "searching":           "searching algorithms",
    "search algorithms":   "searching algorithms",
    "sort":                "sorting algorithms",
    "sorting":             "sorting algorithms",
    "sort algorithms":     "sorting algorithms",
    "sorts":               "sorting algorithms",
    "structure":           "data structures",
    "data structure":      "data structures",
    "collections":         "data structures",
    "object oriented":     "oop",
    "object-oriented":     "oop",
    "oops":                "oop",
    "user-defined":        "user defined",
    "udf":                 "user defined",
    "control":             "control flow",
    "conditions":          "control flow",
    "loops":               "control flow",
    "function":            "functions",   # plural category
    "lib":                 "libraries",
    "modules":             "libraries",
}

# ── Concept aliases (these trigger a specific concept with example) ────────────
concept_aliases = {
    "variable":    "variables",
    "integer":     "int",  "whole number": "int",
    "decimal":     "float", "double": "float",
    "string":      "str",  "text": "str",
    "boolean":     "bool", "true": "bool", "false": "bool",
    "operator":    "operators",
    "if statement":"if",   "elif": "if", "else": "if", "condition": "if",
    "for":         "for loop",
    "while":       "while loop",
    "def":         "functions", "return": "functions",
    "parameter":   "functions", "argument": "functions", "default": "functions",
    "local":       "scope",  "global": "scope",
    "recursive":   "recursion", "factorial": "recursion", "fibonacci": "recursion",
    "library":     "libraries", "module": "libraries", "import": "libraries",
    "math":        "libraries", "random": "libraries", "numpy": "libraries",
    "linear":      "linear search",
    "binary":      "binary search",
    "bubble":      "bubble sort",
    "selection":   "selection sort",
    "insertion":   "insertion sort",
    "lists":       "list",  "array": "list",
    "tuples":      "tuple",
    "dict":        "dictionary", "dictionaries": "dictionary", "key value": "dictionary",
    "sets":        "set",
    "lifo":        "stack",
    "fifo":        "queue",
    "object":      "classes", "objects": "classes", "class": "classes",
    "inheritance": "inheritance", "inherit": "inheritance",
    "encapsulation": "encapsulation", "encapsulate": "encapsulation",
    "polymorphism":  "polymorphism", "polymorph":  "polymorphism",
    "abstraction":   "oop",
    "big o notation":"big o", "complexity": "big o",
    "time complexity":"big o", "o(n)": "big o", "o(1)": "big o",
}

INSTRUCTIONS = """HOW TO USE PyPal
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Suggested Prompts

TYPE A CATEGORY: get a brief overview.
TYPE A SPECIFIC TOPIC: get a definition + code example.

   Data types              →  int  float  str  bool
   Variables
   Operators
   Control flow             →  if  for loop  while loop
   UDF                       →  functions  scope  recursion
   Libraries                 →  numpy math random
   Searching               →  linear search  binary search
   Sorting                   →  bubble sort  selection sort  insertion sort
   Big O Notation
   Data structures       →  list  tuple  dictionary  set  stack  queue
   OOP                      →  classes  inheritance  encapsulation  polymorphism

TYPE A COMMAND:

   clear  — clear chat history
   help   — show instructions
   exit   — exit the chatbot

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ── Lookup logic ───────────────────────────────────────────────────────────────
def find_response(user_input):
    q = user_input.strip().lower()

    # 1. Exact category match
    if q in categories:
        return ("category", categories[q])

    # 2. Category alias match
    if q in category_aliases:
        key = category_aliases[q]
        if key in categories:
            return ("category", categories[key])

    # 3. Exact concept match
    if q in concepts:
        return ("concept", concepts[q])

    # 4. Concept alias match
    if q in concept_aliases:
        key = concept_aliases[q]
        if key in concepts:
            return ("concept", concepts[key])
    
    # 5. Keyword match
    for key in concepts:
        if re.search(rf'\b{re.escape(key)}\b', q):
            return ("concept", concepts[key])
        if re.search(rf'\b{re.escape(q)}\b', key):
            return ("concept", concepts[key])
    return ("none", None)

    return ("none", None)


# ── GUI ────────────────────────────────────────────────────────────────────────
PURPLE  = "#6c4ab6"
LIGHT_P = "#ede8f8"
CODE_BG = "#0d1117"
CODE_FG = "#e6edf3"
WHITE   = "#ffffff"
DARK    = "#2d2540"
MUTED   = "#777777"
RED     = "#cc4444"
GREEN   = "#2e7d32"

root = tk.Tk()
root.title("Welcome")
root.geometry("800x600")
root.configure(bg=LIGHT_P)

# Header
hdr = tk.Frame(root, bg=PURPLE, pady=10)
hdr.pack(fill="x")
tk.Label(hdr, text="PyPal - Your Python Study Pal",
         font=("Helvetica", 15, "bold"), fg=WHITE, bg=PURPLE).pack(side="left", padx=16)
tk.Label(hdr, text="Grade 12 CS — ICS4U",
         font=("Helvetica", 10), fg="#c8b8f0", bg=PURPLE).pack(side="right", padx=16)

# Chat display
chat_frame = tk.Frame(root, bg=LIGHT_P)
chat_frame.pack(fill="both", expand=True, padx=12, pady=(8, 0))

scrollbar = tk.Scrollbar(chat_frame)
scrollbar.pack(side="right", fill="y")

chat_box = tk.Text(
    chat_frame, yscrollcommand=scrollbar.set,
    state="disabled", wrap="word",
    bg=WHITE, fg=DARK, relief="flat", bd=0,
    font=("Helvetica", 12), padx=14, pady=10,
    cursor="arrow"
)
chat_box.pack(fill="both", expand=True)
scrollbar.config(command=chat_box.yview)

# Text tags
chat_box.tag_config("bot_label",    foreground=PURPLE,  font=("Helvetica", 11, "bold"))
chat_box.tag_config("user_label",   foreground="#3a7bd5",font=("Helvetica", 11, "bold"))
chat_box.tag_config("summary",      foreground=DARK,    font=("Helvetica", 11))
chat_box.tag_config("cat_title",    foreground=DARK,  font=("Helvetica", 11, "bold"))
chat_box.tag_config("cat_item",     foreground=GREEN,   font=("Helvetica", 11, "bold"))
chat_box.tag_config("cat_desc",     foreground=DARK,    font=("Helvetica", 11))
chat_box.tag_config("code",         foreground=CODE_FG, background=CODE_BG,
                    font=("Courier New", 11), lmargin1=10, lmargin2=10, spacing1=4, spacing3=6)
chat_box.tag_config("error",        foreground=RED,     font=("Helvetica", 11, "italic"))
chat_box.tag_config("hint",         foreground=MUTED,   font=("Helvetica", 10, "italic"))
chat_box.tag_config("divider",      foreground="#cccccc")

def append(text, tag="summary"):
    chat_box.config(state="normal")
    chat_box.insert("end", text, tag)
    chat_box.config(state="disabled")
    chat_box.see("end")

# ── Display helpers ────────────────────────────────────────────────────────────
def show_welcome():
    append("PyPal  ", "bot_label")
    append("Hi! Type any concept covered in class and I'll help you revise! ദ്ദി(ᵔᗜᵔ)\n", "summary")
    append("Click  Instructions  to see how to search.\n\n", "hint")

def show_category(query, data):
    append("You  ",   "user_label")
    append(f"{query}\n\n", "summary")
    append("PyPal  ", "bot_label")
    append(f"{data['title']}\n", "cat_title")
    append(f"{data['overview']}\n\n", "hint")
    for name, desc in data["items"]:
        append(f"  {name:<20}", "cat_item")
        append(f"{desc}\n", "cat_desc")
    append("\n" + "─" * 60 + "\n\n", "divider")

def show_concept(query, data):
    append("You  ", "user_label")
    append(f"{query}\n\n", "summary")
    append("PyPal  ", "bot_label")
    append(f"{data['title']}\n", "cat_title")
    append(f"{data['summary']}\n\n", "summary")
    chat_box.config(state="normal")
    code_text = data["example"]
    # header frame
    header_frame = tk.Frame(chat_box, bg="#0d1117")
    header_frame.columnconfigure(0, weight=1)
    lang_label = tk.Label(
        header_frame,
        text=" python",
        bg="#0d1117",
        fg="#a855f7",
        font=("Courier New", 9, "bold")
    )
    lang_label.grid(row=0, column=0, sticky="w", padx=6, pady=3)
    copy_text = tk.StringVar(value=" Copy ")
    def do_copy():
        root.clipboard_clear()
        root.clipboard_append(code_text)
        copy_text.set(" Copied! ")
        # reset after 2 seconds
        root.after(2000, lambda: copy_text.set(" Copy "))
    copy_btn = tk.Button(
        header_frame,
        textvariable=copy_text,
        font=("Courier New", 8, "bold"),
        bg="#21262d",
        fg="white",
        relief="flat",
        cursor="hand2",
        command=do_copy
    )
    copy_btn.grid(row=0, column=1, sticky="e", padx=6)
    chat_box.window_create("end", window=header_frame)
    chat_box.insert("end", "\n")
    # code block
    chat_box.insert("end", code_text + "\n", "code")
    chat_box.config(state="disabled")
    append("\n" + "─" * 60 + "\n\n", "divider")

def show_error(query):
    append("You  ",   "user_label")
    append(f"{query}\n\n", "summary")
    append("PyPal  ", "bot_label")
    append(f"Hmmm, I can't find any notes for '{query}' (ó﹏ò｡) Check  Instructions  to learn more.\n\n", "error")

def show_instructions():
    append("PyPal  ", "bot_label")
    append(INSTRUCTIONS + "\n", "hint")

def clear_chat():
    chat_box.config(state="normal")
    chat_box.delete("1.0", "end")
    chat_box.config(state="disabled")
    show_welcome()

# ── Send logic ─────────────────────────────────────────────────────────────────
def send(event=None):
    raw = entry.get().strip()
    if not raw: return
    entry.delete(0, "end")
    q = raw.lower()

    if q == "exit":
        root.destroy()
        return
    if q == "clear":
        clear_chat()
        return
    if q == "help":
        show_instructions()
        return

    kind, data = find_response(q)
    if kind == "category":
        show_category(raw, data)
    elif kind == "concept":
        show_concept(raw, data)
    else:
        show_error(raw)

# ── Input bar ──────────────────────────────────────────────────────────────────
input_frame = tk.Frame(root, bg=LIGHT_P, pady=10, padx=12)
input_frame.pack(fill="x")

entry = tk.Entry(
    input_frame, font=("Helvetica", 13), fg=DARK, bg=WHITE,
    relief="flat", bd=0, insertbackground=PURPLE,
    highlightthickness=2, highlightbackground="#c8b8f0", highlightcolor=PURPLE
)
entry.pack(side="left", fill="x", expand=True, ipady=8, ipadx=10, padx=(0, 10))
entry.bind("<Return>", send)
entry.focus()

tk.Button(
    input_frame, text="Exit",
    font=("Helvetica", 11, "bold"), fg=WHITE, bg=RED,
    relief="flat", padx=12, pady=8,
    activebackground="#aa2222", activeforeground=WHITE,
    cursor="hand2", command=root.destroy
).pack(side="right")

tk.Button(
    input_frame, text="Instructions",
    font=("Helvetica", 11, "bold"), fg=PURPLE, bg=WHITE,
    relief="flat", padx=12, pady=8,
    activebackground=LIGHT_P, cursor="hand2",
    command=show_instructions
).pack(side="right", padx=(0, 6))

tk.Button(
    input_frame, text="Send",
    font=("Helvetica", 11, "bold"), fg=WHITE, bg=PURPLE,
    relief="flat", padx=18, pady=8,
    activebackground="#5a3a9a", activeforeground=WHITE,
    cursor="hand2", command=send
).pack(side="right", padx=(0, 6))

show_welcome()
root.mainloop()
