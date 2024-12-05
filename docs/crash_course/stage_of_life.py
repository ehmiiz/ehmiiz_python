# if person is < 2, baby
# elif person is at least 2 yrs but less than 4, it's toddler
# elif at least 4 yrs old but less than 13, it's kid
# elif at least 13 yrs old but less than 20, teenager
# elif at least 20 yrs old but less than 65, adult
# else it's elder

person = 3

if person < 2:
    stage = 'baby'
elif person < 4:
    stage = 'toddler'
elif person < 13:
    stage = 'kid'
elif person < 20:
    stage = 'teenager'
elif person < 65:
    stage = 'adult'
else:
    stage = 'elder'
print(stage)