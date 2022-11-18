file = input("File name: ")
name, extension = file.split(".")

if (
    extension == "gif"
    or extension == "jpg"
    or extension == "jpeg"
    or extension == "png"
):
    print("image/gif")
elif extension == "pdf" or extension == "txt" or extension == "zip":
    print("application/pdf")
else:
    print("extension not found")
