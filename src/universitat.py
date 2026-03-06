from lxml import etree


doc = etree.parse("xml/universitat.xml")


print("\nNombre de la universidad:")

for nombre in doc.xpath("/universidad/nombre/text()"):
    print(nombre + "\n")