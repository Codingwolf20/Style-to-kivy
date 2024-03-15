class MainMenu(Screen):
   def build(self):
       self.theme_cls.primary_palette = "Cyan"
       self.theme_cls.accent_palette = "Indigo"  # Lime
       self.theme_cls.theme_style = "Light"

       sm.add_widget(SignInScreen(name='sign_in_screen'))
       sm.add_widget(MainMenu(name='main_menu'))
       sm.add_widget(TermsConditionsScreen(name='terms_conditions_screen'))
       sm.add_widget(MyInformation(name='my_information'))

       return sm

   def color_changer(self):
       if self.theme_cls.theme_style == "Dark":
           self.theme_cls.theme_style = "Light"
           self.theme_cls.primary_palette = "Cyan"
           self.theme_cls.accent_palette = "Indigo"
       elif self.theme_cls.theme_style == "Light":
           self.theme_cls.theme_style = "Dark"
           self.theme_cls.primary_palette = "DeepPurple"
           self.theme_cls.accent_palette = "Teal"
