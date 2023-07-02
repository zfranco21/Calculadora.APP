from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        self.icon = "calculator.png"
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(background_color="black", foreground_color="white",
                                  multiline=False, halign="right", font_size=55,
                                  readonly=True)

        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label, font_size=28, background_color="grey",
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equal_button = Button(
            text="=", font_size=30, background_color="grey",
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
        )
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        # Agregar marca de agua con el nombre del creador
        creator_label = Label(text="created by Franco Herrera", font_size=12, color=(0.5, 0.5, 0.5, 1),
                              size_hint=(None, None), size=(self.solution.width,20),
                              pos_hint={'center_x': 0.5})
        main_layout.add_widget(creator_label)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                solution = str(eval(self.solution.text))
                self.solution.text = solution
            except ZeroDivisionError:
                self.show_error_popup("Error: Division by zero")
            except:
                self.show_error_popup("Error: Invalid expression")

    def show_error_popup(self, message):
        content = BoxLayout(orientation='vertical')
        label = Label(text=message, font_size=20, color=(1, 1, 1, 1))
        content.add_widget(label)
        popup = Popup(title='Error', content=content, size_hint=(0.5, 0.5))
        popup.open()


if __name__ == "__main__":
    app = MainApp()
    app.run()
