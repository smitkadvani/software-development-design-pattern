from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class CheckBox(ABC):
    @abstractmethod
    def check(self):
        pass

class MacBotton(Button):
    def render(self):
        print("Mac button")

class MacCheckBox(CheckBox):
    def check(self):
        print(f"Mac checkbox rendered")

class LinuxButton(Button):
    def render(self):
        print(f"Linux button")

class LinuxCheckBox(CheckBox):
    def check(self):
        print("Linux checkbox") 

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    
    @abstractmethod
    def create_check_box(self):
        pass 

class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()
    
    def create_check_box(self):
        return LinuxCheckBox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacBotton()

    def create_check_box(self):
        return MacCheckBox()


class Application:
    def __init__(self, factory:GUIFactory):
        self.factory = factory
    
    def create_ui(self):
        self.button = self.factory.create_button()
        self.check_box = self.factory.create_check_box()
    
    def render_ui(self):
        self.button.render()
        self.check_box.check()

print("Creating Mac application")
macApplication = Application(MacFactory())
macApplication.create_ui()
macApplication.render_ui()

print("Creating Linux application")
linuxApplication = Application(LinuxFactory())
linuxApplication.create_ui()
linuxApplication.render_ui()
        
        