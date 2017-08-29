gesturesPath = "/home/pedro/Dropbox/pastaPessoal/3Dprinter/inmoov/scripts/zorba/gestures"

i01 = Runtime.createAndStart("i01", "InMoov")
i01.setMute(True)

zorba2 = Runtime.createAndStart("zorba", "ProgramAB")
zorba2.startSession("Pedro", "zorba")



i01.loadGestures(gesturesPath)
