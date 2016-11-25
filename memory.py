import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

turn = 0
card1 = 0
card2 = 0
state = 0
CARD_WIDTH = 50
CARD_HEIGHT = 100
NUM_CARDS = 16
NUM_PAIRS = NUM_CARDS / 2
exposed = [False] * NUM_CARDS
list_main = [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
random.shuffle(list_main)

def new_game():
    global exposed, state, card1, card2, list_main, turn
    exposed = [False] * NUM_CARDS
    state = 0
    card1 = None
    card2 = None
    list_main = [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
    random.shuffle(list_main)
    turn = 0

def canvas2card(pos):
    return pos[0] // CARD_WIDTH

def card_clicked(card):
    global exposed, state, card1, card2, turn

    if not exposed[card]:
        exposed[card] = True

        if state == 0:
            state = 1
            card1 = card
        elif state == 1:
            state = 2
            card2 = card
        else:
            if list_main[card1] != list_main[card2]:
                exposed[card1] = False
                exposed[card2] = False
            state = 1
            card1 = card
            card2 = None
            turn += 1


def mouseclick(pos):
    card = canvas2card(pos)
    card_clicked(card)

def draw(canvas):
    label.set_text("Ход = " + str(turn))
    draw_text(canvas)


def draw_text(canvas):
    global list_main, CARD_WIDTH, CARD_HEIGHT
    i = 0
    width1 = - 38
    width2 = -51
    canvas.draw_line([1, 1], [100 * NUM_PAIRS, 1], 2, 'White')
    canvas.draw_line([1, 98], [100 * NUM_PAIRS, 98], 2, 'White')

    while width2 <= CARD_WIDTH * NUM_CARDS:
        canvas.draw_line([width2 + 50, 1], [width2 + 50, 98], 2, 'White')
        width2 = width2 + 50

    while i < NUM_CARDS:
        if exposed[i]:
            canvas.draw_text(str(list_main[i]), [width1 + 50, CARD_HEIGHT / 2 + 8], 50, 'White')
        i = i + 1
        width1 = width1 + 50


frame = simplegui.create_frame("Мемори", CARD_WIDTH * NUM_CARDS, CARD_HEIGHT)
frame.add_button("Новая игра", new_game)
label = frame.add_label("Ход = "+str(turn))

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()



