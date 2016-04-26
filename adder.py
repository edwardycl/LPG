while True:
	print('Input 1st number:')
	a = int(input())
	print('Input 2nd number: ')
	b = int(input())
	if a==0 and b==0:
		break
	print('a + b = ', a+b)
	print('a - b = ', a-b)
	print('a * b = ', a*b)
	if b!=0:
		print('a / b = ', a/b)
		print('a % b = ', a%b)
	print('a ** b = ', a**b)
