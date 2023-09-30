from src.phonebook import Phonebook
import unittest

class TestPhonebook(unittest.TestCase):
    def test_add_with_correct_name(self):
        expected_answer = 'Numero adicionado'
        phonebook = Phonebook()
        answer = phonebook.add("marcelo", "98253444")
        assert expected_answer == answer

    def test_add_with_blank_number(self):
        #test not passed, user should not be able to add a blank number
        expected_answer = 'Numero invalido'
        phonebook = Phonebook()
        answer = phonebook.add("marcelo", "")
        assert expected_answer == answer
    def test_add_with_wrong_name_word_hashtag(self):
        expected_answer = 'Nome invalido'
        phonebook = Phonebook()
        answer = phonebook.add("marce#lo", "98253444")
        assert expected_answer == answer

    def test_add_entries_with_wrong_at_sign(self):
        expected_answer = 'Nome invalido'
        phonebook = Phonebook()
        answer = phonebook.add("marce@lo", "98253444")
        assert expected_answer == answer

    def test_add_entries_with_wrong_exclamation(self):
        expected_answer = 'Nome invalido'
        phonebook = Phonebook()
        answer = phonebook.add("marce!lo", "98253444")
        assert expected_answer == answer

    def test_add_entries_with_wrong_dollar_sign(self):
        expected_answer = 'Nome invalido'
        phonebook = Phonebook()
        answer = phonebook.add("marce$lo", "98253444")
        assert expected_answer == answer

    def test_add_entries_with_wrong_percentage(self):
        expected_answer = 'Nome invalido'
        phonebook = Phonebook()
        answer = phonebook.add("marce%lo", "98253444")
        assert expected_answer == answer

    def test_lookup_entry_with_correct_name(self):
        expected_answer = '190'
        phonebook = Phonebook()
        answer = phonebook.lookup("POLICIA")
        assert expected_answer == answer

    def test_lookup_entry_with_wrong_name_hashtag(self):
        expected_answer = 'Nome invalido'
        phonebook = Phonebook()
        answer = phonebook.lookup("marce#lo")
        assert expected_answer == answer

        #Erro de digitação no retorno do método de procurar por numero = Nome invaldo

    def test_lookup_entry_with_wrong_name_at_sign(self):
        expected_answer = 'Nome invalido'
        phonebook = Phonebook()
        answer = phonebook.lookup("marce@lo")
        assert expected_answer == answer

    def test_lookup_entry_with_wrong_name_exclamation(self):
        expected_answer = 'Nome invalido'
        phonebook = Phonebook()
        answer = phonebook.lookup("marce!lo")
        assert expected_answer == answer

    # Erro de digitação no retorno do método de procurar por numero = Nme invalido

    def test_lookup_entry_with_wrong_name_dollar_sign(self):
        expected_answer = 'Nome invalido'
        phonebook = Phonebook()
        answer = phonebook.lookup("marce$lo")
        assert expected_answer == answer

    def test_lookup_entry_with_wrong_name_percentage(self):
        expected_answer = 'Nome invalido'
        phonebook = Phonebook()
        answer = phonebook.lookup("marce%lo")
        assert expected_answer == answer

    # Erro de digitação no retorno do método de procurar por numero = Nome nvalido
    def test_get_names(self):
        expected_list_of_users_names = ['POLICIA', 'marcelo']
        phonebook = Phonebook()
        phonebook.add('marcelo','1234')
        list_from_phonebook = phonebook.get_names()
        assert expected_list_of_users_names == list_from_phonebook

    def test_get_numbers(self):
        expected_list_of_users_numbers = ['190', '1234']
        phonebook = Phonebook()
        phonebook.add('marcelo','1234')
        list_from_phonebook = phonebook.get_numbers()
        assert expected_list_of_users_numbers == list_from_phonebook

    def test_clear(self):
        expected_answer = 'phonebook limpado'
        phonebook = Phonebook()
        response = phonebook.clear()
        assert expected_answer == response

    def test_search(self):
        expected_answer = [{'POLICIA', '190'}]
        phonebook = Phonebook()
        response = phonebook.search('POLICIA')
        assert response == expected_answer

    def test_get_phonebook_sorted(self):
        expected_answer = list({"Andre":"123",'POLICIA':"190", "qarlos":"555"})
        phonebook = Phonebook()
        phonebook.add('qarlos', '555')
        phonebook.add('Andre', '123')
        response = phonebook.get_phonebook_sorted()
        response = list(response)
        print(response)
        print(expected_answer)
        assert expected_answer == response

    def test_get_phonebook_reversed(self):
        expected_answer = list({"qarlos":"555", 'POLICIA': "190", "Andre":"123"})
        phonebook = Phonebook()
        phonebook.add('qarlos', '555')
        phonebook.add('Andre', '123')
        response = phonebook.get_phonebook_reverse()
        response = list(response)
        assert expected_answer == response

    def test_delete_name_sucess(self):
        expected_answer = 'Numero deletado'
        phonebook = Phonebook()
        response = phonebook.delete("POLICIA")
        assert expected_answer == response

    def test_change_number(self):
        expected_answer = "Numero alterado"
        phonebook = Phonebook()
        response = phonebook.change_number('POLICIA', '5')
        assert expected_answer == response

    def test_change_number_by_passing_name_which_does_not_exist(self):
        expected_answer = "Nome nao encontrado"
        phonebook = Phonebook()
        response = phonebook.change_number('Bombeiro', '5')
        assert expected_answer == response

    def test_change_number_by_passing_invalid_name(self):
        expected_answer = "Numero ou nome invalido"
        phonebook = Phonebook()
        response = phonebook.change_number(5, '5')
        assert expected_answer == response

    def test_get_name_by_number(self):
        expected_answer = "POLICIA"
        phonebook = Phonebook()
        repsonse = phonebook.get_name_by_number("190")
        assert repsonse == expected_answer

    def test_get_name_by_number_by_passing_invalid_number(self):
        expected_answer = "Numero invalido"
        phonebook = Phonebook()
        repsonse = phonebook.get_name_by_number("")
        assert repsonse == expected_answer

    def test_get_name_by_number_by_passing_number_which_does_not_exist_in_phonebook(self):
        expected_answer = "Numero nao encontrado"
        phonebook = Phonebook()
        repsonse = phonebook.get_name_by_number("5555555")
        assert repsonse == expected_answer