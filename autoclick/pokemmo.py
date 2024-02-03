from autoclick import helpers
import random
import time


# tombol dpad untuk menjalankan karakter
grass_keys = {
    'up': (222, 416),
    'right': (300, 490),
    'down': (222, 580),
    'left': (136, 490),
}

# letak box di gunakan untuk memilih pokemon
select_pokemon_boxs = [
    (248, 335),
    (551, 335),
    (861, 335),
    (248, 418),
    (551, 418),
    (861, 418),
]


# button yang digunakan memilih jurus
select_move_boxs = [
    (5, 310),
    (5, 443),
    (1175, 310),
    (1175, 443),
]


grass_buttons = {'A': (938, 558), 'box_3': (46, 246)}

moves = ['down', 'up', 'left', 'right']


#
def fight():
    print('sedang gelut')
    # check jika sedang memiliki pokemon yang mati

    # masuk ke pilih menu
    helpers.tap(28, 576)

    time.sleep(2)
    select = random.choice(select_move_boxs)
    helpers.tap(*select)

    # check apakah masih dalam mode tempur
    time.sleep(2)


def jalan_melingkar():
    for key in grass_keys.values():
        helpers.tapHold(*key, 10)


def select_pokemon():
    print(f'pilih pokemon')
    select = random.choice(select_pokemon_boxs)
    helpers.tap(*select)


def fishing():
    print('klik pancing')
    helpers.tap(*grass_buttons['box_3'])
    time.sleep(2)
    for _ in range(5):
        print('klik A')
        helpers.tap(*grass_buttons['A'])
        time.sleep(0.5)
    return True


def is_in_grass(ss):
    return helpers.image_has_text(
        ss, '2', location=(5, 141, 5 + 17, 141 + 23), debug=True
    ) or helpers.image_has_text(
        ss, 'Z', location=(5, 141, 5 + 17, 141 + 23), debug=True
    )


def is_in_fight(ss):
    is_fight = helpers.image_has_text(
        ss, 'FIGHT', location=(28, 576, 28 + 61, 576 + 33)
    )
    return is_fight


def is_select_pokemon(ss):
    for pos in select_pokemon_boxs:
        if helpers.image_has_text(
            ss,
            'HP:',
            location=(pos[0], pos[1], pos[0] + 52, pos[1] + 22),
            debug=False,
        ):
            return True
    return False


def is_pilih_jurus_baru(ss):
    return helpers.image_has_text(
        ss, 'move', location=(685, 269, 685 + 222, 269 + 65)
    ) and helpers.image_has_text(
        ss, 'cancel', location=(929, 310, 929 + 69, 310 + 21)
    )


def pilih_jurus_baru(ss):
    # lokasi masing masing button move yang sudah ada
    moves = [(263, 287), (477, 287), (263, 408), (477, 408)]

    # extract nama move baru
    new_move = helpers.extract_text_from_image(
        ss, location=(699, 408, 699 + 314, 408 + 37)
    ).lower()
    existsing_move = []
    print(f'new_move : {new_move}')

    for move in moves:
        # mengambil data semua jurus yang sudah ada
        existsing_move.append(
            helpers.extract_text_from_image(
                ss, location=(*move, move[0] + 207, move[1] + 37)
            ).lower()
        )

    print(existsing_move)
    existsing_move_text = ', '.join(existsing_move)
    selected_move = helpers.gpt(
        f'which is better to replace the {new_move} move between {existsing_move_text} for attack style gameplay and which is not the HM type in pokemon choose one of the existing move just give the answer no need for explanation and no reason So just send the name of the movie from the options above'
    )

    for move in existsing_move:
        if move in selected_move.lower():
            selected_move = move

    if selected_move != '':
        selected_move = selected_move.lower()
        print(f'selected move to replace: {selected_move}')
        helpers.send_notify(
            f'POKEMMO: new move {new_move} replace to {selected_move}'
        )

        selected_move_index = existsing_move.index(selected_move)
        selected_move_box = moves[selected_move_index]
        helpers.tap(selected_move_box[0] + 30, selected_move_box[1])
        time.sleep(2)
        # pilih yes
        helpers.tap(630, 350)

    else:
        helpers.tap(930, 320)
        time.sleep(2)
        # pilih yes
        helpers.tap(630, 350)
