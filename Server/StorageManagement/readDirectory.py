import os


def get_directory_list(path):
    temp = []
    entries = os.scandir(path)
    for entry in entries:
        print(entry.name, "/", entry.stat().st_size)
        temp.append({'name': entry.name, "size": entry.stat().st_size})
    return temp
