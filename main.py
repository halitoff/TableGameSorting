def selection_sort(cards: list[list[str, int]]):
    """Сортировка выбором по убыванию"""
    N = len(cards)
    cards = list(cards)
    for a in range(N - 1):
        m = cards[a][1]
        p = a
        for b in range(a + 1, N):
            if m < cards[b][1]:
                m = cards[b][1]
                p = b

        if p != a:
            t = cards[a][1]
            cards[a][1] = cards[p][1]
            cards[p][1] = t

    return cards

def sorting(array: bytes):
    """
    Array — входной массив, который передаётся сюда от процессора сортировочной машины.
    Array приходит в виде bytes.
    """
    if not isinstance(array, bytes):  # Проверим входные данные на соответствие типу bytes
        raise Exception("Array must be bytes")  # Если не соответствует, то вызываем ошибку

    array = array.decode("utf-8")  # Преобразуем входные данные в utf-8
    array = eval(array)  # Получаем список карт

    # Разбираем карты по колодам
    red_cards = [list(card) for card in array if card[0] == "Красный"]
    black_cards = [list(card) for card in array if card[0] == "Чёрный"]
    blue_cards = [list(card) for card in array if card[0] == "Синий"]
    purple_cards = [list(card) for card in array if card[0] == "Фиолетовый"]
    gold_cards = [list(card) for card in array if card[0] == "Золотой"]

    # Сортируем карты внутри колод
    for cards in [red_cards, black_cards, blue_cards, purple_cards, gold_cards]:
        selection_sort(cards)

    # Подготавливаем строку для вывода
    output_data = str((red_cards, black_cards, blue_cards, purple_cards, gold_cards))
    output_data = output_data[1:-1]  # Удаляем ненужные скобки
    output_data = output_data.encode('utf-8')  # Кодируем

    return output_data  # Возвращаем строку в сортировочную машину


if __name__ == '__main__':
    """Точка входа для тестирования работы алгоритма"""
    test_array = [('Красный', 8),
                  ('Золотой', 3),
                  ('Фиолетовый', 8),
                  ('Фиолетовый', 2),
                  ('Чёрный', 1),
                  ('Золотой', 4),
                  ('Золотой', 12),
                  ('Синий', 7),
                  ('Чёрный', 3),
                  ('Золотой', 5),
                  ('Чёрный', 10),
                  ('Золотой', 6),
                  ('Чёрный', 7),
                  ('Красный', 4),
                  ('Фиолетовый', 11),
                  ('Красный', 11),
                  ('Золотой', 8),
                  ('Фиолетовый', 7),
                  ('Чёрный', 11),
                  ('Золотой', 10),
                  ('Золотой', 7),
                  ('Синий', 11),
                  ('Фиолетовый', 1),
                  ('Чёрный', 8),
                  ('Красный', 1),
                  ('Фиолетовый', 4),
                  ('Синий', 3),
                  ('Фиолетовый', 10),
                  ('Красный', 9),
                  ('Фиолетовый', 9),
                  ('Синий', 5),
                  ('Красный', 3),
                  ('Чёрный', 6),
                  ('Красный', 7),
                  ('Синий', 6),
                  ('Чёрный', 5),
                  ('Чёрный', 12),
                  ('Синий', 8),
                  ('Синий', 4),
                  ('Красный', 2),
                  ('Чёрный', 2),
                  ('Фиолетовый', 6),
                  ('Золотой', 11),
                  ('Красный', 10),
                  ('Красный', 5),
                  ('Фиолетовый', 5),
                  ('Фиолетовый', 12),
                  ('Синий', 2),
                  ('Чёрный', 4),
                  ('Золотой', 9),
                  ('Красный', 6),
                  ('Фиолетовый', 3),
                  ('Золотой', 1),
                  ('Золотой', 2),
                  ('Синий', 12),
                  ('Синий', 9),
                  ('Красный', 12),
                  ('Синий', 10),
                  ('Чёрный', 9),
                  ('Синий', 1)]
    test_array = str(test_array).encode('utf-8')
    test_result = sorting(test_array)
    print(test_result.decode())
