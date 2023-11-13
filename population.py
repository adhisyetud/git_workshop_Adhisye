with open("data/cities.csv", "r") as f:
    lines = f.readlines()[1:]       #Skip Header Row

total = 0
for line in lines:
    name, population = line.split(",")
    print(f"Adding {name} to population")
    total += int(population)

#Test
print(f"Average population: {total / len(lines):,}")
