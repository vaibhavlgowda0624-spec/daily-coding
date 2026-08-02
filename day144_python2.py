import zipfile

with zipfile.ZipFile("files.zip", "r") as zipf:
    print(zipf.namelist())
