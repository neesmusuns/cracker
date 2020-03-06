added_symbols = []
leet = []
random = []
symbols = [0,1,2,3,4,5,6,7,8,9,"!","?","#","$","%","*","&"]
alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1#$%&*?"

# symbols appended to the end of the passwords
with open("passwords.txt", "r") as f:
    for line in f:
        for s in symbols:
            for z in symbols:
                added_symbols.append("".join(line.strip() + str(s) + str(z)))

# leet speech
with open("passwords.txt", "r") as f:
    for line in f:
        leet.append(line.translate(str.maketrans({'t':'7','s':'5','l':'1','o':'0','a':'4','e':'3'})).strip())

# random passwords with length = 4
# for each i there are 69^3 = 328.509 possible passwords
def gen_rand(i):
    n = len(alphabet)  # 69
    s = alphabet[i]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                random.append("".join([s,alphabet[a],alphabet[b],alphabet[c]]))

gen_rand(0)

#print(added_symbols)
#print(leet)
#print(random)


