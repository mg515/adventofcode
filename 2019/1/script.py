

with open('input.txt') as mass:
    masses = [int(x) for x in mass.read().splitlines()]

def fuel_recursion(x, rec_sum):
    
    fuel_for_fuel = x//3 - 2
    if fuel_for_fuel <= 0:
        return rec_sum
    
    return fuel_recursion(fuel_for_fuel, rec_sum + fuel_for_fuel)

sol = 0
for ms in masses:
    sol += fuel_recursion(ms, 0)

print(sol)