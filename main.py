import webbrowser
from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock

class MainApp(App):
    def build(self):
        self.tap_count = 0
        
        # ボタンの背景画像として画像を設定。これによりスワイプ等の誤操作を防ぎ、タップイベントを確実に取得します。
        self.btn = Button(
            background_normal='994b3b39-93a8-443f-b4b4-126ba0400b9f.png',
            background_down='994b3b39-93a8-443f-b4b4-126ba0400b9f.png',
            text='',
            font_size='32sp',
            color=(1, 1, 1, 1),
            bold=True
        )
        self.btn.bind(on_release=self.on_tap)
        return self.btn

    def on_tap(self, instance):
        if self.tap_count < 3:
            self.tap_count += 1
            if self.tap_count == 3:
                self.btn.text = "起動中..."
                Clock.schedule_once(self.open_url, 3)

    def open_url(self, dt):
        webbrowser.open("https://udify.app/chat/GW74LLZvrKZIdxPQ")
        self.stop()

if __name__ == '__main__':
    MainApp().run()
