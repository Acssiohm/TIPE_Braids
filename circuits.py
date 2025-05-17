from braids_homotopy import *

class Permutation :
	def __init__(self, perm):
		self.perm = perm

	def apply(self, i):
		assert(i >= 1)
		k = i-1
		if k >= len(self.perm):
			return i  
		return self.perm[k]

	def __mul__(self, other):
		r = max(len(self.perm), len(other.perm))
		return Permutation([self.apply(other.apply(i+1)) for i in range(r)])
	
	def __truediv__(self,other):
		r = max(other.perm+[0])
		n = max(r, len(other.perm))
		res = [k for k in range(1, n+1)]
		for i, s in enumerate(other.perm):
			res[s-1] = i+1
		return self*Permutation(res)

	def __str__(self):
		return "(" + " ".join([str(i) for i in self.perm]) + ")"

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other):
		r = max(len(self.perm), len(other.perm))
		for i in range(1, r+1):
			if self.apply(i) != other.apply(i):
				return False
		return True 

	def nb_inv(self):
		n = 0
		for j in range(1, len(self.perm)+1):
			for i in range(1, j):
				if self.apply(i) > self.apply(j) :
					n += 1
		return n

	def inv(self):
		return Permutation([])/self

def cycle(liste):
	n = max(liste)
	res = [k for k in range(1, n+1)]
	prec = liste[-1]
	for a in liste :
		res[prec-1] = a
		prec = a
	return Permutation(res)

def r_gate(a, b):
	return (b, b.inv()*a*b)

def rinv_gate(a, b):
	return (a*b*a.inv(), a)	

class RCircuit :
	
	def __init__(self):
		self.constants = {}
		self.add_constant(0, cycle([1,4,3,5,2]))
		self.add_constant(1, cycle([1,5,3,4,2]))
		self.add_constant(2, cycle([1, 2, 4]))
		self.add_constant(3, cycle([5, 2, 1]))
		self.r_gates = []
		self.outputs = []
		self.inputs = []

	def add_constant(self, i,perm): 
		self.constants[2*i] = perm
		self.constants[2*i+1] = perm.inv()
	
	def add_r_gate(self, j, inv):
		self.r_gates.append((j, inv))

	def add_swap_gate(self, i):
		# print("  "*(2*i)+"x---x")
		self.add_r_gate(2*i+1, 1)
		self.add_r_gate(2*i  , 1)
		self.add_r_gate(2*i+2, 1)
		self.add_r_gate(2*i+1, 1)

	def add_c_gate(self, i, inv):
		# print("  "*(2*i) + "--- c"+("" if inv == 1 else "*"))
		self.add_r_gate(2*i+1, inv)
		self.add_r_gate(2*i+2, inv)
		self.add_r_gate(2*i+2, inv)
		self.add_r_gate(2*i+1, inv)

	def add_c(self, control, target, inv):
		assert(control != target)
		if control < target :
			for i in range(target-1, control, -1):
				self.add_swap_gate(i)
			self.add_c_gate(control, inv)
			for i in range(control+1, target):
				self.add_swap_gate(i)
		else :
			for i in range(control-1, target-1, -1):
				self.add_swap_gate(i)
			self.add_c_gate(target, inv)
			for i in range(target, control):
				self.add_swap_gate(i)

	def add_toffoli_gate(self, e1, e2, s):
		self.add_c(  3, s, 1)
		self.add_c( e2, s,-1)
		self.add_c(  1, s, 1)
		self.add_c( e1, s,-1)
		self.add_c(  2, s, 1)
		self.add_c( e2, s, 1)
		self.add_c(  0, s, 1)
		self.add_c( e1, s, 1)
		self.add_c(  3, s, 1)

	def set_outputs(self, outputs):
		self.outputs = outputs

	def add_output(self, output):
		self.outputs.append(output)

	def set_inputs(self, inputs):
		self.inputs = inputs

	def add_input(self, inpt):
		self.inputs.append(inpt)

	def calculate(self, entry):
		m = max(max(self.constants.keys()), max(self.inputs), max(self.outputs))
		lines = [Permutation([]) for _ in range(2*m+2)]
		for k,v in self.constants.items() :
			lines[k] = v
		for i,e in enumerate(self.inputs):
			lines[2*e] = entry[i]
			lines[2*e+1] = entry[i].inv()
		
		for r in self.r_gates :
			j,inv = r
			a = lines[j]
			b = lines[j+1]
			if inv == 1 :
				ra,rb = r_gate(a,b) 
			else :
				ra,rb = rinv_gate(a, b)
			lines[j] = ra
			lines[j+1] = rb

		for i in range(len(lines)//2):
			if lines[2*i]*lines[2*i+1] != Permutation([]) : 
				print("!!!!!!!!!!!!!!")

		return [lines[2*o] for o in self.outputs]

	def get_braid(self):
		return Braid([ (j+1)*inv for j,inv in self.r_gates])

zero = cycle([3, 4, 5])
one = cycle([4, 3, 5])

def test_toffoli_gate(c1 , c2, t):
	rc = RCircuit()
	rc.add_toffoli_gate(c1,c2,t)
	rc.set_inputs([t, c1, c2])
	rc.set_outputs([t, c1, c2])
	false_true = [zero, one]
	for i1,e1 in enumerate(false_true) :
		for i2,e2 in enumerate(false_true) :
			for i3,e3 in enumerate(false_true) :
				e = [e1, e2, e3]
				s = rc.calculate(e)
				res_expected = i1^(i2 * i3)
				print(i1, i2, i3, res_expected, s[0] == false_true[res_expected], e[1] == s[1] and e[2] == s[2]  )


if __name__ == "__main__" :
	# print(delta_n(20))
	test_toffoli_gate(5, 6, 4)
	# params = [(5, 6, 4), (5, 7, 4), (7, 8, 4)]
	# for p in params :
	# 	rc = RCircuit()
	# 	rc.add_toffoli_gate(*p)
	# 	b = rc.get_braid()
	# 	T = list(reversed(b.braid))
	# 	T = Braid(T)
	# 	T = forme_normale(T, 20)
	# 	print(T)
		# for i in range(len(T[1])-1):
		# 	s1 = T[1][i]
		# 	s2 = T[1][i+1]
		# 	assert(is_normal(s1, s2, 26))

# [hi, ihjikj, jk, kj, jihgfedcbkjihgfedclkml, cdefghijkbcdefghij, jk, kj, jihgfkjihglkml, lmghijfghi, ijklhighfedgfe, efghijdefghilm, ijklhi, ih]
# [hinomn, ihjikj, jk, kj, jihgfedcbkjihgfedclkml, cdefghijkbcdefghij, jk, kj, jihgfkjihglkmlnmon, nomnlmghijfghi, ijklhighfedgfe, efghijdefghilmno, ijklmnhi, ih]
# [nomnlmkljkijhiabcdefghijklmnopqrsabcdefghijklmnabcdefghijklmabcdefghijklabcdefghijkabcdefghijabcdefghicdefghcdefgcdefcdeadonmlkjihgfedcbaponmlkjihgfedcbqponmlkjihgfedcrqponmlkjihgfedabcaba, 
# fghefgihjikjlksrqponmlkjihgfedcbasrqposrqpsrqsrskjikjkmefghijklmnopqrsdefghijklmnopqrcdefghijklmnopqbcdefghijklmnopsrqsrs, 
# hijklmnoghijklmnfghijklmedcbfedcghijkl, cbdced, defghijklmnocdefghbc, cdefghijklmnobcdefghijklmn, nomnlmkljkijhighfgefdecd, defghcbdcedfeg, gfhgijklmno, ghijklmnofghijklmn, nomnlmkljkijhigh, hijklmnogfhgihjikjlkmlnm, mnolmn, nomn, nomlkjihgfednmlkjihgfe, efghijklmndefghijklm, mnlmkljkijhi, ijklmnohijklmn]