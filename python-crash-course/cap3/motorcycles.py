motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)
motorcycle[0]='ducati'
print(motorcycle)
motorcycle.append('honda')
print(motorcycle)
del motorcycle[2]
print(motorcycle)
last_owned = motorcycle.pop()
print("The last motorcycle I owned was a " + last_owned.title() )


