# The following script will send a quote to a Log and Python every minute

cron   =  Runtime.createAndStart('cron', 'Cron')
log   =  Runtime.createAndStart('log', 'Log')

# add a task which sends text to the log service Log.log(string) every minute
cron.addTask('* * * * *','log','log', 'hello sir, time for your coffee')
# add a task to send text to a python function every minute
cron.addTask('* * * * *','python','doThisEveryMinute', 'hello sir, time for your coffee')

def doThisEveryMinute(text):
	print (str(datetime.datetime.now().time()), text)

listOfTasks = cron.getCronTasks()
for i in listOfTasks:
	print(i.name, i.cronPattern, i.method)
