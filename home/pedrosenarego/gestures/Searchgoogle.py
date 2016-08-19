import webbrowser
def searchGoogle(search):
  search = search.replace(' ', '+')
  webbrowser.open('https://www.google.com/search?gs_ivs=1&q=' + str(search))
  True
  
  
