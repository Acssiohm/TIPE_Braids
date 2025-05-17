import time
import random
from math import *

class Node :
	def __init__(self, elem):
		self.elem = elem
		self.next = None
		self.pred = None
	
	def link_to(self, other):
		self.next = other
		other.pred = self

	def insert_after(self, elem):
		assert( self.next != None )
		other = Node(elem)
		other.link_to(self.next)
		self.link_to(other)
	
	def insert_before(self, elem):
		assert(self.pred != None)
		self.pred.insert_after(elem)

	def remove(self):
		assert(self.pred != None)
		assert(self.next != None)
		self.pred.link_to(self.next)
		self.pred = None
		self.next = None

	def find_first_until(self, elem, end, rev = False):
		if self == end :
			return None
		elif elem == self.elem :
			return self
		elif not rev :
			return self.next.find_first_until(elem, end, rev) 
		else :
			return self.pred.find_first_until(elem, end, rev) 

class LinkedList :
	def __init__(self):
		self.first = Node(None)
		self.last = Node(None)
		self.first.link_to(self.last)
	
	def append(self, elem):
		self.last.insert_before(elem)

	def push_first(self, elem):
		self.first.insert_after(elem)

	def to_list(self):
		res = []
		node = self.first.next
		while node != self.last :
			res.append(node.elem)
			node = node.next
		return res

	def __str__(self):
		return str(self.to_list())

# renvoie une liste chainée des éléments de la liste l
def link_list(l : list) -> LinkedList :
	res = LinkedList()
	for elem in l :
		res.append(elem)
	return res

# renvoie -1, 0 ou 1 du même signe que a 
def signe (a : int) -> int :
	if a > 0 :
		return 1
	if a < 0 :
		return -1
	return 0

# Affiche la liste chainée entre deux noeuds donnés deb -> fin
def print_sub(deb : Node, fin : Node):
	if deb != fin and deb.next != None:
		print(deb.elem, end = ' ')
		print_sub(deb.next, fin)
	else :
		print()

class Braid :

	def __init__(self, b : list) :
		self.braid = b

	def copy(self) :
		return Braid(list(self.braid))

	# Retire les epsilons
	def simplify_epsilons(self) :
		self.braid = [ b for b in self.braid if b != 0 ]

	# Renvoie l'inverse de la tresse
	def inv(self) :
		n = len(self.braid)
		return Braid([-self.braid[n-i-1] for i in range(n)])

	# Renvoie la tresse à la puissance k dans Z
	def pow(self, k : int) :
		if k == 1:
			return self.copy()
		if k == 0:
			return Braid([])
		if k < 0 :
			return self.inv().pow(-k)

		square = self*self
		even_power = square.pow(k//2)
		if k % 2 == 1 :
			return even_power*self
		return even_power

	def __pow__(self, k) :
		return self.pow(k)

	def __mul__(self, other) :
		return Braid(self.braid+other.braid)

	def __truediv__(self, other) :
		return self * other.inv()

	def __eq__(self, other) :
		# assert(False)
		# print("eq")
		return (self/other).is_null()

	def is_null(self) -> bool :
		self.simplify_epsilons()
		return self.reduction_poignees()

	# -+ --> +- si e = 1 , +- --> -+ si e = -1
	def retourner(self, e=1) :
		stable = False
		x = self.copy()
		while not stable :
			self.simplify_epsilons()
			i = 0
			stable = True
			while i < len(self.braid) - 1 :
				j = i + 1
				if e*self.braid[i] < 0 and e*self.braid[j] > 0 :
					stable = False
					si = -self.braid[i]
					sj = self.braid[j]

					diff = abs(abs(si) - abs(sj)) 
					if diff > 1 :
						self.braid[i] = sj
						self.braid[j] = -si 
						# assert(x == self)
					elif diff == 0 :
						y = self.copy()
						self.braid[i] = 0
						self.braid[j] = 0

						# if(y != self) :
						# 	print(self, y)
						# 	exit(0)

					else : # diff == 1
						self.braid[i] = sj
						self.braid[j] = si
						self.braid.insert(j+1, -sj)
						self.braid.insert(j+2, -si)
						# assert(x == self)

				i += 1 
		self.simplify_epsilons()
	
	def reduire_en_mot_vide(self) :
		self.retourner()
		jonction = 0
		while jonction < len(self.braid) and self.braid[jonction] > 0 :
			jonction += 1
		positif = self.braid[:jonction]
		negatif = self.braid[jonction:]
		self.braid = negatif+positif
		self.retourner()

	def retournement_sous_mots(self) :
		b = self.copy()
		b.reduire_en_mot_vide()
		return b.braid == []

	def poignees_nichees(self, deb : Node, fin : Node, k : int) :
		assert(deb != fin)
		while True :
			s = 0
			node1 = None 
			node2 = None
			node = deb.next
			while node != fin :
				if abs(node.elem) == k :
					if node.elem*s >= 0 :
						s = node.elem
						node1 = node
					else :
						node2 = node
						break
				node = node.next
			if node2 == None :
				return 
			self.reduire_poignee(node1, node2, k)
			# ATTENTION : ici node1 et node2 ne sont pas définis car supprimés de la liste chainée 

	def reduire_poignee(self, deb : Node, fin : Node, k : int) :
		assert(abs(deb.elem) == k and abs(fin.elem) == k and signe(deb.elem)*signe(fin.elem) < 0) # une poignée de être de la forme sk^e.u.sk 
		self.poignees_nichees(deb, fin, k+1)
		e = signe(deb.elem)
		s = 0
		node = deb.next
		while node != fin :
			next_node = node.next
			if abs(node.elem) != k+1 :
				node = next_node
				continue
			sk = signe(node.elem)
			# assert(sk*s >= 0 and sk != 0) # Après réduction des poignées nichées on doit avoir que des sigma_k+1 du même signe
			s = sk
			node.elem = sk * k
			node.insert_before(-e*(k+1))
			node.insert_after(e*(k+1))
			node = next_node
		deb.remove()
		fin.remove()

	def reduction_poignees(self) :
		# print("réduction !")
		# assert(False)
		linked_braid = link_list(self.braid)
		while True :
			node = linked_braid.first.next 
			if node == linked_braid.last :
				return True
			mn = abs(node.elem) 
			while node != linked_braid.last : 
				mn = min(mn, abs(node.elem))
				node = node.next
			self.poignees_nichees(linked_braid.first, linked_braid.last, mn)
			node = linked_braid.first.next 
			while node != linked_braid.last : 
				if abs(node.elem) == mn :
					return False
				node = node.next

	def to_letters(self) :
		if self.braid == [] : 
			return "Empty_braid"
		res = ""
		for s in self.braid :
			l = chr(abs(s)+ord('a')-1) if s != 0 else '.' 
			if s < 0 :
				l = l.upper()
			res += l
		return res

	def to_string(self) :
		if self.braid == [] : 
			return "Empty_braid"
		res = ""
		for s in self.braid :
			res += "("+str(s)+")"
		return res

	def __str__(self) :
		return self.to_letters()

	def __repr__(self):
		return self.to_letters()

	def calc_permutation(self):
		"""
		calcule la permutation induite par une tresse sur les brins
		"""
		perm = list(range(self.n + 1))
		for generator in self.braid:
			i = abs(generator) - 1
			perm[i], perm[i + 1] = perm[i + 1], perm[i]
		return tuple(perm)
	

def delta_n(n):
	"""
	génère la TF ∆n
	"""
	delta = []
	for k in range(1, n):
		for i in range(1, n - k + 1):
			delta.append(i)
	return Braid(delta)

def grille(u, v):
	x = u.inv()*v
	x.retourner()
	# assert(u.inv()*v == x)
	vp = Braid([ s for s in x.braid if s > 0])
	up = Braid([ s for s in x.braid if s < 0])
	# assert(vp.braid + up.braid == x.braid)
	up = up.inv()
	# assert(u*vp == v*up)
	return (up, vp)

def anti_grille(u, v):
	x = u*v.inv()
	x.retourner(-1)
	up = Braid([ s for s in x.braid if s > 0])
	vp = Braid([ s for s in x.braid if s < 0])
	# assert(vp.braid + up.braid == x.braid)
	vp = vp.inv()
	# assert(vp*u==up*v)
	return (up, vp)

memo = dict()
def pgcd_comp_a(a, b):
	# memo[(a.braid, b.braid)] = 0
	(c, d) = grille(a, b) # ad = bc
	(e, f) = anti_grille(c, d) # ed = fc
	(g, p) = anti_grille(a, e) # pa = ge et p = 1 --> a = ge
	assert(p.braid == [])
	# assert(a == g*e)
	return (g, e) # pgcd(a, b) , (g\a)

def dr(t,  dn):
	(x, res) = pgcd_comp_a(dn, t)
	# assert( x == t )
	# assert(x*res == dn)
	return res

def PaveA(t, s, dn):
	return pgcd_comp_a(t*s, dn)

def MultGauche(S, t, dn):
	Sp = []
	curr_t = t
	for s in S :
		(sp, tp) = PaveA(curr_t, s, dn)
		Sp.append(sp)
		curr_t = tp
	if curr_t.braid != []:
		Sp.append(curr_t)
	# print(S, Sp, t)
	return Sp

# def PaveP(t, s, dn):
# 	return pgcd_comp_a(s*t, dn)

def phi(t, m, n):
	if m % 2 == 1 :
		return Braid([ n-s for s in t.braid])
	return t.copy()

def add_simple_to_normal_form(forme_normale, t, e, n, dn):
	m = forme_normale[0]
	# print(m)
	if e == 1:
		t0 = phi(t, m, n)
	elif e == -1 :
		t0 = phi(dr(t, dn), m+1, n) # m+1 car on a mis dr(t) au lieu de dr_tilde(t)
		m -= 1
	else :
		print("ERREUR")
		exit(0)
	pos_forme_normale = MultGauche(forme_normale[1], t0 , dn)
	# print("égalité")
	if pos_forme_normale[0] == dn :
		return (m+1, pos_forme_normale[1:])
	return (m, pos_forme_normale)

def normal_form(b, n, dn):
	print(b)
	S = (0, [])
	for s in reversed(b.braid):
		S = add_simple_to_normal_form(S, Braid([abs(s)]), signe(s), n, dn )
		# print(s, S)
		print("#", end = "")
		if S[1][-1].braid == [] :
			S = (S[0], S[1][:-1])
	print()
	# 	# print(S)
	# while S[1][-1].braid == []: #################################################### 
	# 	# assert(S[1][-1].braid == [])
	# 	S = (S[0], S[1][:-1])
	return S

def forme_normale(b, n):
	for s in b.braid :
		assert(s < n)
	return normal_form(b, n, delta_n(n))

def generer_tresses_aleatoires(n : int, brins : int, length : int) -> Braid :
	if length == 0 :
		for _ in range(n):
			yield []
	else :
		for l in generer_tresses_aleatoires(n, brins ,length-1):
			i = random.randint(-(brins-1), brins-1)
			if i == 0 :
				i = 1
			yield [i]+l


def time_test (n : int, brins : int, size: int ) -> (float, float, float) :
	duree1 = 0
	duree2 = 0
	# n = 0 
	for i in generer_tresses_aleatoires(n, brins, size):
		# n += 1
		b = Braid(i)
		time0 = time.time()
		v1 = b.reduction_poignees()
		time1 = time.time()
		v2 = b.retournement_sous_mots()
		time2 = time.time()
		if v1 != v2 :
			print(v1, v2)
		duree1 += time1 - time0
		duree2 += time2 - time1
	ratio =  duree2/duree1 if duree1 != 0 else -1
	print(size)
	print("poignees : ",duree1/n, "\nretournement :" , duree2/n, "\nratio :", ratio)
	print()
	return duree1, duree2, ratio

def time_tests(n : int, brins : int, max_size : int) -> list :
	assert(max_size > 2)
	res = [time_test(n, brins, s) for s in range(2, max_size)]
	return res

def braid_of_string( s ) :
	res = []
	for a in s :
		i = ord(a)
		if ord('a') <= i <= ord('z') :
			res.append(i-ord('a')+1)
		elif ord('A') <= i <= ord('Z'):
			j = i-ord('A')+1
			res.append(-j)
		else :
			print("unrecognized letter ", a )
			exit(1)
	return res 

def braid_of_normal(nf, n):
	m = nf[0]
	S = nf[1]
	res = delta_n(n)**m
	for b in S :
		res = res*b
	return res

def test_normal(b, n):
	return b == braid_of_normal( forme_normale(b,n), n)

def is_normal(s1, s2, n):
	dn = delta_n(n)
	(g, e) = pgcd_comp_a(dn, s1*s2)
	return g == s1 

if __name__ == "__main__" :
	T = [8, 9, 9, 8, 2, 3, 1, 2, 6, 7, 5, 6, 10, 11, 9, 10, 6, 7, 5, 6, -10, -11, -11, -10, 8, 9, 9, 8, 10, 11, 9, 10, 8, 9, 9, 8, 
	10, 11, 9, 10, 4, 5, 3, 4, 4, 5, 3, 4, 10, 11, 11, 10, 8, 9, 9, 8, 10, 11, 9, 10, 6, 7, 5, 6, -10, -11, -11, -10, 
	10, 11, 11, 10, 6, 7, 5, 6, 2, 3, 1, 2, 10, 11, 9, 10, 6, 7, 5, 6, 4, 5, 3, 4, 4, 5, 3, 4, 10, 11, 9, 10, 
	10, 11, 9, 10, 8, 9, 9, 8, 12, 13, 11, 12, 12, 13, 11, 12, 10, 11, 9, 10, 6, 7, 5, 6, 12, 13, 11, 12, 12, 13, 11, 12]
	# T = [1, -2, 1, 2, 1, 3, -1, -2, -1, -2, -1, 2, 2, -3, -2]
	T = Braid(T)
	# T = Braid(braid_of_string("braidwordaBabacABABAbbCB"))

	T = forme_normale(T, 20)
	print(T, len(T[1]))
	for i in range(len(T[1])-1):
		s1 = T[1][i]
		s2 = T[1][i+1]
		assert(is_normal(s1, s2, 26))
	# print(forme_normale(Braid([-1]), 3), test_normal(Braid([-1, 2, 1]), 3))
	# N = 6
	# for b in generer_tresses_aleatoires(100, N, 10):
		# print(test_normal(Braid(b), N))
