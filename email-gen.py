import random
import string

def generate_fake_name():
    first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'Robert', 'Emma', 'William', 'Olivia', 'Nicholas', 'Alexander', 'Sophia', 'Daniel', 'Grace', 'Matthew', 'Hannah', 'Christopher', 'Lily', 'Joshua', 'Samantha', 'Andrew', 'Mia']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Reed', 'Clark', 'Lewis', 'Walker', 'Hall', 'Allen', 'Young', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams']
    return f"{random.choice(first_names)}{random.choice(last_names)}".lower()

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_random_password(length=64):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def get_cockli_domain():
    # Display available domains and prompt the user to select one
    cockli_domains = ["cock.li", "airmail.cc", "firemail.cc", "tfwno.gf", "cock.lu", "aaathats3as.com", "national.shitposting.agency", "cumallover.me"]
    print("Available Cock.li domains:")
    for i, domain in enumerate(cockli_domains, start=1):
        print(f"{i}: {domain}")
    
    choice = int(input("Select a domain by entering its number (or enter 0 for a random domain): "))
    if choice == 0:
        return random.choice(cockli_domains)
    elif 1 <= choice <= len(cockli_domains):
        return cockli_domains[choice - 1]
    else:
        print("Invalid choice. A random domain will be used.")
        return random.choice(cockli_domains)

def generate_email(domain=None):
    domain = domain if domain else get_cockli_domain()
    
    name = generate_fake_name()
    random_string = generate_random_string(random.randint(2, 4))
    username = f"{name}{random_string}"
    email = f"{username}@{domain}"
    password = generate_random_password()
    return email, password

# Generate a Cock.li email
cockli_email, cockli_password = generate_email()
print(f"Cock.li email: {cockli_email} | Password: {cockli_password}")

#Generate ProtonMail email
proton_email, proton_password = generate_email("proton.me")
print(f"ProtonMail email: {proton_email} | Password: {proton_password}")