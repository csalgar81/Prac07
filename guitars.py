from guitar_class import Guitar
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

guitars = []

guitar = Guitar(input('Name: '), int(input('Year: ')), float(input('Cost: $')))
while guitar.name != '':
    guitars.append(guitar)
    print(guitar," added.")
    guitar = Guitar(input('Guitar name: '), int(input('Year: ')), float(input('Cost: $')))

print('These are my Guitars:')

for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = '(vintage)'
    else:
        ''
    print("Guitar {}: {:>20} ({}), worth ${:10.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost,vintage_string))

