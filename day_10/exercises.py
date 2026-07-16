# level 1
# 1

# iterate 0 - 10 using for loop
for number in range(11):
    print(number)

# iterate 0 - 10 using while loop
number = 0
while number <= 10:
    print(number)
    number += 1

# 2

# iterate 10 - 0 using for loop.
for number in range(10, -1, -1):
    print(number)

# iterate 10 - 0 using while loop.

number = 10
while number >= 0:
    print(number)
    number -= 1

# 3

count = 0

for triangle in range(7):
    count += 1
    print('#' * count)

# shorter version
for triangle in range(1, 8):
    print('#' * triangle)

# 4
# nested loops.

for row in range(8):
    for column in range(8):
     print('#', end=' ')
    print()
   

# 5.

for numbers in range(11):
    print(f'{numbers} x {numbers} = {numbers ** 2}')

# 6.

languages = ['Python', 'Numpy','Pandas','Django', 'Flask']

for language in languages:
    print(language)

# 7. 

# print only even numbers from 0 -100
for numbers in range(101):
    if numbers % 2 == 0:
        print(numbers)

# 8

# print only odd numbers from 0 - 100
for numbers in range(101):
    if numbers % 2 == 1:
        print(numbers)


# level 2

# 1

# sum of 0 - 100, using for loop.

total = 0

for numbers in range(101):
    total += numbers
print(f'the sum of all numbers is {total}')


# 2
# sum of all even and sum of all odds

even = 0
odd = 0

for i in range(101):
    if i % 2 == 0:
     even += i
    else:
        odd += i
print(f'the sum of all evens is {even}. and the sum of all odds are {odd}')


# level 3

# 1

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];


for country in countries:
    if 'land' in country:
     print(country)
    

# 2

fruit_list = ['banana', 'orange', 'mango', 'lemon']

for fruit in reversed(fruit_list):
    print(fruit)

for fruit in range(len(fruit_list)-1, -1, -1):
    print(fruit_list[fruit])