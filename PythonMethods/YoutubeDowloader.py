import webbrowser

urlselec = input("url: ")
urlselec = urlselec[:12]+"ss"+urlselec[12:]
webbrowser.open(urlselec)
