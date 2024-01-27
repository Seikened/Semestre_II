# Calculador de hiotenusa


a = float (input("Introduce tu cateto A: "))
b = float (input("Introduce tu cateto B: "))
h = "¿?"
print(f"""
           /|
          / |
         /  |
        /   |
       /    |
      /     |
     /      |
  ({h})   ({a})
   /        |
  /         |
 /__({b})___|
      """)

# Calculo

h = ((a**2)+(b**2))**(0.5)
print(f"""
           /|
          / |
         /  |
        /   |
       /    |
      /     |
     /      |
  ({h})   ({a})
   /        |
  /         |
 /__({b})___|
      """)