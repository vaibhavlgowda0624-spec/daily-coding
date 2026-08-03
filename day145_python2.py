import zipfile

with zipfile.ZipFile("files.zip", "r") as zipf:
    zipf.extractall("output")

print("Files Extracted")
