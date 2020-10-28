import unittest
import pprint
from HW3 import find_document, get_owner, get_location, create_new_document, delete_document, move_document


class TestFindDocument(unittest.TestCase):


    def setUp(self):
        print('>>>>>>>>SetUp')
        self.documents = [{"type": "passport", "number": "2207", "name": "Василий Гупкин"},
                     {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                     {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
                    ]
    def test_document_found_v1(self):
        print('document_found_v1')
        self.assertEqual(find_document(self.documents, '2207'), {'result': 0})
    def test_document_found_v2(self):
        print('document_found_v2')
        self.assertEqual(find_document(self.documents, '11-2'),  {'result': 1})
    def test_document_NOTfound(self):
        print('document_NOTfound')
        self.assertEqual(find_document(self.documents, '11'), {'result': None, 'massage': 'Document is not found'})

class TestGetOwner(unittest.TestCase):
    # Метод, которы запускается перед каждым тест-кейсом (имя метода должно быть строго setUp() )!!!
    def setUp(self):
        print('>>>>>>>>SetUp')
        self.documents = [{"type": "passport", "number": "2207", "name": "Василий Гупкин"},
                          {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                          {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
                          {"type": "insurance", "number": "2"}
                          ]

    def test_get_owner_v1(self):
        print('get_owner_v1')
        self.assertEqual(get_owner(self.documents, '2207'), {'result': "Василий Гупкин"})

    def test_get_owner_v2(self):
        print('get_owner_v2')
        self.assertEqual(get_owner(self.documents, '11-2'), {'result': "Геннадий Покемонов"})

    def test_get_owner_NOTfound(self):
        print('get_owner_NOTfound')
        self.assertEqual(get_owner(self.documents, '11'), {'result': None, 'massage': 'Document is not found'})

    def test_get_owner_NOTfound_owner(self):
        print('NOTfound_owner')
        self.assertEqual(get_owner(self.documents, '2'), {'result': None, 'massage': 'Document has not owner'})

class TestGetLocation(unittest.TestCase):
    def setUp(self):
        print(f'SetUp')
        self.documents = [{"type": "passport", "number": "2207", "name": "Василий Гупкин"},
                          {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                          {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
                         ]
        self.directories = {'1': ['2207', '11-2', '5455 028765'],
                            '2': ['10006'],
                            '3': []
                            }

    def test_get_location_v1(self):
        print('get_location_v1')
        self.assertEqual(get_location(self.documents, self.directories, '2207'), {'result': "1"})

    def test_get_location_v2(self):
        print('get_location_v2')
        self.assertEqual(get_location(self.documents, self.directories, '10006'), {'result': "2"})

    def test_get_location_NOTFound_doc(self):
        print('get_location_NOTFound_doc')
        self.assertEqual(get_location(self.documents, self.directories, '07'), {'result': None, 'massage': 'Document is not found'})

class TestCreateNewDocument(unittest.TestCase):
    def setUp(self):
        print(f'SetUp')
        self.documents = [{"type": "passport", "number": "2207", "name": "Василий Гупкин"},
                          {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                          {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
                         ]
        self.directories = {'1': ['2207', '11-2', '5455 028765'],
                            '2': ['10006'],
                            '3': []
                            }

    def test_create_new_document_v1(self):
        print('create_new_document_v1')
        self.assertEqual(create_new_document(self.documents, self.directories, '1'), {'result': 'empty_answer'})
        print(self.documents)
        print(self.directories)

    def test_create_new_document_NOTfound_dir(self):
        print('create_new_document_NOTfound_dir')
        self.assertEqual(create_new_document(self.documents, self.directories, '0'), {'result': None, 'massage': 'Directory is not found'})

class TestDeleteDocument(unittest.TestCase):
    def setUp(self):
        print(f'SetUp')
        self.documents = [{"type": "passport", "number": "2207", "name": "Василий Гупкин"},
                          {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                          {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
                          {"type": "insurance", "number": "000", "name": "Аристарх Павлов"}
                          ]
        self.directories = {'1': ['2207', '11-2', '5455 028765'],
                            '2': ['10006'],
                            '3': []
                            }

    def test_delete_document_v1(self):
        print('delete_document_v1')
        self.assertEqual(delete_document(self.documents, self.directories, '11-2'), {'result': 'empty_answer'})
        # print(self.documents)
        # print(self.directories)

    def test_delete_document_v2(self):
        print('delete_document_v2')
        self.assertEqual(delete_document(self.documents, self.directories, '10006'), {'result': 'empty_answer'})
        # print(self.documents)
        # print(self.directories)

    def test_delete_document_NOTfound_doc(self):
        print('delete_document_NOTfound_doc')
        self.assertEqual(delete_document(self.documents, self.directories, '1'), {'result': None, 'massage': 'Document is not found'})