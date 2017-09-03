#!/usr/bin/env python3

'''

kolko i krzyzyk // bardzo prosta wersja, sterowanie klawiatura numeryczna//
==============================================================================

getch numery klawiszy
______________________
9 - 57
8 - 56
7 - 55
6 - 54
5 - 53
4 - 52
3 - 51
2 - 50
1 - 49

wychodzi sie esc, kolko zaczyna
^^^^^^^^^^^^^^^^^^^^^^^^^

'''
import curses
from curses import wrapper
from time import sleep

def main(stdscr):
    stdscr = curses.initscr()
    
    curses.curs_set(False)#wyswietlanie kursora
    curses.noecho() #do wczytywania klawiszy, wylacza automatyczne wypisywanie 
    curses.cbreak() #nie trzeba enter zeby reagowalo na klawisz
    stdscr.keypad(True)#mozna uzywac curses.KEY...
    
    begin_x = 20
    begin_y = 7
    ht = 3 #height/width
    wt = 5
    ruch = 0 #parzyste koklo, np krzyzyk
    p1=p2=p3=p4=p5=p6=p7=p8=p9 = 0 #sprawdzanie zajetosci
    
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
    #koniec tworzenia planszy
    

    
    while True:
        key = stdscr.getch()
        
        if key is 27:
            break
        
        if key is 49:
            if p1 != 0:
                continue
            elif (ruch%2==0):
                pad1.addch(1,2,ord("O"))
            else:
                pad1.addch(1,2,ord("X"))
            pad1.refresh()
            p1 = 1
            ruch = ruch + 1
        if key is 50:
            if p2 != 0:
                continue
            elif (ruch%2==0):
                pad2.addch(1,2,ord("O"))
            else:
                pad2.addch(1,2,ord("X"))
            pad2.refresh()
            p2=1
            ruch = ruch + 1
        if key is 51:
            if p3 != 0:
                continue
            elif (ruch%2==0):
                pad3.addch(1,2,ord("O"))
            else:
                pad3.addch(1,2,ord("X"))
            pad3.refresh()
            p3=1
            ruch = ruch + 1
        if key is 52:
            if p4 != 0:
                continue
            elif (ruch%2==0):
                pad4.addch(1,2,ord("O"))
            else:
                pad4.addch(1,2,ord("X"))
            pad4.refresh()
            p4=1
            ruch = ruch + 1
            
        if key is 53:
            if p5 != 0:
                continue
            elif (ruch%2==0):
                pad5.addch(1,2,ord("O"))
            else:
                pad5.addch(1,2,ord("X"))
            pad5.refresh()
            p5=1
            ruch = ruch + 1
            
        if key is 54:
            if p6 != 0:
                continue
            elif (ruch%2==0):
                pad6.addch(1,2,ord("O"))
            else:
                pad6.addch(1,2,ord("X"))
            pad6.refresh()
            p6=1
            ruch = ruch + 1
            
        if key is 55:
            if p7 != 0:
                continue
            elif (ruch%2==0):
                pad7.addch(1,2,ord("O"))
            else:
                pad7.addch(1,2,ord("X"))
            pad7.refresh()
            p7=1
            ruch = ruch + 1
            
        if key is 56:
            if p8 != 0:
                continue
            elif (ruch%2==0):
                pad8.addch(1,2,ord("O"))
            else:
                pad8.addch(1,2,ord("X"))
            pad8.refresh()
            ruch = ruch + 1
        if key is 57:
            if p9 != 0:
                continue
            elif (ruch%2==0):
                pad9.addch(1,2,ord("O"))
            else:
                pad9.addch(1,2,ord("X"))
            p9 = 1
            pad9.refresh()
            ruch = ruch + 1
        
        
        
        
        
        
        

    
    
    
    #zamykanie curses
    
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

wrapper(main)  #wraper przywraca terminal do normalnego stanu
