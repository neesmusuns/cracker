from random import randint

added_symbols = []
leet = []
symbols = [0,1,2,3,4,5,6,7,8,9,"!","?","#","$","%","*","&"]
alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1#$%&*?"

# symbols appended to the end of the passwords
with open("passwords.txt", "r") as f:
    for line in f:
        for s in symbols:
            added_symbols.append("".join(line.strip() + str(s)))

# leet speech
with open("passwords.txt", "r") as f:
    for line in f:
        leet.append(line.translate(str.maketrans({'t':'7','s':'5','l':'1','o':'0','a':'4','e':'3'})).strip())

def r():
    return randint(0, 68)

# random passwords with length = 4
# for each i there are 69^3 = 328.509 possible passwords
def gen_rand(l):
    password = ""
    for i in range(l):
        password += alphabet[r()]
    return password

print(gen_rand(12))



#print(added_symbols)
#print(leet)


