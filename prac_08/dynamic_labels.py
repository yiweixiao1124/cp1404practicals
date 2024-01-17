from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = {"Bob Brown": "021565", "Cat Cyan": "549644", "Oren Ochre": "024685"}

    def build(self):
        """Build the Kivy GUI"""

        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Creotes label from dictionary"""
        for name in self.name_to_phone:
            temp_label = Label(text=name)
            temp_label.color = (1, 0, 0, 1)
            self.root.ids.label_box.add_widget(temp_label)


DynamicLabelsApp().run()
