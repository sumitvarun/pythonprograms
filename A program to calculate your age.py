#Simple program to calculate your age.

print('Answer the question to know how long you have lived in this life ..')
name = input('Name:')
print('what is your age?',(name),'?')
age = int(input('age:'))
#int means integer such as 1,2,3 or -1,-2, -3
days = age *365
minutes = age * 525948
seconds = age * 31556926

print(name,'has been alive for',days,'days',minutes,'minute',seconds,'seconds')
print('Thanks for using my age calc program')