from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.list import MDList,ThreeLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from helper import username_helper, password_helper
from login import MenuScreen

Window.size = (350, 60)

navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Navigation Drawer"
                        elevation: 35
                        right_action_items: [["clock",lambda x: app.navigation_draw('')]]
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
                    
                    MDLabel:
                        text:"Welcome To NoteBook" 
                        halign:'center' 
                        font_style: 'Subtitle1'

                          
                        Image:
                            source:''
                            spacing: '8dp'
                            padding: '8dp'
                            halign:'center'
                            
                            

                         
                         
                        
                    MDBottomAppBar:  
                        MDToolbar:
                            title: "Notes"
                            elevation: 35
                            left_action_items: [["notebook", lambda x: nav_drawer.set_state('toggle')]]
                            mode: 'end' 
                            type:'bottom'

        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                Image:
                    source:'mine.jpg'
                MDLabel:
                    text: '       Deepak Bhardwaj '
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                
                MDLabel:
                    text: '         9643762201 '
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]    

                MDLabel:
                    text: '         iamdeepak199@gmail.com'
                    font_style: 'Caption'  
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Profile'
                            IconLeftWidget:
                                icon: 'face-profile'
                        OneLineIconListItem:
                            text:'Message'
                            IconLeftWidget:
                                icon: 'chat'
                        OneLineIconListItem:
                            text:'Search'
                            IconLeftWidget:
                                icon: 'magnify'                
                        OneLineIconListItem:
                            text:'Upload'
                            Button:
                                on_press: root.manager.current = 'stop'
                                
                            IconLeftWidget:
                                icon: 'file-upload'
                        OneLineIconListItem:
                            text:'Logout'
                            IconLeftWidget:
                                icon: 'logout'
                                         


"""
KV ="""
#:import NoTransition Kivy.uic.screenmanager.NoTransition
MDFloatLayout:
    md_bg_color:1,1,1,1
    ScreenManager:
        id: scr 
        transition : NoTransition()
        MDScreen
        
"""

class Menuscreen(Screen):
    pass
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))

class DeepakApp(MDApp):

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen


DeepakApp().run()


