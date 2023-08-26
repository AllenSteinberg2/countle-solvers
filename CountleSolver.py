def solve(n, sol):
	if len(n) == 1:
		if n[0] == sol:
			return ["Solved!"]
		else:
			return []
	elif sol in n:
		return ["Solved!"]
	else:
		for i in range(len(n)):
			for j in range(len(n)):
				if(j != i):
					nNew = n.copy()
					nNew.remove(n[i])
					nNew.remove(n[j])
					
					n0 = nNew.copy()
					n1 = nNew.copy()
					n2 = nNew.copy()
					n3 = nNew.copy()

					n0.append(n[i]+n[j])
					if(n[i]-n[j] >= 0):
						n1.append(n[i]-n[j])
					n2.append(n[i]*n[j])
					if(n[j] != 0 and n[i]/n[j] == int(n[i]/n[j])):
						n3.append(int(n[i]/n[j]))

					S0 = solve(n0, sol)
					S1 = solve(n1, sol)
					S2 = solve(n2, sol)
					S3 = solve(n3, sol)

					if(len(S0) != 0):
						S0.append(str(n[i]) + " + " + str(n[j]) + " = " + str(n[i]+n[j]))
						return S0
					elif(len(S1) != 0):
						S1.append(str(n[i]) + " - " + str(n[j]) + " = " + str(n[i]-n[j]))
						return S1
					elif(len(S2) != 0):
						S2.append(str(n[i]) + " * " + str(n[j]) + " = " + str(n[i]*n[j]))
						return S2
					elif(len(S3) != 0):
						S3.append(str(n[i]) + " / " + str(n[j]) + " = " + str(int(n[i]/n[j])))
						return S3
		return []

print("This program solves a countle-type problem. The program does not attempt to find the most efficient solution. Note that if a solution is found, the program may output operations which are unnecessary to arrive at the solution. It may take a few seconds to output its findings.")
numbers = list(map(int, input("Enter starting numbers (up to six values) separated by commas: ").split(',', 6)))
sol = int(input("Enter final number: "))

solution = solve(numbers, sol)

if(len(solution) == 0):
	print("No solution!")
else:
	for i in range(len(solution)-1, -1, -1):
		print(solution[i])

input()