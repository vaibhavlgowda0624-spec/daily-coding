import zipfile

with zipfile.ZipFile("files.zip", "w") as zipf:
    zipf.write("sample.txt")

print("ZIP file created")
