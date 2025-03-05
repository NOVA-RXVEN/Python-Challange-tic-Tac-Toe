import random 
import string

def randPass(length):
    if length < 10:
        return "The Password must be at least 10 characters"
    
    lowercases = string.ascii_lowercase
    uppercases = string.ascii_uppercase
    digits = string.digits
    punctuations = string.punctuation
    
    password = [random.choice(lowercases),random.choice(uppercases), random.choice(digits), random.choice(punctuations)]
    
    characters  = lowercases + uppercases + digits + punctuations
    
    password = password + random.choices(characters, k = length - len(password))
    random.shuffle(password)
    
    return "".join(password)

passLength = random.randint(10, 16)
password = randPass(passLength)

print(f"Password: {password}") 