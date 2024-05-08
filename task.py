import random

class Piece:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def move(self):
        pass

class Ağlar(Piece):
    def move(self):
        print(f"{self.color} {self.name} daşı hərəkət edir...")
        direction = random.choice(["şimal", "cənub", "şərq", "qərb"])
        steps = random.randint(1, 3)
        print(f"{direction} istiqamətində {steps} addım atıldı.")

class Qaralar(Piece):
    def move(self):
        print(f"{self.color} {self.name} daşı hərəkət edir...")
        if random.random() < 0.5:
            direction = random.choice(["şimal", "cənub", "şərq", "qərb"])
            print(f"{direction} istiqamətində iki addım atıldı.")
        else:
            print("Normal hərəkət: Hər hansı bir istiqamətdə bir addım atıldı.")

ağ = Ağlar("Şah", "Ağ")
ağ = Ağlar("Piyada", "Ağ")
ağ = Ağlar("At", "Ağ")
qara = Qaralar("Vəzir", "Qara")
qara = Qaralar("Fil", "Qara")
qara = Qaralar("Top", "Qara")

ağ.move()
qara.move()
