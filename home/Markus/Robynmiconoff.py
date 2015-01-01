mic = 1

def input(cmd):
    # print 'python object is',msg_[service]_[method]
    cmd = msg_keyboard_keyCommand.data[0]
    print 'python data is', cmd
    
    if (cmd == "M"):
        if mic == 1:
            ear.lockOutAllGrammarExcept("robin")
            i01.mouth.speak("i'm not listening")
            global mic
            mic = 0
        elif mic == 0:
            ear.clearLock()
            i01.mouth.speak("i can hear again")
            global mic
            mic = 1
      
