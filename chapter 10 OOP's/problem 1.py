class programmer:
    company = "Google"
    def __init__(self,name , salary , pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("chaitanya", 1700000, 441802)
print(p.name, p.salary, p.pin, p.company)

d = programmer("dinkar", 1700000, 441802)
print(d.name, d.salary, d.pin, d.company)

