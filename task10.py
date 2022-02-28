# 10.	Найти расстояние между двумя точками пространства.
#
print('Введите координаты точек (X1;Y1;Z1) и (X2;Y2;Z2)')
x1 = float(input('X1 = '))
y1 = float(input('Y1 = '))
z1 = float(input('Z1 = '))
x2 = float(input('X2 = '))
y2 = float(input('Y2 = '))
z2 = float(input('Z2 = '))
dx = x2 - x1
dy = y2 - y1
dz = z2 - z1
print(f'Расстояние между точками равно {round((dx**2 + dy**2 + dz**2)**0.5, 2)}')
