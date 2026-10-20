# Temperaturen
temp1 = 77
temp2 = 50
temp3 = 69

# Berechnungs-Funktion
def fahrenheit_in_celsius(temp):
    # Berechnet Temperatur
    return (temp - 32) * (5 / 9) # Gibt den berechneten Wert zurück 
    
# Gibt Werte aus
print(fahrenheit_in_celsius(temp1))
print(fahrenheit_in_celsius(temp2))
print(fahrenheit_in_celsius(temp3))
