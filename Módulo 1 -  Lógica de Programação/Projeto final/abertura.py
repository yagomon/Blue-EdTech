from time import sleep
# Abretura do jogo

string = '███████╗██╗   ██╗██████╗ ███████╗██████╗    ''██████╗  █████╗ ████████╗ █████╗ ████████╗ █████╗ \n''██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗    ''██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗╚══██╔══╝██╔══██╗\n''███████╗██║   ██║██████╔╝█████╗  ██████╔╝    ''██████╔╝███████║   ██║   ███████║   ██║   ███████║\n''╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗    ''██╔══██╗██╔══██║   ██║   ██╔══██║   ██║   ██╔══██║\n''███████║╚██████╔╝██║     ███████╗██║  ██║    ''██████╔╝██║  ██║   ██║   ██║  ██║   ██║   ██║  ██║\n''╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝    ''╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝'
def abertura():
    global string
    print('=-'*47)
    print()
    for i in string: 
        sleep(0.001) 
        print(i, end='', flush=True)
    print()
    print()
    print('=-'*47)

    # Introdução ao jogo
    string = "\nDona Blue comprou uma fazenda e começou a plantar alimentos orgânicos em sua horta.\nAlguns legumes e verduras não ficaram felizes com a suspensão dos agroTÓXICOS e começaram uma revolta!\n\nVocê é uma Super Batata orgânica e deve derrotar os vegetais dependentes químicos arruaceiros.\nMostre que é possível crescer forte e saudável sem depender de agroTÓXICOS.\n\nSó você pode derrotar os vilões e restaurar a ordem na Bluefarm!!!"
    for i in string: 
        sleep(0.040) 
        print(i, end='', flush=True)
    print()
    print()


