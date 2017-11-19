#########################################
# Security.py
# description: used as a general template
# categories: simulator
# more info @: http://myrobotlab.org/service/Security
#########################################


# start the service
security = Runtime.start("security","Security")

# store & crypt secret infomations
security.addSecret("amazon.polly.user.key", "FIE38238733459852");
security.addSecret("amazon.polly.user.secret", "Ujffkds838234jf/kDKJkdlskjlfkj");
security.saveStore()

# get & decrypt secret infomations
security.loadStore()
print security.getSecret("amazon.polly.user.key")
print security.getSecret("amazon.polly.user.secret")
