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
    def test_add_new_book_length_less_than_40(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    @pytest.mark.parametrize('book_name', 
        [
            '',  # пустое название
            'Странная история доктора Джекила и мистера Хайда', #больше 40 символов
        ])

    # 2. книг с недопустимой длиной (пустые или более 40 символов) не добавлена
    def test_add_new_book_length_more_than_40(self, collector, book_name):
        collector.add_new_book(book_name)
        # книга не должна добавиться
        assert book_name not in collector.books_genre

    # 3. жанр для книги установлен, книга есть в словаре (существующая)
    def test_set_book_genre_book_in_dictionary(self, collector):
        collector.books_genre = {
            'Шерлок': 'Ужасы',
            'Фантастические твари': 'Фантастика'
        }
        collector.set_book_genre('Шерлок', "Детективы")
        assert collector.books_genre['Шерлок'] == 'Детективы'
    
    # 4. ошибка при попытке добавления жанра несуществующей книге
    def test_set_book_genre_nonexistent_book(self, collector):
        collector.set_book_genre('Не существующая книга', 'Комедии')
        assert 'Не существующая книга' not in collector.books_genre

    @pytest.mark.parametrize('name_book, genre', 
        [
        ('Гарри Поттер', 'Фантастика'),
        ('Петсон и Финдус', 'Мультфильмы'),
        ('Хоббит, или туда и обратно', 'Фантастика'),
        ('Оно', 'Ужасы'),
        ])
    
    # 5. вывод жанра по имени книги
    def test_get_book_genre_get_true(self, collector, name_book, genre):
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)
        assert collector.get_book_genre(name_book) == genre

    @pytest.mark.parametrize('name_book, genre',
                [
                ('Гарри Поттер', 'Фантастика'),
                ('Петсон и Финдус', 'Мультфильмы'),
                ('Хоббит, или туда и обратно', 'Фантастика'),
                ('Оно', 'Ужасы'),
                ])    

    # 6. успешный вывод книг определенного жанра
    def test_get_books_with_specific_genre_list_of_books_show(self, collector, name_book, genre):
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)
        assert name_book in collector.get_books_with_specific_genre(genre)

    # 7. вывод текущего словаря с двумя добавленными книгами
    def test_get_books_genre_show_dictionary(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Фантастические твари')
        collector.set_book_genre('Фантастические твари', 'Фантастика')
        result = collector.get_books_genre()
        assert result == {
                'Гарри Поттер': 'Фантастика', 
                'Фантастические твари': 'Фантастика'
                }
    
    # 8. вывод книг, жанр которой отсутствует в списке genre_age_rating
    def test_get_books_for_children_is_not_genre_age_ratingp(self, collector):
        collector.add_new_book('Финдус и Петсон')
        collector.set_book_genre('Финдус и Петсон', 'Мультфильмы')
        collector.add_new_book('Пила')
        collector.set_book_genre('Пила', 'Ужасы')
        result = collector.get_books_for_children()
        assert result == ['Финдус и Петсон']

    # 9. книга добавлена в избранное
    def test_add_book_in_favorites_book_added(self, collector):
        collector.add_new_book('Снежная королева')
        collector.add_new_book('Две зимы')
        collector.add_book_in_favorites('Снежная королева')
        assert 'Снежная королева' in collector.favorites

    # 10. успешное удаление книги из избранного, книги в избранном нет
    def delete_book_from_favorites_book_deleted(self, collector):
        collector.add_new_book('Шоколадный дедушка')
        collector.add_new_book('Шоколадус')
        collector.add_book_in_favorites('Шоколадный дедушка')
        collector.delete_book_from_favorites('Шоколадный дедушка')
        assert 'Шоколадный дедушка' not in collector.favorites 

    # 11. получен список избранных книг
    def test_get_list_of_favorites_books_true(self, collector):
        collector.add_new_book('Снежная королева')
        collector.add_new_book('Две зимы')
        collector.add_book_in_favorites('Снежная королева')
        result = collector.get_list_of_favorites_books()
        assert result == ['Снежная королева']

