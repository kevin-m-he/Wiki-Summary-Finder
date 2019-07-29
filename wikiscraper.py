import wikipedia

while True:
    searchitem = input('What would you like to search on Wikipedia?\n')
    #wikipedia.search(searchitem,results=15) gives 15 results
    lst = wikipedia.search(searchitem)
    dic = dict()
    count = 0
    print('__________________________________________')
    for i in lst:
        count = count+1
        dic[i] = dic.get(i,0)+count
        print('Search Result '+str(count)+':',i)

    pagetitle = input('__________________________________________\n\nSelect which page summary you would like to see...\nEnter Search Result Number: ')
    try:
        x = int(pagetitle)
    except:
        print('Please enter the search result number:')
        continue
    page = None
    for val,key in dic.items():
        if x == key:
            page = val
    try:
        print('\n',wikipedia.summary(page))
    except:
        print('Could not find search summary')
    quit = input('\nWould you like to search again? (yes/no)')
    if quit == 'yes':
        continue
    else:
        print('\nThanks for Searching!')
        break