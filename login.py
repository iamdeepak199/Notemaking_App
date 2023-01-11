from kivy.app import App
from kivy.lang import Builder
from kivy.modules import screen
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.uix.screen import Screen
from kivymd.uix.list  import IconLeftWidget,ImageLeftWidget
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.textfield import MDTextField
from subprocess import call
from helper import username_helper
from helper import password_helper

class MenuScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='Profile'))


class DeepakApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        image=ImageLeftWidget(source="i.png")
        icon=IconLeftWidget(icon="android", pos_hint={'center_x': 0.5, 'center_y': 0.6}, size_hint_x=None,
                               width=5000)


        button = MDRectangleFlatButton(text='Login', pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                       on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        self.password = Builder.load_string(password_helper)
        screen.add_widget(image)
        screen.add_widget(icon)
        screen.add_widget(self.username)
        screen.add_widget(self.password)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        if self.username.text is "":
            check_string = ' Please Enter a username'
        else:
            check_string = 'Welcome ' +self.username.text

        close_button = MDFlatButton(text='Back', on_release=self.close_dialog)
        more_button = MDFlatButton(text='Create Prpfile',on_release=self.open_dialog)
       # print(self.username.text)
        #print(self.password.text)
        self.dialog = MDDialog(title='User name', text= check_string,size_hint=(0.7, 1),buttons=[close_button,more_button])
        self.dialog.open()
    def close_dialog(self,obj):
        self.dialog.dismiss()

    def open_dialog(self,obj):
        self.dialog.on_open()


DeepakApp().run()
