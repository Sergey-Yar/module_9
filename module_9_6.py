#Генераторы
def all_variants(text):
    var = len(text)
    for i in range(var):
        for j in range(i, var):
            yield text[i:j + 1]

a = all_variants("abc")
for i in a:
    print(i)