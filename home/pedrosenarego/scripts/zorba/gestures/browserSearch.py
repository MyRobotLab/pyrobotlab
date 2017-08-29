import webbrowser
def browserSearch(browser,search):
  search = search.replace(' ', '+')
  webbrowser.open('https://www.'+str(browser)  + str(search))
  True
  
