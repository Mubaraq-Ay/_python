system_tools = [
    'git', 
    'python', 
    'linux'
]

frontend = input('enter your preferred frontend framework: ')
backend = input('enter your preferred backend framework: ')

system_tools.append(frontend)
system_tools.append(backend)

print(system_tools)
print('Number of tools: ',len(system_tools))

command = 'sudo apt-get install ' + ' '.join(system_tools)
print(command) 