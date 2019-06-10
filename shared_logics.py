from kivy.app import App


def get_widget_with_id(id):
    app = App.get_running_app()
    root_label = app.root
    return root_label.ids[id]