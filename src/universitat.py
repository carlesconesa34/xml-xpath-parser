from lxml import etree


doc = etree.parse("xml/universitat.xml")


print("\nNombre de la universidad:")

for nombre in doc.xpath("/universidad/nombre/text()"):
    print(nombre + "\n")


print("País de la universidad:")

for pais in doc.xpath("/universidad/pais/text()"):
    print(pais + "\n")


print("Nombres de las carreras:")

for nombre_carrera in doc.xpath("//carrera/nombre/text()"):
    print(nombre_carrera)
    
