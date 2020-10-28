def find_document(documents, number = ''):
    if number == '':
        number = input('Enter document number: ')
    index = -1
    for docum in documents:
        index = index + 1
        for v in docum.values():
            if v == number:
                return {'result': index}
    return {'result': None, 'massage': 'Document is not found'}

def get_owner(documents, doc_number = ''):
    if doc_number == '':
        doc_number = input('Enter document number: ')
    doc_index = find_document(documents, doc_number)
    if doc_index['result'] == None:
        print(f'Document №{doc_number} not found', end='\n\n')
        return {'result': None, 'massage': 'Document is not found'}
    else:
        if 'name' in documents[doc_index['result']].keys():
            return {'result': documents[doc_index['result']]['name']}
        else:
            return {'result': None, 'massage': 'Document has not owner'}

def get_location(documents, directories, number_doc=''):
    if number_doc == '':
        number_doc = input('Enter document number: ')

    find_doc = find_document(documents, number_doc)
    if find_doc['result'] == None:
        print(f'Document №{number_doc} not found', end = '\n\n')
        return {'result': None, 'massage': 'Document is not found'}
    else:
        return {'result': list({key: value for key, value in directories.items() if number_doc in value}.keys())[0]}

def get_list_of_documents():
  print('[List of the documents]')
  for docum in documents_:
    print(f'{docum["type"]} "{docum["number"]}" {docum["name"]}')
  print('',end='\n\n')
  return 'empty_answer'

def create_new_document(documents, directories, shelf_number = ''):
    if shelf_number == '':
        shelf_number = input('Enter direcrory number: ')
    if shelf_number not in directories.keys():
        print('Directory is not found', end = '\n\n')
        return {'result': None, 'massage': 'Directory is not found'}
    else:
        new_document = {}
        new_document["type"] = input('Enter type document: ')
        new_document["number"] = input('Enter document number: ')
        new_document["name"] = input('Enter name of owner: ')
        documents.append(new_document)
        directories[shelf_number].append(str(new_document["number"]))
        print('Complited', end = '\n\n')
    return {'result': 'empty_answer'}

def delete_document(documents, directories, doc_number = ''):
    if doc_number == '':
        doc_number = input('Enter document number: ')
    index_for_delite = find_document(documents, doc_number)
    if index_for_delite['result'] == None:
        print('Document is not found', end = '\n\n')
        return {'result': None, 'massage': 'Document is not found'}
    else:
        number_shelf = get_location(documents, directories, doc_number)
        documents.pop(index_for_delite['result'])
        directories[number_shelf['result']].remove(doc_number)
        print('Completed', end = '\n\n')
        return {'result': 'empty_answer'}

def move_document(documents, directories, doc_number = '', shelf_number = ''):
    if doc_number == '':
        doc_number = input('Enter document number: ')

    doc_index = find_document(documents, doc_number)
    if doc_index['result'] == None:
        print('Document is not found', end = '\n\n')
        return {'result': None, 'massage': 'Document is not found'}

    if shelf_number == '':
        shelf_number = input('Enter directory for move: ')

    if shelf_number not in directories.keys():
        print('Directory is not found', end = '\n\n')
        return {'result': None, 'massage': 'Directory is not found'}

    obsolete_position = get_location(documents, doc_number)
    directories[obsolete_position['result']].remove(doc_number)
    directories[shelf_number['result']].append(doc_number)
    print('Completed', end = '\n\n')
    return {'result':'empty_answer'}

def create_shelf(directories, new_shelf_number = ''):
    if new_shelf_number == '':
        new_shelf_number = input('Enter the number of the new shelf: ')
    if new_shelf_number in directories.keys():
        print('A shelf with this number exists', end = '\n\n`')
        return {'result': None, 'massage': 'A shelf with this number exists'}
    directories[new_shelf_number] = []
    print('Completed', end = '\n\n')
    return {'result':'empty_answer'}

def print_menu():
  print('[Print menu]')
  print(f'lIST OF THE COMMANDS: ')
  print('[0] Get list of the commabds')
  print('[1] Get list of the documents ')
  print('[2] Get list of the shelfs')
  print('[3] Get owner document')
  print('[4] Get location of the document')
  print('[5] Create new document')
  print('[6] Delete document')
  print('[7] Move document')
  print('[8] Create new shelf')
  print('[9] Exit', end = '\n\n')
  return 'empty_answer'

def get_derrictories_list():
  for key in directories_.keys():
    print(f'    {key}: {directories_[key]}')
  print()
  return 'empty_answer'