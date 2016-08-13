import webbrowser
def browserSearch(browser,search):
  search = search.replace(' ', '+')
  webbrowser.open('https://www.'+str(browser) + 'results?search_query=' + str(search))
  True
  
