# A small example of Gray code to decimal conversion and also the conversion from decinmal to Gray code
# to verify that the methods work OK
from org.myrobotlab.math import MathUtils
for x in range(0, 16):
    print x, "\t", "{0:016b}".format(MathUtils.decimalToGray(x)), "\t", MathUtils.grayToDecimal(MathUtils.decimalToGray(x))
