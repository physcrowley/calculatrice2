import pgzrun

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
a = "0" # premier chiffre -> sera affiché au début
b = "" # deuxieme chiffre -> vide au début
c = "" # operateur qui sera affiche au GUI -> vide au début
ans = 0.0 # reponse nulle au début
#a = str(a)
#b = str(b)
#c = str(c)
#ans = str(ans)
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
    # global a, b, c, ans # tu ne les modifies pas
    screen.clear()
    screen.blit('background', (0,0))
    
    if not giveans and not waiting: #affiche la question pendant que l'utilisateur l'entre
        to_show = str(a+c+b)
    else:
        to_show = str(ans) #affiche la reponse
    if waiting:
        to_show = 'Press Enter to use the calculator' #affiche le message d'acceuil

    screen.draw.text(to_show, topleft=(35, 130), color=(0, 0, 0), fontsize=48)
def on_key_down(key):
    global waiting, ent_num1, a
    if key==keys.RETURN: # debute la calculatrice
        waiting = False
        ent_num1 = True
        a = "" # enlève le premier 0
def on_mouse_down(pos):
    global waiting, giveans, ent_num1, ent_num2, op, adding, subtracting, multiplying, dividing, a, b, c, ans
    # global SBOX0, SBOX1, SBOX2, SBOX3, SBOX4, SBOX5, SBOX6, SBOX7, SBOX7, SBOX8, SBOX9, SBOXP, SBOXN, SBOXM, SBOXV, SBOXD, SBOXE
    if ent_num1 == True: # recoit les intrants et construit un str representant le premier nombre
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
            ent_num1 = False
            op = True
            #ent_num1 is False and op is True # arrete d'attendre des intrants pour le premier nombre et attend un intrant pour l'operateur
    if op == True: # attend un intrant operateur
        if  SBOXP.collidepoint(pos):
            adding = True
            ent_num2 = True
            c = '+'
        elif  SBOXN.collidepoint(pos):
            subtracting = True
            ent_num2 = True
            c = '-'
        elif  SBOXM.collidepoint(pos):
            multiplying = True
            ent_num2 = True
            c = '*'
        elif SBOXD.collidepoint(pos):
            dividing = True
            ent_num2 = True
            c = '/'
        op = False
        ent_num2 = True
    if ent_num2 == True: #attend un intrant pour le d
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
        if  SBOXE.collidepoint(pos): # juste =
        # if  SBOXP.collidepoint(pos) or SBOXN.collidepoint(pos) or SBOXM.collidepoint(pos) or SBOXD.collidepoint(pos):
            ent_num2 = False
    if  SBOXE.collidepoint(pos):
        giveans = True
        a = float(a)
        b = float(b)
        #c = float(c) # c'est l'opérateur, pas un nombre
        #ans = float(ans) #inutile
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

pgzrun.go()