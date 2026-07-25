import sys
print('full sys.arg list:', sys.argv)

if len(sys.argv) > 1:
    user_name = sys.argv[1]
    print(f'welcome back, {user_name}')
else:
    print('you didnt pass a name')


total = int(sys.argv[1]) + int(sys.argv[2])
print(total)