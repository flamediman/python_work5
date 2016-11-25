import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

list1 = []

def draw(canvas):
    for sq in list1:
       canvas.draw_polygon([(sq[0], sq[1]), (sq[0] + 49, sq[1]), (sq[0] + 49, sq[1] + 49), (sq[0], sq[1] + 49)], 1, 'white', 'green')

def ex(pos, list):
    for sq in list:
        if (pos[0] == sq[0] and pos[1] == sq[1]):
            return True
        else:
            return False

def click(pos):
    a = [pos[0] // 50 * 50, pos[1] // 50 * 50]

    if ex(a, list1):
        list1.pop(list1.index(a))
    else:
        list1.append(a)

frame = simplegui.create_frame("кравдраты", 400, 200)

frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)


frame.start()
