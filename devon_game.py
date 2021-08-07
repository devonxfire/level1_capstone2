import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy image). 
# I downloaded and replaced the images with a mouse as the 'hero' 3 'cats' as the enemies, and 'cheese' as the prize

player = pygame.image.load("mouse.png")
enemy = pygame.image.load("cat.png")
enemy2 = pygame.image.load("cat2.png")
enemy3 = pygame.image.load("cat3.png")
prize = pygame.image.load("cheese.png")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

# Added height and width properties to 'prize' and other 2 enemies

prize_height = prize.get_height()
prize_width = prize.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

# Store the positions of the player and enemy as variables so that you can change them later.

playerXPosition = 100
playerYPosition = 50

# Make the enemy start off screen and at a random y position.

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)

# Added the other 2 enemy starting positions

enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)
enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, 45)

# Make the prize start at a random position

prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)

# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other. 

keyUp= False
keyDown = False
# Adding left and right buttons
keyLeft = False
keyRight = False


# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later. 

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy, (enemyXPosition, enemyYPosition))

    # Added other 2 enemies

    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))

    # Added prize

    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True

            # My attempt at getting player to move left or right, unfortunately unsuccessful
            if event.key == pygame.K_LEFT:
                keyLeft = True

            if event.key == pygame.K_RIGHT:
                keyRight = True

        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False


            # My attempt at getting player to move left or right, unfortunately unsuccessful
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False


    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1

    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    # My attempt at moving Left and Right. Changed player position to X axis:

    if keyLeft == True:
        if playerXPosition > 0 : # This makes sure that the user does not move the player left of the window.
            playerXPosition -= 1

    if keyRight == True:
        if playerXPosition > 0 : # This makes sure that the user does not move the player right of the window.
            playerXPosition += 1

    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    # Added box for other 2 enemies

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition
    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    # Added box for the prize

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemyBox):
    
        # Display losing status to the user: 
        
        print("You lose!")

        pygame.quit()
        exit(0)

    # Added the below so the user wins if the mouse collides with the prize (cheese)

    if playerBox.colliderect(prizeBox):

        print("You win!")

        pygame.quit()
        exit(0)

    # If user collides with enemy 2 or enemy 3, they lose

    if playerBox.colliderect(enemy2Box):

        print("You lose!")

        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3Box):
        print("You lose!")

        # Quite game and exit window: 
        pygame.quit()
        exit(0)
        
    # If the enemy is off the screen the user wins the game:
    # I commented out the below, so the game doesn't quit once the first enemy has passed through the screen

    # if enemyXPosition < 0 - enemy_width:
    #
    #     # Display wining status to the user:
    #
    #     print("You win!")
    #
    #     # Quite game and exit window:
    #     pygame.quit()
    #
    #     exit(0)
    
 
    
    # Make enemies and prize approach the player.
    
    enemyXPosition -= 0.15
    enemy2XPosition -= .07
    enemy3XPosition -= .09
    prizeXPosition -= 0.10
    
    # ================The game loop logic ends here. =============
  
