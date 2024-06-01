import os
from typing import Dict


def list_directory_contents(directory: str):
    """

    :param directory: path of the directory to fetch the list of files and subdirectories in it.
    :return:
    """
    directory_contents = os.listdir(directory)

    if len(directory_contents) == 0:
        print("Empty Directory")
    else:
        print("Directory Contents are: ", directory_contents)


def report_file_sizes(directory: str):
    """
    Method to display file name, and it's size in bytes
    :param directory: path of the directory
    :return: None
    """
    directory_contents = os.listdir(directory)

    for content in directory_contents:
        if os.path.exists(os.path.join(directory, content)):
            print(f"File name is: {content} and size (In Bytes) is: {os.path.getsize(os.path.join(directory, content))}")


def count_file_extensions(directory: str) -> Dict[str, int]:
    """
    method to count each extension.
    :param directory: path of the directory to fetch the list of files to count the extensions
    :return: Dictionary of extensions as keys and their count as values.
    """
    file_extensions = {}
    directory_contents = os.listdir(directory)

    for content in directory_contents:
        content_path = os.path.join(directory, content)

        if os.path.isfile(content_path):
            extension = os.path.splitext(content)[1].lower()
            if extension not in file_extensions:
                file_extensions[extension] = 1
            else:
                file_extensions[extension] += 1

    return file_extensions


directory_path = input("Enter directory path: ")

if os.path.exists(directory_path):
    list_directory_contents(directory_path)
    report_file_sizes(directory_path)
    print("File extensions are: ", count_file_extensions(directory_path))
else:
    print(f"Directory does not exist or Invalid path given. Please check this give path: {directory_path}")





