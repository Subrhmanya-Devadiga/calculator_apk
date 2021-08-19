from ctypes import Array
from kivy.app import App
from kivy.core import window
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


Builder.load_file("calculator.kv")

class CalcUi(Widget):
    def clear(self):
        self.ids.calcinput.text="0"

    def bit_clear(self):
        display_value = self.ids.calcinput.text
        if display_value != "0":
            display_value = display_value[:-1]
            self.ids.calcinput.text = f'{display_value}'
        if display_value == "":
            self.ids.calcinput.text = f'0'

    def change_sign(self):
        display_value = self.ids.calcinput.text  
        if "-" not in display_value:
            self.ids.calcinput.text=f'-{display_value}'
        else:
            display_value[0] == "-"
            display_value = display_value.replace('-','')
            self.ids.calcinput.text=f'{display_value}'



    def button_value(self,value):
        display_value = self.ids.calcinput.text
        print(type(display_value))
        if "Error" in display_value:
            display_value=""
        if display_value == "0":
            self.ids.calcinput.text=""
            self.ids.calcinput.text=f'{value}'
        else:
            self.ids.calcinput.text=""
            self.ids.calcinput.text=f'{display_value}{value}'

    def dot(self):
        display_value = self.ids.calcinput.text
        self.ids.calcinput.text = f'{display_value}.' 


    def equals(self):
        display_value = self.ids.calcinput.text
        try:
            answer = eval(display_value)
            self.ids.calcinput.text = f'{round(answer,4)}'
        except:
            self.ids.calcinput.text = "Error"

    def percent(self):
        try:
            display_value = self.ids.calcinput.text
            if "+" in display_value:
                answer = eval(display_value)
                array_value = display_value.split("+")
                a = float(array_value[0])
                b = array_value[1]
                b = b.split("%")
                b = float(b[0])
                answer = a+(a*(b/100))
                self.ids.calcinput.text = f'{round(answer,4)}'
            if "-" in display_value:
                array_value = display_value.split("-")
                a = float(array_value[0])
                b = array_value[1]
                b = b.split("%")
                b = float(b[0])
                answer = a-(a*(b/100))
                self.ids.calcinput.text = f'{round(answer,4)}'
            if "*" in display_value:
                array_value = display_value.split("*")
                a = float(array_value[0])
                b = array_value[1]
                b = b.split("%")
                b = float(b[0])
                answer = a*(a*(b/100))
                self.ids.calcinput.text = f'{round(answer,4)}'
            if "/" in display_value:
                array_value = display_value.split("/")
                a = float(array_value[0])
                b = array_value[1]
                b = b.split("%")
                b = float(b[0])
                answer = a/(a*(b/100))
                self.ids.calcinput.text = f'{round(answer,4)}'
        except:
            self.ids.calcinput.text = f'Error'


class CalculatorApp(App):
    def build(self):
        return CalcUi()

if __name__ == '__main__':
    CalculatorApp().run()