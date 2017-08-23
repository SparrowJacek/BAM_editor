import win32api
import os


def get_drives():
    drive_paths = [drive_letter for drive_letter in win32api.GetLogicalDriveStrings().split('\0') if drive_letter]
    drive_letters = [drive_path[:-1] for drive_path in drive_paths]
    drive_names = [win32api.GetVolumeInformation('{0}\\'.format(drive_letter))[0] for drive_letter in drive_letters]
    drives_with_names = ['{0}({1})'.format(name, letter) for name, letter in zip(drive_names, drive_letters)]
    return zip(drives_with_names, drive_paths)


def get_popular_directories():
    user_path = os.path.expanduser('~')
    popular_directory_names = ['Desktop', 'Downloads', 'Documents']
    return ((name, os.path.join(user_path, name)) for  name in popular_directory_names if os.path.isdir(os.path.join(user_path, name)))


