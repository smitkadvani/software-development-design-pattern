class ApplicationInstance:
    instance = None
    def __init__(self):
        self.isLoggedIn = False
    
    @staticmethod
    def getInstance():
        if not ApplicationInstance.instance :
            ApplicationInstance.instance = ApplicationInstance()
        return ApplicationInstance.instance


app1 = ApplicationInstance.getInstance()
print(app1.isLoggedIn)
app2 = ApplicationInstance.getInstance()
print(app2.isLoggedIn)
app2.isLoggedIn = True
print(app1.isLoggedIn)
print(app2.isLoggedIn)