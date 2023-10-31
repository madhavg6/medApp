from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.graphics import RoundedRectangle, Color

class CurvedButton(ButtonBehavior, Label):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
       self.background_normal = ''
       self.background_down = ''
       self.size_hint = (None, None)
       self.size = (200, 70)
       self.font_name = 'Century'
       self.color = (1, 1, 1, 1)
       self.pos_hint = {'center_x': 0.5, 'y': 0.04}

       with self.canvas.before:
           Color(0, 0.7, 0.3, 1)
           self.rounded_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20])
           self.bind(pos=self.update_rect, size=self.update_rect)

   def update_rect(self, *args):
       self.rounded_rect.pos = self.pos
       self.rounded_rect.size = self.size

class MainScreen(Screen):
  def __init__(self, **kwargs):
      super().__init__(**kwargs)
      self.create_layout()

  def create_layout(self):
      self.size_hint = (1, 1)

      Window.clearcolor = (0, 0.4, 0, 1)

      startbutton = Button(
          background_normal='images/startbutton.png',
          background_down='images/startbutton.png',
          size_hint=(None, None),
          size=(700, 700),
          pos_hint={'center_x': 0.47, 'center_y': 0.25},
      )
      startbutton.bind(on_press=self.on_button_press)
      self.add_widget(startbutton)

      comp = Label(
          text='Diagnose now.',
          pos_hint={'center_x': 0.5, 'center_y': 0.37},
          color=(0.2, 0, 0, 1),
          font_name='Century',
          font_size=30
      )
      self.add_widget(comp)


      camimage = Image(
          source='images/cam2.png',
          pos_hint={'center_x': 0.5, 'center_y': 0.65},
      )
      self.add_widget(camimage)

      camtitle = Image(
          source='images/camtitle.png',
          pos_hint={'center_x': 0.5, 'center_y': 0.45},
      )
      self.add_widget(camtitle)

      leaf1 = Image(
          source='images/leaf1.png',
          pos_hint={'center_x': 0.5, 'center_y': 0.67}
      )
      self.add_widget(leaf1)

      leaf2 = Image(
          source='images/leaf2.png',
          pos_hint={'center_x': 0.5, 'center_y': 0.32}
      )
      self.add_widget(leaf2)


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

       curved_button = CurvedButton(
           text='Main Screen',
           on_press=self.on_button_press
       )
       self.add_widget(curved_button)

       anatomyimage = Image(
           source='images/anatomy.png',
           pos_hint={'center_x': 0.5, 'center_y': 0.5}
       )
       self.add_widget(anatomyimage)

       focus = Label(
           text='CHOOSE AREA OF FOCUS',
           pos_hint={'center_x': 0.5, 'center_y': 0.95},
           color=(1, 1, 1, 1),
           font_name='Century',
           font_size=30
       )
       self.add_widget(focus)


       mh_button = Button(
           color=(1, 1, 1, 1),
           size_hint=(None, None),
           size=(200, 80),
           font_name='Century',
           background_color=(0, 1, 0, 1),
           pos_hint={'center_x': 0.8, 'y': 0.8}
       )
       mh_button.bind(on_press=self.on_mh_button_press)
       mh_button.opacity = 0.0
       self.add_widget(mh_button)

       mh = Label(
           text='Mental Health',
           pos_hint={'center_x': 0.8, 'center_y': 0.85},
           color=(1, 1, 1, 1),
           font_name='Century',
           font_size=15
       )
       self.add_widget(mh)

       fh_button = Button(
           color=(1, 1, 1, 1),
           size_hint=(None, None),
           size=(200, 80),
           font_name='Century',
           background_color=(0, 1, 0, 1),
           pos_hint={'center_x': 0.2, 'y': 0.8}
       )
       fh_button.bind(on_press=self.on_fh_button_press)
       fh_button.opacity = 0.0
       self.add_widget(fh_button)

       fh = Label(
           text='Facial Hygiene',
           pos_hint={'center_x': 0.2, 'center_y': 0.85},
           color=(1, 1, 1, 1),
           font_name='Century',
           font_size=15
       )
       self.add_widget(fh)

       diet_button = Button(
           color=(1, 1, 1, 1),
           size_hint=(None, None),
           size=(200, 80),
           font_name='Century',
           background_color=(0, 1, 0, 1),
           pos_hint={'center_x': 0.2, 'y': 0.25}
       )
       diet_button.bind(on_press=self.on_diet_button_press)
       diet_button.opacity = 0.0
       self.add_widget(diet_button)

       diet = Label(
           text='Diet',
           pos_hint={'center_x': 0.2, 'center_y': 0.3},
           color=(1, 1, 1, 1),
           font_name='Century',
           font_size=15
       )
       self.add_widget(diet)

       gas_button = Button(
           color=(1, 1, 1, 1),
           size_hint=(None, None),
           size=(200, 80),
           font_name='Century',
           background_color=(0, 1, 0, 1),
           pos_hint={'center_x': 0.8, 'y': 0.3}
       )
       gas_button.bind(on_press=self.on_gas_button_press)
       gas_button.opacity = 0.0
       self.add_widget(gas_button)

       gas = Label(
           text='Gastrointestinal',
           pos_hint={'center_x': 0.8, 'center_y': 0.35},
           color=(1, 1, 1, 1),
           font_name='Century',
           font_size=15
       )
       self.add_widget(gas)


       skin_button = Button(
           color=(1, 1, 1, 1),
           size_hint=(None, None),
           size=(200, 80),
           font_name='Century',
           background_color=(0, 1, 0, 1),
           pos_hint={'center_x': 0.2, 'y': 0.55}
       )
       skin_button.bind(on_press=self.on_skin_button_press)
       skin_button.opacity = 0.0
       self.add_widget(skin_button)

       skin = Label(
           text='Skin',
           pos_hint={'center_x': 0.2, 'center_y': 0.6},
           color=(1, 1, 1, 1),
           font_name='Century',
           font_size=15
       )
       self.add_widget(skin)


   def on_button_press(self, instance):
       app = App.get_running_app()
       app.sm.transition = SlideTransition(direction='right')
       app.sm.current = 'main'

   def on_mh_button_press(self, instance):
       print("Button pressed1")

   def on_fh_button_press(self, instance):
       print("Button pressed2")

   def on_diet_button_press(self, instance):
       print("Button pressed3")

   def on_gas_button_press(self, instance):
       print("Button pressed4")

   def on_skin_button_press(self, instance):
       app = App.get_running_app()
       app.sm.transition = SlideTransition(direction='left')
       app.sm.current = 'skin'

class SkinScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_layout()

    def create_layout(self):
        skin_title = Label(
            text='Skin',
            pos_hint={'center_x': 0.5, 'center_y': 0.9},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=60
        )
        self.add_widget(skin_title)

        skin_choose = Label(
            text='Choose From the Following',
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=15
        )
        self.add_widget(skin_choose)

        prone_button = Button(
            text='Acne Prone Skin',
            size_hint=(None, None),
            size=(200, 80),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.5, 'y': 0.7}
        )
        prone_button.bind(on_press=self.on_prone_button_press)
        self.add_widget(prone_button)

        dry_button = Button(
            text='Dry Skin',
            size_hint=(None, None),
            size=(200, 80),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.5, 'y': 0.6}  # Adjust the position as needed
        )
        dry_button.bind(on_press=self.on_dry_button_press)
        self.add_widget(dry_button)

        oily_button = Button(
            text='Oily Skin',
            size_hint=(None, None),
            size=(200, 80),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.5, 'y': 0.5}
        )
        oily_button.bind(on_press=self.on_oily_button_press)
        self.add_widget(oily_button)

        irritation_button = Button(
            text='Skin Irritation',
            size_hint=(None, None),
            size=(200, 80),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.5, 'y': 0.4}
        )
        irritation_button.bind(on_press=self.on_irritation_button_press)
        self.add_widget(irritation_button)

        second_button = Button(
            text='Back',
            size_hint=(None, None),
            size=(200, 80),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.5, 'y': 0.1}  # Adjust the position as needed
        )
        second_button.bind(on_press=self.on_second_button_press)
        self.add_widget(second_button)


    def on_second_button_press(self, instance):
        app = App.get_running_app()
        app.sm.transition = SlideTransition(direction='right')
        app.sm.current = 'second'
    def on_prone_button_press(self, instance):
        app = App.get_running_app()
        app.sm.transition = SlideTransition(direction='left')
        app.sm.current = 'prone'
    def on_oily_button_press(self, instance):
        print("Button pressed7")

    def on_irritation_button_press(self, instance):
        print("Button pressed7")

    def on_dry_button_press(self, instance):
        app = App.get_running_app()
        app.sm.transition = SlideTransition(direction='left')
        app.sm.current = 'dryskin'


class ProneScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_layout()
    def create_layout(self):
        acne_choose = Label(
            text='Acne Prone Skin',
            pos_hint={'center_x': 0.5, 'center_y': 0.9},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=40
        )
        self.add_widget(acne_choose)

        green_tea = Button(
            text='Green Tea',
            size_hint=(None, None),
            size=(200, 80),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.5, 'y': 0.7}
        )
        green_tea.bind(on_press=self.on_green_tea_press)
        self.add_widget(green_tea)

        coconut_oil = Button(
            text='Coconut Oil',
            size_hint=(None, None),
            size=(200, 80),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.5, 'y': 0.6}
        )
        coconut_oil.bind(on_press=self.on_coconut_oil_press)
        self.add_widget(coconut_oil)

        sunflower_oil = Button(
            text='Sunflower Oil',
            size_hint=(None, None),
            size=(200, 80),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.5, 'y': 0.5}
        )
        sunflower_oil.bind(on_press=self.on_sunflower_oil_press)
        self.add_widget(sunflower_oil)

        honey = Button(
            text='Honey',
            size_hint=(None, None),
            size=(200, 80),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.5, 'y': 0.4}
        )
        honey.bind(on_press=self.on_honey_press)
        self.add_widget(honey)

        clay_face = Button(
            text='Clay Face Mask',
            size_hint=(None, None),
            size=(200, 80),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.5, 'y': 0.3}
        )
        clay_face.bind(on_press=self.on_clay_face_press)
        self.add_widget(clay_face)

        acne_back = Button(
            text='Back',
            size_hint=(None, None),
            size=(200, 80),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.5, 'y': 0.1}  # Adjust the position as needed
        )
        acne_back.bind(on_press=self.on_acne_back_press)
        self.add_widget(acne_back)

    def on_green_tea_press(self, instance):
        app = App.get_running_app()
        app.sm.transition = SlideTransition(direction='left')
        app.sm.current = 'greentea'

    def on_coconut_oil_press(self, instance):
        app = App.get_running_app()
        app.sm.transition = SlideTransition(direction='left')
        app.sm.current = 'cocooil'

    def on_sunflower_oil_press(self, instance):
        app = App.get_running_app()
        app.sm.transition = SlideTransition(direction='left')
        app.sm.current = 'sunoil'

    def on_honey_press(self, instance):
        print("Button pressed10")

    def on_clay_face_press(self, instance):
        print("Button pressed11")

    def on_acne_back_press(self, instance):
        app = App.get_running_app()
        app.sm.transition = SlideTransition(direction='right')
        app.sm.current = 'second'

class GreenTeaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_layout()
    def create_layout(self):
        acne_label2 = Label(
            text='Acne Prone Skin',
            pos_hint={'center_x': 0.5, 'center_y': 0.9},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=50
        )
        self.add_widget(acne_label2)

        greentea_label = Label(
            text='Green Tea',
            pos_hint={'center_x': 0.5, 'center_y': 0.825},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=30
        )
        self.add_widget(greentea_label)

        potent = Label(
            text='Contains Potent Antioxidants - Catechins',
            pos_hint={'center_x': 0.5, 'center_y': 0.775},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=22
        )
        self.add_widget(potent)

        anti_ex = Label(
            text='       • Has anti-inflammatory and antimicrobial effects \n \n       • Regulates sebum production which reduces\n        likelihood of clogged pores',
            pos_hint={'center_x': 0.465, 'center_y': 0.7},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=20
        )
        self.add_widget(anti_ex)

        gtprop = Label(
            text='       These properties make green tea a viable option\n       for treating acne, as inflammation and bacterial\n       overgrowth are both contributing factors to\n       acne development',
            pos_hint={'center_x': 0.47, 'center_y': 0.5},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=20
        )
        self.add_widget(gtprop)

        gtben = Label(
            text='       Green tea can provide its benefits \n       as a drink or as an exfoliator. \n       Mix with honey to create a powdery paste, \n       then apply to skin for 5-10 minutes, \n       then rinse skin thoroughly.',
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=20
        )
        self.add_widget(gtben)

        gt_back = Button(
            text='Back',
            size_hint=(None, None),
            size=(150, 60),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.7, 'y': 0.03}  # Adjust the position as needed
        )
        gt_back.bind(on_press=self.on_gt_back_press)
        self.add_widget(gt_back)

    def on_gt_back_press(self, instance):
        app = App.get_running_app()
        app.sm.transition = SlideTransition(direction='right')
        app.sm.current = 'second'

class CocoOilScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_layout()
    def create_layout(self):
        acne_label3 = Label(
            text='Acne Prone Skin',
            pos_hint={'center_x': 0.5, 'center_y': 0.9},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=50
        )
        self.add_widget(acne_label3)

        cocooil_label = Label(
            text='Coconut Oil',
            pos_hint={'center_x': 0.5, 'center_y': 0.825},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=30
        )
        self.add_widget(cocooil_label)

        lauric = Label(
            text='Contains Lauric Acid and Vitiman E',
            pos_hint={'center_x': 0.5, 'center_y': 0.775},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=22
        )
        self.add_widget(lauric)

        cocooil_ex = Label(
            text='       • has antimicrobial properties that fight acne causing\n        bacteria \n \n       • High concentration of fatty acids \n       → penetrate skins surface \n \n       • Provides deep hydration \n \n       • Improves skin elasticity \n \n       • Protects skin from damage caused by free radicals',
            pos_hint={'center_x': 0.48, 'center_y': 0.62},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=17
        )
        self.add_widget(cocooil_ex)

        note = Label(
            text='     Note: Keep in mind that that it may not be suitable for \n                     those with oily skin as it can clog pores.',
            pos_hint ={'center_x': 0.5, 'center_y': 0.4},
            color = (1, 1, 1, 1),
            font_name = 'Century',
            font_size = 17
        )
        self.add_widget(note)

        oilrub = Label(
            text='     Simply rub the oil in circular \n     motions all over your face and \n     neck, giving yourself a gentle \n     massage as you go',
            pos_hint={'center_x': 0.7, 'center_y': 0.3},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=17
        )
        self.add_widget(oilrub)

        coco_back = Button(
            text='Back',
            size_hint=(None, None),
            size=(150, 60),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.7, 'y': 0.03}  # Adjust the position as needed
        )
        coco_back.bind(on_press=self.on_coco_back_press)
        self.add_widget(coco_back)
    def on_coco_back_press(self, instance):
        app = App.get_running_app()
        app.sm.transition = SlideTransition(direction='right')
        app.sm.current = 'second'
class SunOilScreen(Screen):
    def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.create_layout()

    def create_layout(self):
        acne_label3 = Label(
            text='Acne Prone Skin',
            pos_hint={'center_x': 0.5, 'center_y': 0.9},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=50
            )
        self.add_widget(acne_label3)

        sunoil_label = Label(
            text='Sunflower Oil',
            pos_hint={'center_x': 0.5, 'center_y': 0.825},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=30
            )
        self.add_widget(sunoil_label)

        oliec = Label(
            text='Rich in oleic acid, linoleic acid, and\n vitamin E and has calming properties',
            pos_hint={'center_x': 0.5, 'center_y': 0.75},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=22
            )
        self.add_widget(oliec)

        sunoil_ex = Label(
            text='       • Helps maintain skins natural barrier\n \n       • Provides antioxidant protection \n \n       • Promotes wound healing \n \n       • Noncomedogenic, will not clog pores \n \n       • Highly absorbent \n \n       • Reduces skin irritation and itchiness \n \n       •Hydrates skin to be softer and smoother',
            pos_hint={'center_x': 0.48, 'center_y': 0.55},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=17
        )
        self.add_widget(sunoil_ex)

        note2 = Label(
            text='     Note: Cold-pressed sunflower oil is the best \n     option for skincare as it retains its nutrients.',
            pos_hint={'center_x': 0.5, 'center_y': 0.35},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=17
        )
        self.add_widget(note2)

        sunoilrub = Label(
            text='     Simply rub the oil in circular \n     motions all over your face and \n     neck, giving yourself a gentle \n     massage as you go',
            pos_hint={'center_x': 0.7, 'center_y': 0.2},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=17
        )
        self.add_widget(sunoilrub)

        sun_back = Button(
            text='Back',
            size_hint=(None, None),
            size=(150, 60),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.7, 'y': 0.03}  # Adjust the position as needed
        )
        sun_back.bind(on_press=self.on_sun_back_press)
        self.add_widget(sun_back)

    def on_sun_back_press(self, instance):
        app = App.get_running_app()
        app.sm.transition = SlideTransition(direction='right')
        app.sm.current = 'second'


class DrySkinScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_layout()
    def create_layout(self):
        dryskin_label = Label(
            text='Dry Skin',
            pos_hint={'center_x': 0.5, 'center_y': 0.9},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=50
        )
        self.add_widget(dryskin_label)


        dryskin_sol = Label(
            text='People can also prevent dry skin by \navoiding things that may trigger dryness \nor irritation, including:',
            pos_hint={'center_x': 0.5, 'center_y': 0.8},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=20
        )
        self.add_widget(dryskin_sol)

        dryskin_ex = Label(
            text='       • scratching their skin \n \n       • excessive air conditioning \n \n       • shaving using a blunt razor or \n       without shaving gel \n \n       • bathing or showering too often \n \n       • rubbing skin too hard when towel drying \n \n       • bathing or showering in water that is too hot \n \n       • using lotions that contain alcohol \n \n       • wearing clothes that rub the skin \n \n       • frequent contact with detergents \n \n       • sitting under direct heat from a heater or fire \n \n       • staying outside in windy conditions  \n         without covering the skin',
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=20
        )
        self.add_widget(dryskin_ex)

        aloe = Button(
            text='Aloe Vera Sol.',
            size_hint=(None, None),
            size=(150, 55),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.8, 'y': 0.92}
        )
        aloe.bind(on_press=self.on_aloe_press)
        self.add_widget(aloe)

    def on_aloe_press(self, instance):
        app = App.get_running_app()
        app.sm.transition = SlideTransition(direction='left')
        app.sm.current = 'aloe'

class AloeVeraScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_layout()

    def create_layout(self):
        dryskin_label2 = Label(
            text='Dry Skin',
            pos_hint={'center_x': 0.5, 'center_y': 0.9},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=50
        )
        self.add_widget(dryskin_label2)

        aloe_label = Label(
            text='Aloe Vera',
            pos_hint={'center_x': 0.5, 'center_y': 0.825},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=30
        )
        self.add_widget(aloe_label)

        polyenz = Label(
            text='Contains polysaccharides and enzymes',
            pos_hint={'center_x': 0.5, 'center_y': 0.775},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=25
        )
        self.add_widget(polyenz)

        aloe_ex = Label(
            text='       • Hydrates and Soothes skin \n \n       • sugars form a protective layer which prevents \n       moisture loss \n \n       • Enzymes exfoliate dead skin cells \n \n       • Promotes cell turnover \n \n       • Results in smoother and more hydrated skin',
            pos_hint={'center_x': 0.48, 'center_y': 0.625},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=17
        )
        self.add_widget(aloe_ex)

        antiinf = Label(
            text='Has anti-inflammatory properties and \n       contains lignin',
            pos_hint={'center_x': 0.5, 'center_y': 0.46},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=25
        )
        self.add_widget(antiinf)

        antiinf_ex = Label(
            text='       • helps reduce redness and irritation \n \n       • Lignin enhances penetrative effect \n       are absorbed into the skin \n \n       • Ensures vital properties of aloe \n       of other substances on skin',
            pos_hint={'center_x': 0.44, 'center_y': 0.33},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=17
        )
        self.add_widget(antiinf_ex)

        formation = Label(
            text='       Aloe vera is best applied to \n       the skin through the \n       formation of a gel.',
            pos_hint={'center_x': 0.7, 'center_y': 0.15},
            color=(1, 1, 1, 1),
            font_name='Century',
            font_size=20
        )
        self.add_widget(formation)

        aloe_back = Button(
            text='Back',
            size_hint=(None, None),
            size=(150, 60),
            font_name='Century',
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.7, 'y': 0.03}  # Adjust the position as needed
        )
        aloe_back.bind(on_press=self.on_aloe_back_press)
        self.add_widget(aloe_back)

    def on_aloe_back_press(self, instance):
        app = App.get_running_app()
        app.sm.transition = SlideTransition(direction='right')
        app.sm.current = 'second'


class MyApp(App):
   def build(self):
       self.sm = ScreenManager(transition=SlideTransition(direction='right'))
       main_screen = MainScreen(name='main')
       second_screen = SecondScreen(name='second')
       skin_screen = SkinScreen(name='skin')
       prone_screen = ProneScreen(name='prone')
       greentea_screen = GreenTeaScreen(name='greentea')
       cocooil_screen = CocoOilScreen(name='cocooil')
       sunoil_screen = SunOilScreen(name='sunoil')
       dry_screen = DrySkinScreen(name='dryskin')
       aloe_screen = AloeVeraScreen(name='aloe')
       self.sm.add_widget(main_screen)
       self.sm.add_widget(second_screen)
       self.sm.add_widget(skin_screen)
       self.sm.add_widget(prone_screen)
       self.sm.add_widget(greentea_screen)
       self.sm.add_widget(cocooil_screen)
       self.sm.add_widget(sunoil_screen)
       self.sm.add_widget(dry_screen)
       self.sm.add_widget(aloe_screen)
       return self.sm

if __name__ == '__main__':
   MyApp().run()
