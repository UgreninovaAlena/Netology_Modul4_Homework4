import HW3
import pprint


documents = [{"type": "passport", "number": "2207", "name": "Василий Гупкин"},
             {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
             {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
                     {"type": "insurance", "number": "2"}
            ]
print(documents)
# print(HW3.get_owner(documents, '2'))
print(documents[0].keys())
if 'name' in documents[0].keys(): print('++')
print(HW3.get_owner(documents, '2'))