import pygame as pg


print('Setup Started')
pg.init()
window = pg.display.set_mode(size = (600,480))
print('Setup End')

while True:
    # Check for all events
    for event in pg.event.get():
        if  event.type == pg.QUIT:
            pg.quit() # Close Windows
            quit()