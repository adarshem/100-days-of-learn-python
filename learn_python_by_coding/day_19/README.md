# Python Class Instances, State, and Higher-Order Functions

## Class Instances and State

### 1. Defining a Class and Creating Instances
- A class is a blueprint for creating objects.
- **Example:**
  ```python
  class Dog:
      def __init__(self, name):
          self.name = name
      def bark(self):
          return f"{self.name} says woof!"
  
  my_dog = Dog("Buddy")
  print(my_dog.bark())
  ```

### 2. State and Instance Variables
- Instance variables store data unique to each instance.
- The `self` keyword refers to the instance.
- **Example:**
  ```python
  class Counter:
      def __init__(self):
          self.count = 0
      def increment(self):
          self.count += 1
          return self.count
  
  c = Counter()
  print(c.increment())
  ```

## Higher-Order Functions

### 3. Functions as First-Class Citizens
- Functions can be passed as arguments, returned from functions, and assigned to variables.
- **Example:**
  ```python
  def greet(name):
      return f"Hello, {name}!"
  
  def process(func, name):
      return func(name)
  
  print(process(greet, "Alice"))
  ```

### 4. Using `map`, `filter`, and `reduce`
- **`map(func, iterable)`** applies a function to all items.
- **`filter(func, iterable)`** filters items based on a condition.
- **`reduce(func, iterable)`** reduces an iterable to a single value.
- **Example:**
  ```python
  from functools import reduce
  
  nums = [1, 2, 3, 4]
  squared = list(map(lambda x: x ** 2, nums))
  evens = list(filter(lambda x: x % 2 == 0, nums))
  total = reduce(lambda x, y: x + y, nums)
  
  print(squared, evens, total)
  ```

## Conclusion
- Use classes to define objects with **state** (instance variables and methods).
- **Higher-order functions** help write concise, reusable code.
- Functions can be **passed** and **returned** just like variables.

---

### Need More Help?
If you have any questions or need further explanations, feel free to reach out! 🚀

