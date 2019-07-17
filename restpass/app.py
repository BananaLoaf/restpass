from threading import Thread
import time

import npyscreen
import pyperclip

from restpass import PAYLOAD
from restpass.generator import Generator

MAX_CHARS = 30


def copy_button(parent_app):
    class CopyButton(npyscreen.ButtonPress):
        def __init__(self, *args, **keywords):
            super().__init__(*args, **keywords)

        def whenPressed(self):
            if parent_app.output_raw:
                pyperclip.copy(parent_app.output_raw)
                parent_app.output_raw = ""

                parent_app.reset_widgets()

    return CopyButton


def paste_button(destination):
    class PasteButton(npyscreen.ButtonPress):
        def __init__(self, *args, **keywords):
            super().__init__(*args, **keywords)

        def whenPressed(self):
            destination.set_value(pyperclip.paste())

    return PasteButton


class RestpassApp(npyscreen.NPSAppManaged):
    def __init__(self):
        super().__init__()
        self.KILL = False

        self.form = None

        self.hide_output_checkbox = None
        self.show_length_slider = None

        self.length_slider = None
        self.input_entry = None
        self.input_paste_button = None
        self.salt_entry = None
        self.salt_paste_button = None

        self.alphabet_select = None

        self.output_title = None
        self.copy_button = None

        self.output_raw = None

    def init_widgets(self):
        self.form = npyscreen.Form(name=f"{PAYLOAD['name']}-v{PAYLOAD['version']}")

        self.hide_output_checkbox = self.form.add(npyscreen.Checkbox, name="Hide output", value=False)
        self.show_length_slider = self.form.add(npyscreen.TitleSlider, out_of=MAX_CHARS, name="Show length:")
        self.separator()

        self.length_slider = self.form.add(npyscreen.TitleSlider, value=8, lowest=3, out_of=MAX_CHARS, name="Length:")
        self.input_entry = self.form.add(npyscreen.TitlePassword, name="Input:")
        self.input_paste_button = self.form.add(paste_button(destination=self.input_entry), name="Paste")
        self.salt_entry = self.form.add(npyscreen.TitlePassword, name="Salt:")
        self.salt_paste_button = self.form.add(paste_button(destination=self.salt_entry), name="Paste")
        self.alphabet_select = self.form.add(npyscreen.TitleMultiSelect, max_height=4, value=[0, 1, 2], name="Alphabet:", values=["Digits", "Lowercase", "Uppercase", "Symbols"], scroll_exit=True)
        self.separator()

        self.output_title = self.form.add(npyscreen.TitleFixedText, name="Output:")
        self.copy_button = self.form.add(copy_button(parent_app=self), name="Copy")

    def reset_widgets(self):
        self.input_entry.set_value("")
        self.salt_entry.set_value("")
        self.length_slider.set_value(3)
        self.alphabet_select.set_value([0, 1, 2])

    def separator(self):
        self.form.add(npyscreen.FixedText, value="––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")

    def main(self):
        thread = Thread(target=self.update)
        try:
            self.init_widgets()
            thread.start()
            self.form.edit()
        except KeyboardInterrupt:
            self.KILL = True
            thread.join()  # Wait for thread to shutdown JIC
            self.form.exit_editing()

    def update(self, delay=0.1):
        while not self.KILL:
            if self.input_entry.get_value():
                generator = Generator(source=self.input_entry.get_value())
                if self.salt_entry.get_value():
                    generator.set_salt(self.salt_entry.get_value().encode("utf-8"))

                alphabet = self.alphabet_select.get_selected_objects()
                if alphabet:
                    digits = True if "Digits" in alphabet else False
                    lowercase = True if "Lowercase" in alphabet else False
                    uppercase = True if "Uppercase" in alphabet else False
                    symbols = True if "Symbols" in alphabet else False

                    generator.set_rules(digits=digits, lowercase=lowercase, uppercase=uppercase, symbols=symbols)

                    self.output_raw = generator.generate(length=int(self.length_slider.get_value()))
                    if self.hide_output_checkbox.value:
                        show_length = int(self.show_length_slider.get_value())
                        output_str = self.output_raw[:show_length] + "*" * (len(self.output_raw) - show_length)
                    else:
                        output_str = self.output_raw

                    self.output_title.set_value(output_str)
                else:
                    self.output_title.set_value("")
            else:
                self.output_title.set_value("")

            self.form.display()
            time.sleep(delay)
