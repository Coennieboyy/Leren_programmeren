import pgzrun

WIDTH = 800
HEIGHT = 600

alien = Actor('steve')
alien.pos = 100, 56
alien.topright = 0, 10

WIDTH = 500
HEIGHT = alien.height + 20


def draw():
    screen.clear()
    screen.draw.circle((400, 300), 30, 'white')

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Oof!")
    else:
        print("You missed me!")

def on_mouse_down():
    print("You clicked!")

def on_mouse_down(pos, button):
    if button == mouse.LEFT and alien.collidepoint(pos):
        print("Oof!")
    
def on_mouse_down(pos):
    if alien.collidepoint(pos):
        sounds.classic_hurt.play()
        alien.image = 'steve_hurt'

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        sounds.classic_hurt.play()
        alien.image = 'steve_hurt'
        time.sleep(1)
        alien.image = 'steve'

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()


def set_alien_hurt():
    alien.image = 'steve_hurt'
    sounds.classic_hurt.play()


def set_alien_normal():
    alien.image = 'steve'

def set_alien_hurt():
    alien.image = 'steve_hurt'
    sounds.classic_hurt.play()
    clock.schedule_unique(set_alien_normal, 1.0)

pgzrun.go()