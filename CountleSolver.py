def solve(n, sol):
	if len(n) == 0:
		return[]
	elif len(n) == 1:
		if n[0] == sol:
			return [["Solved!"]]
		else:
			return []
	elif sol in n:
		return [["Solved!"]]
	else:
		Sret = [] # Set of all solutions to return
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
					else:
						n1 = []
					n2.append(n[i]*n[j])
					if(n[j] != 0 and n[i]/n[j] == int(n[i]/n[j])):
						n3.append(int(n[i]/n[j]))
					else:
						n3 = []

					S = [solve(n0, sol), solve(n1, sol), solve(n2, sol), solve(n3, sol)]

					for soln in S[0]:
						soln.append([n[i], " + ", n[j], " = ", n[i]+n[j]])
						Sret.append(soln)
					for soln in S[1]:
						soln.append([n[i], " - ", n[j], " = ", n[i]-n[j]])
						Sret.append(soln)
					for soln in S[2]:
						soln.append([n[i], " * ", n[j], " = ", n[i]*n[j]])
						Sret.append(soln)
					for soln in S[3]:
						soln.append([n[i], " / ", n[j], " = ", int(n[i]/n[j])])
						Sret.append(soln)

		return Sret
	
def find_best_solution(solns):
	min_length = 10
	min_index = -1
	for i in range(len(solns)):
		if(len(solns[i]) < min_length):
			min_length = len(solns[i])
			min_index = i
	return solns[min_index]

print("This program solves a countle-type problem. The program will output a solution which requires the fewest number of steps (there may be more than one such solution). It may take a while to find an answer.")
numbers = list(map(int, input("Enter starting numbers (up to six values) separated by commas: ").split(',', 6)))
sol = int(input("Enter final number: "))

solutions = solve(numbers, sol)

if(len(solutions) == 0):
	print("No solutions!")
else:
	solution = find_best_solution(solutions)
	for i in range(len(solution)-1, -1, -1):
		for j in range(len(solution[i])):
			print(solution[i][j], end='')
		print()

input()