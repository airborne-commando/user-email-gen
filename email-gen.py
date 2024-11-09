import random,string

        # Print the ASCII art
print("""
▓█████  ███▄ ▄███▓ ▄▄▄       ██▓ ██▓         ▄████ ▓█████  ███▄    █ ▓█████  ██▀███   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒        ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░       ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░       ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒   ░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░     ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
   ░   ░      ░     ░   ▒    ▒ ░  ░ ░      ░ ░   ░    ░      ░   ░ ░    ░     ░░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
   ░  ░       ░         ░  ░ ░      ░  ░         ░    ░  ░         ░    ░  ░   ░           ░  ░            ░ ░     ░                                                                                                                              
""")


d=['cock.li','airmail.cc','firemail.cc','tfwno.gf','cock.lu','aaathats3as.com','national.shitposting.agency','cumallover.me']
n = [
    'John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'Robert', 'Emma', 'William', 'Olivia',
    'James', 'Linda', 'Charles', 'Sophia', 'Daniel', 'Chloe', 'Matthew', 'Lily', 'Joseph', 'Grace',
    'Christopher', 'Zoe', 'Anthony', 'Mia', 'Joshua', 'Avery', 'Andrew', 'Ellie', 'Ryan', 'Harper',
    'Nicholas', 'Aria', 'Tyler', 'Amelia', 'Jacob', 'Hannah', 'Benjamin', 'Abigail', 'Elijah', 'Ella',
    'Logan', 'Madison', 'Lucas', 'Scarlett', 'Samuel', 'Riley', 'Henry', 'Victoria', 'Alexander', 'Penelope',
    'Jackson', 'Layla', 'Sebastian', 'Nora', 'Jack', 'Lillian', 'Dylan', 'Brooklyn', 'Aiden', 'Addison',
    'Mason', 'Maya', 'Ethan', 'Savannah', 'Isaac', 'Claire', 'Caleb', 'Samantha', 'Christian', 'Anna',
    'Eli', 'Paisley', 'Jonathan', 'Aubrey', 'Aaron', 'Hazel', 'Adam', 'Genesis', 'Connor', 'Skylar',
    'Cameron', 'Isla', 'Luke', 'Sadie', 'Evan', 'Violet', 'Nathan', 'Aurora', 'Isaiah', 'Mila',
    'Owen', 'Elena', 'Adrian', 'Autumn', 'Brayden', 'Ariana', 'Nolan', 'Jasmine', 'Hunter', 'Piper',
    'Lincoln', 'Stella', 'Gavin', 'Leah', 'Jason', 'Nevaeh', 'Cooper', 'Madelyn', 'Carson', 'Bella',
    'Chase', 'Gabriella', 'Jaxon', 'Kennedy', 'Blake', 'Aurora', 'Leo', 'Ruby', 'Asher', 'Eva',
    'Ryder', 'Naomi', 'Bentley', 'Serenity', 'Sawyer', 'Everly', 'Brody', 'Alice', 'Xavier', 'Luna',
    'Jeremiah', 'Hadley', 'Declan', 'Peyton', 'Mateo', 'Sophie', 'Ayden', 'Natalia', 'Hudson', 'Ivy',
    'Easton', 'Aaliyah', 'Jordan', 'Arianna', 'Brandon', 'Vivian', 'Dominic', 'Willow', 'Austin', 'Eliana',
    'Cole', 'Julia', 'Jaden', 'Josephine', 'Justin', 'Delilah', 'Leo', 'Clara', 'Grayson', 'Liliana',
    'Robert', 'Melanie', 'Kevin', 'Cora', 'Landon', 'Quinn', 'Zachary', 'Bailey', 'Tyler', 'Andrea',
    'Jose', 'Kaylee', 'Nathaniel', 'Charlie', 'Ayden', 'Kimberly', 'Eli', 'Katherine', 'Carson', 'Jade',
    'Diego', 'Alexandra', 'Bryson', 'Morgan', 'Aiden', 'Lauren', 'Damian', 'Rylee', 'Weston', 'Aubree',
    'Max', 'Alexa', 'Leo', 'Arianna', 'Carlos', 'Isabelle', 'Vincent', 'Hailey', 'Micah', 'Jocelyn',
    'Juan', 'Kinsley', 'Cole', 'Isabel', 'Elliot', 'Jordyn', 'Malachi', 'Faith', 'Miles', 'Ximena',
    'Maxwell', 'Eliza', 'Eric', 'Adeline', 'Ashton', 'Gabrielle', 'Graham', 'Emery', 'George', 'Cecilia',
    'Joel', 'Reagan', 'Everett', 'Valeria', 'Grant', 'Makayla', 'Jameson', 'Raelynn', 'Tristan', 'Athena',
    'Jonah', 'Maria', 'Maverick', 'Jade', 'Rylan', 'Lyla', 'Kayden', 'Brynn', 'Harrison', 'Emilia',
    'Ryder', 'Maeve', 'Axel', 'Brielle', 'Avery', 'Eloise', 'Beau', 'Sydney', 'Kai', 'Jordyn',
    'Rowan', 'Laila', 'Sawyer', 'Rosalie', 'Brady', 'Kylie', 'Silas', 'Catherine', 'Emmett', 'Adalyn',
    'Brantley', 'Vera', 'Ezekiel', 'Holly', 'Bentley', 'Alyssa', 'Jax', 'Juliette', 'Parker', 'Lola',
    'Roman', 'Brynlee', 'Camden', 'Lia', 'Knox', 'Daisy', 'Bennett', 'London', 'Xander', 'Alyvia',
    'Chandler', 'Talia', 'Tanner', 'Journey', 'Corbin', 'Alina', 'Hugo', 'Sabrina', 'Zane', 'Amiyah',
    'Cruz', 'Sienna', 'Cade', 'Bristol', 'Marshall', 'Liana', 'Maddox', 'Nylah', 'Nash', 'Aspen',
    'Griffin', 'Malia', 'Rhett', 'Sarai', 'Dalton', 'Avianna', 'Hendrix', 'Lainey', 'Jett', 'Tatum',
    'Wade', 'Makenna', 'Paxton', 'Winter', 'Knox', 'Myla', 'Titus', 'Lena', 'Duke', 'Charlee',
    'Gideon', 'Amara', 'Atticus', 'Mae', 'Damon', 'Nina', 'Franklin', 'Palmer', 'Anderson', 'Nadia',
    'Enzo', 'Lennox', 'Princeton', 'Ada', 'Emerson', 'Ophelia', 'Reid', 'Samara', 'Rhys', 'Demi',
    'Erik', 'Jolie', 'Ellis', 'Milani', 'Clark', 'Amalia', 'Rowan', 'Esme', 'Zander', 'Karter',
    'Grady', 'Sage', 'Brooks', 'Ember', 'Cason', 'Fiona', 'Porter', 'Adrianna', 'Jasper', 'Gracie',
    'Lennon', 'Daniella', 'Remy', 'Giselle', 'Finn', 'Yaretzi', 'Braylon', 'Jazlyn', 'Moses', 'Kamila',
    'Stephen', 'Veronica', 'Waylon', 'Alejandra', 'Warren', 'Leila', 'Royce', 'Catalina', 'Roy', 'Danica',
    'Archer', 'Aniyah', 'Clayton', 'Kaia', 'Malcolm', 'Myra', 'Ari', 'Amina', 'Kyler', 'Alondra',
    'Tatum', 'Selah', 'Phoenix', 'Evangeline', 'Kobe', 'Annabella', 'Winston', 'Adelina', 'Rocco', 'Ivory',
    'Ares', 'Noelle', 'Edwin', 'Magnolia', 'Rylan', 'Mariam', 'Milan', 'Oaklynn', 'Ridge', 'Rosie',
    'Callum', 'Selena', 'Kellan', 'Jayla', 'Reed', 'Aviana', 'Colby', 'Harlow', 'Quentin', 'Alayna',
    'Zane', 'Annalise', 'Drake', 'Scarlet', 'Kane', 'Ivanna', 'Skyler', 'Amelie', 'Emmitt', 'Elianna',
    'Briggs', 'Renata', 'Madden', 'Kaitlyn', 'Zayden', 'Charleigh', 'Kyson', 'Saylor', 'Samson', 'Francesca',
    'Kason', 'Marina', 'Jamison', 'Malaya', 'Zeke', 'Julianna', 'Cohen', 'Frances', 'Emory', 'Nala',
    'Omari', 'Dahlia', 'Reece', 'Kelsey', 'Zachariah', 'Elaina', 'Kendrick', 'Carmen', 'Adonis', 'Brylee',
    'Dax', 'Leilani', 'Cyrus', 'Paris', 'Dorian', 'Kiera', 'Bodhi', 'Elliana', 'Nico', 'Remington',
    'Kian', 'Wren', 'Colt', 'Noa', 'Abram', 'Mercy', 'Troy', 'Keira', 'Luciano', 'Louisa',
    'Cullen', 'Ellianna', 'Alaric', 'Salem', 'Harlan', 'Belen', 'Mekhi', 'Raina', 'Shane', 'Dayana',
    'Dillon', 'Isabela', 'Jonas', 'Regina', 'Johan', 'Averie', 'Kamden', 'Aisha', 'Jaiden', 'Janelle',
    'Saul', 'Kiana', 'Milo', 'Ariella', 'Jaxson', 'Novalee', 'Nelson', 'Armani', 'Johnny', 'Laney',
    'Rafael', 'Malani', 'Wade', 'Dulce', 'Leon', 'Matilda', 'Moses', 'Stevie', 'Dawson', 'Anaya',
    'Leonidas', 'Braelynn', 'Derek', 'Yasmin', 'Finley', 'Madilynn', 'Sullivan', 'Faye', 'Walker', 'Layne',
    'Royce', 'Kensley', 'Alec', 'Mina', 'Alvin', 'Leyla', 'Lawson', 'Antonella', 'Jensen', 'Aleah',
    'Harvey', 'Mabel', 'Baylor', 'Lilian', 'Hendrix', 'Bryanna', 'Callen', 'Monroe', 'Makai', 'Gianna'
]

s = [
    'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez',
    'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin',
    'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson',
    'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores',
    'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell', 'Carter', 'Roberts',
    'Gomez', 'Phillips', 'Evans', 'Turner', 'Diaz', 'Parker', 'Cruz', 'Edwards', 'Collins', 'Reyes',
    'Stewart', 'Morris', 'Morales', 'Murphy', 'Cook', 'Rogers', 'Gutierrez', 'Ortiz', 'Morgan', 'Cooper',
    'Peterson', 'Bailey', 'Reed', 'Kelly', 'Howard', 'Ramos', 'Kim', 'Cox', 'Ward', 'Richardson',
    'Watson', 'Brooks', 'Chavez', 'Wood', 'James', 'Bennett', 'Gray', 'Mendoza', 'Ruiz', 'Hughes',
    'Price', 'Alvarez', 'Castillo', 'Sanders', 'Patel', 'Myers', 'Long', 'Ross', 'Foster', 'Jimenez',
    'Powell', 'Jenkins', 'Perry', 'Russell', 'Sullivan', 'Bell', 'Coleman', 'Butler', 'Henderson', 'Barnes',
    'Gonzales', 'Fisher', 'Vasquez', 'Simmons', 'Romero', 'Jordan', 'Patterson', 'Alexander', 'Hamilton', 'Graham',
    'Reynolds', 'Griffin', 'Wallace', 'Moreno', 'West', 'Cole', 'Hayes', 'Bryant', 'Herrera', 'Gibson',
    'Ellis', 'Tran', 'Medina', 'Aguilar', 'Stevens', 'Murray', 'Ford', 'Castro', 'Marshall', 'Owens',
    'Harrison', 'Fernandez', 'McDonald', 'Woods', 'Washington', 'Kennedy', 'Wells', 'Vargas', 'Henry', 'Chen',
    'Freeman', 'Webb', 'Tucker', 'Guzman', 'Burns', 'Crawford', 'Olson', 'Simpson', 'Porter', 'Hunter',
    'Gordon', 'Mendez', 'Silva', 'Shaw', 'Snyder', 'Mason', 'Dixon', 'Munoz', 'Hunt', 'Hicks',
    'Holmes', 'Palmer', 'Wagner', 'Black', 'Robertson', 'Boyd', 'Rose', 'Stone', 'Salazar', 'Fox',
    'Warren', 'Mills', 'Meyer', 'Rice', 'Schmidt', 'Garza', 'Daniels', 'Ferguson', 'Nichols', 'Stephens',
    'Soto', 'Weaver', 'Ryan', 'Gardner', 'Payne', 'Grant', 'Dunn', 'Kelley', 'Spencer', 'Hawkins',
    'Arnold', 'Pierce', 'Vazquez', 'Hansen', 'Peters', 'Santos', 'Hart', 'Bradley', 'Knight', 'Elliott',
    'Cunningham', 'Duncan', 'Armstrong', 'Hudson', 'Carroll', 'Lane', 'Riley', 'Andrews', 'Alvarado', 'Ray',
    'Delgado', 'Berry', 'Perkins', 'Hoffman', 'Johnston', 'Matthews', 'Pena', 'Richards', 'Contreras', 'Willis',
    'Carpenter', 'Lawrence', 'Sandoval', 'Guerrero', 'George', 'Chapman', 'Rios', 'Estrada', 'Ortega', 'Watkins',
    'Greene', 'Nunez', 'Wheeler', 'Valdez', 'Harper', 'Burke', 'Larson', 'Santiago', 'Maldonado', 'Morrison',
    'Franklin', 'Carlson', 'Austin', 'Dominguez', 'Carr', 'Lawson', 'Jacobs', 'Obrien', 'Lynch', 'Singh',
    'Vega', 'Bishop', 'Montgomery', 'Oliver', 'Jensen', 'Harvey', 'Williamson', 'Gilbert', 'Dean', 'Sims',
    'Espinoza', 'Howell', 'Li', 'Wong', 'Reid', 'Hanson', 'Le', 'Mckinney', 'Cameron', 'Berry',
    'Fowler', 'Carrillo', 'Stokes', 'Hopkins', 'Fleming', 'Reynolds', 'Newton', 'Garner', 'Hicks', 'Crawford',
    'Price', 'Nguyen', 'Patterson', 'Richards', 'Ford', 'Porter', 'Castro', 'Perez', 'Reid', 'Barnes',
    'Foster', 'Watkins', 'Ford', 'Lawrence', 'Mason', 'West', 'Reyes', 'Ward', 'Grant', 'Perry',
    'Gibson', 'Kim', 'Duncan', 'Bryant', 'Hill', 'Burke', 'Curtis', 'Sanders', 'Simmons', 'Butler',
    'Cunningham', 'Lawson', 'Robertson', 'Terry', 'Cook', 'Hudson', 'Dixon', 'Henry', 'Lane', 'Payne',
    'Soto', 'Knight', 'Hudson', 'Weaver', 'Marshall', 'Peters', 'Gomez', 'Miles', 'Jordan', 'Perry',
    'Fisher', 'Ramos', 'Johnston', 'Reid', 'Wright', 'Roberts', 'Martinez', 'Hughes', 'Weaver', 'Pierce',
    'Hamilton', 'Sullivan', 'Parker', 'Brooks', 'Wells', 'Foster', 'Bennett', 'King', 'Mills', 'Morris',
    'Rogers', 'Russell', 'Murphy', 'Ferguson', 'Arnold', 'Peterson', 'Palmer', 'Stevens', 'Harrison', 'Simmons',
    'Butler', 'Phillips', 'Graham', 'Soto', 'Mason', 'Spencer', 'Porter', 'Morris', 'Stewart', 'Sanchez',
    'Sanders', 'Stevens', 'Coleman', 'White', 'Perry', 'Patterson', 'Lawson', 'Long', 'Nguyen', 'Walker',
    'Gonzalez', 'Young', 'Brooks', 'Bailey', 'Jenkins', 'Wheeler', 'Rodriguez', 'Wallace', 'Patterson', 'Knight',
    'Simmons', 'Holmes', 'Roberts', 'Porter', 'Campbell', 'Gomez', 'Mitchell', 'Edwards', 'Flores', 'Bennett',
    'Clark', 'Russell', 'Coleman', 'Gomez', 'Harris', 'Wheeler', 'Roberts', 'Cole', 'Long', 'King',
    'White', 'Perry', 'Watson', 'Jenkins', 'Young', 'Wright', 'Cooper', 'Bailey', 'Flores', 'Cruz'
]

g=lambda l:''.join(random.choices(string.ascii_lowercase+string.digits,k=l))
p=lambda:''.join(random.choice(string.ascii_letters+string.digits+string.punctuation)for _ in range(64))
e=lambda d:(f"{random.choice(n).lower()}{random.choice(s).lower()}{g(random.randint(2,4))}@{d}",p())
print("\n".join(f"{i+1}: {domain}" for i, domain in enumerate(d)))
c,cp=e(d[random.randint(0,7) if not (i:=input("Select a domain (1-8) or press Enter for random: ")) else max(0,min(int(i)-1,7))])
pm,pmp=e('proton.me')
print(f"Cock.li: {c} | {cp}\nProtonMail: {pm} | {pmp}")

import random

# Expanded lists of prefixes, core words, and suffixes
prefixes = [
    'aether', 'binary', 'crypto', 'digital', 'epsilon', 'fractal', 'gamma', 'helix', 'infinity', 'joule',
    'kelvin', 'lambda', 'matrix', 'nano', 'omega', 'photon', 'quantum', 'radiant', 'synth', 'tensor',
    'utopia', 'vector', 'warp', 'xenon', 'yttrium', 'zeta', 'aurora', 'binary', 'celestial', 'dynamo',
    'eclipse', 'flux', 'gravity', 'helios', 'isotope', 'jupiter', 'kaleidoscope', 'lithium', 'magma', 'nebula',
    'orbit', 'pulsar', 'quasar', 'radium', 'singularity', 'tachyon', 'uranium', 'vortex', 'wormhole', 'x-ray',
    'yukon', 'zircon', 'atomic', 'bionic', 'carbon', 'dyson', 'entropy', 'fusion', 'galactic', 'hadron',
    'ionic', 'kinetic', 'laser', 'magnetic', 'neutrino', 'ozone', 'particle', 'quantum', 'relativity', 'scalar',
    'thermal', 'ultraviolet', 'vacuum', 'wavelength', 'x-factor', 'yield', 'zero-point', 'acceleron', 'borealis', 'cosmo',
    'dimension', 'electron', 'fermion', 'graviton', 'horizon', 'interstellar', 'jovian', 'kelvin', 'luminous', 'multiverse',
    'neutron', 'orbital', 'planck', 'qubit', 'resonance', 'supernova', 'tesseract', 'unified', 'void', 'wavefunction',
    'xenomorph', 'yang', 'zeitgeist', 'absolute', 'blackhole', 'continuum', 'dark-matter', 'event-horizon', 'fibonacci'
]

core_words = [
    'cascade', 'nebula', 'vortex', 'prism', 'nexus', 'quanta', 'fusion', 'nova', 'pulsar', 'quasar',
    'radiance', 'singularity', 'spectrum', 'tempest', 'zenith', 'aurora', 'cosmos', 'eclipse', 'galaxy', 'horizon',
    'infinity', 'nebula', 'orbit', 'parallax', 'quantum', 'radiant', 'stellar', 'universe', 'vortex', 'wormhole',
    'x-ray', 'yocto', 'zephyr', 'atom', 'binary', 'core', 'dimension', 'entropy', 'fractal', 'gravity',
    'helix', 'isotope', 'joule', 'kinetic', 'luminous', 'matrix', 'neutron', 'oscillation', 'photon', 'quark',
    'resonance', 'scalar', 'tensor', 'uncertainty', 'vector', 'wave', 'x-factor', 'yield', 'zero-point', 'accelerate',
    'beam', 'collide', 'diffract', 'emit', 'fission', 'gravitate', 'harmonize', 'ionize', 'jump', 'kaleidoscope',
    'levitate', 'magnify', 'neutralize', 'oscillate', 'polarize', 'quantize', 'radiate', 'synchronize', 'teleport', 'unify',
    'vibrate', 'warp', 'x-ray', 'yield', 'zoom', 'amplify', 'bend', 'compress', 'distort', 'expand',
    'fluctuate', 'gyrate', 'hover', 'implode', 'juggle', 'knot', 'loop', 'morph', 'negate', 'orbit'
]

suffixes = [
    'nexus', 'prime', 'quantum', 'rex', 'sigma', 'tau', 'ultra', 'vortex', 'wave', 'xen',
    'yin', 'zeta', 'aeon', 'byte', 'core', 'dyne', 'echo', 'flux', 'giga', 'hyper',
    'ion', 'jolt', 'kilo', 'lux', 'mega', 'neo', 'omni', 'pico', 'quad', 'rift',
    'sync', 'tera', 'uni', 'volt', 'watt', 'xeno', 'yotta', 'zetta', 'apex', 'binary',
    'cipher', 'delta', 'epsilon', 'fractal', 'gamma', 'helix', 'infinity', 'joule', 'kappa',
    'lambda', 'mu', 'nu', 'omicron', 'pi', 'qubit', 'rho', 'sigma', 'theta', 'upsilon',
    'phi', 'chi', 'psi', 'omega', 'absolute', 'beta', 'cosmic', 'dimension', 'entropy', 'fusion',
    'gravity', 'horizon', 'isotope', 'kinetic', 'luminous', 'matrix', 'neutron', 'orbital', 'photon', 'quark',
    'relativity', 'singularity', 'tachyon', 'uncertainty', 'vacuum', 'wormhole', 'x-factor', 'yang', 'zero-point', 'acceleron',
    'boson', 'chromodynamic', 'deuterium', 'eigenstate', 'fermion', 'gluon', 'hadron', 'inflaton', 'lepton', 'meson'
]

# Function to generate a random username
def generate_username():
    prefix = random.choice(prefixes)
    core_word = random.choice(core_words)
    suffix = random.choice(suffixes)
    username = prefix + core_word + suffix

    # Optionally add a random number with a probability of 50%
    if random.random() < 0.5:
        number = random.randint(1, 999)
        username += str(number)

    return username

# Generate and print a random username
username = generate_username()
print("your username is:", username)

