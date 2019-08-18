import wikipedia

while True:
    searchitem = input('What would you like to search on Wikipedia?\n')
    # wikipedia.search(searchitem,results=10)
    words = wikipedia.search(searchitem)
    storedwords = dict()
    count = 0
    print('__________________________________________')
    # Appends wikipedia search summary into storedwords dictionary
    for i in words:
        count = count+1
        storedwords[i] = storedwords.get(i,0)+count
        print('Search Result '+str(count)+':',i)

    pagetitle = input('__________________________________________\n\nSelect which page summary you would like to see...\nEnter Search Result Number: ')
    # Prompts user for search result number
    try:
        x = int(pagetitle)
    except:
        print('Please enter the search result number:')
        continue
    page = None
    # Prints the summary for the user
    for val,key in storedwords.items():
        if x == key:
            page = val
    try:
        print('\n',wikipedia.summary(page))
    except:
        print('Could not find search summary')
    # Prompts the user if they want to search again or quit
    quit = input('\nWould you like to search again? (yes/no)')
    if quit.lower() == 'yes':
        continue
    else:
        print('\nThanks for Searching!')
        break
