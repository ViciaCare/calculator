from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.solution = TextInput(multiline=False, readonly=False, halign="right", font_size=30, input_filter="float")
        main_layout.add_widget(self.solution)
        return main_layout


MainApp().run()
