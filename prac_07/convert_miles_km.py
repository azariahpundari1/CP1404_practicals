from kivy.app import App
from kivy.lang import Builder


MILES_TO_KM = 1.60934


class ConvertMilesToKM(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def convert_miles(self):
        value = self.valid_number()
        kilometers = value * MILES_TO_KM
        self.root.ids.output.text = str(kilometers)

    def handle_increment(self, increment):
        value = self.valid_number() + increment
        self.root.ids.input.text = str(value)
        self.convert_miles()

    def valid_number(self):
        value = float(self.root.ids.input.text)
        if value >= 0:
            return value
        elif ValueError:
            return 0


ConvertMilesToKM().run()