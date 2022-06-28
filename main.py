from search_engine import SearchEngine

def main():
    directory = input('Please enter a the name of a directory: ')

    mode = int(input('''Enter mode number (1-5) as in what data structure to use:
        1. Linked List
        2. Binary Search Tree
        3. AVL
        4. Hash Table
        5. Trie\n'''))


    print('Building Search Engine...')
    print()
    engine = SearchEngine(directory, mode)

    answer = 'y'
    while (answer == 'y'):
        term = input('Search (enter a term to query): ')
        ranking = engine.search(term)
        print("Displaying results for " + "'" + term + "':")
        if ranking is None:
            print('    No results :(')
        else:
            rank = 1
            for doc in ranking:
                print('    ' + str(rank) + '. ' + doc)
                rank += 1
            print()
        answer = ''
        while not (answer == 'y' or answer == 'n'):
            answer = input('Would you like to search another term (y/n) ')


if __name__ == '__main__':
    main()