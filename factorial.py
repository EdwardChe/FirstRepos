def fract(x):
	if x == 1:
		return 1
	else:
		return x * fract(x-1)

x = int(input('Введите число: '))
print(fract(x))
