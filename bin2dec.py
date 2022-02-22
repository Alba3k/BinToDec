def bin2dec(binNumber):
	decNumber = 0
	index = 1
	binNumber = binNumber[::-1]
	for i in binNumber:
		number = int(i) * index
		decNumber = decNumber + number
		index = index * 2
	return decNumber

print('ВВЕДИТЕ ДВОИЧНОЕ 8-БИТНОЕ ЧИСЛО')
binNumber = input('>')

if len(binNumber) != 8:
	print('ВВЕДИТЕ ПРАВИЛЬНОЕ 8-БИТНОЕ ЧИСЛО')
elif not binNumber.isdigit():
	print('ВВЕДИТЕ ПРАВИЛЬНОЕ 8-БИТНОЕ ЧИСЛО')
else:
	print(bin2dec(binNumber))