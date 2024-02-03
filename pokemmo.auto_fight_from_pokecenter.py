# mancing
from autoclick import helpers
from autoclick import pokemmo
import time


options = [
    'HOENN - Lilycove City grass hunt - lv. 22 - 26',
    'HOENN - Peltaburg City fishing',
    'HOENN - Fallarbor Town Grass lv. 15 - 18',
]
selected_option = helpers.create_select_interface(options)


def is_in_pokecenter(ss):
    in_pokecenter = helpers.locateCenterOnImage(
        './imgs/pokemmo/pokecenter_joy.png', ss, confidence=0.9
    )

    return in_pokecenter


def keluar_pc(option):
    # keluar dari pokecenter
    for x in range(3):
        time.sleep(1)
        helpers.tap(500, 330)
    helpers.tapHold(*pokemmo.grass_keys['down'], 2)
    time.sleep(5)
    if option == 0:
        # keluar dari pokecenter peket bawah 6 kali dan kiri baru ke bawah
        helpers.tapHold(*pokemmo.grass_keys['left'], 3.1)
        time.sleep(1)
        helpers.tapHold(*pokemmo.grass_keys['down'], 3)
    elif option == 1:
        helpers.tapHold(*pokemmo.grass_keys['down'], 3)
        time.sleep(1)
        helpers.tapHold(*pokemmo.grass_keys['left'], 5)
    elif option == 2:
        helpers.tapHold(*pokemmo.grass_keys['down'], 0.3)
        time.sleep(1)
        helpers.tapHold(*pokemmo.grass_keys['left'], 8.5)
        time.sleep(1)
        helpers.tapHold(*pokemmo.grass_keys['down'], 8)


def in_grass(option):

    if option in [0]:
        helpers.tapHold(*pokemmo.grass_keys['down'], 3)
        time.sleep(1)
        helpers.tapHold(*pokemmo.grass_keys['up'], 3)
    elif option in [2]:
        helpers.tapHold(*pokemmo.grass_keys['left'], 2)
        time.sleep(1)
        helpers.tapHold(*pokemmo.grass_keys['right'], 2)

    elif option in [1]:
        pokemmo.fishing()


while True:
    ss = helpers.screenshot()
    # break
    if pokemmo.is_in_fight(ss):
        pokemmo.fight()
    elif is_in_pokecenter(ss):
        keluar_pc(selected_option)
    elif pokemmo.is_in_grass(ss):
        in_grass(selected_option)
    elif pokemmo.is_pilih_jurus_baru(ss):
        pokemmo.pilih_jurus_baru(ss)
    elif pokemmo.is_select_pokemon(ss):
        pokemmo.select_pokemon()
    #
    time.sleep(1)
