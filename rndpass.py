from string import digits
secure_random = random.systemrandom()
password ="".join(secure_random.choice(symbols) for i in range (10))
print(password) 
                                  
