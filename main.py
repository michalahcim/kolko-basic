#!/usr/bin/env python3

'''

kolko i krzyzyk // bardzo prosta wersja, sterowanie klawiatura numeryczna//

'''
import curses
from curses import wrapper
from time import sleep

def main(stdscr):
    stdscr = curses.initscr()
    
    curses.noecho() #do wczytywania klawiszy, wylacza automatyczne wypisywanie 
    curses.cbreak() #nie trzeba enter zeby reagowalo na klawisz
    stdscr.keypad(True)#mozna uzywac curses.KEY...
    
    begin_x = 20
    begin_y = 7
    ht = 3 #height/width
    wt = 5
    
    
    #plansza
    #win = curses.newwin(height, width, begin_y, begin_x) #y,x (0,0)to lewy gorny rog
    #pad to jest co innego niz win ale nazwa pad lepiej mi pasuje
    pad1 = curses.newwin(ht,wt,7,1)
    pad2 = curses.newwin(ht,wt,7,6)
    pad3 = curses.newwin(ht,wt,7,11)
    pad4 = curses.newwin(ht,wt,4,1)
    pad5 = curses.newwin(ht,wt,4,6)
    pad6 = curses.newwin(ht,wt,4,11)
    pad7 = curses.newwin(ht,wt,1,1)
    pad8 = curses.newwin(ht,wt,1,6)
    pad9 = curses.newwin(ht,wt,1,11)
    #for y in range(0,99):
     #   for x in range(0,99):
      #      pad.addch(y,x, ord('a')+(x*x+y*y) % 26)
        #    pad.border()
       #     pad.refresh(0,0,5,5,30,60) # 0,0, start_y, start_x, koniec_y, koniec_x
         #   sleep(0.000001)
    #stdscr.border()
    
    #plansza ramka
    
    pad1.box()
    pad2.box()
    pad3.box()
    pad4.box()
    pad5.box()
    pad6.box()
    pad7.box()
    pad8.box()
    pad9.box()
    
    pad8.addch(1,2,ord("X"))
    pad1.addch(1,2,ord("O"))
    pad3.addch(1,2,ord("O"))
    pad4.addch(1,2,ord("X"))
    
    
    #odswiezanie
    pad1.refresh()
    pad2.refresh()
    pad3.refresh()
    pad4.refresh()
    pad5.refresh()
    pad6.refresh()
    pad7.refresh()
    pad8.refresh()
    pad9.refresh()
    stdscr.getch()
    #koniec tworzenia planszy
    
    
    
    
    
    #zamykanie curses
    
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

wrapper(main)  #wraper przywraca terminal do normalnego stanu
