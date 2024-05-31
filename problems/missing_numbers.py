str_input: str = '134568'

first_index_el: int = int(str_input[0])
last_index_el: int = int(str_input[-1])

new_str = ''

for i in range(first_index_el, last_index_el + 1):
    if str(i) not in str_input:
        new_str += str(i)

print(new_str)