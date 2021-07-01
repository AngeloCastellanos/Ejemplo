miLista = ['Matematicas', 'Fisica', 'Quimica', 'Historia', 'lengua']

scores = []

for lista in miLista:
    score = input('¿Que nota has sacado en ' + miLista + '?')
    scores.append(score)

for i in range(len(miLista)):
    print('En ' + miLista[i] + ' has sacado ' + scores[i])