from kivy.app import App
from kivy.uix import button
from functools import partial
import python.src.pla_layout_generator.main as pla_gen


class PlaGen(App):
    # def build(self):
        # return label.Label(text="Hello World!")
        # return button.Button(text="Welcome to the world!", background_color=(155, 0, 51, 53))

    def disable(self, instance, *args):
        instance.disabled = True

    def update(self, instance, *args):
        instance.text = "I am Disabled!"

    def disp_pla(self, instance, *args):
        instance.text = pla_gen.generate_pla_layout()[1]

    def build(self):
        mybtn = button.Button(text="Click me to disable", pos=(300, 350), size_hint=(.25, .18))

        # mybtn.bind(on_press=partial(self.disable, mybtn))

        # mybtn.bind(on_press=partial(self.update, mybtn))

        mybtn.bind(on_press=partial(self.disp_pla, mybtn))

        return mybtn





if __name__ == '__main__':
    PlaGen().run()
