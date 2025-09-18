inventory = []
def add_item(item):
    inventory.append(item)

def count_items(items):
    if not items:
        return 0
    return 1 + count_items(items[1:])

def main():
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

list = lambda x :print(f"item:{x}")

for item in inventory:
    list(item)

total = count_items(inventory)
print(f"total number of items:{total}")

