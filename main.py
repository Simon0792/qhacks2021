#Import dependencies
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
Window.size = (400, 700)

#SCREEN 1 -- Signup Screen
class signUpWindow(Screen):
    fullName = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    #check for correct information
    def submit(self):
        if self.fullName.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                self.reset()
                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.fullName.text = ""

#SCREEN 2 -- Login screen
class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    #If user and pass fields are not empty, grant access, else deny.
    def loginBtn(self):
        if self.email.text != "" and self.password.text != "":
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "thankyou"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


#SCREEN 3 -- Main Screen
#HERE IS WHERE WE MIGHT HAVE TO CHANGE THE QUESTIONS
class MainWindow(Screen):
    questionOne = ObjectProperty(None)
    questionTwo = ObjectProperty(None)
    questionThree = ObjectProperty(None)
    questionFour = ObjectProperty(None)
    questionFive = ObjectProperty(None)

    #this could become the submit button
    def logOut(self):
        #Here we could link the THANK YOU screen
        sm.current = "login"

    #probably useless
    '''
    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created
    '''

#SCREEN 4 -- Thank you screen
class thankYouWindow(Screen):

    def logOut(self):
        sm.current = "login"

#SCREEN 5 -- Thank you screen
class howItWorksWindow(Screen):

    def homePage(self):
        sm.current = "login"


#PAGES END
class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all fields with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()

screens = [LoginWindow(name="login"), signUpWindow(name="create"),MainWindow(name="main"), thankYouWindow(name='thankyou'), howItWorksWindow(name='howitworks')]
for screen in screens:
    sm.add_widget(screen)
#FIRST WINDOW -- HOME PAGE
sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
