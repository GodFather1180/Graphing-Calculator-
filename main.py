import PySimpleGUI as sg
import turtle
import math


ml = []
math_mode = True
graph_mode = False

global q_pos
layout = [[sg.Text('GC 33')],
          [
            sg.Canvas(size=(315, 270),
                      background_color="black",
                      key='-canvas-')
          ],
          [
            sg.Button('GRAPH',button_color=('yellow', 'purple')),
            sg.Button('MATH',button_color=('yellow', 'purple')),
            sg.Button('CLEAR',button_color=('yellow', 'purple'))
          ],
          [
            sg.Button('2nd', size=(4, 1)),
            sg.Button('X', size=(5, 1)),
            sg.Button('del', size=(3, 1)),
            sg.Button('▲', size=(5, 1), pad=((12, 0), 0),button_color=('black', 'Orange'))
          ],
          [
            sg.Button('sin', size=(4, 1)),
            sg.Button('cos', size=(4, 1)),
            sg.Button('tan', size=(4, 1)),
            sg.Button('◄', size=(1, 1), pad=((10, 0), 0),button_color=('black', 'Orange')),
            sg.Button('►', size=(1, 1), pad=((5, 0), 0),button_color=('black', 'Orange'))
          ],
          [
            sg.Button('(', size=(4, 1)),
            sg.Button(')', size=(4, 1)),
            sg.Button('^', size=(4, 1)),
            sg.Button('▼', size=(5, 1), pad=((12, 0), 0),button_color=('black', 'Orange'))
          ],
          [
            sg.Button('7', size=(2, 1)),
            sg.Button('8', size=(2, 1)),
            sg.Button('9', size=(2, 1)),
            sg.Button('+', size=(1, 1)),
          ],
          [
            sg.Button('4', size=(2, 1)),
            sg.Button('5', size=(2, 1)),
            sg.Button('6', size=(2, 1)),
            sg.Button('-', size=(1, 1))
          ],
          [
            sg.Button('1', size=(2, 1)),
            sg.Button('2', size=(2, 1)),
            sg.Button('3', size=(2, 1)),
            sg.Button('x', size=(1, 1))
          ],
          [
            sg.Button('(-)', size=(2, 1)),
            sg.Button('0', size=(2, 1)),
            sg.Button('=', size=(2, 1)),
            sg.Button('/', size=(1, 1))
          ]]

window = sg.Window('My new window', layout, finalize=True)

canvas = window['-canvas-'].TKCanvas

canvas.configure(bg='black')

#G-VAR

while True:  # Event Loop
  event, values = window.read()
  if event == sg.WIN_CLOSED:
    break

  t = turtle.RawTurtle(canvas)
  tb = turtle.RawTurtle(canvas)
  t.hideturtle()
  tb.hideturtle()

  #functions
  def t_answer(answer):
      tans = turtle.RawTurtle(canvas)
      tans.hideturtle()
      tans.hideturtle()
      tans.penup()
      tans.goto(((310/2,185/2-(1*5))))
      tans.pendown()
      tans.write(answer, move=False, align="right", font=("Arial", 15, "bold"))
    
  
  def clear_screen():
    t_clear_screen = turtle.RawTurtle(canvas)
    t_clear_screen.speed(0)
    t_clear_screen.hideturtle()
    t_clear_screen.penup()
    t_clear_screen.goto(157.5, 135)
    t_clear_screen.color("white")
    t_clear_screen.begin_fill()
    t_clear_screen.right(90)
    t_clear_screen.forward(270)
    t_clear_screen.right(90)
    t_clear_screen.forward(316)
    t_clear_screen.right(90)
    t_clear_screen.forward(270)
    t_clear_screen.right(90)
    t_clear_screen.forward(315)
    t_clear_screen.end_fill()
  
  def math_input():
    
    tm = turtle.RawTurtle(canvas)
    tm.hideturtle()
    tm.speed(0)
    tm.penup()
    tm.goto(-310/2,220/2)
    tm.pendown()

    #### MOVE EQUAL CHECK HERE
    
    #numbers 
    if event == "1":
      ml.append("1")
    if event == "2":
      ml.append("2")
    if event == "3":
      ml.append("3")
    if event == "4":
      ml.append("4")
    if event == "5":
      ml.append("5")
    if event == "6":
      ml.append("6")
    if event == "7":
      ml.append("7")
    if event == "8":
      ml.append("8")
    if event == "9":
      ml.append("9")
    if event == "0":
      ml.append("0")

    #basic opreators
    if event == "+":
      ml.append(" + ")
    if event == "-":
      ml.append(" - ")
    if event == "(-)":
      ml.append(" - ")
    if event == "x":
      ml.append(" * ")
    if event == "/":
      ml.append(" / ")
    if event == "(":
      ml.append("( ")
    if event == ")":
      ml.append(" )")
    if event == "^":
      ml.append(" ** ")
    if event == "sin":
      ml.append("sin( ")
    if event == "cos":
      ml.append("cos( ")
    if event == "tan":
      ml.append("tan( ")
    if event == "X":
      ml.append("X")
    
    #move line down
    

    
    #del / clear function
    if event == "del":
      del ml[-1]
      clear_screen()

    if event == "CLEAR":
      ml.clear()
      clear_screen()
    
    #turtle output
    math_type = "".join(ml)
    tm.write(math_type, move=False, align="left", font=("Arial", 15, "bold"))
      
    #terminal output
    print(ml)

    #calculate_math
    

    
    
  def loading_animation(color):
    tb.color("black", color)
    tb.begin_fill()
    tb.circle(5)
    tb.end_fill()

    tb.color("black", "white")
    tb.begin_fill()
    tb.circle(5)
    tb.end_fill()

  def draw_grid():

    c = 11
    grid_width = 240
    while c > 0:

      t.forward(grid_width)
      t.backward(grid_width)
      t.penup()
      t.right(90)
      t.forward(20)
      t.left(90)
      t.pendown()
      c = c - 1
    t.penup()
    t.forward(20)
    t.left(90)
    c = 11
    while c > 0:
      t.pendown()
      t.forward(grid_width)
      t.backward(grid_width)
      t.penup()
      t.right(90)
      t.forward(20)
      t.left(90)
      c = c - 1

    t.right(90)
    t.backward(grid_width / 2)
    t.left(90)
    t.width(2)
    t.pencolor("red")
    t.pendown()
    t.forward(grid_width)
    t.backward(grid_width / 2)
    t.right(90)
    t.forward(grid_width / 2)
    t.backward(grid_width)
    t.forward(grid_width / 2)
    t.penup()
  
  pj = turtle.RawTurtle(canvas)
  def draw_points():
    
      x = -6
      y = 0
  
      while -7 < x < 6:
        #loading_animation("blue")
        res = 0.1
        x = x + res
  
        #GRAPH

        s_eq = (''.join(ml))
        print(s_eq, "s-eq")
  
        calc = s_eq.replace("sin(", "math.sin(")
        calc = calc.replace("cos(", "math.cos(")
        calc = calc.replace("tan(", "math.tan(")
        calc = calc.replace("x", "*")

        x_w_brackets = ("(" + str(x) + ")")
        print(x_w_brackets)
        print(x, "xxx")
        calc = calc.replace("X", ( str(x_w_brackets)))
        print(calc, "eq")
    
        calc = (eval(calc))

        print (calc, "calc")
        
        
        y = calc
        t.hideturtle()
        t.forward(x * 20)
        t.left(90)
        t.forward(y * 20)
  
        # point join
        current_x_pos = (x*20)
        current_y_pos = (y*20)

        pj.penup()
        pj.goto(current_x_pos, current_y_pos)
        pj.hideturtle()
        pj.pendown()

        
  
        t.fillcolor('blue')
        t.begin_fill()
        t.circle(2)
        t.end_fill()
  
        t.backward(y * 20)
        t.right(90)
        t.backward(x * 20)

  if event == "MATH":
    math_mode = True
    graph_mode = False
    clear_screen()
    print("math mode")

  if event == "GRAPH":
    clear_screen()
    math_mode = False
    graph_mode = True

  if graph_mode == True:
    #turtle setup

        
    t.penup()
    t.speed(0)
    tb.speed(0)
    t.goto(-120, 100)
    tb.penup()
    tb.goto(-130, 110)
    tb.pendown()
    t.pendown()
    t.hideturtle()
    tb.hideturtle()

  
      
  
    math_input()
  
    if event == "=":
      draw_grid()
      draw_points()



    

    
  if math_mode == True:
      math_input()
      print("b")

      if event == "=":
      
        s_eq = (''.join(ml))
        print(s_eq, "s-eq")

        calc = s_eq.replace("sin(", "math.sin(")
        calc = calc.replace("cos(", "math.cos(")
        calc = calc.replace("tan(", "math.tan(")
        calc = calc.replace("arcsin(", "math.arcsin(")
        calc = calc.replace("arccos(", "math.arccos(")
        calc = calc.replace("arctan(", "math.arctan(")
        
        calc = (eval(calc))
        
        t_answer(calc)
        
        
        