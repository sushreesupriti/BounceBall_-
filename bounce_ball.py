from tkinter import *
import random
import time

# import modules


class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id= canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y=-2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.score=0
        self.highScore = 0
        self.show_score = canvas.create_text(40,10,text=f'Score = {self.score}' ,fill="red")
        self.showHighScore = canvas.create_text(740,10,text=f'High Score = {self.highScore}' ,fill="red")
        

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False
    
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            

        if self.hit_paddle(pos) == True:
            self.y = -2
            self.x += paddle.x
            
            self.score +=100
            canvas.delete(self.show_score)
            self.show_score = canvas.create_text(40,10,text=f'Score = {self.score}',fill="red")
            
        if pos[0] <= 0:
            self.x = ((self.score // 1000)+ 3) 
        elif pos[2] >= self.canvas_width:
            self.x = -1 * ((self.score // 1000)+ 3)

    
class Paddle:
    def __init__(self,canvas,color):
        self.canvas= canvas
        self.id=canvas.create_rectangle(0,0,150,10,fill=color)
        self.canvas.move (self.id,325,500)
        self.x=0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] == 0:
            self.x = 0
        elif pos[0] < 0:
            self.canvas.move(self.id, -1 * pos[0], 0)
            self.x = 0

        elif pos[2] == self.canvas_width:
            self.x = 0
        elif pos[2] > self.canvas_width:
            self.canvas.move(self.id, -1 * (pos[2] - self.canvas_width), 0)
            self.x = 0

    def turn_left(self,evt):
        if self.x > -4 and self.x <= 0:
            self.x -= 2
        elif self.x > 0:
            self.x = -2
    def turn_right(self,evt):
        if self.x < 4 and self.x >= 0:
            self.x += 2
        elif self.x < 0:
            self.x = 2

class Game:
    def __init__(self):
        self.highScore = 0
        self.currentScore = 0
        self.btn = None

    def run_game(self):
        self.btn.destroy()
        while True:
            if ball.hit_bottom == True:
                canvas.delete(ball.show_score)
                canvas.delete(ball.showHighScore)
                self.currentScore = ball.score
                if self.highScore < self.currentScore:
                    self.highScore = self.currentScore
                    canvas.create_text(400 ,250 ,text=f'Congratulations! You have a new record: {self.currentScore}',fill="black")
                else:
                    canvas.create_text(400 ,200 ,text=f'Your Score was {self.currentScore}',fill="black")
                    canvas.create_text(400 ,250 ,text=f'Highest Score in the session was {self.highScore}',fill="black")
                break
            paddle.draw()
            ball.draw()    
            tk.update_idletasks()
            tk.update()
            time.sleep(0.01)
        self.game_over()

    def game_over(self):
        canvas.create_text(400 ,300 ,text="Game Over",fill="red")
        canvas.create_text(400 ,350 ,text="Click the button below to restart the game!",fill="black")

        self.btn = Button(tk ,text="Re-Start", bd="10",command=self.restart_game)
        self.btn.pack()
        mainloop()

    def restart_game(self):
        global canvas
        global paddle
        global ball

        canvas.delete(ALL)

        paddle = Paddle(canvas,"green")
        ball = Ball(canvas,paddle,"green")
        ball.highScore = self.highScore
        canvas.delete(ball.showHighScore)
        ball.showHighScore = canvas.create_text(740,10,text=f'High Score = {self.highScore}' ,fill="red")
        self.run_game()

tk=Tk()  
# It helps to display the root window and manages all the other components of the tkinter application.
tk.title("Game")  # tk.title() used for giving the window a title. 
tk.resizable(0,0)  # it makes the window a fixed size
tk.wm_attributes("-topmost",1)  # wm stands for window manager .

canvas=Canvas(tk,width=800,height=600,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas,"green")
ball = Ball(canvas,paddle,"green")
new = Game()

new.btn=Button(tk ,text="start " , bd="10",command=new.run_game)
new.btn.pack()
mainloop()



