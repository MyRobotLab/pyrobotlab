subject = 0

def COUNTER():
    global subject
    subject = subject + 1
    if (subject == 1):
       print "subject", subject
       resp = alice2.getResponse("SUBJECT1")
    if (subject == 2):
       print "subject", subject
       resp = alice2.getResponse("SUBJECT2")
    if (subject == 3):
       print "subject", subject
       resp = alice2.getResponse("SUBJECT3")
    if (subject == 4):
       print "subject", subject
       resp = alice2.getResponse("SUBJECT4")
    if (subject == 5):
       print "subject", subject
       resp = alice2.getResponse("SUBJECT5")
    if (subject == 6):
       print "subject", subject
       resp = alice2.getResponse("SUBJECT6")
  
def GETMEMO():
    resp = alice2.getResponse("MEMOTRIGGER")
