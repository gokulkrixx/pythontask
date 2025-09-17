 
grocery_list = ["milk", "bread", "eggs"]


def add_item(item):
    grocery_list.insert(0,item)
    grocery_list.pop()
    return grocery_list
add_item("butter")
print(grocery_list)

list = lambda x: print(f"item:{x}")
for x in grocery_list:
    list(x)


def count_characters(items):
    if not items:
        return 0
    return len(items[0])+count_characters(items[1:])
print(count_characters(grocery_list))



