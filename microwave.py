import time as t
import os

class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False
    
    def turn_on(self) -> None:
        if self.turned_on:
            print(f"Microwave ({self.brand}) is already turned on.")
        else:
            self.turned_on = True
            print(f"Microwave ({self.brand}) is now turned on.")
        
    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f"Microwave ({self.brand}) is now turned off.")
        else:
            print(f"Microwave ({self.brand}) is already turned off.")

    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f"Running ({self.brand}) for {seconds} seconds")
            for sec in range(seconds):
                seconds -= 1
                print(f"Running microwave ({self.brand}) for {seconds} seconds")
                t.sleep(1)
                os.system("clear")
            print("Done")
        else:
            print("Turn your microwave on first")

    def __mul__(self, others):
        return "None"
    def __str__(self):
        return f"{self.brand} Ratting: {self.power_rating}"

smeg: Microwave = Microwave("Smeg", "B")
bosch: Microwave = Microwave("Bosch", "C")

print(smeg * bosch)
print(bosch)