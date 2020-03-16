#!/usr/bin/python
# vim: set fileencoding=<utf-8>

import os
import re

to_sanitize_files = []
bad_char = [
    '³', '²', '®', 'º', '½', 'Ã', '°', '£', 'À', 'Å', 'Ì', 'Ã', 'Ê', 'Ü', 'À', 'µ', '§', '¿', 'Î', '¹', 'Ú', 'È', 'û',
    '¾', '¤' '¼', 'Ó', '½', '±'
]


def check_folder(work_file: str):
    work_file = f"new_src\\{work_file[4:]}"
    path = "\\".join(work_file.split("\\")[:-1])
    if not os.path.isdir(path):
        os.makedirs(path)


def work_other_file(work_file: str):
    print("Encoding {} in UTF-8.".format(work_file))
    check_folder(work_file)
    with open(work_file, "r", encoding="1252", errors='ignore') as other_file:
        with open("new_src\\{}".format(work_file[4:]), "w", encoding="utf-8") as new_file:
            for line in other_file.readlines():
                new_file.write(line)


def work_source_file(work_file: str):
    print("Encoding and sanitize {} in UTF-8.".format(work_file))
    check_folder(work_file)
    with open(work_file, "r", encoding="1252", errors='ignore') as source_file:
        with open("new_src\\{}".format(work_file[4:]), "w", encoding="utf-8") as new_file:
            file_content = source_file.read()
            groups = re.findall("(?://[^\n]*|/\*(?:(?!\*/).)*\*/)", file_content)
            for index, group in enumerate(groups):
                if any(x in group for x in bad_char):
                    file_content = file_content.replace(group, "", 1)
            new_file.write(file_content)
        with open("new_src\\{}".format(work_file[4:]), "r", encoding="utf-8") as new_file:
            lines = new_file.readlines()
            new_lines = []
        with open("new_src\\{}".format(work_file[4:]), "w", encoding="utf-8") as new_file:
            for line in lines:
                if line.isspace():
                    new_lines.append("\n")
                else:
                    new_lines.append(line)
            new_file.writelines(new_lines)


if __name__ == "__main__":
    print("Game-Emulation.com")
    print("Working...")
    for dir_path, sub_dirs, files in os.walk("src"):
        to_sanitize_files.extend(os.path.join(dir_path, x) for x in files)

    for file in to_sanitize_files:
        if not file.endswith((".cpp", ".h", ".c")):
            work_other_file(file)
        else:
            work_source_file(file)
    print("Game-Emulation.com")
