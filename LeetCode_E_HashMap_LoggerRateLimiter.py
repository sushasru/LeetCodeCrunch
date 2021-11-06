class Logger:
    def __init__(self):
        msgq = []

    def shouldPrintMessage(self,timestamp,message):
        pass

param1 = Logger()
param1.shouldPrintMessage(1, "foo")
param1.shouldPrintMessage(2, "bar")
param1.shouldPrintMessage(3, "foo")
param1.shouldPrintMessage(8, "bar")
param1.shouldPrintMessage(10, "foo")
param1.shouldPrintMessage(11, "foo")
