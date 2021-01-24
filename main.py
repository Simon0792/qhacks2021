# Import dependencies
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout  # for pop-up upload
from kivy.factory import Factory  # for pop-up upload
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Window.size = (400, 700)

userPts = 0  # global
import os


# SCREEN 1 -- Signup Screen
class signUpWindow(Screen):
    fullName = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    # check for correct information
    def submit(self):
        if self.fullName.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
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


# SCREEN 2 -- Login screen
class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    # If user and pass fields are not empty, grant access, else deny.
    def loginBtn(self):
        if self.email.text != "" and self.password.text != "":
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "questionaaire"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

    def howWorks(self):
        sm.current = "howitworks"


# SCREEN 3 -- Main Screen
# HERE IS WHERE WE MIGHT HAVE TO CHANGE THE QUESTIONS
class MainWindow(Screen):
    questionOne = ObjectProperty(None)
    questionTwo = ObjectProperty(None)
    questionThree = ObjectProperty(None)
    questionFour = ObjectProperty(None)
    questionFive = ObjectProperty(None)

    # this could become the submit button
    def logOut(self):
        # Here we could link the THANK YOU screen
        sm.current = "login"

    # probably useless
    '''
    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created
    '''


# SCREEN 4 -- Thank you screen
class thankYouWindow(Screen):

    def logOut(self):
        sm.current = "login"


# SCREEN 5 -- How it works screen
class howItWorksWindow(Screen):

    def homePage(self):
        sm.current = "login"

# SCREEN 6
# Questionaaire & upload
# TODO: was "Screen" type
class Questionaaire(Screen):
    # class variable - questionaaire
    questionOne = ObjectProperty(None)
    questionTwo = ObjectProperty(None)
    questionThree = ObjectProperty(None)
    questionFour = ObjectProperty(None)
    questionFive = ObjectProperty(None)
    conditions = ObjectProperty(None)

#CHECK
    #add if condition true

    def checkedBox(self):
        self.ids['buttonQuest'].background_color = 62, 78, 254, 0
    def submit(self):
        if self.questionOne.state == 'down' and self.questionTwo.state == 'down' \
                and self.questionThree.state == 'down' and self.questionFour.state == 'down' \
                and self.questionFive.state == 'down' and self.conditions.state == 'down':
                    global userPts
                    userPts += 5
                    self.reset()
                    sm.current = "thankyou"
        else:
            invalidInput()

    def reset(self):
        self.questionOne.text = ""
        self.questionTwo.text = ""
        self.questionThree.text = ""
        self.questionFour.text = ""
        self.questionFive.text = ""

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)
        self.dismiss_popup()
    def rememberPop(self):
        remember()


# Popup screen for upload
class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


# PAGES END
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


def invalidInput():
    pop = Popup(title='Invalid Input',
                content=Label(text='All have to be Yes.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()

def remember():
    pop = Popup(title='Remember:',
                content=Label(text='•Blue Bin: plastic, metal\nand glass packaging\n\n•Grey Box: paper products,cardboard and plastic bags\n\n•Green Bin: food waste, soiled paper products\nand yard waste\n\n•Garbage: non-hazardous waste\nthat cannot be reused, recycled or composted'),
                size_hint=(None, None), size=(400, 300))
    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()

screens = [Questionaaire(name="questionaaire"),
           LoginWindow(name="login"),
           signUpWindow(name="create"),
           MainWindow(name="main"),
           thankYouWindow(name='thankyou'),
           howItWorksWindow(name='howitworks')]

for screen in screens:
    sm.add_widget(screen)

# FIRST WINDOW -- HOME PAGE
sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
