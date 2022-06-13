from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.icon = "10.png"
        self.operators = ["+", "-", "*", "/"]
        self.last_was_operater = None
        self.last_button = None

        main_layout = BoxLayout(orientation = "vertical")
        self.solution = TextInput(background_color = "black", foreground_color = "yellow", multiline=False, halign="right", font_size=30, readonly=True)

        main_layout.add_widget(self.solution)
        buttons = [

            ["INP", "EXP", "EXT", "EXE", "OFF", "ON"],
            ["2nd", "dey", "Sin", "Cos", "Tan", "C"],
            ["M", "M+", "M-", "Lg", "Ln", "CE"],
            ["1/X^2", "(", ")", "+", "-", "CM"],
            ["X^y", "Y^x", "%", "*", "/", "RM"],
            ["X!", "Y!", "7", "8", "9", "EE"],
            ["1/X", "1/Y", "4", "5", "6", "MRC"],
            ["X^2", "Y^2", "1", "2", "3", "CPT"],
            ["X^3", "Y^2", "e", "0", ".", "ENT:"],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label, font_size=30, background_color="green",pos_hint={"center_x": 0.5, "center_y": 0.5},
                )

                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equal_button = Button(
                    text="=", font_size=30, background_color="green", pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            self.solution.text = ""
        else:
            if current and (
                self.last_was_operater and button_text in self.operators):
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
                    solution = str(eval(self.solution.text))
                    self.solution.text = solution




if __name__ == "__main__":
    app = MainApp()
    app.run()