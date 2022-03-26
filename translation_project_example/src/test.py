from example import setlocale, print_hello, print_formatted
import pytest
import gettext
import locale

class TestLocale:

    def test_en_locale(self):
        _, ngettext = setlocale('en')
        hello = print_hello()
        assert(print_hello() == "Hello world!\nIvan is the best architect in the world!\nMy name is Arnold")
        assert(print_formatted(1, ngettext) == "I got 1 apple")
        assert(print_formatted(5, ngettext) == "I got 5 apples")

    def test_ru_locale(self):
        _, ngettext = setlocale('ru')
        assert(print_hello() == "Привет мир!\nИван лучший архитектор проектов в мире!\nА меня зовут Арнольд")
        assert(print_formatted(1, ngettext) == "У меня 1 яблоко")
        assert(print_formatted(5, ngettext) == "У меня 5 яблок")

    def test_uk_locale(self):
        _, ngettext = setlocale('uk')
        assert(print_hello() == "Привіт світ!\nІван найкращий архітектор проектів у світі!\nА мене звуть Арнольд")
        assert(print_formatted(1, ngettext) == "У мене 1 яблуко")
        assert(print_formatted(5, ngettext) == "У мене 5 яблук")