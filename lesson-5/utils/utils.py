from os import path


def get_current_dir_path(file):
    return path.split(path.join(path.abspath(file)))[0]


def get_target_file_path(current_file, name):
    dir_path = get_current_dir_path(current_file)
    return path.join(dir_path, name)
