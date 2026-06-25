# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# length of the set it_companies

print(len(it_companies))
it_companies.add('twitter')

print(it_companies)

companies = 'meta', 'paystack', 'flutterwave'
it_companies.update(companies)
print(it_companies)

it_companies.remove('Apple')
print(it_companies)

# remove - remove an item if it exists, and if it doesn't, throw an error.
# discard - remove an item if it exists, if it doesnt, just move on