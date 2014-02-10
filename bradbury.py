import time, sys

class Race:
    def stand(self):
        print "really tall"
    def where(self):
        print "across the void, across the universe"

def callMethod(o, name):
    getattr(o, name)()

f = Race()

print ('O,Thomas'),
sys.stdout.flush()
for i in range(3):
    time.sleep(0.5)
    print ("."),
    sys.stdout.flush()

print ('will a Race one day stand'),

callMethod(f, "stand")
sys.stdout.flush()

time.sleep(2.5)

sys.stdout.flush()
for i in range(3):
    time.sleep(0.5)
    print ("."),
    sys.stdout.flush()

callMethod(f, "where")
sys.stdout.flush()
