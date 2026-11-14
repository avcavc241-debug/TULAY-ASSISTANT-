
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.025, 0.04, 0.09, 1)

class TulayApp(App):
    def build(self):
        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        root.add_widget(Label(
            text="[b]TULAY[/b]\nتولاي",
            markup=True,
            font_size=36
        ))

        root.add_widget(Label(
            text="أهلاً علي ❤️\nأنا تولاي، مساعدتك الشخصية",
            font_size=22
        ))

        self.chat = Label(
            text="أنا جاهزة للتحدث معك",
            font_size=20
        )
        root.add_widget(self.chat)

        self.message = TextInput(
            hint_text="اكتب رسالتك...",
            multiline=False,
            size_hint_y=None,
            height=55
        )
        root.add_widget(self.message)

        send = Button(
            text="إرسال",
            size_hint_y=None,
            height=55
        )
        send.bind(on_press=self.send_message)
        root.add_widget(send)

        return root

    def send_message(self, instance):
        msg = self.message.text.strip()
        if msg:
            self.chat.text = (
                "علي: " + msg +
                "\n\nتولاي: أهلاً بيك علي، آني وياك ❤️"
            )
            self.message.text = ""

TulayApp().run()
