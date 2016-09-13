from guitar_class import Guitar

fender_strat = Guitar('fender stratocaster',1975,12000)
hendrix_style = Guitar("Hendrix's style", 2012, 25698)
slash = Guitar("Slash' style", 1987, 21587)

print(fender_strat)
print(slash.get_age())
print(hendrix_style.is_vintage())

