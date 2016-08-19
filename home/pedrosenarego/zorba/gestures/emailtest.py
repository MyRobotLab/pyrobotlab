def emailtest(to,TEXT,SUBJECT):

  import smtplib
  
    
  message = 'Subject: %s\n\n%s' % (SUBJECT, TEXT+"\n\n\n\n------------------------------------------------\n\nSent from my robot Zorba the almighty!! \nWe apologize if its not written in the best way, sometimes zorba misunderstands the message!! \n\n Pedro - Research Engineer\n Zorba - Plastic robot")
  
  mail = smtplib.SMTP('smtp.gmail.com',587)

  mail.ehlo()

  mail.starttls()

  mail.login('pedrogilsenarego@gmail.com','****pass****')

  mail.sendmail('pedrogilsenarego@gmail.com',to,message)

  mail.close()