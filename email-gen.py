import random,string
d=['cock.li','airmail.cc','firemail.cc','tfwno.gf','cock.lu','aaathats3as.com','national.shitposting.agency','cumallover.me']
n=['John','Jane','Michael','Emily','David','Sarah','Robert','Emma','William','Olivia']
s=['Smith','Johnson','Williams','Brown','Jones','Garcia','Miller','Davis','Rodriguez','Martinez']
g=lambda l:''.join(random.choices(string.ascii_lowercase+string.digits,k=l))
p=lambda:''.join(random.choice(string.ascii_letters+string.digits+string.punctuation)for _ in range(64))
e=lambda d:(f"{random.choice(n).lower()}{random.choice(s).lower()}{g(random.randint(2,4))}@{d}",p())
print("\n".join(f"{i+1}: {domain}" for i, domain in enumerate(d)))
c,cp=e(d[max(0,min(int(input("Select a domain (1-8) or 0 for random: "))-1,7))])
pm,pmp=e('proton.me')
print(f"Cock.li: {c} | {cp}\nProtonMail: {pm} | {pmp}")
