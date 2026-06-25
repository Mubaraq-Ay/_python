# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# length of the set it_companies

print(len(it_companies))
it_companies.add('twitter')

print(it_companies)

companies = {'meta', 'paystack', 'flutterwave'}
it_companies.update(companies)
print(it_companies)

it_companies.remove('Apple')
print(it_companies) 

# remove - remove an item if it exists, and if it doesn't, throw an error.
# discard - remove an item if it exists, if it doesnt, just move on

# level 2

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# join A and B
print(A.union(B))

# intersection
print(A.intersection(B))

# A subset of B ?
print(A.issubset(B))

# A and B disjoint sets
print(A.isdisjoint(B))

print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B))

# symmetric difference - items that exist in one set but not in both sets

del (A, B)


# level 3

age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(age))

age = set(age)
print(age)
print(len(age))

# string - is the collection of characters
# list - is an ordered and mutable collection of data
# tuple - is an ordered and immutable collection of data
# set = is an unordered and unindexed collection of data. it is mutable


 

