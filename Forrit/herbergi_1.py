# Útgáfa 1.1
import sys
import time
import select
import graphics
from graphics import *

# Hlutir sem þarf að satna í skólasofu og útiveru
bok = 0
blom = 0


class leikjaland(object):

# Hér ver verið að taka á móti leikmanni og spyrja um kyn.
    print('Velkomin\\nn í leikjaland')
    def velja_kyn(self):
        kyn = input('Veldu kyn, strákur eða stelpa: ')
        if kyn == 'strákur':
            win = GraphWin("strákur", 600, 600)
            myImage = Image(Point(300,300), "boy.gif")
            myImage.draw(win)
            txt = Text(Point(310,330),'Þú ert strákur')
            txt.draw(win)
            time.sleep(5)
            win.close()
            print('Þú ert ' +kyn)
        elif kyn == 'stelpa':
            win = GraphWin("stelpa", 600, 600)
            myImage = Image(Point(300,300), "girl.gif")
            myImage.draw(win)
            txt = Text(Point(150,330),'Þú ert stelpa')
            txt.draw(win)
            time.sleep(5)
            win.close()
            print('Þú ert ' + kyn)
        else:
            print('Vinsamlega veldu kyn, strákur eða stelpa')
            self.velja_kyn()

# Hér byrjar herbergi_1
    def Herbergi_1(self):
        #print('test1')
        while (1):
            try:
                fot= input('Viltu fara í skólann eða út að leika, velja\\skrifa skolafot eða utifot: ')
                fot=fot
                break
            except:
                print ('Þú hefur ekki valið föt')

# leikmaður fer í skolastofuna(herbergi 2)
        if fot == 'skolafot':
            print('Þú ert komin\\nn í skólann')
            self.skolastofa(bok,blom)

# Leikmaður fer í útiveru(herbergi 3)
        elif fot == 'utifot':
            print('Þú ert komin\\nn út')
            self.utivera(bok,blom)

# Ef ekki er valið skólaföt eða útiföt
        else:
            print ('Þú hefur ekki valið föt')
            self.Herbergi_1()

# Leikmaðurinn fer í skólastofu
    def skolastofa(self,bok,blom):
        #print('test2')
        print('Velkomin\\nn í skólann, nú ert þú í stærðfræði og þú átt að reikna 3 dæmi, gangi þér vel!')
        daemi_1 = input('Hvað er 5+6? ')
        daemi_2 = input('hvað er 8*9? ')
        daemi_3 = input('Hvað er 15-3? ')
        if daemi_1 == '11' and daemi_2=='72' and daemi_3 =='12':
            print('rétt')
            bok =+ 1
            bok=bok
            self.skipta_um_fot(bok,blom)
        elif daemi_1 != '11' and daemi_2=='72' and daemi_3 =='12':
            print('Dæmi 1 er ekki rétt!. Reyndu aftur:')
            self.skolastofa(bok,blom)
        elif daemi_1 == '11' and daemi_2 !='72' and daemi_3 =='12':
            print('Dæmi 2 er ekki rétt!. Reyndu aftur:')
            self.skolastofa(bok,blom)
        elif daemi_1 == '11' and daemi_2=='72' and daemi_3 !='12':
            print('Dæmi 3 er ekki rétt!. Reyndu aftur:')
            self.skolastofa(bok,blom)
        elif daemi_1 != '11' and daemi_2 !='72' and daemi_3 =='12':
            print('Dæmi 1 og 2 eru ekki rétt!. Reyndu aftur:')
            self.skolastofa(bok,blom)
        elif daemi_1 != '11' and daemi_2=='72' and daemi_3 !='12':
            print('Dæmi 1 og 3 eru ekki rétt!. Reyndu aftur:')
            self.skolastofa(bok,blom)
        elif daemi_1 == '11' and daemi_2 !='72' and daemi_3 !='12':
            print('Dæmi 2 og 3 eru ekki rétt!. Reyndu aftur:')
            self.skolastofa(bok,blom)
        else:
            print('ekkert er rétt. Reyndu aftur:')
            self.skolastofa(bok,blom)

    def utivera(self,bok,blom):
        #print('Test3')
        print('Nú birtist mynd!')
        print('Teldu hvað það eru mörg gul blóm á myndinni')

        win = GraphWin("Blóm", 400, 400)
        myImage = Image(Point(200,100), "flow.gif")
        myImage.draw(win)
        txt = Text(Point(200,300),'Teldu hvað það eru mörg gul blóm á myndinni')
        txt.draw(win)
        time.sleep(5)
        win.close()

        spurning1 = input('Hvað voru mörg gul blóm á myndinni? ')

        print('Nú birtist önnur mynd, teldu hvað það eru mörg svín á myndinni!')
        win = GraphWin("Dýr", 600, 600)
        myImage = Image(Point(300, 300), "dyr.gif")
        myImage.draw(win)
        txt = Text(Point(300,550),'Teldu hvað það eru mörg svín á myndinni!')
        txt.draw(win)
        time.sleep(5)
        win.close()

        spurning2 = input('Hvað eru mörg svín á myndinni? ')

        print('Nú birtist síðasta myndin, skoðaðu vel hvað er á myndinni')
        win = GraphWin("Himinn", 600, 600)
        myImage = Image(Point(300, 300), "himinn.gif")
        myImage.draw(win)
        txt = Text(Point(300,550),'Skoðaðu vel hvað er á myndinni')
        txt.draw(win)
        time.sleep(5)
        win.close()

        spurning3 = input('Hvað passar ekki inn í? Ský, himinn, bíll eða stjörnur? ')

        if spurning1 == '3' and spurning2 == '4' and spurning3 == 'bíll':
            print('Allt rétt meistari!')
            blom =+ 1
            blom = blom
            self.skipta_um_fot(bok,blom)
        elif spurning1 != '3' and spurning2 == '4' and spurning3 == 'bíll':
            print('Allt rétt nema 1 meistari, reyndu aftur!')
            self.utivera(bok,blom)
        elif spurning1 == '3' and spurning2 != '4' and spurning3 == 'bíll':
            print('Allt rétt nema 2 meistari, reyndu aftur!')
            self.utivera(bok,blom)
        elif spurning1 == '3' and spurning2 == '4' and spurning3 != 'bíll':
            print('Allt rétt nema 3 meistari, reyndu aftur!')
            self.utivera(bok,blom)
        elif spurning1 == '3' and spurning2 != '4' and spurning3 != 'bíll':
            print('Dæmi 1 rétt meistari, reyndu aftur!')
            self.utivera(bok,blom)
        elif spurning1 != '3' and spurning2 == '4' and spurning3 != 'bíll':
            print('Dæmi 2 rétt meistari, reyndu aftur!')
            self.utivera(bok,blom)
        elif spurning1 != '3' and spurning2 != '4' and spurning3 == 'bíll':
            print('Dæmi 3 rétt meistari, reyndu aftur!')
            self.utivera(bok,blom)
        else:
            print('Ekkert er rétt, reyndu aftur!')
            self.utivera(bok,blom)

# Fallið leyfir leikmanni að koma til baka og skipta um föt til að fara í hitt herbergið
    def skipta_um_fot(self,bok,blom):
        #print('test4')
        if bok == 1 and blom != 1:
            print('Þú ert búin\\nn í skólanum í dag, nú er tími til að fara í útiföt að drífa sig út að leika.')
            self.utivera(bok,blom)
        elif bok != 1 and blom == 1:
            print('Vonandi var gaman úti að leika, nú er tími til að fara í skólaföt að drífa sig í skólann.')
            self.skolastofa(bok,blom)
        elif bok == 1 and blom == 1:
            print('Nú hefur þú klárað þrautirnar 2 og ert að fara í lokaborðið.')
            #herbergi4()

def  main():
    leikur=leikjaland()
    leikur.velja_kyn()
    leikur.Herbergi_1()

if __name__  == '__main__':
    main()
