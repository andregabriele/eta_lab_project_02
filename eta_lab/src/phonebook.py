class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """

        #fix typos in string returned below (@, $) statements
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome invalido'

        #comparasion should check if number is equals to zero.
        if len(number) == 0:
            #fix, "Numero invalido" should be returned instead "Nome invalido"
            return 'Numero invalido'

        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    # fix typos in string returned below (#, !, %) statements
    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome invalido'

        return self.entries[name]

    def get_names(self):
        """
        #implements return of list
        :return: return all names in phonebook
        """
        #fix, return from this function should be a list, not a set (dict_keys[])
        return list(self.entries.keys())

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        #fix, return from this function should be a list, not a set (dict_values[])
        return list(self.entries.values())

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search

        """
        result = []
        for name, number in self.entries.items():
            #fix, should append name into result if name contains search_name string
            if search_name in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        #fix, entries is not sorted
        return dict(sorted(self.entries.items()))

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        #fix, item was not sorted
        return dict(sorted(self.entries.items(), reverse=True))

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return 'Numero deletado'

    def change_number(self, name, number):
        if name and isinstance(name, str) and number and isinstance(number, str):
            if name in self.entries.keys():
                for name_phonebook, number_phonebook in self.entries.items():
                    if name == name_phonebook:
                        self.entries[name_phonebook] = number
                        return "Numero alterado"
            return "Nome nao encontrado"
        return "Numero ou nome invalido"

    def get_name_by_number(self, number):
        if number and isinstance(number, str):
            for key, value in self.entries.items():
                if number == value:
                    return key
            return "Numero nao encontrado"
        return "Numero invalido"
