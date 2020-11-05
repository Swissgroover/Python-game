import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_O = ["O", "o"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

gun = 0
sword = 0
flower = 0

required = ("\nKasuta A, B, or C\n")

def intro():
  print ("Peale purjus peaga õhtut ärkad "
  "järgmisel hommikul pimedas metses. Pea valutab " 
  "ja avastad end uues keskonnas uute ülesannetega "
  "ebatavalises kohas. Vaikselt hakkab vaikus hääbuma ja "
  "kuuled rohitsevat orci enda seljataga, kes "
  "jookseb sinu poole. Sinu võimalused:")
  time.sleep(1)
  print ("""  A. Võtad kivi ja vistad teda?
  B. Viskad pikali ja ootad?
  C. Põgened""")
  choice = input(">>> ")
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nJama lugu. "
    "\n\nSa surid!")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()

def option_rock(): 
  print ("\nOrc sai tabamuse, aga toibub. ta hakkab "
  "uuesti sinupoole jooksma. Kas sa:")
  time.sleep(1)
  print ("""  A. Põgened
  B. Viskad veel ühe kivi
  C. Põgened koopasse""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nSa otsustasid visata veel ühe kivi. " 
    "kuid ei teinud midagi erilist. Lihtsalt põrkas vast "
    "orci pead. Veist läks kehvasti. \n\nSa surid!")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  print ("\nSa kardad, kuna koobas on pime ja kõle. "
  "Enne kui sisenesid, nägid helkivat mööka põrandal. "
  "Kas võtsid selle üles?. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    sword = 1 
  else:
    sword = 0
  print ("\nMis järgmiseks teed?")
  time.sleep(1)
  print ("""  A. Peidad vaikuses?
  B. Kakled
  C. Põgened?""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nKas tõesti lähed pimedasse tagasi? Ma arvan "
    "et orcid näevad pimedas päris hästi. pole kindel, aga "
    "aga ma arvan et jah, niiet......\n\nsa surid!")
  elif choice in answer_B:
   if sword > 0:
    print ("\nSa ootasid, peegelduv möök paistis orcile "
    "Kui ta hakkas lähmeale tulema, sa hakkasid ehmuma ja paanitsema. "
    "Kui orc hakkas mööka sinu käest ära võtma "
    "sa torkasid selle läbi tema! "
    " \n\nJääd ellu!")
   else: 
     print ("\nOleksid pidanud kaklema! Möku! "
     " \n\nKutupiilu!")
  elif choice in answer_C:
    print ("Kui orc sisenes koopasse, sa vaikselt hiilisid "
    "välja. Sa oled mitu meetrit eemal, aga orc "
    "keerab ja näeb sind jooksmas.")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\nSa jooksed kiiresti, kuid orc on suurem "
  "ja palju kiirem. Mis edasi?:")
  time.sleep(1)
  print ("""  A. Peidad end puude taha?
  B. Arvad et kütad kaussi?
  C. Jooksed eemal olevasse linna?""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("Üpris loll tegu, või mis?. "
    "\n\nkutu!")
  elif choice in answer_B:
    print ("\nhehe, orcile kaussi kütta? "
    "\n\nKutu!")
  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()
    
def option_town():
  print ("\nKui rägielt punud, avastad mudas roostes mööga. "
  "Sa kiirelt üritad seda krabada, kuid ebaõnnestud "
  "Üritad rahulikult hingata, samal ajal kui peitu poed. "
  "Vana äbariku maja taga üritad vaikselt oodata millal orc möödub. "
  "Nuka taga välja joosted märkad Roosi end lähedal. "
  "Korjad üles? Roosi? päriselt?Y/N")
  choice = input(">>> ")
  if choice in yes:
    flower = 1 
  else:
    flower = 0
  print ("Sa kuuled ta jalasamme, ning valmistud ennast "
  "talle vastu hakkama.")
  time.sleep(1)
  if flower > 0:
    print ("\nSa krabad põõsast suvalise lille ja loodad(kuidagi) "
    "et see peatab ta??? whaaaaat??? aganoh... toimib! Orc oli neiu"
    "kes on romatik! "
    "\n\nLäks vist vähe imelikuks, aga elad!")
  else: 
     print ("\nÄkki oleks pidanud lille proovima? "
     "\n\nBOOM!! Surnud!")

intro()