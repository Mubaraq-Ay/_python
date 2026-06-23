countries =['germany', 
            'france', 
            'belgium', 
            'sweden', 
            'denmark', 
            'finland', 
            'norway', 
            'iceland', 
            'estonia'
        ]

user_country = input('enter a country name: ')
check_if_exists = user_country in countries

print(check_if_exists)
