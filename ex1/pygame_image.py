import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_flip = pg.transform.flip(bg_img,True,False)


    #こうかとん
    bird_image = pg.image.load("fig/3.png")
    bird_image = pg.transform.flip(bird_image,True,False)
    bird_rct = bird_image.get_rect()
    bird_rct.center = 300,200



    tmr = 0
    while True:
        x = tmr%3200
        w = 0
        h = 0

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            h = -1
        if key_lst[pg.K_DOWN]:
            h = 1
        if key_lst[pg.K_RIGHT]:
            w = 2
        if key_lst[pg.K_LEFT]:
            w = -1


        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_flip,[-x+1600,0])
        screen.blit(bg_img,[-x+3200,0])

        bird_rct.move_ip(w-1,h)
        screen.blit(bird_image,bird_rct)

        pg.display.update()
        tmr += 1   
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()