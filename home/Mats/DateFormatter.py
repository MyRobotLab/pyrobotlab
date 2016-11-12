from java.util import Date
from java.util import Locale
from java.text import DateFormat
dateFormatter = DateFormat.getDateInstance(DateFormat.FULL, Locale.FRANCE);
today = Date()
print today
dateOut = dateFormatter.format(today);
print dateOut
