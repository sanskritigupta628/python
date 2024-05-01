import random
import string 

s1 = string.ascii_uppercase
s2 = string.ascii_lowercase
s3 = string.digits
s4 = string.punctuation

s = []
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)

random.shuffle(s)

plen = int(input("Enter the length of password:"))


password = ''.join(random.sample(s, plen))

print("Generated password:", password)