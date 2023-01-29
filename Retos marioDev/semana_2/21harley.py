def diccionarioHacker():
    return {
        'A':["4","/\\","@","/-\\","^","aye","(L","Д"],
        'B':["I3","8","13","|3","ß","!3","(3","/3",")3","|-]","j3","6"],
        'C':["[","¢","{","<","(","©"],
        'D':[")","|)","(|","[)","I>","|>","?","T)","I7","cl","|}",">","|]"],
        'E':["3","&","£","€","ë","[-","|=-"],
        'F':["|=","ƒ","|#","ph","/=","v"],
        'G':["&","6","(_+","9","C-","gee","(?,","[,","{,","<-","(.",],
        'H':["#","/-/","[-]","]-[",")-(","(-)",":-:","|~|","|-|","]~[","}{","!-!","1-1","\-/","I+I","/-\\"],
        'I':["[]","|","!","eye","3y3","][","1"],
        'J':[",_|","_|","._|","._]","_]",",_]","]",";","1"],
        'K':[">|","|<","/<","1<","|c","|(","|{"],
        'L':["|_","7","1","£","|"],
        'M':["/\\/\\","/\V\\","JVI","[V]","[]V[]","|\\/|","^^","<\/>","{'V'}","(v)","(V)","|V|","nn","IVI","|\\|\\","]\\/[","1^1","ITI","JTI",],
        'N':["^/","|\|","/\/","[\]","<\>","{\}","|V","/V","И","^","ท"],
        'O':["0","Q","()","oh","[]","p","<>","Ø"],
        'p':["|*","|o","|º","?","|^","|>",'|"',"9","[]D","|°","|7",],
        'Q':["(_,)","9","()_","2","0_","<|","&"],
        'R':["I2","|`","|~","|?","/2","|^","lz","|9","2","12","®","[z","Я",".-","|2","|-"],
        'S':["5","$","z","§","ehs","es","2"],
        'T':["7","+","-|-","']['","†",'"|"',"~|~"],
        'U':["(_)","|_|","v","L|","µ","บ"],
        'V':["\/","|/","\|"],
        'W':["\/\/","VV","\\N","'//","\\'","\^/","(n)","\V/","\X/","\|/","\_|_/","\_:_/","Ш","Щ","uu","2u","\\//\\//","พ","v²"],
        'X':["><","Ж","}{","ecks","×","?",")(","]["],
        'Y':["j","`/","Ч","7","\|/","¥","\//"],
        'Z':["2","7_","-/_","%",">_","s","~/_","-\_","-|_"]
        #nos falta la p en adelante url:https://www.gamehouse.com/blog/leet-speak-cheat-sheet/
    }
def encritar_hacker(cadena=str):
    new_cadena=''
    lenguaje_hacker=diccionarioHacker()
    for i in range(len(cadena)):
        if lenguaje_hacker[cadena[i].upper()]!=None :
           new_cadena+=lenguaje_hacker[cadena[i].upper()][0]
        else:
            new_cadena+=cadena[i]
    return new_cadena

def desencritar_hacker(cadena=str):
    lenguaje_hacker=diccionarioHacker()
    new_cadena=''
    i=0
    aux=''
    iterador=0
    while i<len(cadena):
        aux+=cadena[iterador]
        for clave in lenguaje_hacker.keys():
            if lenguaje_hacker[clave][0]==aux:
                new_cadena+=clave
                aux=""
                i+=1
                break
        if iterador+1>=len(cadena):
            break
        iterador+=1
    return new_cadena
    

def main():
    aux=encritar_hacker("hola")
    print(aux)
    print(desencritar_hacker(aux))

if __name__ == '__main__':
    main()