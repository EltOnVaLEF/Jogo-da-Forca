from random import randint
import threading
import time
import os

class TempoEsgotadoErro(Exception):
    pass


class Cronometro:
    def __init__(self,duracao):
        self.tempo = duracao
        self.rodando = False

    def iniciar(self):
        self.rodando = True
        threading.Thread(target=self.cronometro).start()
    
    def parar(self):
        self.rodando = False
    

    def cronometro(self):
        while self.rodando and self.tempo > 0: 
            time.sleep(1)
            self.tempo -=1
        if self.tempo == 0:
            print (f'\n{Line("jogo da forca")}\n{"TEMPO ESGOTADO":^50}\n{Line("jogo da forca")}')
            print (f'Aperte Enter para continuar')
            self.parar


def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def tempo_esgotado():
    raise TempoEsgotadoErro(f'')

def Main_Tittle():
    tittle = 'Jogo da Forca'
    tam = len('jogo da forca')
    return (f'{"-"*tam}==|> {tittle} <|=={"-"*tam}')


def Menu(*opções:list,):
    for cont,word in enumerate(opções):
        print (f'{cont+1} | {word}')


def Line(name:str):
    tam = len(name)*3 + 10
    return (f'{"-"*tam}')


def Answer(resp_limit:int):
    while True:
        catch_resp = str (input ('--|>> '))
        try:
            catch_resp = int(catch_resp)
            if catch_resp > 0 and catch_resp <= resp_limit:
                return catch_resp
            else:
                print ('Digite um número valido!')
        except:
            print ('Digite um número valido!')


def Difficulty_Selector(Difficulty, Atual):
    print (Line('jogo da forca'))
    if Difficulty == Atual:
        print ('Está dificuldade já está selecionada!')
        Line ('jogo da forca')
        return Difficulty
    else:
        print ('Deseja Definir o jogo para ', end='')
        if Difficulty == 1:
            print ('Fácil')
        elif Difficulty == 2:
            print ('Normal')
        else:
            print ('Dificil')
        print ('(1) Sim\n(2) Não')
        print (Line('jogo da forca'))
        resp = Answer(2)
        if resp == 1:
            print ('Dificuldade modificada')
            return Difficulty
        else:
            return Atual
        

def Game_Modes(Sudden_Death=bool,Timer=bool):
    mods = ['Sudden Death','Timer']
    for cont, name in enumerate(mods):
            print (f'{cont+1} | {name:<29}',end='| ')
            if cont == 0:
                if Sudden_Death == True:
                    print ('Ativado')
                else:
                    print ('Desativado')
            elif cont == 1:
                if Timer == True:
                    print ('Ativado')
                else:
                    print ('Desativado')
    print ('3 | Voltar')
    print (Line('jogo da forca'))


def Game_Start_Menu(Dificulty,Points_Multiplier,Sudden_Death,Timer):
    limpar()
    mods = [Sudden_Death,Timer]
    print (f'{Main_Tittle()}\n')
    print (f'{"":<9} | {"Dificuldade":<12} > ',end='')
    if Dificulty == 1:
        print (f'{"Fácil":<11}|')
    elif Dificulty == 2:
        print (f'{"Normal":<11}|')
    elif Dificulty == 3:
        print (f'{"Difícil":<11}|')
    print (f'{"":<9} | {"Multiplier":<12} > {Points_Multiplier}{"x":<8}|')
    for cont, name in enumerate(mods):
        if cont == 0:
            print (f'{"":<9} | {"Sudden Death":<12} > ',end='')
            if Sudden_Death == True:
                print (f'{"Ativado":<11}|')
            else:
                print (f'{"Desativado":<11}|')
        elif cont == 1:
            print (f'{"":<9} | {"Timer":<12} > ',end='')
            if Timer == True:
                print (f'{"Ativado":<11}|')
            else:
                print (f'{"Desativado":<11}|')
    print (f'')
    print (Line('jogo da forca'))
    print (f'{"Iniciar Jogo?":^50}')
    print (f'{"(1) Sim / (2) Não":^50}')
    print (Line('jogo da forca'))
    return Answer(2)


def Theme_Selector():
    tema_sort = randint(1,8)
    if tema_sort == 1:
        tema = "animais"
    elif tema_sort == 2:
        tema = "cores"
    elif tema_sort == 3:
        tema = "esportes"
    elif tema_sort == 4:
        tema = "filmes"
    elif tema_sort == 5:
        tema = "frutas"
    elif tema_sort == 6:
        tema = "objetos"
    elif tema_sort == 7:
        tema = "paises"
    else:
        tema = "profissoes"
    return tema


def Word_Selector(tema,Difficulty):
    name_sort = randint(0,14)
    with open (f'words/{tema}.data', 'r') as Temas:
        lista_de_nomes = Temas.readlines()
        main_word = lista_de_nomes[name_sort]
        while True:
            if Difficulty == 3:
                if len(main_word) <= 7:
                    name_sort = randint(0,14)
                    main_word = lista_de_nomes[name_sort]
                else:
                    break
            else:
                break
        return main_word


def Game_Start(Theme:str, Word:str, Sudden_Death, Timer,Points):
    limpar()
    try:
        tittle_str = Main_Tittle()
        linha = Line('jogo da forca')
        tentativas = []
        Theme = Theme.capitalize()
        Word = Word.lower().strip("\n")
        hidden_word = ['_' for _ in Word]
        if Sudden_Death == True:
            Life = 2
        else:
            Life = 6
        if Timer == True:
            crom = Cronometro(90)
            crom.iniciar()   
        while Life > 0:
            if Timer == True:
                if crom.tempo == 0:
                    tempo_esgotado()
            print(f'{tittle_str}')
            if Timer == True:
                print(f'Tema: {Theme} | Vidas Restantes: {Life} | Tempo Restante: {crom.tempo}s')
            else:
                print(f'Tema: {Theme} | Vidas Restantes: {Life}')
            print(f'{linha}')
            print(f"| {''.join(hidden_word)}",end= '')
            letra = input (' | Digite uma letra: ').strip().lower()
            if letra in Word and letra not in tentativas:
                for pos, char in enumerate(Word):
                    if char == letra:
                        hidden_word[pos] = letra
            else:
                Life -= 1
                tentativas.append(letra)
            if "_" not in hidden_word:
                print (linha)
                print (f'{"VOCÊ VENCEU!":^50}')
                print (f'{"A PALAVRA ERA {}".format(Word.capitalize()):^50}')
                if Sudden_Death == False:
                    print (f'{"Pontos: {}".format ((255*Life)*Points):^50}')
                else:
                    print (f'{"Pontos: {}".format ((255*(Life*6))*Points):^50}')
                print (linha)
                input (f'Aperte Enter para continuar')
                break
            limpar()
        limpar()
        if Life == 0:
                print (linha)
                print (f'{"SUAS VIDAS ACABARAM, VOCÊ PERDEU!":^50}')
                print (f'{"A PALAVRA ERA {}".format(Word.capitalize()):^50}')
                print (linha)
                if Timer == True:
                    crom.parar()
                input (f'Aperte Enter para continuar')
                limpar()
    except TempoEsgotadoErro:
        if Timer == True:
            crom.parar()
        limpar()

    

