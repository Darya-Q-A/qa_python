from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    @pytest.mark.parametrize('book_name', 
        [
            'Граф Аверин',
            'История кавалера де Грие иии Манон Леско',  # ровно 40 символов
        ])
    #1. удачное добавление в словарь книги (название <= 40)
    def test_add_new_book_length_less_than_40(self, book_name):
        new_book_length_less_than_40 = BooksCollector()
        new_book_length_less_than_40.add_new_book(book_name)
        assert book_name in new_book_length_less_than_40.books_genre

    @pytest.mark.parametrize('book_name', 
        [
            '',  # пустое название
            'Странная история доктора Джекила и мистера Хайда', #больше 40 символов
        ])

    # 2. книг с недопустимой длиной (пустые или более 40 символов) не добавлена
    def test_add_new_book_length_more_than_40(self, book_name):
        new_book_length_more_less_than_40 = BooksCollector()
        new_book_length_more_less_than_40.add_new_book(book_name)
        # книга не должна добавиться
        assert book_name not in new_book_length_more_less_than_40.books_genre

    # 3. жанр для книги установлен, книга есть в словаре (существующая)
    def test_set_book_genre_book_in_dictionary(self):
        book_from_books_genge = BooksCollector()
        book_from_books_genge.books_genre = {
            'Шерлок': 'Ужасы',
            'Фантастические твари': 'Фантастика'
        }
        book_from_books_genge.set_book_genre('Шерлок', "Детективы")
        assert book_from_books_genge.books_genre['Шерлок'] == 'Детективы'
    
    # 4. ошибка при попытке добавления жанра несуществующей книге
    def test_set_book_genre_nonexistent_book(self):
        nonexistent_book = BooksCollector()
        nonexistent_book.set_book_genre('Не существующая книга', 'Комедии')
        assert 'Не существующая книга' not in nonexistent_book.books_genre

    @pytest.mark.parametrize('name_book, genre', 
        [
        ('Гарри Поттер', 'Фантастика'),
        ('Петсон и Финдус', 'Мультфильмы'),
        ('Хоббит, или туда и обратно', 'Фантастика'),
        ('Оно', 'Ужасы'),
        ])
    
    # 5. вывод жанра по имени книги
    def test_get_book_genre_get_true(self, name_book, genre):
        genre_book = BooksCollector()
        genre_book.add_new_book(name_book)
        genre_book.set_book_genre(name_book, genre)
        assert genre_book.get_book_genre(name_book) == genre

    @pytest.mark.parametrize('name_book, genre',
                [
                ('Гарри Поттер', 'Фантастика'),
                ('Петсон и Финдус', 'Мультфильмы'),
                ('Хоббит, или туда и обратно', 'Фантастика'),
                ('Оно', 'Ужасы'),
                ])    

    # 6. успешный вывод книг определенного жанра
    def test_get_books_with_specific_genre_list_of_books_show(self, name_book, genre):
        genre_book_show = BooksCollector()
        genre_book_show.add_new_book(name_book)
        genre_book_show.set_book_genre(name_book, genre)
        assert name_book in genre_book_show.get_books_with_specific_genre(genre)

    # 7. вывод текущего словаря с двумя добавленными книгами
    def test_get_books_genre_show_dictionary(self):
        dictionary_of_books = BooksCollector()
        dictionary_of_books.add_new_book('Гарри Поттер')
        dictionary_of_books.set_book_genre('Гарри Поттер', 'Фантастика')
        dictionary_of_books.add_new_book('Фантастические твари')
        dictionary_of_books.set_book_genre('Фантастические твари', 'Фантастика')
        result = dictionary_of_books.get_books_genre()
        assert result == {
                'Гарри Поттер': 'Фантастика', 
                'Фантастические твари': 'Фантастика'
                }
    
    # 8. вывод книг, жанр которой отсутствует в списке genre_age_rating
    def test_get_books_for_children_is_not_genre_age_ratingp(self):
        book_for_children = BooksCollector()
        book_for_children.add_new_book('Финдус и Петсон')
        book_for_children.set_book_genre('Финдус и Петсон', 'Мультфильмы')
        book_for_children.add_new_book('Пила')
        book_for_children.set_book_genre('Пила', 'Ужасы')
        result = book_for_children.get_books_for_children()
        assert result == ['Финдус и Петсон']

    # 9. книга добавлена в избранное
    def test_add_book_in_favorites_book_added(self):
        book_add_in_favorites = BooksCollector()
        book_add_in_favorites.add_new_book('Снежная королева')
        book_add_in_favorites.add_new_book('Две зимы')
        book_add_in_favorites.add_book_in_favorites('Снежная королева')
        assert 'Снежная королева' in book_add_in_favorites.favorites

    # 10. успешное удаление книги из избранного, книги в избранном нет
    def delete_book_from_favorites_book_deleted(self):
        book_to_delete = BooksCollector()
        book_to_delete.add_new_book('Шоколадный дедушка')
        book_to_delete.set_book_genre('Шоколадный дедушка', 'Детективы')
        book_to_delete.add_new_book('Шоколадус')
        book_to_delete.set_book_genre('Шоколадус', 'Детективы')
        book_to_delete.add_book_in_favorites('Шоколадный дедушка')
        book_to_delete.delete_book_from_favorites('Шоколадный дедушка')
        assert 'Шоколадный дедушка' not in book_to_delete.favorites 

    # 11. получен список избранных книг
    def test_get_list_of_favorites_books_true(self):
        book_in_favorites = BooksCollector()
        book_in_favorites.add_new_book('Снежная королева')
        book_in_favorites.set_book_genre('Снежная королева', 'Фантастика')
        book_in_favorites.add_new_book('Две зимы')
        book_in_favorites.set_book_genre('Две зимы', 'Фантастика')
        book_in_favorites.add_book_in_favorites('Снежная королева')
        result = book_in_favorites.get_list_of_favorites_books()
        assert result == ['Снежная королева']

