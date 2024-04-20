from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
Window.size = (400,300)
class MyApp(App): 
 def build(self): 
  self.title = 'my first app'
  return Label(text = "Hello World!")
 
MyApp().run()