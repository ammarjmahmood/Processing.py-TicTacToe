#Keep state of each sqaure on board
top_left = 0 # 0 - empty, 1 - x, 2 - O
top_middle = 0
top_right = 0
 
middle_left = 0
middle_middle = 0
middle_right = 0
 
 
bottom_left = 0
bottom_middle = 0
bottom_right = 0
 
#starts with X
turn = 1
 
#game over
game_over = False
 
#tie game
tie_game = False
 
#start game is false
start = False
 
#num of clicks to determine winner
numOfClicks = 0  #number of clicks
 
#num of games
numOfGames = 0
 
#allows a box not to be clicked twice
mouse_pressed = False
mouse_pressed2 = False
mouse_pressed3 = False
mouse_pressed4 = False
mouse_pressed5= False
mouse_pressed6= False
mouse_pressed7= False
mouse_pressed8= False
mouse_pressed9= False
 
#x and o score
xscore = 0
oscore = 0
noscore = 0

#ultimate winner
xultimate = False
oultimate = False
noultimate = False

#amount of rounds
amount_rounds = 0
 
#################################################################################################################
 
 
def setup():
    global winner_winner_chicken_dinner
    winner_winner_chicken_dinner = loadImage( "winner.gif" )
    size(800,750)
    
    
def draw():
    global start
    global xultimate 
    global oultimate
    global noultimate
    
    #this if statement allows us to draw the gameboard
    starting_game_function_key()
    if start == False:
        reset() 
    elif xultimate == True :
        xultimateScreen()
    elif oultimate == True :
        oultimateScreen()
    elif noultimate == True :
        noultimateScreen()
    else :
        draw_game_board()
        textSize(22)
        text("RESTART GAME/START A NEW ROUND - SPACE BAR", 20,730)
        
        score_board()
        draw_the_players()
        check_winner()
        check_tie_game()
        ultimate_winner()
 
 
 
###################################################################################################################
 
def starting_game_function_key(): 
    global start
    
    if start == False :
        if mousePressed and (mouseButton == RIGHT) or mousePressed and (mouseButton == LEFT) : # to start the game 
            start = True 
 
    
def keyPressed() :
    global start
    
    if keyCode == 32: # to restart # 32 = space bar
        start = False
        
            
 
 
def draw_game_board():
    strokeWeight(10)
    for y in range(3):
        for x in range(3) :
            fill(255)
            rect(200*x,200*y,200,200)
    
    
def reset() :
    global mouse_pressed,mouse_pressed2,mouse_pressed3,mouse_pressed4,mouse_pressed5,mouse_pressed6,mouse_pressed7,mouse_pressed8,mouse_pressed9
    global top_left, top_middle, top_right
    global middle_left, middle_middle, middle_right
    global bottom_left, bottom_middle, bottom_right
    global game_over 
    global tie_game
    global numOfClicks
    global turn
    global oultimate
    global xultimate
    global noultimate
    global xscore
    global oscore
    global noscore
    global amount_rounds
    
    strokeWeight(10)
    rect(600, -10, 220, 780)
    noStroke()
    fill(41, 217, 185) # blue turquoise ish background
    rect(0,0,600,750)
    #rect color
    fill(150)
    #text color
    fill(255)
    textSize(50)
    text("TIC - TAC - TOE", 100, 100)
    text("---------------",100,150)
    textSize(25)
    text("Instructions:", 220,200)
    text("The game is played on a grid that's 3 by 3", 40, 250)
    text("You are X and your friend is O", 120, 300)
    text("When all 9 squares are full, the game is over", 25,350)
    text("The first player to get 3, 3 in a row wins", 40,400)
    textSize(25)
    text("----------------------------", 100,450)
    textSize(22.5)
    text("TO RESTART GAME AFTER WIN/TIE PRESS UP ARROW", 20,500)
    text("CLICK ANYWHERE TO PLAY ", 140,550)
    score_board()
    
    if top_left == 1 or top_left == 2 or top_left == 0:
        top_left = 0
    if top_middle == 1 or top_middle == 2 or top_middle == 0:
        top_middle = 0
    if top_right == 1 or top_right == 2 or top_right == 0:
        top_right = 0
    
    if middle_left == 1 or middle_left == 2 or middle_left == 0:
        middle_left = 0
    if middle_middle == 1 or middle_middle == 2 or middle_middle == 0:
        middle_middle = 0
    if middle_right == 1 or middle_right == 2 or middle_right == 0:
        middle_right = 0
    
    if bottom_left == 1 or bottom_left == 2 or bottom_left == 0:
        bottom_left = 0
    if bottom_middle == 1 or bottom_middle == 2 or bottom_middle == 0:
        bottom_middle = 0
    if bottom_right == 1 or bottom_right == 2 or bottom_right == 0:
        bottom_right = 0
    
    if game_over :
        game_over = False
    
    if tie_game :
        tie_game = False
    
    if mouse_pressed :
        mouse_pressed = False
    
    if mouse_pressed2 :
        mouse_pressed2 = False
    
    if mouse_pressed3 :
        mouse_pressed3 = False
    
    if mouse_pressed4 :
        mouse_pressed4 = False
    
    if mouse_pressed5 :
        mouse_pressed5 = False
    
    if mouse_pressed6 :
        mouse_pressed6 = False
    
    if mouse_pressed7 :
        mouse_pressed7 = False
    
    if mouse_pressed8 :
        mouse_pressed8 = False
    
    if mouse_pressed9 :
        mouse_pressed9 = False
 
    numOfClicks = 0
    turn = 1
    
    if xultimate == True :
        xultimate = False
    if oultimate == True:
        oultimate = False
    if noultimate == True:
        noultimate = False
        
        
    if xscore == 3 :
        xscore = 0
        oscore = 0
        noscore = 0
        amount_rounds = 0
    if oscore == 3 :
        oscore = 0
        xscore = 0
        noscore = 0
        amount_rounds = 0
    if noscore == 3 or noscore > 3 :
        noscore = 0
        xscore = 0
        amount_rounds = 0
        oscore = 0
    if amount_rounds == 3:
        noscore = 0
        xscore = 0
        amount_rounds = 0
        oscore = 0
        
    stroke(8, 8, 8)
        
def draw_the_players():
    global top_left, top_middle, top_right
    global middle_left, middle_middle, middle_right
    global bottom_left, bottom_middle, bottom_right
    
    if top_left == 2:
        # draws O
        ellipse(100,100,150,150)
    elif top_left == 1:
        # draw top left x 
        line(0,0,200,200)
        line(200,0,0,200)
        
    if top_middle == 2:
        #draws O
        ellipse(300,100,150,150)
    elif top_middle == 1:
        #Draw X
        line(200,0,400,200)
        line(400,0,200,200)
        
    if top_right == 2:
        #draw O
        ellipse(500,100,150,150)
    elif top_right == 1:
        #draws x
        line(400,0,600,200)
        line(600,0,400,200)    
        
#####################################################
        
    if middle_left == 2:
        #draws O
        ellipse(100,300,150,150)
    elif middle_left == 1:
        #draw X
        line(0,200,200,400)
        line(200,200,0,400)
        
    if middle_middle == 2:
        #draws O
        ellipse(300,300,150,150)
    elif middle_middle == 1:
        #draws X
        line(200,200,400,400)
        line(400,200,200,400)
        
    if middle_right == 2:
        #Draws O
        ellipse(500,300,150,150)
    elif middle_right == 1:
        #draw X
        line(400,200,600,400)
        line(600,200,400,400)
        
#######################################################    
        
        
    if bottom_left == 2:
        #draws O
        ellipse(100,500,150,150)
    if bottom_left == 1:
        #draw X
        line(0,400,200,600)
        line(200,400,0,600)
 
    if bottom_middle == 2:
        #draw O
        ellipse(300,500,150,150)
    elif bottom_middle == 1:
        #draws X
        line(200,400,400,600)
        line(400,400,200,600)
            
    if bottom_right == 2:
        #draws O
        ellipse(500,500,150,150)    
    elif bottom_right == 1:
        #draws X
        line(400,400,600,600)
        line(600,400,400,600)
      
    
############################################################################################################################################
# cross line in row if win
#across
    if top_left == 1 and top_middle == 1 and top_right == 1 : 
        stroke(245, 66, 84)
        line(0,100,600,100)
    elif top_left == 2 and top_middle == 2 and top_right == 2:
        stroke(245, 66, 84)
        line(0,100,600,100)
        
    elif middle_middle == 1 and middle_left == 1 and middle_right == 1:
        stroke(245, 66, 84)
        line(0,300,600,300)
    elif middle_middle == 2 and middle_left == 2 and middle_right == 2 :
        stroke(245, 66, 84)
        line(0,300,600,300)
    
    elif bottom_left == 1 and bottom_middle == 1 and bottom_right == 1:
        stroke(245, 66, 84)
        line(0,500,600,500)
    elif bottom_left == 2 and bottom_middle == 2 and bottom_right == 2 :
        stroke(245, 66, 84)
        line(0,500,600,500)
    
#down
    elif top_left == 1 and middle_left == 1 and bottom_left == 1:
        stroke(245, 66, 84)
        line(100,0,100,600)
    elif top_left == 2 and middle_left == 2 and bottom_left == 2 :
        stroke(245, 66, 84)
        line(100,0,100,600)
    
    elif top_middle == 1 and middle_middle == 1 and bottom_middle == 1:
        stroke(245, 66, 84)
        line(300,0,300,600)
    elif top_middle == 2 and middle_middle == 2 and bottom_middle == 2 :
        stroke(245, 66, 84)
        line(300,0,300,600)
    
    elif top_right == 1 and middle_right == 1 and bottom_right == 1:
        stroke(245, 66, 84)
        line(500,0,500,600)
    elif top_right == 2 and middle_right == 2 and bottom_right == 2 :
        stroke(245, 66, 84)
        line(500,0,500,600)
 
#diagonal 
    elif top_left == 1 and middle_middle == 1 and bottom_right == 1:
        stroke(245, 66, 84)
        line(0,0,600,600)
    elif top_left == 2 and middle_middle == 2 and bottom_right == 2 :
        stroke(245, 66, 84)
        line(0,0,600,600)
    
    elif top_right == 1 and middle_middle == 1 and bottom_left == 1:
        stroke(245, 66, 84)
        line(600,0,0,600)
    elif top_right == 2 and middle_middle == 2 and bottom_left == 2 :
        stroke(245, 66, 84)
        line(600,0,0,600)
 
 
 
 
def score_board():
    global xscore
    global oscore
    global noscore
    
    rect(600, 0, 220, 780)
    fill(8, 8, 8)
    
    xscoreboard = ("X's Score: %i" % (xscore))
    text(xscoreboard, 620, 275)
    
    oscoreboard = ("O's Score: %i" % (oscore))
    text(oscoreboard, 620, 315)
    
    noscoreboard = ("Tie Game: %i" % (noscore))
    print(noscoreboard)
 
    
    
def check_winner():
    global game_over 
    global turn
    global xscore
    global oscore
    global numOfGames
    global amount_rounds
    
    if game_over == True:
        if turn == 2:
            fill(255)
            textSize(50)
            x = ("X wins round %i of 3" % (amount_rounds))#xscore
            text(x, 20, 675)
        elif turn == 1:
            fill(255)
            textSize(50)
            o = ("O wins round %i of 3" % (amount_rounds))#oscore
            text(o, 20, 675)
  
def check_tie_game():
    global tie_game
    global noscore
    global amount_rounds
    
    if tie_game == True:
        fill(255)
        textSize(50)
        roundss = ("Tie Game! Round %i of 3" % (amount_rounds))#xscore
        text(roundss, 20, 675)
        print("Amount of noscore rounds", noscore)
        
 
def switch_turn() :
        global turn
        #switch turns
        if turn == 1:
            turn = 2
        else :
            turn = 1    
    
    
def ultimate_winner():
    global xscore
    global oscore
    global noscore
    global xultimate
    global noultimate
    global oultimate
    global amount_rounds
    
    if xscore == 3 and oscore < 3:
        print("X is the ultimate WINNER")
        xultimate = True
    elif oscore == 3 and xscore < 3:
        print("O is the ultimate WINNER")
        oultimate = True
    elif noscore == 3 and xscore == oscore:
        print("This is a ultimate tie game")
        noultimate = True
    elif amount_rounds == 3 and xscore > oscore:
        print("X is the ultimate WINNER")
        xultimate = True
    elif amount_rounds == 3 and oscore > xscore :
        print("O is the ultimate WINNER")
        oultimate = True
    elif amount_rounds == 3 and oscore == xscore :
        print("This is a ultimate tie game")
        noultimate = True
        
        
def xultimateScreen():
    
    fill(41, 217, 185) # blue turquoise ish background
    rect(0,0,600,700)
    #rect color
    fill(150)
    #text color
    fill(255)
    textSize(50)
    text("X WINS THE GAME", 100, 100)
    text("---------------",100,150)
    stroke(8, 8, 8)
    image(winner_winner_chicken_dinner, 90, 250, 450,360)
    #                                    x    y
 
    
def oultimateScreen():

    fill(41, 217, 185) # blue turquoise ish background
    rect(0,0,600,700)
    #rect color
    fill(150)
    #text color
    fill(255)
    textSize(50)
    text("O WINS THE GAME", 100, 100)
    text("---------------",100,150)
    image(winner_winner_chicken_dinner, 90, 250, 450,360)
    
    
def noultimateScreen():
    
    fill(41, 217, 185) # blue turquoise ish background
    rect(0,0,600,700)
    #rect color
    fill(150)
    #text color
    fill(255)
    textSize(50)
    text("Everyone is a Winner:)", 50, 100)
    text("---------------",90,150)
    image(winner_winner_chicken_dinner, 90, 250, 450,360)
    
    
def mousePressed():
    println( [mouseX, mouseY] )
    global numOfClicks
    global game_start
    global top_left, top_middle, top_right
    global middle_left, middle_middle, middle_right
    global bottom_left, bottom_middle, bottom_right
    global turn
    global game_over
    global mouse_pressed,mouse_pressed2,mouse_pressed3,mouse_pressed4,mouse_pressed5,mouse_pressed6,mouse_pressed7,mouse_pressed8,mouse_pressed9
    global tie_game
    global xscore
    global oscore
    global noscore
    global amount_rounds
    
    if game_over == False and start == True :
        
        if (mouseX > 0 and mouseX < 200) and (mouseY > 0 and mouseY < 200) and (mouse_pressed == False) :
            #player 1's turn/move since 1 = x
            top_left = turn
            switch_turn()
            mouse_pressed = True
            numOfClicks = numOfClicks +1
            
        elif (mouseX > 200 and mouseX < 400) and (mouseY > 200 and mouseY < 400) and (mouse_pressed2 == False) :
            middle_middle = turn
            switch_turn()
            mouse_pressed2 = True
            numOfClicks = numOfClicks +1
            
        elif (mouseX > 400 and mouseX < 600) and (mouseY > 400 and mouseY < 600) and (mouse_pressed3 == False):
            bottom_right = turn
            switch_turn()
            mouse_pressed3 = True
            numOfClicks = numOfClicks +1
            
        elif (mouseX > 0 and mouseX < 200) and (mouseY > 200 and mouseY < 400) and (mouse_pressed4 == False):
            middle_left = turn
            switch_turn()
            mouse_pressed4 = True
            numOfClicks = numOfClicks +1
            
        elif (mouseX > 200 and mouseX < 400) and (mouseY > 400 and mouseY < 600) and (mouse_pressed5 == False):
            bottom_middle = turn
            switch_turn()
            mouse_pressed5 = True
            numOfClicks = numOfClicks +1
            
        elif (mouseX > 0 and mouseX < 200) and (mouseY > 400 and mouseY < 600) and (mouse_pressed6 == False):
            bottom_left = turn 
            switch_turn()
            mouse_pressed6 = True
            numOfClicks = numOfClicks +1
            
        elif (mouseX > 200 and mouseX < 400) and (mouseY > 0 and mouseY < 200) and (mouse_pressed7 == False):
            top_middle = turn
            switch_turn()
            mouse_pressed7 = True
            numOfClicks = numOfClicks +1
            
        elif (mouseX > 400 and mouseX < 600) and (mouseY > 0 and mouseY < 200) and (mouse_pressed8 == False) :
            top_right = turn
            switch_turn()
            mouse_pressed8 = True
            numOfClicks = numOfClicks +1
            
        elif (mouseX > 400 and mouseX < 600) and (mouseY > 200 and mouseY < 400) and (mouse_pressed9 == False):
            middle_right = turn
            switch_turn()
            mouse_pressed9 = True
            numOfClicks = numOfClicks +1
    
    # check for winners
        
        if top_left == 1 and top_middle == 1 and top_right == 1 :
            print("Winner!! X")
            game_over = True
            xscore += 1
            amount_rounds += 1
            print("X:", xscore, "-", "O:", oscore)
        elif top_left == 2 and top_middle == 2 and top_right == 2 :
            print("Winner!! O")
            game_over = True
            oscore += 1
            amount_rounds = 3
            print("X:", xscore, "-", "O:", oscore)
        elif bottom_left == 1 and bottom_middle == 1 and bottom_right == 1:
            print ("Winner!! X")
            game_over = True
            xscore += 1
            amount_rounds += 1
            print("X:", xscore, "-", "O:", oscore)
        elif bottom_left == 2 and bottom_middle == 2 and bottom_right == 2:
            print("Winner!! O")
            game_over = True
            oscore += 1
            amount_rounds += 1
            print("X:", xscore, "-", "O:", oscore)
        elif bottom_right ==1 and middle_middle == 1 and top_left == 1:
            print("Winnner!! X") 
            game_over = True
            xscore += 1
            amount_rounds += 1
            print("X:", xscore, "-", "O:", oscore)
        elif bottom_right == 2 and middle_middle == 2 and top_left == 2:
            print("Winner!! O")
            game_over = True
            oscore += 1
            amount_rounds += 1
            print("X:", xscore, "-", "O:", oscore)
        elif middle_right == 1 and middle_middle == 1 and middle_left == 1:
            print("Winner!! X")
            game_over = True
            xscore += 1
            amount_rounds += 1
            print("X:", xscore, "-", "O:", oscore)
        elif middle_right == 2 and middle_middle == 2 and middle_left == 2:
            print("Winner!! O")
            game_over = True
            oscore += 1
            amount_rounds += 1
            print("X:", xscore, "-", "O:", oscore)
        elif bottom_left == 1 and middle_left == 1 and top_left == 1:
            print("Winner!! X")
            game_over = True
            xscore += 1
            amount_rounds += 1
            print("X:", xscore, "-", "O:", oscore)
        elif bottom_left == 2 and middle_left == 2 and top_left == 2:
            print("Winner!! O")
            game_over = True
            oscore += 1
            amount_rounds += 1
            print("X:", xscore, "-", "O:", oscore)
        elif bottom_right == 1 and middle_right == 1 and top_right == 1:
            print ("Winner!! X") 
            game_over = True
            xscore += 1
            amount_rounds += 1
            print("X:", xscore, "-", "O:", oscore)
        elif bottom_right == 2 and middle_right ==2 and top_right ==2:
            print("Winner!! O")
            game_over = True
            oscore += 1
            amount_rounds += 1
            print("X:", xscore, "-", "O:", oscore)
        elif bottom_left == 1 and middle_middle == 1 and top_right ==1:
            print("Winner!! X")
            game_over = True
            xscore += 1
            amount_rounds += 1
        elif top_middle == 2 and middle_middle == 2 and bottom_middle == 2:
            print("Winner!! 0")
            game_over = True
            oscore += 1
            amount_rounds += 1
            print("X:", xscore, "-", "O:", oscore)
        elif top_middle == 1 and middle_middle == 1 and bottom_middle == 1:
            print("Winner!! 0")
            game_over = True
            xscore += 1
            amount_rounds += 1
            print("X:", xscore, "-", "O:", oscore)
        
 
    # cheack for tie games
 
    #1 = x 
    # 2 = O
 
        if top_left == 1 and top_middle == 1 and top_right == 2 and middle_left == 2 and middle_middle == 2 and middle_right == 1 and bottom_left == 1 and bottom_middle == 2 and bottom_right == 1 :
            tie_game = True  
            noscore += 1  
            amount_rounds += 1
        elif top_left == 2 and top_middle == 2 and top_right == 1 and middle_left == 1 and middle_middle == 1 and middle_right == 2 and bottom_left == 2 and bottom_middle == 1 and bottom_right == 2 :
            tie_game = True 
            noscore += 1
            amount_rounds += 1
        elif top_left == 2 and top_middle == 1 and top_right == 2 and middle_left == 2 and middle_middle == 1 and middle_right == 1 and bottom_left == 1 and bottom_middle == 2 and bottom_right == 1:
            tie_game = True
            noscore += 1
            amount_rounds += 1
        elif top_left == 1 and top_middle == 2 and top_right == 1 and middle_left == 1 and middle_middle == 2 and middle_right == 2 and bottom_left == 2 and bottom_middle == 1 and bottom_right == 2:
            tie_game = True
            noscore += 1
            amount_rounds += 1
        elif top_left == 1 and top_middle == 2 and top_right == 1 and middle_left == 2 and middle_middle == 1 and middle_right == 1 and bottom_left == 1 and bottom_middle == 1 and bottom_right == 2:
            tie_game = True
            noscore += 1
            amount_rounds += 1
        elif top_left == 2 and top_middle == 1 and top_right == 2 and middle_left == 1 and middle_middle == 2 and middle_right == 2 and bottom_left == 2 and bottom_middle == 2 and bottom_right == 1:
            tie_game = True 
            noscore += 1 
            amount_rounds += 1  
        elif top_left == 1 and top_middle == 1 and top_right == 2 and middle_left == 2 and middle_middle == 1 and middle_right == 1 and bottom_left == 1 and bottom_middle == 2 and bottom_right == 2:
            tie_game = True
            noscore += 1
            amount_rounds += 1
        elif top_left == 2 and top_middle == 2 and top_right == 1 and middle_left == 1 and middle_middle == 2 and middle_right == 2 and bottom_left == 2 and bottom_middle == 1 and bottom_right == 1:
            tie_game = True
            noscore += 1
            amount_rounds += 1
        elif top_left == 1 and top_middle == 2 and top_right == 2 and middle_left == 2 and middle_middle == 1 and middle_right == 1 and bottom_left == 1 and bottom_middle == 1 and bottom_right == 2:
            tie_game = True
            noscore += 1
            amount_rounds += 1
        elif top_left == 1 and top_middle == 2 and top_right == 1 and middle_left == 1 and middle_middle == 2 and middle_right == 2 and bottom_left == 2 and bottom_middle == 1 and bottom_right == 1:
            tie_game = True
            noscore += 1
            amount_rounds += 1
        elif top_left == 2 and top_middle == 1 and top_right == 2 and middle_left == 1 and middle_middle == 2 and middle_right == 1 and bottom_left == 2 and bottom_middle == 1 and bottom_right == 1:
            tie_game = True
            noscore += 1
            amount_rounds += 1
        elif top_left == 1 and top_middle == 2 and top_right == 1 and middle_left == 1 and middle_middle == 2 and middle_right == 1 and bottom_left == 2 and bottom_middle == 1 and bottom_right == 2:
            tie_game = True
            noscore += 1
            amount_rounds += 1
        elif top_left == 1 and top_middle == 2 and top_right == 1 and middle_left == 1 and middle_middle == 2 and middle_right == 2 and bottom_left == 2 and bottom_middle == 1 and bottom_right == 1:
            tie_game = True
            noscore += 1
            amount_rounds += 1
        elif top_left == 2 and top_middle == 1 and top_right == 2 and middle_left == 2 and middle_middle == 1 and middle_right == 2 and bottom_left == 1 and bottom_middle == 2 and bottom_right == 1:
            tie_game = True
            noscore += 1
            amount_rounds += 1
        elif top_left == 2 and top_middle == 1 and top_right == 1 and middle_left == 1 and middle_middle == 2 and middle_right == 2 and bottom_left == 2 and bottom_middle == 1 and bottom_right == 1:
            tie_game = True
            noscore += 1 
            amount_rounds += 1 
        elif top_left == 1 and top_middle == 1 and top_right == 2 and middle_left == 2 and middle_middle == 2 and middle_right == 1 and bottom_left == 1 and bottom_middle == 1 and bottom_right == 2:
            tie_game = True
            noscore += 1
            amount_rounds += 1 
        elif top_left == 1 and top_middle == 2 and top_right == 1 and middle_left == 2 and middle_middle == 1 and middle_right == 1 and bottom_left == 2 and bottom_middle == 1 and bottom_right == 2:
            tie_game = True
            noscore += 1
            amount_rounds += 1
        elif top_left == 1 and top_middle == 2 and top_right == 1 and middle_left == 2 and middle_middle == 2 and middle_right == 1 and bottom_left == 1 and bottom_middle == 1 and bottom_right == 2:
            tie_game = True
            noscore += 1
            amount_rounds += 1
        elif top_left == 2 and top_middle == 1 and top_right == 2 and middle_left == 1 and middle_middle == 1 and middle_right == 2 and bottom_left == 2 and bottom_middle == 2 and bottom_right == 1:
            tie_game = True
            noscore += 1
            amount_rounds += 1
        elif top_left == 2 and top_middle == 1 and top_right == 2 and middle_left == 1 and middle_middle == 1 and middle_right == 2 and bottom_left == 1 and bottom_middle == 2 and bottom_right == 1:
            tie_game = True
            noscore += 1
            amount_rounds += 1
        elif top_left == 2 and top_middle == 1 and top_right == 2 and middle_left == 1 and middle_middle == 2 and middle_right == 1 and bottom_left == 1 and bottom_middle == 2 and bottom_right == 1:
            tie_game = True
            noscore += 1
            amount_rounds += 1
            
