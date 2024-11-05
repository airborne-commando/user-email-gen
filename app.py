from flask import Flask, render_template, request
import random, string

app = Flask(__name__)

d = ['cock.li', 'airmail.cc', 'firemail.cc', 'tfwno.gf', 'cock.lu', 'aaathats3as.com', 'national.shitposting.agency', 'cumallover.me']
n = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'Robert', 'Emma', 'William', 'Olivia']
s = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']

def g(l):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=l))

def p():
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(64))

def e(d):
    return (f"{random.choice(n).lower()}{random.choice(s).lower()}{g(random.randint(2,4))}@{d}", p())

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    selected_domains = d.copy()  # Default to all domains selected

    if request.method == 'POST':
        selected_domains = request.form.getlist('domains')
        
        results = []
        for domain in selected_domains:
            c, cp = e(domain)
            results.append(f"{domain.capitalize()}:\nEmail: {c}\nPassword: {cp}\n")
        
        pm, pmp = e('proton.me')
        results.append(f"ProtonMail:\nEmail: {pm}\nPassword: {pmp}")
        
        result = "\n".join(results)
    
    return render_template('index.html', domains=d, selected_domains=selected_domains, result=result)

if __name__ == '__main__':
    app.run(debug=True)