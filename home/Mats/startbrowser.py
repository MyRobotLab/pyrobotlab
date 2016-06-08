webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
webgui.startBrowser("http://localhost:8888/#service/i01.ear")
