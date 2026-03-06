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
print()


print("Nombres de todos los alumnos:")
print()
for nombre_alumno in doc.xpath("//alumno/nombre/text()"):
    print(nombre_alumno)
print()


print("Identificadores de todas las carreras:")
print()
for id_carrera in doc.xpath("//carrera/@id"):
    print(id_carrera)
print()


print("Datos de la carrera cuyo identificador es c01:")
print()
for datos_c01 in doc.xpath("//carrera[@id='c01']//text()"):
    print(datos_c01)
print()


print("Centro en que se estudia de la carrera cuyo id es c02:")
print()
for centro_c02 in doc.xpath("//carrera[@id='c02']/centro/text()"):
    print(centro_c02)
print()


print("Nombre de las carreras que tengan subdirector:")
print()
for carreras_con_subdirector in doc.xpath("//carrera[subdirector!='']/nombre/text()"):
    print(carreras_con_subdirector)
print()





