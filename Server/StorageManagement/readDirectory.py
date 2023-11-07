import os


def get_directory_list(path):
    temp = []
    entries = os.scandir(path)
    for entry in entries:
        ext = ""
        if "." in entry.name and entry.name.split(".")[0] != "":
            ext = entry.name.split(".")[-1]
        temp.append({'name': entry.name, "ext": ext,
                    "size": entry.stat().st_size})
    print(temp)
    return temp
