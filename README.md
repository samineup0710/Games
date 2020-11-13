# Games
BUG GAME

This game is made  using turtle module only from python library.

Turtle module:
              Turtle is a built in module in python. It was part of the original Logo programming language developed by Wally Feurzig and Seymour Papert in 1966. Using turtle you can draw any shape, image on the screen and it is fun to work with turtle graphics.
              Turtle is a toolkit that provides a simple and enjoyable way to draw pictures on windows or screen. We can say that, turtle graphics controlling a graphical entity in a graphic window with x,y coordinates.
              
              
 Let's dive deep into the program.
 Things needed
 
 1.   Setting up the screen:
                To start using the module, you need to import it like any other module in python.
                import turtle
            
 2.   Creating the bug's head using turtle module and set its shape color and sizes.
 
 
 3.   Functions to move the bug by calling move() from turtle module.Here you need to test the direction of its head so that we can move X and Y coordinates.
      if the required direction is not found then it is set to that direction and move the bug.
     
 4.   call win.listen() fun to listen the key press from keyboards.
 
 5.   setting the food its shape and colors using random.choice method.Also we call random module to move foods to random position.
 
 6.   To add the body parts need to create empty list and append.Adding the parts to the bug's head is not enough. Those parts need to move when the bug's head moves. The logic I’ve used moves the last partwhich is in the position x to x-1 and x-1 to x-2 and so on.
      But the part which is right above the head is a special case. Where does that go? It goes in the place of the head.
    
 7.   Add Border Collisions: We need to make sure that the bug dies when it collides with the border. We already have the coordinates of the border, we just need to reset the bug's head position when it touches those coordinates. Also, the snake needs to stop moving and hence change the direction to stop.
      Also, the parts need to disappear when the bug dies. For this, all we need to do is, set the part’s position outside the window coordinates. Now when the game restarts we need fresh new part and hence clear the body list.
    
 8.   Add Body Collisions:The bug needs to die when it touches itself. So we’re going to go through the entire body list and check if the distance between the body part and head is less than 15. If it is, reset the head position and head direction.
 
 9.   Setting the scores: We need to analyze the situations when the score increases. First one is when the head collides with the food. Increase the score and update the high_score. We use the disp.write() to write the score on the screen.
 
 10.  Resetting: We need to reset the score when the bug's head collides with the border and with its own body parts.
 
 
 

 
