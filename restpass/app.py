import npyscreen
import pyperclip
from restpass.generator import Generator
from restpass import NAME, VERSION
from threading import Thread
import time


MAX_CHARS = 30


class CopyButton(npyscreen.ButtonPress):
    parent_app = None

    def __init__(self, *args, **keywords):
        super().__init__(*args, **keywords)

    @classmethod
    def get(cls, parent_app):
        cls.parent_app = parent_app
        return cls

    def whenPressed(self):
        if self.parent_app.result:
            pyperclip.copy(self.parent_app.result)

            self.parent_app.source_entry.set_value("")
            self.parent_app.salt_entry.set_value("")
            self.parent_app.length_slider.set_value(3)

            self.parent_app.rules_select.set_value([0, 1, 2])
            self.parent_app.custom_alphabet_entry.set_value("")


class RestpassApp(npyscreen.NPSAppManaged):
    def __init__(self):
        super().__init__()

        self.form = None
        self.hide_checkbox = None
        self.show_length_slider = None

        self.source_entry = None
        self.salt_entry = None
        self.length_slider = None

        self.rules_select = None
        self.custom_alphabet_entry = None

        self.result_title = None
        self.copy_button = None

        self.result = None

    def init_widgets(self):
        self.form = npyscreen.Form(name=f"{NAME}-v{VERSION}")

        self.hide_checkbox = self.form.add(npyscreen.Checkbox, name="Hide result", value=False)
        self.show_length_slider = self.form.add(npyscreen.TitleSlider, out_of=MAX_CHARS, name="Show length:")
        self.separator()
        self.source_entry = self.form.add(npyscreen.TitleText, name="Source:", )
        self.salt_entry = self.form.add(npyscreen.TitleText, name="Salt:")
        self.length_slider = self.form.add(npyscreen.TitleSlider, value=3, lowest=3, out_of=MAX_CHARS, name="Length:")
        self.separator()
        self.rules_select = self.form.add(npyscreen.TitleMultiSelect, max_height=4, value=[0, 1, 2], name="Rules:", values=["Digits", "Lowercase", "Uppercase", "Symbols"], scroll_exit=True)
        self.custom_alphabet_entry = self.form.add(npyscreen.TitleText, name="Custom alphabet:", )
        self.separator()
        self.result_title = self.form.add(npyscreen.TitleFixedText, name="Result:")
        self.copy_button = self.form.add(CopyButton.get(parent_app=self), name="Copy to clipboard")

    def separator(self):
        self.form.add(npyscreen.FixedText, value="––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")

    def main(self):
        self.init_widgets()
        Thread(target=self.update).start()
        self.form.edit()

    def update(self, delay=0.1):
        while True:
            if self.source_entry.get_value():
                generator = Generator(source=self.source_entry.get_value())
                if self.salt_entry.get_value():
                    generator.set_salt(self.salt_entry.get_value().encode("utf-8"))

                if self.custom_alphabet_entry.get_value():
                    generator.set_custom_alphabet(self.custom_alphabet_entry.get_value())
                else:
                    rules = self.rules_select.get_selected_objects()
                    digits = True if "Digits" in rules else False
                    lowercase = True if "Lowercase" in rules else False
                    uppercase = True if "Uppercase" in rules else False
                    symbols = True if "Symbols" in rules else False

                    generator.set_rules(digits=digits, lowercase=lowercase, uppercase=uppercase, symbols=symbols)

                self.result = generator.generate(length=int(self.length_slider.get_value()))
                if self.hide_checkbox.value:
                    show_length = int(self.show_length_slider.get_value())
                    show_str = self.result[:show_length] + "*" * (len(self.result) - show_length)
                else:
                    show_str = self.result

                self.result_title.set_value(show_str)
            else:
                self.result_title.set_value("")

            self.form.display()
            time.sleep(delay)


def main():
    RestpassApp().run()


if __name__ == '__main__':
    main()
