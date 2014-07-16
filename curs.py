#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

"""
Autor: albertgumi@gmail.com
Data: 04/07/2014

Per a trobar una versió actualitzada del codi anar al repositori:
https://github.com/ertgumil/curs-python

El codi aquí mostrat es distribueix sota llicència GPLv3. Trobeu una còpa:
http://www.gnu.org/licenses/
"""


"""
TEMA 1
"""

def ex000():
	print("Has aconseguit cridar el fitxer de codi")


"""
TEMA 2
"""

def ex001():
	print("Hello world")


"""
TEMA 3
"""

def ex002():
	x = 1
	print("La variable x és un enter:\t", x)
	x = 2.0
	print("La variable x és un real:\t", x)
	x = "python"
	print("La variable x és un string:\t", x)

def ex003():
	x = 1
	y = 2.0
	print("Resultat de 1/2.0: ",x/y)

def ex004():
	x = 1
	print(x,": ",type(x))
	y = -2.0
	print(y,": ",type(y))
	z = x/y
	print(z,"(x/y): ",type(z))
	a = (2+3j) * (3+5j)
	print(a,": ",type(a))

def ex005():
	x = 2
	print("2 és enter? ", type(x) is int)
	x = 3.3
	print("3.3 és enter? ", type(x) is int)
	print("3.3 és real? ", type(x) is float)

def ex006():
	print("2+3:\t",2+3)
	print("2-3:\t",2-3)
	print("3*2:\t",3*2)
	print("9/2:\t",9/2)
	print("9//2:\t",9//2)
	print("14%5:\t",14%4)
	print("9**2:\t",9**2)

def ex007():
	l = [10,5,6,23,65,23,2,21,41]
	print("llista\n",l)
	l.append(10)
	print("append(10)\n", l)
	l.extend(l[:3])
	print("extend([10,5,6]\n",l)
	l.insert(0,2)
	print("insert(0,2)\n",l)
	l.remove(23)
	print("remove(23)\n",l)
	print("index(65)\n",l.index(65))
	print("count(10)\n",l.count(10))
	l.sort()
	print("sort()\n",l)
	l.reverse()
	print("reverse()\n",l)

def ex008():
	t = (1,2,3,'a')
	print("tupla\t\t",t)
	print("count('a')\t",t.count('a'))
	print("index('a')\t",t.index('a'))


def ex009():
	edat = {'salvador': 23, 'maria': 41, 'helena': 39}
	print("Diccionari:\n",edat)
	print("Valor helena\n",edat['helena'])
	print("Claus\n",edat.keys())
	print("Valors\n",edat.values())


"""
TEMA 4
"""

def ex010():
	print("True & 1\t",True & 1)
	print("0 and True\t",0 and True)
	print("True or False\t",True or False)
	print("True ^ False\t",True ^ False)
	print("not True\t",not True)
	print("not(True|False)\t",not(True | False))

def ex011():
	edat = -2
	if edat < 18 and edat >= 0:
	   print("Jove")
	elif edat >= 18:
	   print("Adult")
	else:
	   print("Encara no ha nascut")

def ex012():
	for i in [0, 1, 2]:
	    print("Hola " + str(i))
	print("Final")

def ex013():
	m = [[1,2,3],[4,5,6]]
	for i in m:
		for j in i:
			print(j)

def ex014():
	i = 0
	c = 0
	while i < 5:
		c = c + i + i + 1
		i = i + 1
		print(c)

def ex015():
	acc = 0
	for i in range(1,10):

		if i % 2 == 0:
			pass
		elif i % 5 == 0:
			break
		elif i % 3 == 3:
			acc = acc + 1
		else:
			continue
		acc = acc + 1
	print(acc)


"""
TEMA 5
"""

# Aquestes funcions es poden cridar per el nom estàndard exXYZ o pel nom propi

def f(x):
    return math.sin(x)

ex015 = f # Alias de la funció

def fact(x):
    llista = []
    for i in range(1,x+1):
        llista.append(math.factorial(i))
    return llista

ex016 = fact # Alias de la funció

def potencia (x = 2, y = 3):
    return x**y

ex017 = potencia # Alias de la funció

def imprimeix_matriu (matriu):
    for i in range(0,len(matriu)):
        for j in range(0,len(matriu[0])):
            print(matriu[i][j])

ex018 = imprimeix_matriu # Alias de la funció

def bool_a_binari(logic):
    if logic == True:
        return 1
    else:
        return 0

ex019 = bool_a_binari # Alias de la funció

def recursiu(n):
	if(n <= 0):
		return 1
	else:
		return n*recursiu(n-1)

ex020 = recursiu # Alias de la funció

def ex021():
	f = lambda x: math.sin(x)
	print(f(3))
	g = lambda x,y: -1 * x**y
	print(g(1,1))

def ex022():
	ll = list(range(1,10))
	def cub(x): return x**3
	print(list(map(cub,ll)))

def ex023():
	def fil(x):
		if(x < 0):
			return x    
	v = list(range(-10,10))
	print(list(filter(fil,v)))

def ex024():
	v = list(range(-10,10))
	print(list(filter(lambda x: x < 0,v)))


"""
TEMA 6
"""



"""
TEMA 7
"""

def ex025():
	for i in range(10,-10,-1):
	     try:
	         i/i
	     except ZeroDivisionError:
	         print ("Error: divisio entre 0")

def ex026():
	for i in range(10,-10,-1):
	     try:
	         i/i
	     except TypeError:
	         print ("Type Error")
	     except ValueError:
	         print ("Value Error")
	     except:
	         print ("Un altre error")

def ex027():
	for i in range(10,-10,-1):
		if(i==0):
			raise ValueError("No s'accepta el valor 0")
		i/i


"""
TEMA 8
"""

def ex028():
	arr = np.array([[1,2],[3,4]])
	print(arr)

def ex029():
	z = np.zeros((2,2), dtype=int)
	print("Zeros (2,2) int")
	print(z)
	z = np.zeros((2,2), dtype=complex)
	print("Zeros (2,2) complex")
	print(z)
	z = np.zeros((2,2), dtype=float)
	print("Zeros (2,2) float")
	print(z)

def ex030():
	o = np.ones((3,3), np.float128)
	print(o)

def ex031():
	m = np.array([[1,2],[3,4],[5,6]])
	print("Matriu inicial")
	print(m)
	z = np.zeros_like(m)
	print("Matriu zeros like")
	print(z)
	o = np.ones_like(m)
	print("Matriu ones like")
	print(o)

def ex032():
	arr = np.linspace(-2,2,6)
	print("Array inicial")
	print(arr)
	b = arr.reshape((2,3))
	print("Arrai redimensionada")
	print(b)

def ex033():
	x = np.zeros((3,3))
	print("x")
	print(x)
	y = x.copy()
	print("y copy()")
	print(y)
	y[1,1] = -1
	print("y modificada")
	print(y)
	print("x no es veu afectada")
	print(x)

def ex034():
	plt.plot([1,2,3,4,5])
	plt.show()

def ex035():
	x = np.arange(0, 2*np.pi, 0.1);
	y = np.sin(x)
	plt.plot(x, y)
	plt.show()

def ex036():
	plt.scatter([2.5,2,3],[3,2,1])
	plt.show()

def ex037():
	plt.bar([1,2,3],[4,9,2])
	plt.show()

def ex038():
	plt.pie([1,2,3,4,5,6])
	plt.show()

def ex039():
	X, Y = np.mgrid[0:10, 0:10]
	plt.quiver(X, Y)
	plt.show()