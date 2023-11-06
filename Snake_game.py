from tkinter import *
import random
from PIL import ImageTk,Image
from tkinter import ttk
#

#window settings
win=Tk()
win.title("Snake-Game")
win.iconbitmap("assets\\snake.ico")
win.resizable(False,False)
win.config(bg="sea green")
window_width=330
window_height=120
screen_width=win.winfo_screenwidth()
screen_height=win.winfo_screenheight()
centre_x=int(screen_width/2)-int(window_width/2)
centre_y=int(screen_height/2)-int(window_height/2)
win.geometry(f"{window_width}x{window_height}+{centre_x}+{centre_y}")


#function
def change_color():
    x=random.choice([1,2,3,4])
    if(x==1):
        game_name.config(fg="yellow")
    elif(x==2):
        game_name.config(fg="green")
    elif(x==3):
        game_name.config(fg="blue")
    elif(x==4):
        game_name.config(fg="red")

    frame_1.after(300,change_color)

def next():
    global User_name,frame_1
    User_name=str(name_section.get())
    if(User_name!=""):
        frame_1.destroy()
        frame_2.grid(pady=10,padx=10)
        win.geometry("225x270")
        win.config(bg="white")
        next_img()
        load_next()
        bar_increase()

    else:
        name_error = Label(frame_1, text="please enter your name", bg="red", fg="white", font=("Helvetica", 8, "bold"))
        name_error.grid(row=3,columnspan=2)
        win.geometry("330x145")


def next_img():
    global current,img_hol
    current+=1
    if(current>=0 and current<=5):
        img_hol.config(image=img_list[current])
    elif(current>=6):
        current=0
        img_hol.config(image=img_list[current])
    frame_2.after(30,next_img)
#progress bar
def bar_increase():
    global bar,bar_value
    bar_value=int(bar["value"])
    if(bar_value<=99):
        bar.step(1)
    else:
        bar.step(0)
    frame_2.after(200,bar_increase)
#loading text
def load_next():
    global y,loading_name,bar_value
    y+=1
    if(bar_value<100):
        if (y == 1):
            loading_name.config(text=str(bar_value) + "% Loading.", font=("bold", 10), anchor="center")
        elif (y == 2):
            loading_name.config(text=str(bar_value) + "% Loading..", font=("bold", 10), anchor="center")
        elif (y == 3):
            loading_name.config(text=str(bar_value) + "% Loading...", font=("bold", 10), anchor="center")
        elif (y >= 3):
            y = 0
            loading_name.config(text=str(bar_value) + "% Loading", font=("bold", 10), anchor="center")
    else:
        loading_name.config(text="Done", font=("bold", 10), anchor="center")
        win_2()



    frame_2.after(200,load_next)


#globalvarirable
User_name=""
direction="down"


#creating frame
frame_1=Frame(win)
frame_1.config(bg="sea green")

#creating stuffs for frame 1
game_name=Label(frame_1,text="Snake game",bg="sea green",fg="red",width=20,borderwidth=3,relief=GROOVE,font=("Helvetica", 18,"bold"))
name_lab=Label(frame_1,text="Enter the name:",bg="sea green",borderwidth=3,font=(10),fg="white")
name_section=Entry(frame_1,borderwidth=4,bg="sea green",fg="white")
start_button=Button(frame_1,text="Start",font=("Helvetica", 12,"bold"),command=next,anchor="center",borderwidth=5)



#sorting stuffs
game_name.grid(row=0,column=0,columnspan=2)
name_lab.grid(row=1,column=0)
name_section.grid(row=1,column=1,columnspan=2)
start_button.grid(row=2,columnspan=2)


#frame 2
#creating frame 2
frame_2=Frame(win)

#creating stuffs for frame 2
current=0
y=0
bar_value=0
loading_image1=ImageTk.PhotoImage(Image.open("assets\\load\\frame-1.png"))
loading_image2=ImageTk.PhotoImage(Image.open("assets\\load\\frame-2.png"))
loading_image3=ImageTk.PhotoImage(Image.open("assets\\load\\frame-3.png"))
loading_image4=ImageTk.PhotoImage(Image.open("assets\\load\\frame-4.png"))
loading_image5=ImageTk.PhotoImage(Image.open("assets\\load\\frame-5.png"))
loading_image6=ImageTk.PhotoImage(Image.open("assets\\load\\frame-6.png"))
img_list=[loading_image1,loading_image2,loading_image3,loading_image4,loading_image5,loading_image6]
img_hol=Label(frame_2,image=img_list[current])
#creting progress bar
bar=ttk.Progressbar(frame_2,mode="determinate",maximum=102)
loading_name=Label(frame_2,text=str(bar_value)+"% Loading",font=("bold",10),anchor="center")

#sorting frame 2 stuffs
img_hol.grid(row=0,column=0,columnspan=1)
bar.grid(row=1,column=0)
loading_name.grid(row=2,column=0)

def win_2():
    # game settings
    game_width = 700
    game_height = 700
    space_size = 50
    speed = 100
    body_parts = 3
    snake_color = "green"
    food_color = "red"
    background_color = "black"
    flag = False
    win2 = Tk()
    win2.title("Snake-Game")
    win2.iconbitmap("assets\\snake.ico")
    win2.resizable(False, False)
    win2.config(bg=background_color)

    class Snake:
        def __init__(self):
            self.body_size = body_parts
            self.coordinates = []
            self.square = []

            for i in range(0, body_parts):
                self.coordinates.append([0, 0])

            for x, y in self.coordinates:
                sqaure = canva.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color, tag="snake")
                self.square.append(sqaure)

    class Food:
        def __init__(self):
            x = random.randint(0, (game_width / space_size) - 1) * space_size
            y = random.randint(0, (game_height / space_size) - 1) * space_size

            self.coordinates = [x, y]
            canva.create_oval(x, y, x + space_size, y + space_size, fill=food_color, tag="food")

    # function
    def next_turn(snake, food):
        x, y = snake.coordinates[0]
        if (direction == "up"):
            y -= space_size
        elif (direction == "down"):
            y += space_size
        elif (direction == "right"):
            x += space_size
        elif (direction == "left"):
            x -= space_size
        snake.coordinates.insert(0, (x, y))
        square = canva.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color)
        snake.square.insert(0, square)
        if x == food.coordinates[0] and y == food.coordinates[1]:
            global score
            score += 1
            score_label.config(text=f"Score:{score}")

            canva.delete("food")
            food = Food()

        else:
            del snake.coordinates[-1]
            canva.delete(snake.square[-1])
            del snake.square[-1]

        if (check_collision(snake)):
            game_over()
        else:
            win2.after(speed, next_turn, snake, food)

    def change_direction(new_direction):
        global direction
        if (new_direction == "down"):
            if (direction != 'up'):
                direction = "down"
        elif (new_direction == "up"):
            if (direction != 'down'):
                direction = "up"
        elif (new_direction == "right"):
            if (direction != "left"):
                direction = "right"
        elif (new_direction == "left"):
            if (direction != 'right'):
                direction = "left"

    def check_collision(snake):
        x, y = snake.coordinates[0]
        if (x < 0 or x >= game_width):
            return True
        elif (y < 0 or y >= game_height):
            return True
        for body_part in snake.coordinates[1:]:
            if (x == body_part[0] and y == body_part[1]):
                return True
        return False

    def game_over():
        global flag,User_name,score
        flag = True
        canva.delete(ALL)
        canva.create_text((canva.winfo_screenwidth() / 2) - 420, (canva.winfo_screenheight() / 2) - 100,
                          font=("consolas", 70, 'bold'), text="GAME OVER", fill="red")
        canva.create_text((canva.winfo_screenwidth() / 2) - 420, (canva.winfo_screenheight() / 2) - 200,
                          font=("consolas", 20, 'bold'), text="Press 'enter' to restart or 'ESC' to quit", fill="red")
        canva.create_text((canva.winfo_screenwidth() / 2) - 420, (canva.winfo_screenheight() / 2) - 250,
                          font=("consolas", 15, 'bold'), text=f"{User_name}:{score}", fill="white")

    def restart_game():
        global score, direction, snake, food
        score = 0
        score_label.config(text=f"Score:{score}")
        direction = 'down'
        canva.delete(ALL)
        snake = Snake()
        food = Food()
        next_turn(snake, food)

    def quit_game():
        win2.destroy()
        win.destroy()

    # global variables
    score = 0
    # creating stuffs
    score_label = Label(win2,text=f"Score:{score}", font=("consolas", 30, "bold"), bg=background_color, fg="white")
    canva = Canvas(win2, bg=background_color, height=game_height, width=game_width)
    win2.focus_set()
    win2.bind('<Left>', lambda event: change_direction("left"))
    win2.bind('<Right>', lambda event: change_direction('right'))
    win2.bind('<Up>', lambda event: change_direction('up'))
    win2.bind('<Down>', lambda event: change_direction('down'))
    win2.bind('<Escape>', lambda event: quit_game())
    win2.bind('<Return>', lambda event: restart_game())

    snake = Snake()
    food = Food()
    next_turn(snake, food)
    # sorting stuffs
    score_label.grid(row=0, column=0)
    canva.grid(row=1, column=0)

    win2.update()
    windows_width = win2.winfo_width()
    windows_height = win2.winfo_height()
    screen_width = win2.winfo_screenwidth()
    screen_heigth = win2.winfo_screenheight()
    x = int(screen_width / 2) - int(windows_width / 2)
    y = int(screen_heigth / 2) - int(windows_height / 2)

    win2.geometry(f"{windows_width}x{windows_height}+{x}+{y - 30}")

    win2.mainloop()

#mainloop
change_color()
frame_1.grid(pady=10,padx=10)
win.mainloop()