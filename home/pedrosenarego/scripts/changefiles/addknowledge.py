import os
import sys
import fileinput
import os.path


#### Clean the ending </aiml>############
for line in fileinput.input('/home/pedro/myrobotLab/myrobotLab-1.0.1461/develop/ProgramAB/bots/zorba/aiml/aknowledge.aiml', inplace=1):
    sys.stdout.write(line.replace('</aiml>', ''))


#######add the new sentence############
text_file = open("/home/pedro/myrobotLab/myrobotLab-1.0.1461/develop/ProgramAB/bots/zorba/aiml/aknowledge.aiml", "a")

TotalAmount = '<category><pattern>DOG</pattern><template>Dog is an animal</template></category>\n</aiml>'

text_file.write("%s" % TotalAmount)

text_file.close()