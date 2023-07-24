from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition


class MainScreen(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
       self.create_layout()

   def create_layout(self):
       self.size_hint = (1, 1)
       self.clearcolor = (0.153, 0.376, 0.145, 1)

       Window.clearcolor = (0.153, 0.376, 0.145, 1)

       curved_button = Button(
           text='Get Started',
           color=(1, 0.749, 0, 1),
           size_hint=(None, None),
           size=(200, 80),
           font_name='Century',
           background_color=(0, 1, 0, 1),
           pos_hint={'center_x': 0.4, 'y': 0.05}
       )
       curved_button.bind(on_press=self.on_button_press)
       self.add_widget(curved_button)

       comp = Label(
           text='Receive complementary solutions',
           pos_hint={'center_x': 0.5, 'center_y': 0.35},
           color=(1, 0.749, 0, 1),
           font_name='Century',
           font_size=30
       )
       self.add_widget(comp)

       prob = Label(
           text='to your everyday problems',
           pos_hint={'center_x': 0.5, 'center_y': 0.3},
           color=(1, 0.749, 0, 1),
           font_name='Century',
           font_size=30
       )
       self.add_widget(prob)

       camimage = Image(
           source='images/cam.png',
           pos_hint={'center_x': 0.5, 'center_y': 0.7}
       )
       self.add_widget(camimage)

       arrow = Image(
           source='images/arrow.png',
           pos_hint={'center_x': 0.6, 'center_y': 0.1},
           size_hint=(None, None),
           size=(100, 100)
       )
       self.add_widget(arrow)

   def on_button_press(self, instance):
       app = App.get_running_app()
       app.sm.transition = SlideTransition(direction='left')
       app.sm.current = 'second'

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_layout()

    def create_layout(self):
        self.size_hint = (1, 1)
        self.clearcolor = (0.376, 0.145, 0.153, 1)

        curved_button = Button(
            text='Main Screen',
            color=(1, 0.749, 0, 1),
            size_hint=(None, None),
            size=(200, 80),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.2, 'y': 0.05}
        )
        curved_button.bind(on_press=self.on_button_press)
        self.add_widget(curved_button)

        anatomyimage = Image(
            source='images/anatomy.png',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(anatomyimage)

        focus = Label(
            text='CHOOSE AREA OF FOCUS',
            pos_hint={'center_x': 0.5, 'center_y': 0.95},
            color=(1, 0.749, 0, 1),
            font_name='Century',
            font_size=30
        )
        self.add_widget(focus)

        # Create the second invisible button
        mhfh_button = Button(
            color=(1, 0.749, 0, 1),
            size_hint=(None, None),
            size=(200, 80),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.8, 'y': 0.8}
        )
        mhfh_button.bind(on_press=self.on_mhfh_button_press)
        mhfh_button.opacity = 0.05
        self.add_widget(mhfh_button)

        diet_button = Button(
            color=(1, 0.749, 0, 1),
            size_hint=(None, None),
            size=(200, 80),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.8, 'y': 0.5}
        )
        diet_button.bind(on_press=self.on_diet_button_press)
        diet_button.opacity = 0.05
        self.add_widget(diet_button)

        skin_button = Button(
            color=(1, 0.749, 0, 1),
            size_hint=(None, None),
            size=(200, 80),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.8, 'y': 0.3}
        )
        skin_button.bind(on_press=self.on_skin_button_press)
        skin_button.opacity = 0.05
        self.add_widget(skin_button)


    def on_button_press(self, instance):
        app = App.get_running_app()
        app.sm.transition = SlideTransition(direction='right')
        app.sm.current = 'main'

    def on_mhfh_button_press(self, instance):
        print("Button pressed")

    def on_diet_button_press(self, instance):
        print("Button pressed")

    def on_skin_button_press(self, instance):
        print("Button pressed")


class MyApp(App):
    def build(self):
        self.sm = ScreenManager(transition=SlideTransition(direction='right'))
        main_screen = MainScreen(name='main')
        second_screen = SecondScreen(name='second')
        self.sm.add_widget(main_screen)
        self.sm.add_widget(second_screen)
        return self.sm


if __name__ == '__main__':
    MyApp().run()