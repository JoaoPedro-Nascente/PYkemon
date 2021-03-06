import pygame
from musica import Musica
from displays.allDisplays import *
from battle.pokemonList import *
pygame.init()

theme = 'musica\AfireRedAbertura.wav'#coloca o tema de abertura para tocar
Musica.musica(theme, 0.7)
def main():
    pygame.joystick.init()
    print(pygame.joystick.get_count())

    display = "INIT" # actual display

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if display == "INIT":
            display = draw_init()

        if display == "MENU":
            choosed_pokemon, display = draw_menu()

        elif display == "NAMEIT":
            display, pokeName, pokeGender = draw_nameIt(choosed_pokemon)
            if pokeName.lower() == 'introcomp' or pokeName.lower() == 'intro':
                choosed_pokemon = introbot
            
        elif display == "BATTLE":
            bg_music = 'musica/battle.wav'
            Musica.musica(bg_music, 0.7)
            display = draw_battle(choosed_pokemon, pokeName, pokeGender)
        
        elif display == 'WIN':
            display=draw_win(choosed_pokemon)
        
        elif display == 'LOSE':
            display=draw_lose(choosed_pokemon)
        
        else:
            display= draw_run()

if __name__ == '__main__':
    main()