import game_framework
import main_state
from pico2d import *

name = "PauseState"
image = None


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def handle_event():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            game_framework.pop_state(main_state)


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()