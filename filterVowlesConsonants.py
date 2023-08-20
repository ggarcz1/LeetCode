def filter_vowles(value):
    #defined item to return
    filtered = ''
    #declare list of 'bad' characters
    vowles_list = ['a', 'e', 'i','o','u']
    for idx in value:
        if idx not in vowles_list:
            filtered += idx
    return filtered

def filer_consonants(value):
    #defined item to return
    filtered = ''
    #declare list of 'bad' characters
    vowles_list = ['a', 'e', 'i','o','u']
    for idx in value:
        if idx in vowles_list:
            filtered += idx
    return filtered

value = 'Hello there'

print(filter_vowles(value=value) == 'Hll thr')
print(filer_consonants(value=value) == 'eoee')