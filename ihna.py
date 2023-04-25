#2
string = ['hi', 'mene', 'zvaty', 'vova']
    s = input("введіть текст: ")
def comit_vowels(s):
    volwes = "asdadasd"
    count = 0
    for leters in s:
        if leters in volwes:
            count += 1
        return count
#демонстрація
for s in strings:
    print(f"у рядку {s} голосних літер {count_vowels(s)}")
