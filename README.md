# Python String Methods - Complete Reference

## Basic String Manipulation

### 1. `capitalize()`
Returns a copy of the string with its first character capitalized and the rest lowercased.
```python
text = "hello world"
print(text.capitalize())  # "Hello world"
```

### 2. `casefold()`
Returns a casefolded copy of the string, suitable for case-insensitive comparisons. More aggressive than `lower()`.
```python
text = "Großß"
print(text.casefold())  # "grosss"
print(text.lower())     # "großß"
```

### 3. `center(width[, fillchar])`
Returns a centered string of specified width with optional fill character (spaces by default).
```python
text = "python"
print(text.center(10))      # "  python  "
print(text.center(10, "*")) # "**python**"
```

### 4. `count(sub[, start[, end]])`
Returns the number of occurrences of a substring within the string, optionally restricting the search to a slice.
```python
text = "banana"
print(text.count("a"))    # 3
print(text.count("a", 2)) # 2 (only counts from position 2 onward)
```

### 5. `encode([encoding[, errors]])`
Returns an encoded version of the string as a bytes object.
```python
text = "pythön"
print(text.encode())           # b'pyth\xc3\xb6n'
print(text.encode("ascii", "ignore")) # b'pythn'
```

### 6. `endswith(suffix[, start[, end]])`
Returns `True` if the string ends with the specified suffix, optionally restricting the matching to a slice.
```python
text = "hello.txt"
print(text.endswith(".txt"))  # True
print(text.endswith("lo", 0, 5))  # True
```

### 7. `expandtabs([tabsize])`
Returns a copy of the string where all tab characters are replaced by spaces, with tabsize defaulting to 8.
```python
text = "hello\tworld"
print(text.expandtabs(4))  # "hello   world"
```

### 8. `find(sub[, start[, end]])`
Returns the lowest index where substring is found, or -1 if not found. Optionally restricts search to a slice.
```python
text = "hello world"
print(text.find("world"))  # 6
print(text.find("python")) # -1
```

### 9. `format(*args, **kwargs)`
Formats the string by replacing format fields with values.
```python
text = "My name is {name} and I am {age} years old"
print(text.format(name="John", age=30))  # "My name is John and I am 30 years old"
```

### 10. `format_map(mapping)`
Similar to `format()`, but takes a mapping (like a dictionary) directly.
```python
info = {"name": "Sarah", "age": 25}
text = "My name is {name} and I am {age} years old"
print(text.format_map(info))  # "My name is Sarah and I am 25 years old"
```

### 11. `index(sub[, start[, end]])`
Like `find()`, but raises ValueError when the substring is not found.
```python
text = "hello world"
print(text.index("world"))  # 6
# text.index("python")  # Raises ValueError
```

## Character Checking Methods

### 12. `isalnum()`
Returns `True` if all characters in the string are alphanumeric (letters or numbers) and the string is not empty.
```python
print("Hello123".isalnum())  # True
print("Hello 123".isalnum()) # False (contains space)
```

### 13. `isalpha()`
Returns `True` if all characters in the string are alphabetic and the string is not empty.
```python
print("Hello".isalpha())   # True
print("Hello123".isalpha()) # False
```

### 14. `isascii()`
Returns `True` if all characters in the string are ASCII characters.
```python
print("Hello".isascii())   # True
print("Café".isascii())    # False
```

### 15. `isdecimal()`
Returns `True` if all characters in the string are decimal characters (0-9).
```python
print("123".isdecimal())   # True
print("123.45".isdecimal()) # False (contains period)
```

### 16. `isdigit()`
Returns `True` if all characters in the string are digits. Includes more characters than `isdecimal()`.
```python
print("123".isdigit())     # True
print("²³".isdigit())      # True (superscript digits are digits)
```

### 17. `isidentifier()`
Returns `True` if the string is a valid Python identifier (could be used as a variable name).
```python
print("variable_name".isidentifier())  # True
print("123var".isidentifier())         # False (starts with a digit)
```

### 18. `islower()`
Returns `True` if all cased characters in the string are lowercase and there is at least one cased character.
```python
print("hello".islower())   # True
print("Hello".islower())   # False
```

### 19. `isnumeric()`
Returns `True` if all characters in the string are numeric characters. Broader than `isdigit()`.
```python
print("123".isnumeric())   # True
print("⅓".isnumeric())     # True (numeric fractions are numeric)
```

### 20. `isprintable()`
Returns `True` if all characters in the string are printable or if the string is empty.
```python
print("Hello".isprintable())          # True
print("Hello\nWorld".isprintable())   # False (contains newline)
```

### 21. `isspace()`
Returns `True` if all characters in the string are whitespace and the string is not empty.
```python
print(" \t\n".isspace())   # True
print("  a  ".isspace())   # False (contains non-whitespace)
```

### 22. `istitle()`
Returns `True` if the string is titlecased (all words start with uppercase followed by lowercase).
```python
print("This Is Title Case".istitle())   # True
print("This is Not Title Case".istitle()) # False
```

### 23. `isupper()`
Returns `True` if all cased characters in the string are uppercase and there is at least one cased character.
```python
print("HELLO".isupper())   # True
print("HELLo".isupper())   # False
```

## String Joining and Splitting

### 24. `join(iterable)`
Returns a string by joining all elements in the iterable with the string as separator.
```python
words = ["Hello", "World"]
print("-".join(words))  # "Hello-World"
print("".join(words))   # "HelloWorld"
```

### 25. `ljust(width[, fillchar])`
Returns the string left-justified in a string of specified width with optional fill character (spaces by default).
```python
text = "hello"
print(text.ljust(10))      # "hello     "
print(text.ljust(10, "*")) # "hello*****"
```

### 26. `lower()`
Returns a copy of the string with all cased characters converted to lowercase.
```python
text = "HELLO World"
print(text.lower())  # "hello world"
```

### 27. `lstrip([chars])`
Returns a copy of the string with leading characters (spaces by default) removed.
```python
text = "   hello   "
print(text.lstrip())       # "hello   "
print("xxhello".lstrip("x"))  # "hello"
```

### 28. `maketrans(x[, y[, z]])`
Returns a translation table for use with `translate()`.
```python
# Create a mapping from 'abc' to '123'
trans = str.maketrans("abc", "123")
text = "abcdef"
print(text.translate(trans))  # "123def"
```

### 29. `partition(sep)`
Splits the string at the first occurrence of separator and returns a 3-tuple containing the part before the separator, the separator itself, and the part after.
```python
text = "hello-world"
print(text.partition("-"))  # ('hello', '-', 'world')
```

### 30. `replace(old, new[, count])`
Returns a copy with all occurrences of substring old replaced by new, optionally limiting the number of replacements.
```python
text = "banana"
print(text.replace("a", "o"))     # "bonono"
print(text.replace("a", "o", 2))  # "bonona"
```

### 31. `rfind(sub[, start[, end]])`
Returns the highest index where substring is found, or -1 if not found. Optionally restricts search to a slice.
```python
text = "hello hello"
print(text.rfind("hello"))  # 6 (second occurrence)
```

### 32. `rindex(sub[, start[, end]])`
Like `rfind()`, but raises ValueError when the substring is not found.
```python
text = "hello hello"
print(text.rindex("hello"))  # 6
# text.rindex("python")  # Raises ValueError
```

### 33. `rjust(width[, fillchar])`
Returns the string right-justified in a string of specified width with optional fill character (spaces by default).
```python
text = "hello"
print(text.rjust(10))      # "     hello"
print(text.rjust(10, "*")) # "*****hello"
```

### 34. `rpartition(sep)`
Like `partition()`, but searches from the end of the string.
```python
text = "hello-world-python"
print(text.rpartition("-"))  # ('hello-world', '-', 'python')
```

### 35. `rsplit([sep[, maxsplit]])`
Returns a list of words, splitting from the right using the specified separator (whitespace by default).
```python
text = "hello world python"
print(text.rsplit())       # ['hello', 'world', 'python']
print(text.rsplit(" ", 1)) # ['hello world', 'python']
```

### 36. `rstrip([chars])`
Returns a copy of the string with trailing characters (spaces by default) removed.
```python
text = "   hello   "
print(text.rstrip())     # "   hello"
print("helloxxx".rstrip("x"))  # "hello"
```

### 37. `split([sep[, maxsplit]])`
Returns a list of words, splitting from the left using the specified separator (whitespace by default).
```python
text = "hello world python"
print(text.split())       # ['hello', 'world', 'python']
print(text.split(" ", 1)) # ['hello', 'world python']
```

### 38. `splitlines([keepends])`
Returns a list of the lines in the string, breaking at line boundaries. Line breaks are not included unless keepends is True.
```python
text = "hello\nworld\npython"
print(text.splitlines())     # ['hello', 'world', 'python']
print(text.splitlines(True)) # ['hello\n', 'world\n', 'python']
```

### 39. `startswith(prefix[, start[, end]])`
Returns `True` if the string starts with the specified prefix, optionally restricting the matching to a slice.
```python
text = "hello.txt"
print(text.startswith("hello"))  # True
print(text.startswith("txt", 6)) # True
```

### 40. `strip([chars])`
Returns a copy of the string with leading and trailing characters (spaces by default) removed.
```python
text = "   hello   "
print(text.strip())       # "hello"
print("xxhelloxx".strip("x"))  # "hello"
```

### 41. `swapcase()`
Returns a copy of the string with uppercase characters converted to lowercase and vice versa.
```python
text = "Hello World"
print(text.swapcase())  # "hELLO wORLD"
```

### 42. `title()`
Returns a titlecased version of the string (words start with uppercase, everything else is lowercase).
```python
text = "hello world"
print(text.title())  # "Hello World"
```

### 43. `translate(table)`
Returns a copy of the string where all characters have been mapped through the translation table.
```python
# Replace 'a' with '1', 'b' with '2', and 'c' with '3'
trans = str.maketrans("abc", "123")
text = "abcdef"
print(text.translate(trans))  # "123def"
```

### 44. `upper()`
Returns a copy of the string with all cased characters converted to uppercase.
```python
text = "hello world"
print(text.upper())  # "HELLO WORLD"
```

### 45. `zfill(width)`
Returns a copy of the string padded with zeros on the left to the specified width.
```python
text = "42"
print(text.zfill(5))  # "00042"
```
