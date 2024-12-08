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
		return (self/other).is_null()

	def is_null(self) -> bool :
		return self.reduction_poignees()

	def retourner(self) :
		stable = False
		while not stable :
			self.simplify_epsilons()
			i = 0
			stable = True
			while i < len(self.braid) - 1 :
				j = i + 1
				if self.braid[i] < 0 and self.braid[j] > 0 :
					stable = False
					si = -self.braid[i]
					sj = self.braid[j]
					diff = abs(si - sj) 
					if diff > 1 :
						self.braid[i] = sj
						self.braid[j] = -si 
					elif diff == 0 :
						self.braid[i] = 0
						self.braid[j] = 0
					else : # diff == 1
						self.braid[i] = sj
						self.braid[j] = si
						self.braid.insert(j+1, -sj)
						self.braid.insert(j+2, -si)
				i += 1 
	
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
			assert(sk*s >= 0 and sk != 0) # Après réduction des poignées nichées on doit avoir que des sigma_k+1 du même signe
			s = sk
			node.elem = sk * k
			node.insert_before(-e*(k+1))
			node.insert_after(e*(k+1))
			node = next_node
		deb.remove()
		fin.remove()

	def reduction_poignees(self) :
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

def generer_tresses_aleatoires(n : int, brins : int, length : int) -> Braid :
	if length == 0 :
		for _ in range(n):
			yield []
	else :
		for l in generer_tresses_aleatoires(n, brins ,length-1):
			i = random.randint(-brins, brins)
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

b1 = Braid([-2, -2, -1, -1, 2, 2, 1, 1])
b2 = Braid([1, 1, 2, -1, -1, -1])
print(b1 == b2)