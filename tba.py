import time

print("Hallo daar!, ik ben Serj Tankian")
time.sleep(2)
print("Wie ben jij?")

username = input("Jouw naam:")

print("Hello " + username)
print(" ")
time.sleep(2)

print("Ik ben een vluchteling uit Armenië en")
print("dit is mijn verhaal over hoe ik hier ben gekomen.")
print(" ")
time.sleep(3)

# Inleiding
print("Het is een zonnige dag op een zaterdag ochtend. Je hebt lang gewerkt aan school en heb eindelijk een beetje tijd voor jezelf.")
print("Je gaat kijken of je beste vriend Daron thuis is. Hij woont niet heel ver weg dus je gaat naar zijn huis.")
print("Je loopt dezelfde route die je altijd neemt. Je loopt door het steegje en je ziet zijn huis in de verte.")
print("Nog een paar minuutjes lopen door deze lange straat.")
print(" ")
print("Plotseling hoor je een grote knal. Het was extreem luid maar om een of andere reden kijk je er niet eens van om.")
print("Je bent het gewend. Armenië heeft wel vaker van dit soort explosies ineens uit het niets.")
print("Maar nu zie je de hele straat rennen en schreeuwen. Je weet niet wat je moet doen dus je…")
time.sleep(3)

# Keuze vraag 1
print("A: Rent door naar Daron zijn huis om te kijken of hij het ook hoorde.")
print("B: Rent weg de kant op waar de rest heen rent.")

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]

while True:
        choice1 = input(">>> ")
        if choice1 in answer_A:
                # Stukje 1
                print('Je rent gewoon door naar Daron zijn huis. Je was toch zo dichtbij! Eenmaal aangekomen bij zijn huis zijn er al vijf bommen afgegaan.')
                print('Je klopt op zijn raam. Niks. Je roept naar binnen want je merkt dat zijn raam al open staat.')
                print('Niks. Je loopt om misschien is hij gitaar aan het spelen in de tuin. Ook niet je begint je zorgen te maken.')
                print('Misschien hebben ze hem wel meegenomen. Misschien heeft een van de bommen zijn huis geraakt.')
                print('Nee dat niet want zijn huis is nog in staat. Je rent weer terug om hem misschien te bellen.')
                print('Op de helft van de route rijd er een grote auto met bemanning langs en stopt wanneer ze jou zien. Ze roepen iets onverstaanbaars want de explosies zijn te luid. Ik…')
                print(' ')

                print('A: Loop dicherbij om ze beter te verstaan.')
                print('B: Ren weg van de explosies richting mijn eigen huis.')
                print(' ')

                choice2 = input('>>> ')
                if choice2 in answer_A:
                        # Stukje 3
                        print('Je roept: wat zeggen jullie? En stapt dichter bij. De jongens richten hun wapen op je en roepen nog meer onverstaanbare dingen.')
                        print('Je stapt nog dichterbij en een van de jongens schiet recht voor me op de grond om mij waar te schuwen en wijst naar de kant waar de bommen niet vandaan komen.')
                        print('Ik neem aan dat hij bedoelt dat ik moet rennen. Dus ik knik en ren de andere kant op. Ik kijk nog een keer achter me en zie ze het slachtveld in rijden.')
                        print('Ik roep nog succes maar ik denk dat ze het niet gehoord hebben. Ik kijk weer voor me en ren nog harder als er plotseling een bom recht voor mijn neus beland.')
                        print('Ik schik me kapot en val een paar meter naar achter en ik denk dat ik mijn been gebroken heb. Ik…')

                        print('A: Probeer nog op te staan om te rennen.')
                        print('B: Roep voor hulp aan de mensen die langs mij rennen')
                        print(' ')
                
                        choice3 = input('>>> ')        
                        if choice3 in answer_A:
                                # Stukje 7
                                print('Ik pak mijn been vast en probeer nog op te staan. Het lukt niet. Dit is het. Ik ben nog zo jong. Hoe kan ik nu al opgeven?')
                                print('Ik heb nog een heel leven voor me! Sta op! Hoor ik in mijn hoofd. Maar het lukt echt niet.')
                                print('Ik voel plotseling iets heel erg prikken in mijn maag. Ik voel in mijn maag een hard stukje. De explosie heeft iets in mijn maag geschoten.')
                                print('Ik bloed langzaam dood terwijl de tranen over mijn wangen glijden.')
                                print(' ')
                                print(' ')

                                print('Einde 1: Je bent vermoord door een bom...')
                                time.sleep(5)
                                break
                        elif choice3 in answer_B:
                                # Stukje 8
                                print('Ik roep om me heen. HELP!! HELP!!. Niemand kijkt überhaupt om. Ze zijn te gefocust op hun eigen leven redden. Ik pak een van de mensen die langs rennen bij hun been.')
                                print('Hij valt. En kijkt achter zich en ziet mij daar liggen. Hij zegt niks, pakt mij op en rent door.')
                                print('Ik vraag naar zijn naam maar hij antwoord niet. Ik tik hem op zijn hoofd en hij reageert niet. Zou hij doof zijn? Ik…')
                                print(' ')

                                print('A: Val uit zijn armen na een grote explosie.')
                                print('B: Val uit zijn armen en krijg last van mijn enkel. Zal ik naar Daron zijn huis gaan?')
                                print(' ')

                                choice4 = input('>>> ')
                                if choice4 in answer_A:
                                        # Stukje 7
                                        print('Ik pak mijn been vast en probeer nog op te staan. Het lukt niet. Dit is het. Ik ben nog zo jong. Hoe kan ik nu al opgeven?')
                                        print('Ik heb nog een heel leven voor me! Sta op! Hoor ik in mijn hoofd. Maar het lukt echt niet.')
                                        print('Ik voel plotseling iets heel erg prikken in mijn maag. Ik voel in mijn maag een hard stukje. De explosie heeft iets in mijn maag geschoten.')
                                        print('Ik bloed langzaam dood terwijl de tranen over mijn wangen glijden.')
                                        print(' ')
                                        print(' ')

                                        print('Einde 1: Je bent vermoord door een bom...')
                                        time.sleep(5)
                                        break
                
                elif choice2 in answer_B:
                        # Stukje 4
                        print('''Ik ren naar huis door het steegje waar ik het meest veilig ben van explosies.
                              Ik zie mijn huis en ren de deur in naar binnen en zie daar mijn moeder en vader staan met mijn broertje en zusje.
                              Ze zijn zo blij om me toch te zien en omhelzen mij gelijk. Ze pakken mijn hand en rennen het huis uit. Ik…''')

                        print('A: Waarschuw mijn ouders dat het heel erg gevaarlijk is buiten.')
                        print('B: Zwijg en ren gewoon achter ze aan.')
                        print(' ')
                        
                        choice11 = input('>>> ')
                        if choice11 in answer_A:
                                # Stukje 9
                                print('''Ik tik op mijn moeder haar schouder en zeg dat het gevaarlijk is buiten. Ze antwoord niet. Ik roep het nog een keer maar dan luider.
                                        Ze schreeuwt: weet ik! En rent door. Maar waarom rennen we dan naar buiten? Roep ik. Dat zie je straks wel. Zegt ze. Ik…''')

                                print('A: Haal mijn schouders op en blijf rennen.')
                                print('B: Probeer los te laten maar het lukt niet. Een explosie volgt en vervolgens lig ik.')
                                print(' ')

                        elif choice11 in answer_B:
                                # Stukje 10
                                print('''We rennen en komen aan bij een auto. Hij is niet van ons. Mijn vader breekt het raam en krijgt de auto aan de praat.
                                                Mijn moeder stapt in en roept: stap in! We gaan. Ik zeg maar pap dit is stelen. Je kan niet zomaar een auto pakken die mensen moeten ook nog vluchten.
                                                Mijn vader zegt stil en stap in. Ik ben te bang om er wat van te zeggen en stap in. We komen uiteindelijk veilig bij een bootje. We stappen in.
                                                Een maand later zijn we aangekomen in Amerika waar ik een nieuw leven start en een band
                                                start om te zingen over wat er allemaal gebeurt in Armenië samen met mijn vrienden: Daron Malakian, Shavo Odadjian en John Dolmayan.''')
                                        break

                                choice12 = input('>>> ')
                                if choice12 in answer_A:
                                        # Stukje 10
                                        print('''We rennen en komen aan bij een auto. Hij is niet van ons. Mijn vader breekt het raam en krijgt de auto aan de praat.
                                                Mijn moeder stapt in en roept: stap in! We gaan. Ik zeg maar pap dit is stelen. Je kan niet zomaar een auto pakken die mensen moeten ook nog vluchten.
                                                Mijn vader zegt stil en stap in. Ik ben te bang om er wat van te zeggen en stap in. We komen uiteindelijk veilig bij een bootje. We stappen in.
                                                Een maand later zijn we aangekomen in Amerika waar ik een nieuw leven start en een band
                                                start om te zingen over wat er allemaal gebeurt in Armenië samen met mijn vrienden: Daron Malakian, Shavo Odadjian en John Dolmayan.''')
                                        break
                                elif choice12 in answer_B:
                                        # Stukje 7
                                        print('Ik pak mijn been vast en probeer nog op te staan. Het lukt niet. Dit is het. Ik ben nog zo jong. Hoe kan ik nu al opgeven?')
                                        print('Ik heb nog een heel leven voor me! Sta op! Hoor ik in mijn hoofd. Maar het lukt echt niet.')
                                        print('Ik voel plotseling iets heel erg prikken in mijn maag. Ik voel in mijn maag een hard stukje. De explosie heeft iets in mijn maag geschoten.')
                                        print('Ik bloed langzaam dood terwijl de tranen over mijn wangen glijden.')
                                        print(' ')
                                        print(' ')

                                        print('Einde 1: Je bent vermoord door een bom...')
                                        time.sleep(5)
                                        break
        elif choice1 in answer_B:
                # Stukje 2
                print('Ik ren maar gewoon mee met de rest ik denk dat het te gevaarlijk is om nu nog naar Daron te gaan. Plus hij zal vast niet thuis zijn vanwege de explosies.')
                print('Uiteindelijk lopen we met een grote groep ver van de explosies weg als er ineens een fluitend geluid boven je ontstaat.')
                print('Get fluitende geluidje word steeds luider en je kijkt omhoog. BOEM!. Je ligt op de grond en je ziet niks. Er zit allemaal zand in je mond en in je ogen.')
                print('Je kan je ogen niet open doen en je keel voelt heel droog aan. Je benen zijn verlamd je kan niet bewegen. Even later kan je toch je ogen open doen.')
                print('Het prikt heel erg maar het moet toch. De hele groep ligt op de grond. Je…')
                print(' ')

                print('A: Gaat kijken of iemand nog leeft.')
                print('B: Rent heel hard naar huis om te kijken of je ouders nog leven.')
                print(' ')

                choice8 = input('>>> ')
                if choice8 in answer_A:
                        # Stukje 5
                        print('Mijn ogen prikken enorm! Maar ik kan weer zien. Ik kijk rustig om me heen en zie een beweging. Ik kijk tussen de dode lichamen en zie dat het een klein kindje is,')
                        print('nog jonger dan ik. Ik pak het kind en vraag of het gaat. Hij is doof geworden door de explosie. Ik kijk of hij nog ergens wonden heeft.')
                        print('Wonderlijk genoeg kan ik nog redelijk lopen, horen en zien. Maar daar gaat het even niet om. De hele groep is dood! Ik…')
                        print(' ')

                        print('A: Pak het kind bij zijn handen en begin te rennen.')
                        print('B: Blijf wachten tot er hulp arriveert om mij en het kindje te redden.')
                        print(' ')

                        
                        choice9 = input('>>> ')
                        if choice9 in answer_A:
                                # Stukje 11
                                print('Ik pak het kind bij zijn handen en spring over de lichamen. Arme mensen. Hebben dat hele stuk gerend en hebben het alsnog niet overleeft.')
                                print('We rennen en we rennen. We komen aan bij een rivier. Waar een groep mensen staat. Ze zingen: LIAR! KILLER! DEMON! Back to the river Aras, freedome!')
                                print('! Ik neem aan dat de rivier Aras heet. Ik vraag rond wat de mensen daar doen.')
                                print('Ze zeggen dat dit de enige veilige plek is in Armenië en dat ze daar wachten op hulp. Ik…')
                                print(' ')

                                print('A: Blijf bij ze. Ze zorgen ervoor dat ik me veilig voel.')
                                print('B: Ik ren langs de rivier. Ver weg van die gekken!')
                                print(' ')

                        elif choice9 in answer_B:
                                # Stukje 12
                                print('''We blijven rustig wachten totdat er hulp arriveert. Na een half uur wachten begint het kind te huilen. Ik weet niet wat ik er mee aan moet dus ik negeer het gewoon.
                                        Ik hoor nog een fluitend geluid en sluit mijn oren en ogen. Ik wacht op het harde geluid. Maar het komt niet. Ik doe mijn ogen open en ik ben ineens in een helemaal witte dimensie.
                                        Waar ik verwelkomd word door mensen met vleugels. Ik kijk om me heen en zie niks behalve wit. Ik vraag wie dat zijn maar ze praten alleen latijn. Dit is de hemel. Ik ben dood!''')

                                print('Einde, je bent in de hemel voor een lange tijd totdat je je vrienden tegenkomt en je daar een nieuw leven start.')
                                break

                                choice10 = input('>>> ')
                                if choice10 in answer_A:
                                        # Stukje 16
                                        print('We blijven bij ze staan. Uiteindelijk komt er iemand over de rivier ons redden met een bootje. We varen voor een maand lang over de grote zee die lijkt alsof het geen einde heeft.')
                                        print('Het duurt lang maar uit eindelijk komen we aan in Amerika waar ik zonder ouders op gegroeid ben en een carriere heb gevolgd als muzikant en heb ik een band gestart met Daron.')
                                        print('We zijn super bekend geworden en touren nu over de hele wereld.')
                                        print(' ')
                                        print(' ')

                                        print('Einde 5')
                                        break
                                elif choice10 in answer_B:
                                        # Stukje 17
                                        print('''We rennen langs de rivier totdat het kind uitglijdt over een steen. Ik probeer hem nog vast te grijpen maar hij valt in de rivier.
                                                Ik spring er achteraan en verdrinken beide in de rivier die te hard stroomt om eruit te komen.''')

                                        print('Einde, je bent verdronken')
                                        break

                elif choice8 in answer_B:
                        # Stukje 6
                        print('''Ik ren zo hard weg naar huis en zie dat mijn huis geraakt is door een bom. Ik val op mijn knieën en begin zo hard te huilen. Mijn ouders mijn broertjes ze zijn allemaal dood.
                                Wat nu? Toch kijken of Daron er is of gewoon door rennen naar een schuilplek? Ik besluit door te rennen naar een schuilplek. Mijn benen worden moe dus ik besluit te stoppen om op adem te komen.
                                Ik zie langs de weg een jongetje zitten van mijn leeftijd. Ik…''')
                        print(' ')

                        print('A: Loop naar hem toe en vraag of het gaat.')
                        print('B: Negeer hem en loop door.')
                        print(' ')

                        if choice8 in answer_B:
                                # Stukje 14
                                print('''Ik loop verder en negeer het kind en ben nogsteeds in de menigte van mensen. Ik vraag me af waar mijn ouders zijn en hoe het met hun gaat. Misschien zijn ze wel dood.
                                        Ik grijp naar mijn broekzak. Maar ik had mijn telefoon niet bij me voel ik nu, dus dat word hem niet. Ik kijk om me heen en zie niemand die ik ken. Uiteindelijk staan we stil.
                                        Ineens hoor je een enorme explosie en alles word zwart…''')

                                print('A: Open je ogen!.')
                                print('B: OPEN JE OGEN!!!!')
                                print(' ')

                                choice22 = input('>>> ')
                                if choice22 in answer_A:
                                        # Stukje 15
                                        print('''Ik doe rustig mijn ogen open en zie niks. Ik kan mijn ogen niet open doen. Alles is zwart. Ik voel een enorme pijn in mijn hele lichaam.
                                                Maar het gaat langzaam weg. Heel langzaam voel ik me weer alsof ik lekker warm in bed lig. Ik word er rustig van. Ik val in slaap.. denk ik. Lekker wachten tot het ochtend is.''')
                                        print('Einde You Died.....')
                                        break
                                elif choice22 in answer_B:
                                        print('''Ik doe rustig mijn ogen open en zie niks. Ik kan mijn ogen niet open doen. Alles is zwart. Ik voel een enorme pijn in mijn hele lichaam.
                                                Maar het gaat langzaam weg. Heel langzaam voel ik me weer alsof ik lekker warm in bed lig. Ik word er rustig van. Ik val in slaap.. denk ik. Lekker wachten tot het ochtend is.''')
                                        print('Einde You Died')
                                        break
                                
