"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in given list"""

    for item in items:
        print(item)


def get_all_evens(nums):
    """Given a list of numbers, return a list of all even numbers"""
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums

def get_odd_indices(items):
    """Given a list, return all elements at odd numbered indices"""

    result = []

    i = 0
    for item in items:
        if i % 2 != 0:
            result.append(item)
        i += 1
    
    return result


def print_as_numbered_list(items):
    """Given a list, output a numbered list"""

    i = 1

    for item in items:
        print(f'{i}. {item}')
        i += 1


def get_range(start, stop):
    """Returns a list of numbers within a specific range"""

    nums = []

    num = start

    while num < stop:
        nums.append(num)
        num += 1


def censor_vowels(word):
    """Given a string, return a string where vowels are replaced with *"""

    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append("*")
        
        else:
            chars.append(letter)
    
    return ''.join(chars)

def snake_to_camel(string):
    """Given a string in snake_case, return to upperCamelCase"""

    camelCase = []

    for item in string.split('_'):
        camelCase.append(f'{item.title()}')
    
    return ''.join(camelCase)


def longest_word_length(words):
    """Return the length of the longest word in given list"""

    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest

def truncate(string):
    """Truncate repeating characetrs into one character"""

    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result) -1]:
            result.append(char)

    return ''.join(result)


def has_balanced_parens(string):
    """Return True if all parentheses in a given string are balanced"""

    parens = 0;

    for char in string:
        if char == '(' or char == ')':
            parens += 1
        
    if parens % 2 != 0:
        return False
    
    return True


def compress(string):
    """Return compressed version of given string"""

    compressed = []

    curr_char = ''
    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(str(char_count))
        
            curr_char = char
            char_count = 0
        
        char_count += 1
    
    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return ''.join(compressed)
