import turtle
import time

wn = turtle.Screen()
wn.title("Animation Demo")
wn.bgcolor("black")

#register the shapes of gif
wn.register_shape("anime1.gif")
wn.register_shape("anime2.gif")
wn.register_shape("anime3.gif")
wn.register_shape("anime4.gif")
wn.register_shape("anime5.gif")

player = turtle.Turtle()
player.shape("anime1.gif")
player.color("green") 
player.frame=0

def player_animate():
	if player.frame == 0:
		player.shape("anime2.gif")
		player.frame =1
	elif player.frame ==1:
		player.shape("anime2.gif")
		player.frame =2
	elif player.frame ==2:
		player.shape("anime4.gif")
		player.frame =3
	elif player.frame ==3:
		player.shape("anime5.gif")
		player.frame =0
	
	wn.ontimer(player_animate, 500)
	#it will call the fun player_animate after 500 milli sec = 0.5sec.
player_animate()
while True:
	wn.update()
	
	

wn.mainloop()