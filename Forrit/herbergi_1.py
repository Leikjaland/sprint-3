# Útgáfa 1.1

# Hlutir sem þarf að satna í skólasofu og útiveru
bok = 0
blom = 0


class leikjaland(object):

# Hér ver verið að taka á móti leikmanni og spyrja um kyn.
    print('Velkomin\\nn í leikjaland')
    def velja_kyn(self):
        kyn = input('Veldu kyn, strakur eða stelpa: ')
        if kyn == 'strakur':
            print('Þú ert ' +kyn)
        elif kyn == 'stelpa':
            print('Þú ert ' + kyn)
        else:
            print('Vinsamlega veldu kyn, strakur eða stelpa')
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
            self.skolastofa(bok)

# Leikmaður fer í útiveru(herbergi 3)
        elif fot == 'utifot':
            print('Þú ert komin\\nn út')
        # utivera(blom)

# Ef ekki er valið skólaföt eða útiföt
        else:
            print ('Þú hefur ekki valið föt')
            self.Herbergi_1()

# Leikmaðurinn fer í skólastofu
    def skolastofa(self,bok):
        #print('test2')
        print('Velkomin\\nn í skólann, nú ert þú í stærðfræði og þú átt að reikna 3 dæmi, gangi þér vel!')
        daemi_1 = input('Hvað er 5+6? ')
        daemi_2 = input('hvað er 8*9? ')
        daemi_3 = input('Hvað er 15-3? ')
        if daemi_1 == '11' and daemi_2=='72' and daemi_3 =='12':
            print('rétt')
            bok =+ 1
            bok=bok
            self.skipta_um_fot(bok)
        elif daemi_1 != '11' and daemi_2=='72' and daemi_3 =='12':
            print('Dæmi 1 er ekki rétt!. Reyndu aftur:')
            self.skolastofa(bok)
        elif daemi_1 == '11' and daemi_2 !='72' and daemi_3 =='12':
            print('Dæmi 2 er ekki rétt!. Reyndu aftur:')
            self.skolastofa(bok)
        elif daemi_1 == '11' and daemi_2=='72' and daemi_3 !='12':
            print('Dæmi 3 er ekki rétt!. Reyndu aftur:')
            self.skolastofa(bok)
        elif daemi_1 != '11' and daemi_2 !='72' and daemi_3 =='12':
            print('Dæmi 1 og 2 eru ekki rétt!. Reyndu aftur:')
            self.skolastofa(bok)
        elif daemi_1 != '11' and daemi_2=='72' and daemi_3 !='12':
            print('Dæmi 1 og 3 eru ekki rétt!. Reyndu aftur:')
            self.skolastofa(bok)
        elif daemi_1 == '11' and daemi_2 !='72' and daemi_3 !='12':
            print('Dæmi 2 og 3 eru ekki rétt!. Reyndu aftur:')
            self.skolastofa(bok)
        else:
            print('ekkert er rétt. Reyndu aftur:')
            self.skolastofa(bok)

# Fallið leyfir leikmanni að koma til baka og skipta um föt til að fara í hitt herbergið
    def skipta_um_fot(self,bok):
        #print('test3')
        if bok == 1 and blom != 1:
            print('Þú ert búin\\nn í skólanum í dag, nú er tími til að fara í útiföt að drífa sig út að leika.')
            # utivera()
        elif bok != 1 and blom == 1:
            print('Vonandi var gaman úti að leika, nú er tími til að fara í skólaföt að drífa sig í skólann.')
            # skolastofa()
        elif bok == 1 and blom == 1:
            print('Nú hefur þú klárað þrautirnar 2 og ert að fara í lokaborðið.')
            #herbergi4()

def  main():
    leikur=leikjaland()
    leikur.velja_kyn()
    leikur.Herbergi_1()


if __name__  == '__main__':
    main()
