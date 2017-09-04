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

def wygranko(p):
    if p == 2:
        print("Kolka wygraly")
    elif p ==3:
        print("Krzyzyki wygraly")
    else:
        print("Nikt nie wygral")
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
    global p0 
    
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
        
        #sprawdzanie czy wygranko
        if p1 is p2 is p3 != 0 or p1 is p4 is p7 !=0:
            p0 = p1
            return p0
            break
        elif p4 is p5 is p6 != 0 or p2 is p5 is p8 !=0 or p1 is p5 is p9 !=0 or p3 is p5 is p7 !=0:
            p0 = p5
            return p0
            break
        elif p7 is p8 is p9 !=0 or p3 is p6 is p9 !=0:
            p0 = p9
            return p0
            break
        
            
                
                
                
        
        
        #wczytanie klawisza i ewentualne wstawienie symbolu
        key = stdscr.getch()
        
        if key is 27 or ruch >= 8: #break przy esc i pelnej planszy
            p0 = None
            break
            
        if key is 49:
            if p1 != 0: #czy zajete 
                continue
            elif (ruch%2==0): #jak parzyste
                pad1.addch(1,2,ord("O"))
                p1 = 2  #znaczy ze kolko, do sprawdzania czy wygranko
            else: 
                pad1.addch(1,2,ord("X"))
                p1 = 3 #znaczy ze krzyzyk
            pad1.refresh()
            
            ruch = ruch + 1
            
        if key is 50:
            if p2 != 0:
                continue
            elif (ruch%2==0):
                pad2.addch(1,2,ord("O"))
                p2=2
            else:
                pad2.addch(1,2,ord("X"))
                p2=3
            pad2.refresh()
            
            ruch = ruch + 1
            
        if key is 51:
            if p3 != 0:
                continue
            elif (ruch%2==0):
                pad3.addch(1,2,ord("O"))
                p3=2
            else:
                pad3.addch(1,2,ord("X"))
                p3=3
            pad3.refresh()
           
            ruch = ruch + 1
            
        if key is 52:
            if p4 != 0:
                continue
            elif (ruch%2==0):
                pad4.addch(1,2,ord("O"))
                p4=2
            else:
                pad4.addch(1,2,ord("X"))
                p4=3
            pad4.refresh()
           
            ruch = ruch + 1
            
        if key is 53:
            if p5 != 0:
                continue
            elif (ruch%2==0):
                pad5.addch(1,2,ord("O"))
                p5=2
            else:
                pad5.addch(1,2,ord("X"))
                p5=3
            pad5.refresh()
            
            ruch = ruch + 1
            
        if key is 54:
            if p6 != 0:
                continue
            elif (ruch%2==0):
                pad6.addch(1,2,ord("O"))
                p6=2
            else:
                pad6.addch(1,2,ord("X"))
                p6=3
            pad6.refresh()
            
            ruch = ruch + 1
            
        if key is 55:
            if p7 != 0:
                continue
            elif (ruch%2==0):
                pad7.addch(1,2,ord("O"))
                p7=2
            else:
                pad7.addch(1,2,ord("X"))
                p7=3
            pad7.refresh()
            
            ruch = ruch + 1
            
        if key is 56:
            if p8 != 0:
                continue
            elif (ruch%2==0):
                pad8.addch(1,2,ord("O"))
                p8 = 2
            else:
                pad8.addch(1,2,ord("X"))
                p8 = 3
            pad8.refresh()
            ruch = ruch + 1
            
        if key is 57:
            if p9 != 0:
                continue
            elif (ruch%2==0):
                pad9.addch(1,2,ord("O"))
                p9 = 2
            else:
                pad9.addch(1,2,ord("X"))
                p9 = 3
            
            pad9.refresh()
            ruch = ruch + 1
        
        
        
        
        
        
        

    
    
    
    #zamykanie curses
    
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

wrapper(main)  #wraper przywraca terminal do normalnego stanu
wygranko(p0)
