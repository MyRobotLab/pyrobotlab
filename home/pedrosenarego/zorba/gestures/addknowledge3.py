import os
import sys
import fileinput
import os.path

def addKnowledge3(category,pattern):
  
  
  ##### change somethings to make sense############
  #pattern = pattern.replace('my', 'your')
  
  #### Clean the ending </aiml>############
  
  for line in fileinput.input('/home/pedro/myrobotLab/myrobotLab-1.0.1461/develop/ProgramAB/bots/zorba/aiml/aknowledge.aiml', inplace=1):
      sys.stdout.write(line.replace('</aiml>', ''))

  #######add the new sentence to aiml############
  
  
  text_file = open("/home/pedro/myrobotLab/myrobotLab-1.0.1461/develop/ProgramAB/bots/zorba/aiml/aknowledge.aiml", "a")

  TotalAmount = '<category><pattern>'+str(category)+'</pattern><template>'+str(pattern)+'</template></category>\n</aiml>'

  text_file.write("%s" % TotalAmount)

  text_file.close()
  
  