#!/usr/bin/python3

class abanyamuryango:
    
    umubare = 0
    def __init__(self, name, praenomen, contribution):
        self.name = name
        self.praenomen = praenomen
        self.contribution = contribution
        abanyamuryango.umubare += 1

   
    def list(self):
        print("Name: ",self.name, "Praenom: ",self.praenomen, "contribution: ", self.contribution)
ryango1 = abanyamuryango("Mujawimana", "Domina", 45000)
ryango2 = abanyamuryango("Nyiranizeyimana", "Veronique", 45000)

print(f"Abanyamuryango ni : ", abanyamuryango.umubare)
print("____________________")
ryango1.list()
ryango2.list()
