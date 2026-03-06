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


print("Nombre de los alumnos que estén haciendo proyecto:")
print()
for nombre_alumno_proyecto in doc.xpath("//alumno/estudios[proyecto!='']/../nombre/text()"):
    print(nombre_alumno_proyecto)
print()


print("Códigos de las carreras en las que hay algún alumno matriculado:")
print()
carreras = []
for carreras_con_alumnos in doc.xpath("//alumno/estudios/carrera/@codigo"):
    if(carreras_con_alumnos not in carreras):
        carreras.append(carreras_con_alumnos)
for carrera in carreras:
    print(carrera)
print()


# print(" Apellidos y Nombre de los alumnos con beca.")
# print()
# for alumno_con_beca in doc.xpath(""):
    # print(nombre_alumno_proyecto)
# print()


print("Nombre de las asignaturas de la titulación c04:")
print()
for asignaturas_c04 in doc.xpath("//asignatura[@titulacion='c04']/nombre/text()"):
    print(asignaturas_c04)
print()











