import os
def delete_multiple_files(folder_path:str,file_path:str):
    """
    Given a folder_path and file_path,where folder_path points to a folder from where files will be deleted and file_path
    points to a file that have names of files that needs to be deleted.
    """
    deleted_all = True
    try:
        file = open(file_path)
        for each in file:
            file_name = each.strip()
            file_to_delete = folder_path + '\\' + file_name
            if (res := delete_operatoin(file_to_delete)) == False:
                deleted_all = False
        print("Success!, All The files are deleted ") if deleted_all == True else print("Some files were not FOUND !!!")
    except FileNotFoundError:
        print(f"The file at '{file_path}' does not exist.")
def delete_operatoin(file_to_delete):
    """ This function deletes the file"""
    try:
        os.remove(file_to_delete)
        return True
    except FileNotFoundError:
        print(f"The file at '{file_to_delete}' does not exist.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Call function

# Just add your folder's path inside ""
folder_path = r"C:\Users\compb\OneDrive\Desktop\test"
# Just add file path inside "", this file will have all the names of files that needs to be deleted
file_path = r"C:\Users\compb\OneDrive\Desktop\hello.txt"

delete_multiple_files(folder_path,file_path)
