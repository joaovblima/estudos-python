"""
alien_0 = {'color': 'green', 'points': 5}
print(alien_0["color"])
print(alien_0["points"])
novos_pontos = alien_0["points"]
print("voce ganhou apenas " + str(novos_pontos) + " pontos!")
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
alien_0 = {}
alien_0["cor"] = "verde"
alien_0["pontos"] = 5
print(alien_0)
print(f"O alien eh {alien_0["cor"]}")
alien_0["cor"] = "amarelo"
print(f"agora o alien eh {alien_0["cor"]}")
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print("posicao original de x eh " + str(alien_0["x_position"]))
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] += x_increment
print("posicao de x atualizada: " + str(alien_0["x_position"]))
alien_0["pontos"] = 5
print("pontos do alien " + str(alien_0["pontos"]))
del alien_0["pontos"]
print(alien_0)


alien_0 = {"cor": "verde", "pontos": 5}
alien_1 = {"cor": "amarelo", "pontos": 10}
alien_2 = {"cor": "vermelho", "pontos": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

"""
aliens = []
for numero_de_aliens in range(30):
    novo_alien = {"cor": "verde", "pontos": 5,
                  "velocidade": "lento"}
    aliens.append(novo_alien)

for alien in aliens[:5]:
    print(alien)

print(len(aliens))

print()
for alien in aliens[0:3]:
    if alien["cor"] == "verde":
        alien["cor"] = "roxo"
        alien["velocidade"] = "muito rapido"
        alien["pontos"] = 200

for alien in aliens[:5]:
    print(alien)
