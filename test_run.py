import flet as ft

def main(page: ft.Page):
    print("Flet target main invoked!")
    page.add(ft.Text("Hello from Flet!"))

print("Starting Flet app as WEB_BROWSER...")
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
print("Flet app call completed.")
