# these are projects i built before learning loops

item_1 = input('Enter item 1: ')
price_1 = float(input(f'Enter the price for {item_1}: $ '))

item_2 = input('Enter item 2: ')
price_2 = float(input(f'Enter the price for {item_2}: $ '))

item_3 = input('Enter item 3: ')
price_3 = float(input(f'Enter the price for {item_3}: $ '))

item_4 = input('Enter item 4: ')
price_4 = float(input(f'Enter the price for {item_4}: $ '))

item_5 = input('Enter item 5: ')
price_5 = float(input(f'Enter the price for {item_5}: $ '))

items_list = [item_1, item_2, item_3, item_4, item_5]
price_list = [price_1, price_2, price_3, price_4, price_5]
 

print(items_list)
print(f'${price_list}')

total_cost = sum(price_list)
print(f'Total cost: {total_cost}')

most_expensive_item = max(price_list)
item_index = most_expensive_item
rs = price_list.index()

print(rs)

print(most_expensive_item) 
 
