import pgzero

WIDTH = 600  #Dans ce bloc je definis toutes les variables.
HEIGHT = 852
waiting = True  #message d'acceuil
ent_num1 = False #est-on en train d'entrer le premier nombre?
ent_num2 = False #voir la ligne precedente
op = False #vrai lorsquon choisit l'operateur
adding = False #vrai lorsquon: additione
subtracting = False #soustrait
multiplying = False #mulitplie
dividing = False#divise
giveans = False #vrai lorsquon donne la reponse
a = 0 # premier chiffre
b = 0 # deuxieme chiffre
c = 0 # operateur qui sera affiche au GUI
ans = 0 # reponse
a = str(a)
b = str(b)
c = str(c)
ans = str(ans)
BOX = Rect((30, 50), (550, 180))
SBOX7 = Rect((45, 295), (110, 110)) #Ce bloc definit les rectangles qui serviront de bouttons pour entrer des nombres dans la calculatrice.
SBOX8 = Rect((185, 295), (110, 110))
SBOX9 = Rect((315, 295), (110, 110))
SBOX4 = Rect((45, 430), (110, 110))
SBOX5 = Rect((185, 430), (110, 110))
SBOX6 = Rect((315, 430), (110, 110))
SBOX1 = Rect((45, 565), (110, 110))
SBOX2 = Rect((185, 565), (110, 110))
SBOX3 = Rect((315, 565), (110, 110))
SBOX0 = Rect((45, 700), (110, 110))
SBOXN = Rect((450, 700), (110, 110))
SBOXM = Rect((450, 430), (110, 110))
SBOXD = Rect((450, 295), (110, 110))
SBOXP = Rect((450, 565), (110, 110))
SBOXV = Rect((185, 700), (110, 110))
SBOXE = Rect((315, 700), (110, 110))


def draw():
    global a, b, c, ans
    screen.clear()
    screen.blit('background', (0,0))
    if not giveans and not waiting: #affiche la question pendant que l'utilisateur l'entre
        screen.draw.text(a+c+b, topleft=(35, 130), color=(0, 0, 0), fontsize=48)
    else:
        screen.draw.text(ans, topleft=(35, 130), color=(0, 0, 0), fontsize = 48) #affiche la reponse
    if waiting:
        screen.draw.text('Press Enter to use the calculator', topleft=(35, 130), color=(0, 0, 0,), fontsize=48) #affiche le message d'acceuil
def on_key_down(key):
    global waiting
    global ent_num1
    if key==keys.RETURN: # debute la calculatrice
        waiting = False
        ent_num1 = True
def on_mouse_down(pos):
    global waiting, ent_num1, ent_num2, op, adding, subtracting, multiplying, dividing, a, b, c, SBOX0, SBOX1, SBOX2, SBOX3, SBOX4, SBOX5, SBOX6, SBOX7, SBOX7, SBOX8, SBOX9, SBOXP, SBOXN, SBOXM, SBOXV, SBOXD, SBOXE
    while ent_num1 == True: # recoit les intrants et construit un str representant le premier nombre
        if SBOX0.collidepoint(pos):
            a = a + '0'
        if  SBOX1.collidepoint(pos):
            a = a + '1'
        if  SBOX2.collidepoint(pos):
            a = a + '2'
        if  SBOX3.collidepoint(pos):
            a = a + '3'
        if  SBOX4.collidepoint(pos):
            a = a + '4'
        if  SBOX5.collidepoint(pos):
            a = a + '5'
        if  SBOX6.collidepoint(pos):
            a = a + '6'
        if  SBOX7.collidepoint(pos):
            a = a + '7'
        if  SBOX8.collidepoint(pos):
            a = a + '8'
        if  SBOX9.collidepoint(pos):
            a = a + '9'
        if  SBOXV.collidepoint(pos):
            a = a + '.'
        if  SBOXP.collidepoint(pos) or SBOXN.collidepoint(pos) or SBOXM.collidepoint(pos) or SBOXD.collidepoint(pos):
            ent_num1 is False and op is True # arrete d'attendre des intrants pour le premier nombre et attend un intrant pour l'operateur
    while op == True: # attend un intrant operateur
        if  SBOXP.collidepoint(pos):
            adding = True
            ent_num2 = True
            c = '+'
        if  SBOXN.collidepoint(pos):
            subtracting = True
            ent_num2 = True
            c = '-'
        if  SBOXM.collidepoint(pos):
            multiplying = True
            ent_num2 = True
            c = '*'
        if SBOXD.collidepoint(pos):
            dividing = True
            ent_num2 = True
            c = '/'
        op = False
    while ent_num2 == True: #attend un intrant pour le d
        if  SBOX0.collidepoint(pos):
            b = b + '0'
        if  SBOX1.collidepoint(pos):
            b = b + '1'
        if  SBOX2.collidepoint(pos):
            b = b + '2'
        if  SBOX3.collidepoint(pos):
            b = b + '3'
        if  SBOX4.collidepoint(pos):
            b = b + '4'
        if  SBOX5.collidepoint(pos):
            b = b + '5'
        if  SBOX6.collidepoint(pos):
            b = b + '6'
        if  SBOX7.collidepoint(pos):
            b = b + '7'
        if  SBOX8.collidepoint(pos):
            b = b + '8'
        if  SBOX9.collidepoint(pos):
            b = b + '9'
        if  SBOXV.collidepoint(pos):
            b = b + '.'
        if  SBOXP.collidepoint(pos) or SBOXN.collidepoint(pos) or SBOXM.collidepoint(pos) or SBOXD.collidepoint(pos):
            ent_num1 = False
    while  SBOXE.collidepoint(pos):
        a = float(a)
        b = float(b)
        c = float(c)
        ans = float(ans)
        if adding:
            ans = a + b
            adding = False
        if subtracting:
            ans = a - b
            subtracting = False
        if multiplying:
            ans = a * b
            multiplying = False
        if dividing:
            ans = a / b
            dividing = False

