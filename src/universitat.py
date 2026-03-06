from lxml import etree


doc = etree.parse("xml/universitat.xml")


print("\nNombre de la universidad:")
print()
for nombre in doc.xpath("/universidad/nombre/text()"):
    print(nombre + "\n")


print("País de la universidad:")
print()
for pais in doc.xpath("/universidad/pais/text()"):
    print(pais + "\n")


print("Nombres de las carreras:")
print()
for nombre_carrera in doc.xpath("//carrera/nombre/text()"):
    print(nombre_carrera)
print()


print("Años de plan de estudio de las carreras:")
print()
for plan_carrera in doc.xpath("//carrera/plan/text()"):
    print(plan_carrera)



    
