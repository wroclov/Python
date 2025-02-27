from docx2pdf import convert

name = "your_file_name"

convert("cv/"+name+".docx", "cv/"+name+".pdf")

print(name + ".pdf has length: " + str(len(name+'.pdf')))
