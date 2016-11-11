# An example on how to use the Clock service to execute a Python def at a regular interval
# The def to be executed
def tick(time):
	print time
# Get a handle to this python instance ( use the name of your python service )
python = Runtime.getService("python")
# Start the Clock service
clock = Runtime.createAndStart("clock","Clock")
# Set the clock to pulse everý 20 milliseconds
clock.setInterval(20)
# Add a pulse listener that executes the tick def in this python scipt
clock.addListener("pulse", python.name, "tick")
# Start the clock
clock.startClock()
# Let the clock run for 10 seconds
sleep(10)
# Stop the clock
clock.stopClock()
