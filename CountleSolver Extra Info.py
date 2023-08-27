import time

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
			for j in range(i+1, len(n)):
				nNew = n.copy()
				nNew.remove(n[i])
				nNew.remove(n[j])
				
				n0 = nNew.copy()
				n1 = nNew.copy()
				n2 = nNew.copy()
				n3 = nNew.copy()
				n4 = nNew.copy()
				n5 = nNew.copy()

				n0.append(n[i]+n[j])
				if(n[i]-n[j] >= 0):
					n1.append(n[i]-n[j])
					n4 = []
				else:
					n1 = []
					n4.append(n[j]-n[i])
				n2.append(n[i]*n[j])
				if(n[j] != 0 and n[i]/n[j] == int(n[i]/n[j])):
					n3.append(int(n[i]/n[j]))
					n5 = []
				elif(n[i] != 0 and n[j]/n[i] == int(n[j]/n[i])):
					n3 = []
					n5.append(int(n[j]/n[i]))
				else:
					n3 = []
					n5 = []

				S = [solve(n0, sol), solve(n1, sol), solve(n2, sol), solve(n3, sol), solve(n4, sol), solve(n5, sol)]

				for soln in S[0]:
					soln.append(str(n[i]) + " + " + str(n[j]) + " = " + str(n[i]+n[j]))
					Sret.append(soln)
				for soln in S[1]:
					soln.append(str(n[i]) + " - " + str(n[j]) + " = " + str(n[i]-n[j]))
					Sret.append(soln)
				for soln in S[2]:
					soln.append(str(n[i]) + " * " + str(n[j]) + " = " + str(n[i]*n[j]))
					Sret.append(soln)
				for soln in S[3]:
					soln.append(str(n[i]) + " / " + str(n[j]) + " = " + str(int(n[i]/n[j])))
					Sret.append(soln)
				for soln in S[4]:
					soln.append(str(n[j]) + " - " + str(n[i]) + " = " + str(n[j]-n[i]))
					Sret.append(soln)
				for soln in S[5]:
					soln.append(str(n[j]) + " / " + str(n[i]) + " = " + str(int(n[j]/n[i])))
					Sret.append(soln)

	return Sret
	
def find_best_solution(solns):
	min_length = 10
	min_index = -1
	num_sols = 0
	for i in range(len(solns)):
		if(len(solns[i]) < min_length):
			min_length = len(solns[i])
			min_index = i
			num_sols = 1
		elif(len(solns[i]) == min_length):
			num_sols += 1
	return solns[min_index], num_sols

print("This program solves a countle-type problem. The program will output a solution which requires the fewest number of steps (there may be more than one such solution). It may take a few seconds to find an answer.")
numbers = list(map(int, input("Enter starting numbers (up to six values) separated by commas: ").split(',', 6)))
sol = int(input("Enter final number: "))

t0 = time.perf_counter()

solutions = solve(numbers, sol)

if(len(solutions) == 0):
	print(f"Completed in {time.perf_counter()-t0:0.4f} seconds.")
	print("No solutions!")
else:
	solution, num_sols = find_best_solution(solutions)
	print(f"Completed in {time.perf_counter()-t0:0.4f} seconds.")
	print("Number of minimum-step solutions found (including solutions with different order of operations): " + str(num_sols))
	print()
	for i in range(len(solution)-1, -1, -1):
		print(solution[i])

input()