# To print the file extension

print("Input the filename :")

name = str(input())

y = name.split(".")

y = str(name[-1])

y = "py" or "txt" or "html" or "css"

if y == "py":
    print("The extension of file is 'python'")
    
    if y == "txt":
     print("The extension of file is 'text'")
    
if y == "html":
    print("The extension of file is 'Hypertext Markup Language'")
    
    if y == "css":
        print("The extension of file is 'Cascading Style Sheet'")    
        