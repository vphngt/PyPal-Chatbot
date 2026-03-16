# PyPal — Your Python Study Pal

PyPal is a desktop-based revision chatbot designed to help ICS4U students master Python concepts. Built using Python's `tkinter` library, it acts as an interactive cheat sheet by providing instant definitions, logical overviews, and code examples for a wide range of topics, from basic data types to complex Object-Oriented Programming (OOP) principles.
 
---

## 🚀 Features
 
- **Hierarchical Keyword Search**
  - **Category Search** — Enter a broad category (e.g., `data structures`) to receive a high-level overview of all sub-topics.
  - **Topic Search** — Enter a specific term (e.g., `bool` or `bubble sort`) for a detailed definition and code example.
 
- **Intuitive Dark UI** — A clean, navy-themed interface with dedicated buttons for `Send`, `Instructions`, `Clear`, and `Exit`.
 
- **Code Snippet Integration** — Every code example includes a built-in **Copy** button, allowing students to instantly test snippets in their own IDE.
 
- **Terminal-Style Commands** — Supports direct commands typed in the chat bar:
 
  | Command | Description |
  |---------|-------------|
  | `help`  | Displays navigation instructions |
  | `clear` | Wipes the current chat history for a fresh start |
  | `quit`  | Safely exits the application |
 
- **Smart Error Handling** — Displays a friendly *"keyword not found"* message to guide users back to supported topics.
 
---
 
## 🛠️ Technical Stack
 
| Component     | Details                          |
|---------------|----------------------------------|
| Language      | Python 3.x                       |
| GUI Framework | `tkinter` (standard library)     |
| Regex Matching| `re` module — word-boundary safe |
| No installs   | Runs out of the box              |
 
---
 
## 📂 Supported Topics
 
| Category            | Specific Topics                                        |
|---------------------|--------------------------------------------------------|
| Data Types          | `int`, `float`, `str`, `bool`                          |
| Control Flow        | `if`, `for loop`, `while loop`                         |
| User-Defined Functions | `functions`, `scope`, `recursion`                   |
| Libraries           | `math`, `random`, `numpy`                              |
| Searching Algorithms| `linear search`, `binary search`                       |
| Sorting Algorithms  | `bubble sort`, `selection sort`, `insertion sort`      |
| Data Structures     | `list`, `tuple`, `dictionary`, `set`, `stack`, `queue` |
| OOP                 | `classes`, `inheritance`, `encapsulation`, `polymorphism` |
| Other               | `variables`, `operators`, `big o`                      |
 
---
 
## ▶️ How to Run
 
```bash
python pypal.py
```
 
> No external libraries required. `tkinter` and `re` are both part of Python's standard library.
 
---
 
## 📸 Screenshots
 
> Add your screenshots here.
 
```
![Welcome Screen](screenshots/welcome.png)
![Code Example](screenshots/code_example.png)
```
 
---
 
## 💡 How It Works
 
PyPal uses a **two-tier lookup system**:
 
1. **Exact match** — checks if the input matches a known category or topic directly.
2. **Alias match** — maps common variations (e.g., `"dict"` → `dictionary`, `"lifo"` → `stack`).
3. **Word-boundary regex match** — uses Python's `re` module with `\b` anchors to catch partial inputs like `"bubble"` matching `"bubble sort"`, while preventing false matches (e.g., `"hi"` incorrectly matching `"while"`).
 
If none of the above match, PyPal returns a friendly error message.
 
