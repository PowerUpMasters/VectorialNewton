from sympy import *

#  Metodo de Newton Vectorial para resolver Sistemas de
# Ecuaciones Lineales y No Lineales con Sympy en Python

# Savage Consultores | WhatsApp: +57 -(311)7103897

# Definimos Cuatro Variables Simbolicas
a = Symbol('a')
h = Symbol('h')
x = Symbol('x')
y = Symbol('y')

# Definimos el Sistema de Ecuaciones No Lineal
#  que queremos resolver en esta oportunidad
f = (a**2)+(h**2)-900
g = (h/a)-(10/x)
z = (y**2)+(a**2)-400
w = (y/a)-(10/(a-x))

# Definimos una Funcion Matricial y la Matriz
# Inversa de su Jacobiano de Forma Simbolica
M = Matrix([f,g,z,w])
JI = (M.jacobian([a,h,x,y]))**(-1)

s = Matrix([1,1,1.1,1]) # Aproximacion inicial
# Iteramos mientras que ||M|| > 1E-10
while(M.subs([(a,s[0]),(h,s[1]),(x,s[2]),(y,s[3])]).norm()>1E-10):
	# Actualizamos el valor de s segun Newton Vectorial
	s = s - (JI.subs([(a,s[0]),(h,s[1]),(x,s[2]),(y,s[3])])*M.subs([(a,s[0]),(h,s[1]),(x,s[2]),(y,s[3])]))

# Imprimimos las soluciones por consola		
print "\n==Soluciones originales==\n"
print "a = " + str(s[0])
print "h = " + str(s[1])
print "x = " + str(s[2])
print "y = " + str(s[3])
print "\n"
# Verificamos que cada entrada sea cero o muy cercana a cero
pprint (M.subs([(a,s[0]),(h,s[1]),(x,s[2]),(y,s[3])]))
# Si tomamos: a = abs(a),h = abs(h),x = abs(x),y = abs(y)
# vemos que tambien satisface la solucion del problema
print "\n==Soluciones modificadas==\n"
print "|a| = " + str(abs(s[0]))
print "|h| = " + str(abs(s[1]))
print "|x| = " + str(abs(s[2]))
print "|y| = " + str(abs(s[3]))
print "\n"
pprint (M.subs([(a,abs(s[0])),(h,abs(s[1])),(x,abs(s[2])),(y,abs(s[3]))]))