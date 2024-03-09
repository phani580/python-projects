
import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

numbers=['1','2','3','4','5','6','7','8','9','0']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
print("welcome to pssword generator!")
n_letters=int(input("how many letters do you want:"))
n_numbers=int(input("how many numbers do you want:"))
n_symbols=int(input("how many symbols do you want:"))
password=[]
for i in range(1,n_letters+1):
   char= random.choice(letters)
   password+=char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password+=char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password+=char
print(password)
#random.shuffle(password)
#print(password)
pas=''
for char in password:
    pas+=char
print(pas)