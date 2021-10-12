from docxtpl import DocxTemplate

template_path = r"C:\Users\Bastien\Desktop\test.docx"

doc = DocxTemplate(template_path)
context = {"company_name": "World company"}
doc.render(context)
doc.save("./generated_doc.docx")
