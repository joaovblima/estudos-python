motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)
#alterando elemento da primeira posiçãoo
motorcycle[0]='ducati'
print(motorcycle)
#adicionando mais um elemento a lista utilizando o metodo append()
motorcycle.append('honda')
print(motorcycle)
#deletando o elemento da posição 2
del motorcycle[2]
print(motorcycle)
#removendo e reaproveitando o elemento usando pop()
last_owned = motorcycle.pop()
print("The last motorcycle I owned was a " + last_owned.title() )

motorcycle = ['honda', 'yamaha', 'suzuki']
too_expensive = 'yamaha'
motorcycle.remove(too_expensive)



