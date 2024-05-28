# galleons, sickles, knuts

class Vault: 
    def __init__(self, galleons, sickles, knuts):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        print(f"Galleons: {self.galleons}, Sickles: {self.sickles}, Knuts: {self.knuts}")

potter = Vault(10, 40, 50)
print(potter)