def pascal(n):
	r1, r2 = [1], [1, 1]
	degree = 1
	while degree <= n:
		print(r1)
		r1, r2 = r2, [1] + [sum(pair) for pair in zip(r2, r2[1:]) ] + [1]
		degree += 1


number = input("Please Enter number : ")
pascal(int(number))

