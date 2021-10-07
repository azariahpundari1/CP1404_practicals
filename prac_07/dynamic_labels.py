from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class DynamicLabels(App):
    name = StringProperty()

    def __init__(self, **kwarg):
        super().__init__(**kwarg)
        self.list_of_names = {"Joe", "Bob", "Steven", "Robert"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.display_names()
        return self.root

    def display_names(self):
        for name in self.list_of_names:
            self.name = f"{name}"

# yeah this is the best i can do
DynamicLabels().run()