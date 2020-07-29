#faça um programa que mostre quanta tinta você vai precisar para pintar uma parede.
p1 = float(input('Largura da parede: '))
p2 = float(input('altura da parede: '))
mq = (p1*p2)
t = mq/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(p1, p2, mq))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(t))
