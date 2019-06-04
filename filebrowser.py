import win32api
import os

from kivy.uix.treeview import TreeView, TreeViewLabel


def get_drives():
    drive_letters = [drive_letter[:-1] for drive_letter in win32api.GetLogicalDriveStrings().split('\0') if
                     drive_letter and check_if_drive_not_empty(drive_letter[:-1])]
    drive_names = [win32api.GetVolumeInformation('{0}\\'.format(drive_letter))[0] for drive_letter in drive_letters]
    drives_with_names = ['{0}({1})'.format(name, letter) for name, letter in zip(drive_names, drive_letters)]
    return zip(drives_with_names, drive_letters)


def check_if_drive_not_empty(drive_letter):
    try:
        win32api.GetVolumeInformation('{0}\\'.format(drive_letter))
        return True
    except:
        return False


def get_popular_directories():
    user_path = os.path.expanduser('~')
    popular_directory_names = ['Desktop', 'Downloads', 'Documents']
    return ((name, os.path.join(user_path, name)) for name in popular_directory_names if
            os.path.isdir(os.path.join(user_path, name)))


class TreeViewBrowser(TreeView):
    def __init__(self, **kwargs):
        super(TreeViewBrowser, self).__init__(**kwargs)
        self.root_options = dict(text='Locations')
        self.populate_tree_view()

    def populate_tree_view(self):
        self.populate_drives()
        self.populate_popular_directories()

    def populate_drives(self):
        computer = self.add_node(TreeViewLabel(text='Computer', is_open=True))
        for name, path in get_drives():
            self.add_node(PathViewLabel(path, text=name), computer)

    def populate_popular_directories(self):
        popular_directories = self.add_node(TreeViewLabel(text='Popular directories', is_open=True))
        for name, path in get_popular_directories():
            self.add_node(PathViewLabel(path, text=name), popular_directories)


class PathViewLabel(TreeViewLabel):
    def __init__(self, path, **kwargs):
        super(PathViewLabel, self).__init__(**kwargs)
        self.path = path

    def set_path(self, touch, file_choosers):
        if self.collide_point(*touch.pos) and touch.button == 'left':
            for file_chooser in file_choosers:
                file_chooser.content.path = self.path
