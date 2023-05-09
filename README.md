# Recursive String Functions

In this exercise, you will use recursion to write some functions that manipulate strings.

## Your Task

In `string_recursion.py`, you will find stub implementations of various string functions. You should implement each one of these functions recursively -- without any loops.

The functions are:

1. `print_dashed(s)`: accepts a string parameter `s` and prints the string with each character separated by a dash. For example, `print_dashed('hello')` should print `h-e-l-l-o` to the console.

  * The last character of a string should not have a dash printed after it.
  * If `s` is `None` or the empty string, nothing should be printed.

2. `remove_char(s, c)`: accepts a string `s` and character `c` and returns a string that represents `s` but with all instances of `c` removed. For example, `remove_char('hello', 'l')` should return `heo`.

  * If `s` is `None` or the empty string, `s` should be returned.

3. `to_upper_case(s)`: accepts a string `s` and returns a version of `s` where all lower-case characters are capitalized. For example, `to_upper_case('hello')` should return `'HELLO'`.

  * To convert a character to upper-case, you can use the `upper()` method: for a string `s`, `s.upper()` will convert it to upper-case. For the purposes of this function, you should only use `upper()` on one character at a time.
  * If `s` is `None` or the empty string, `s` should be returned.

4. `get_index(s, c)`: returns the index of the first occurrence of the character `c` in the string `s`, or -1 if `c` is not in `s`. For example, `get_index('hello', 'o')` should return 4. but `get_index('hello', 'z')` should return `-1`.

  * You may find it helpful to store the result of the recursive call in a variable, and inspect the value of that variable to decide what to return in the recursive case. You will need an `if` statement.
  * If either `s` or `c` is `None` or the empty string, -1 should be returned.

5. `prune(s)`: returns a version of `s` with all space characters (`' '`) removed from the front and end of `s` (but not removed from the middle). For example, `prune('  hello, world     ')` should return `'hello, world'`.

  * If `s` is `None` or the empty string, `s` should be returned.

## Testing

The file `test_string_recursion.py` contains some unit tests for the functions, but the tests aren't comprehensive. You should think of other applicable test cases (especially those that evaluate corner cases) and add them.
