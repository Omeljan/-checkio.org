'''
Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, 
за исключением нулей.

Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).

Входные данные: Положительное целое число.

Выходные данные: Произведение цифр как целочисленное (int).

You are given a positive integer. Your function should calculate the product of the 
digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget
 to exclude zeroes).

'''


def checkio(number: int) -> int:
	numbers = str(number)
	couls = ''
	for x in numbers:
		couls = x

	return couls
		


if __name__ == '__main__':
	print('Example:')
	print(checkio(123405))
	
	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio(123405) == 120
	assert checkio(999) == 729
	assert checkio(1000) == 1
	assert checkio(1111) == 1
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")