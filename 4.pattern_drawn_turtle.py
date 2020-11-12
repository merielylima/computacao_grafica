from turtle import *

speed('fast')
#Desenho 3
penup()
setpos(150,0)
pendown()
pencolor('green')
sides = 8
def triangulo(size, sides):     

	for i in range(8):                                                                        
		fd(size)                                                                                             
		left(45)   

for i in range(5):
	triangulo(15*i, sides)

#desenho 1
penup()
goto(-250,0)
pendown()
pencolor('blue')
sides = 3
def triangulo(size, sides):     

	for i in range(3):                                                                        
		fd(size)                                                                                             
		left(120)   
for i in range(5):
	triangulo(15*i, sides)
#desenho 2
penup()
goto(-50,0)
pendown()
pencolor('red')
left(45) 

def triangulo(size, sides):     
	for i in range(4):                                                                        
		fd(size)                                                                                             
		left(90)   

for i in range(5):
	triangulo(15*i, sides)        
	
                          

done()
