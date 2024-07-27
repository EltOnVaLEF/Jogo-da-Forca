import config


Dificuldade = 1
Points_Multiplier = 1.00
Sudden_Death = False
Timer = False
main_tittle = config.Main_Tittle()
line = config.Line('jogo da forca')

while True: #MAIN ------------------------------------------
    print (main_tittle)
    config.Menu('Jogar','Configurações','Sair')
    print (line)
    resp = config.Answer(3)
    if resp == 1:
        config.Main_Tittle()
        resp = config.Game_Start_Menu(Dificuldade,Points_Multiplier,Sudden_Death,Timer)
        config.limpar()
        if resp == 1:
            #GAME START
            Tema = config.Theme_Selector()
            Palavra = config.Word_Selector(Tema,Dificuldade)
            config.Game_Start(Tema,Palavra,Sudden_Death,Timer,Points_Multiplier)
    elif resp == 2: #CONFIGURAÇÕES ------------------------------------------
        while True:
            config.limpar()
            print (main_tittle)
            config.Menu('Dificuldades','Modos de jogo','Voltar')
            print (line)
            resp = config.Answer(3)
            config.limpar()
            if resp == 1: #DIFICULDADES ----------------------------------------
                while True:
                    print (main_tittle)
                    print (f'{"Dificuldade Atual:":<42}',end='')
                    if Dificuldade == 1:
                        print ('Fácil')
                    elif Dificuldade == 2:
                        print ('Normal')
                    elif Dificuldade == 3:
                        print ('Dificil')
                    print (line)
                    config.Menu('Fácil','Normal','Dificil','Voltar')
                    print (line)
                    resp = config.Answer(4)
                    config.limpar()
                    if resp == 4:
                        break
                    else:
                        Dificuldade = config.Difficulty_Selector(resp,Dificuldade)
                        config.limpar()
            elif resp == 2: #MODOS DE JOGO --------------------------------
                print (main_tittle)
                config.Game_Modes(Sudden_Death,Timer)
                resp = config.Answer(3)
                print (line)
                config.limpar()
                if resp == 1: #SUDDEN DEATH ------------------------------
                    if Sudden_Death == False:
                        print ('Deseja Ativar o modo Sudden Death?')
                        print ('(Suas vidas são reduzidas de 6 para 2) | 2.00x')
                        print (line)
                        print ('(1) | Sim\n(2) | Não')
                        print (line)
                        resp = config.Answer(2)
                        if resp == 1:
                            Points_Multiplier += 2.00
                            Sudden_Death = True
                            print ('Modo Sudden Death ativado com sucesso!')
                        
                    else:
                        print ('Deseja Desativar o modo Sudden Death?')
                        print (line)
                        print ('(1) | Sim\n(2) | Não')
                        print (line)
                        resp = config.Answer(2)
                        if resp == 1:
                            Points_Multiplier -= 2.00
                            Sudden_Death = False
                            print ('Modo Sudden Death desativado com sucesso!')
                elif resp == 2: #TIMER -----------------------------
                    if Timer == False:
                        print ('Deseja ativar o modo Timer?')
                        print ('(Ativa um temporizador de 90 segundos | + 0.75x')
                        print (line)
                        print ('(1) | Sim\n(2) | Não')
                        print (line)
                        resp = config.Answer(2)
                        if resp == 1:
                            Points_Multiplier += 0.75
                            Timer = True
                            print ('Timer ativado com sucesso!')
                    else:
                        print ('Deseja desativar o modo Timer?')
                        print (line)
                        print ('(1) | Sim\n(2) | Não')
                        print (line)
                        resp = config.Answer(2)
                        if resp == 1:
                            Points_Multiplier -= 0.75
                            Timer = False
                            print ('Timer desativado com sucesso!')
            else:
                config.limpar()
                break
    else:
        break

                        




