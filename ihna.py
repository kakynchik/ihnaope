#4
def long_words(dictionary):
    return [word for word in dictionary if len(word) >= 5]
dict1 = {'vablokaka': 'a fruit', 'carrot': 'a vegetable', 'python': 'a programming language', 'bike': 'a vehincle'}
print(long_words(dict1))