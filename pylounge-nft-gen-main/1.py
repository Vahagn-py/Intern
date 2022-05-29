

def main(count_of_images):
    # ФОН > КРЫЛЬЯ > ТЕЛО > ОДЕЖДА > ПРИЧЁСКИ > МЕЧИ > АКСЕССУАРЫ

    probability_wieghts_background = [1, 1, 1, 1, 1, 1, 1]  # вероятности фона
    probability_wieghts_wings = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 10]  # веротяности крыльев
    probability_wieghts_body = [1, 1, 8, 8, 8]  # вероятности тела
    probability_wieghts_cloth = [3, 3, 5, 5, 4, 4, 1, 1, 4, 1]  # вероятности одежды
    probability_wieghts_hairs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # вероятности причёски
    probability_wieghts_sword = [5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 10]  # вероятности оружия
    probability_wieghts_acc = [1, 1, 1, 1, 10]  # вероятности аксессуаров

    # ( Название папки с элементом рисунка, список вероятностей для каждого элемента, может ли не выпасть элемент )
    elements = [('Фон/', probability_wieghts_background, False), ('Тело/', probability_wieghts_body, False),
                ('Крылья/', probability_wieghts_wings, True), ('Одежда/', probability_wieghts_cloth, False),
                ('Прически/', probability_wieghts_hairs, False), ('Оружее/', probability_wieghts_sword, True),
                ('Аксессуары/', probability_wieghts_acc, True)]
    # список элементов, которые надо перекрашивать
    elements_for_repainting = ['Крылья/', 'Одежда/', 'Прически/', 'Оружее/']
    # итоговое изображение
    result_img = ''
