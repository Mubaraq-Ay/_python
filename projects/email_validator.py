user_email = input('Enter your email: ')
contain_at = '@' in user_email
contain_dot = '.' in user_email

at_index = user_email.find('@')
user_name = user_email[:at_index]

domain = user_email[at_index + 1:]
is_email_valid = contain_at and contain_dot

print(f'Username: {user_name}')
print(f'Domain: {domain}')
print(f'Valid email: {is_email_valid}')