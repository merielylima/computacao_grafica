import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (10, 8)
fig, ax = plt.subplots()
#contorno
lx = [0,0, 8,8, 0]
ly = [0,6,6,0,0]
plt.plot(lx,ly, color='k')

#estrutura do controle
plt.scatter([5,3],[3.25,3.25],marker = '_',s=20000,linewidth=135,c='#0f2936')#SOMBRA
plt.scatter(2, 3,s=28000, c='#0f2936')#SOMBRA
plt.scatter(6, 3,s=28000, c='#0f2936')#SOMBRA

plt.scatter([5,3],[3.25,3.25],marker = '_',s=20000,linewidth=120,c='#596673') #MEIO
plt.scatter(2, 3,s=25000, c='#596673') # CIRCULO ESQUERDO
plt.scatter(6, 3,s=25000, c='#596673') # CIRCULO DIREITO

#CRUZ 
plt.scatter(2, 3,s=6000,marker = 'P', linewidth=15,c='#0f2936') #CRUZ ESQUERDA SOMBRA
plt.scatter(2, 3,s=6000,marker = 'P', linewidth=9,c='#a3bfcb')  #RUZ ESQUERDA
plt.scatter(6, 3,s=6000,marker = 'X', linewidth=15,c='#0f2936') #CRUZ DIREITA SOMBRA
plt.scatter(6, 3,s=6000,marker = 'X', linewidth=9,c='#a3bfcb')  #CRUZ DIREITA

plt.scatter(2,3,s=600, marker='P', edgecolor='#0f2936', linewidth=7, facecolor='#a3bfcb') # CRUZ MENOR
plt.scatter(2, 3,s=250,marker = 'o',c='r')      #circulo maior
plt.scatter(2, 3,s=10,marker = 'o',c='#a3bfcb') #circulo menor

#SETAS
plt.scatter(2.45, 3,s=200,marker ='>',linewidth=9,c='#0f2936')   # LEFT
plt.scatter(1.55, 3,s=200,marker ='<',linewidth=9, c='#0f2936')  #RIGHT
plt.scatter(2, 3.45,s=200,marker = '^', linewidth=9,c='#0f2936') #UP
plt.scatter(2, 2.55,s=200,marker = 'v',linewidth=9, c='#0f2936') #DOWN

#SOMBRAS START E SELECT
plt.scatter([4.4,3.4],[3,3],marker = ',', s=20,linewidth=13,c='#0f2936')
plt.scatter([4.5,3.5],[3,3],marker = ',', s=20,linewidth=13,c='#0f2936')
plt.scatter([4.6,3.6],[3,3],marker = ',', s=20,linewidth=13,c='#0f2936')

#START E SELECT
plt.scatter([4.4,3.4],[3,3],marker = ',', s=21,linewidth=5,c='#a3bfcb')
plt.scatter([4.5,3.5],[3,3],marker = ',', s=21,linewidth=5,c='#a3bfcb')
plt.scatter([4.6,3.6],[3,3],marker = ',', s=21,linewidth=5,c='#a3bfcb')

#LED
plt.scatter([4],[2.65],marker = ',', s=10,linewidth=10,c='r')
plt.scatter([4],[2.65],marker = ',', s=1,linewidth=1,c='#cccccc')

#SOMBRAS BOTOES
plt.scatter(5.7, 3.3,s=400,marker = 'o', linewidth=10,c='#0f2936') #RED
plt.scatter(6.3, 3.3,s=400,marker = 'o', linewidth=10,c='#0f2936') #BLUE
plt.scatter(6.3, 2.7,s=400,marker = 'o', linewidth=10,c='#0f2936') #GREEN
plt.scatter(5.7, 2.7,s=400,marker = 'o', linewidth=10,c='#0f2936') #YELLOW

#BOTÕES
plt.scatter(5.7, 3.3,s=300,marker = 'o', linewidth=7,c='r')       #RED
plt.scatter(6.3, 3.3,s=300,marker = 'o', linewidth=7,c='#0f2936')       #BLUE
plt.scatter(6.3, 2.7,s=300,marker = 'o', linewidth=7,c='r') #GREEN
plt.scatter(5.7, 2.7,s=300,marker = 'o', linewidth=7,c='#0f2936') #YELLOW

# BARRA SOMBRA
plt.scatter(4,3.7,marker = '_',s=6000,linewidth=33,c='#ffff')#SOMBRA
plt.scatter(3.4, 3.7,s=1000, c='#ffff')#SOMBRA
plt.scatter(4.6, 3.7,s=1000, c='#ffff')#SOMBRA

# BARRA
plt.scatter(4,3.7,marker = '_',s=6000,linewidth=27,c='#3c515c')#
plt.scatter(3.4, 3.7,s=700, c='#3c515c')#
plt.scatter(4.6, 3.7,s=700, c='#3c515c')#

plt.text(3.35, 3.6, "Nintendo",fontsize=16, c = '#ffff',weight="bold")

#FIO DO CONTROLE
plt.plot([4,4,5, 5],[4.33,4.7,5.3,5.5], c= 'k', linewidth = 10)

#plt.savefig('controle.png', format='png')
plt.show()


