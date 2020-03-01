from threading import Thread
from os import system

class Thread (Thread):
    def __init__(self):
        Thread.__init__(self)
        
        
        
    def run(self, process()):        
         

    def processo(self):
        hostname = self.ip #example
        response = system("ping -c 1 " + hostname)

        #and then check the response...
        if response == 0:
            print (hostname, 'is up!')
            self.host.listHostUp.append(hostname)
        else:
            print (hostname, 'is down!')
            