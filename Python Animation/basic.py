import turtle
import time

wn = turtle.Screen()
wn.title("Animation Demo")
wn.bgcolor("black")

player = turtle.Turtle()
player.shape("square")
player.color("green")

def player_animate():
	player.shape("square")
	time.sleep(0.5)
	#dont use sleep in games because it stops the whole program for the specified time.
	player.shape("circle")
	time.sleep(0.5)

while True:
	print("main Loop")
	player_animate()

wn.mainloop()