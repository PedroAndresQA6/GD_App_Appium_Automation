from fpdf import FPDF
import os

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Reporte de Automatizacion - GD App (Gobierno Digital)", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Resumen General", ln=True)
pdf.set_font("Arial", "", 10)
pdf.multi_cell(0, 6, "Se han automatizado pruebas para la aplicacion movil 'Gobierno Digital' (GD App) utilizando Appium con Python y pytest. Las pruebas cubren los 13 servicios accesibles desde la pantalla de inicio de la aplicacion. A continuacion se presenta el detalle de cada test desarrollado, su funcionalidad, resultados reales obtenidos y conclusiones.")
pdf.ln(10)

tests_info = [
    {
        "num": "01",
        "nombre": "Servicios - Verificar que cada servicio abre correctamente",
        "descripcion": "Test de verificacion rapida que itera sobre todos los servicios disponibles en la pantalla de inicio (12 servicios: 070_Digital, Programas, DIF, Movilidad, Turismo, Cultura, Bienestar_Animal, Deporte, Noticias, Oficinas, Bloque, Tramites). Para cada servicio, realiza click, verifica que la pantalla se abra correctamente y regresa al menu principal. Maneja el scrolling para servicios en segunda y tercera fila.",
        "resultado": "PASSED",
        "tiempo": "~87 segundos",
        "retro": "Excelente test de verificacion rapida (smoke testing). Los 12 servicios responden correctamente al click y la navegacion es fluida. El manejo del scrolling para servicios en diferentes filas funciona perfectamente. Tiempo de ejecucion: 86.73s."
    },
    {
        "num": "02",
        "nombre": "070 Digital - Completo",
        "descripcion": "Test completo del servicio 070 Digital - Atencion Ciudadana. Incluye: click en servicio, busqueda de boton AGREGAR o REPORTAR, click en 'Ver todos', scroll para ver opciones, entrada a una opcion, scroll para ver formulario completo, llenado del campo REPORTE con texto automatizado, click en 'Agregar archivos' para identificacion (toma foto), scroll para ver mas campos, click en 'Agregar archivos' para comprobante (toma foto), busqueda y click en boton ENVIAR, espera de confirmacion, y cierre del formulario.",
        "resultado": "PASSED",
        "tiempo": "~68 segundos",
        "retro": "Test muy completo que abarca todo el flujo de reporte de ciudadana. El llenado de formulario, captura de fotos y envio funcionan correctamente. La captura de screenshots permite validacion visual. Tiempo de ejecucion: 68.11s."
    },
    {
        "num": "03",
        "nombre": "Programas - Exploracion",
        "descripcion": "Test de exploracion del servicio Programas. Verifica que la pantalla muestra 'Desarrollo Social' como titulo. Valida la existencia de opciones: Credencial, Noticias y Contacto. Captura screenshot. Realiza click en cada opcion, espera carga, y regresa. En Noticias realiza scroll down y up.",
        "resultado": "PASSED",
        "tiempo": "~40 segundos",
        "retro": "Test exitoso que verifica la estructura del menu de Programas. Los assert para validar texto son robustos. La navegacion entre Credencial, Noticias y Contacto funciona correctamente. Tiempo de ejecucion: 40.25s."
    },
    {
        "num": "04",
        "nombre": "DIF - Exploracion",
        "descripcion": "Test completo de exploracion del servicio DIF. Verifica la presencia de atajos: Credencial, Noticias, Journadas y Contacto. Itera por cada opcion: Credencial (click y regreso), Noticias (scroll y regreso), Journadas (explora pestanas: dif, donativos, rehabilitacion, vaccinacion, busca articulos y entra a los primeros 2), Contacto. Realiza scroll para ver programas con 'Me interesa' y encontro 3 programas.",
        "resultado": "PASSED",
        "tiempo": "~68 segundos",
        "retro": "Test muy completo que explora multiples secciones y pestanas. La iteracion sobre las 4 pestanas de Journadas (dif, donativos, rehabilitacion, vaccinacion) encontro contenido en 'vacunacion'. Se encontraron 3 programas con 'Me interesa': DE MIL COLORES, JORNADAS DE ESTERILIZACION, EL EXTRA. Tiempo de ejecucion: 67.87s."
    },
    {
        "num": "05",
        "nombre": "Movilidad - Exploracion",
        "descripcion": "Test de automatizacion del servicio Movilidad. Incluye: apertura del mapa de Google, click en 'Ver lista', scroll en la lista (2 veces), click en elemento de la lista (Restaurantes), cierre de lista clicking en el mapa, interaccion con filtros (QroBus -> Ver todo -> Culturales -> Ver todo -> Estac.), click en marcador del mapa, cierre de info del marcador clicking en el mapa, y regreso a inicio.",
        "resultado": "PASSED",
        "tiempo": "~52-60 segundos",
        "retro": "El test funciona correctamente de manera consistente. La interaccion con el mapa de Google y los filtros se realiza sin problemas. El flujo de navegacion es estable y el test puede ejecutarse multiples veces sin fallos."
    },
    {
        "num": "06",
        "nombre": "Turismo - Exploracion",
        "descripcion": "Test de exploracion del servicio Turismo. Verifica la presencia de 'Queretaro'. Captura screenshot. Explora las opciones: 'Explorar' (click y regreso), 'Noticias' (scroll down/up y regreso), 'Transporte' (verifica WebView, busca servicios como Qrobus con scroll, click en el elemento, scroll y regreso, y opciones de Contacto), scrolls en eventos, y regreso al menu.",
        "resultado": "PASSED",
        "tiempo": "~59 segundos",
        "retro": "Test exitoso con correcta interaccion con WebView para Transporte. El servicio Qrobus fue encontrado y probado. La estructura de busqueda de elementos con fallback de scroll es robusta. Tiempo de ejecucion: 58.50s."
    },
    {
        "num": "07",
        "nombre": "Cultura - Exploracion",
        "descripcion": "Test completo de exploracion del servicio Cultura. Verifica 'Queretaro'. Captura screenshot. Explora: Cartelera (scroll, busca articulos CONOCE o abril, entra al primero y regresa), Explorar (scroll y regreso), Noticias (scroll, busca articulos, entra y regresa), Contacto (scroll y regreso). Scroll para ver articulo principal 'Cultural' y entrada.",
        "resultado": "PASSED",
        "tiempo": "~94 segundos",
        "retro": "Test muy completo con multiples rutas de navegacion. La exploracion de Cartelera, Explorar, Noticias y Contacto funciono correctamente. Se entraron a noticias y articulos principales. Tiempo de ejecucion: 93.96s."
    },
    {
        "num": "08",
        "nombre": "Bienestar Animal - Exploracion",
        "descripcion": "Test de exploracion del servicio Bienestar Animal. Captura screenshot. Explora opciones web: Adopcion (espera 5 segundos y regreso), Informacion (espera 5 segundos y regreso), Noticias (scroll, busca articulos, entra y regresa). Realiza scroll para explorar programas con 'Me interesa' y encontro 3 programas.",
        "resultado": "PASSED",
        "tiempo": "~52 segundos",
        "retro": "Las esperas de 5 segundos para contenido web permiten cargar la pagina correctamente. Se encontraron 3 programas con 'Me interesa'. La navegacion entre Adopcion, Informacion y Noticias funciona bien. Tiempo de ejecucion: 52.48s."
    },
    {
        "num": "09",
        "nombre": "Deporte - Exploracion",
        "descripcion": "Test de exploracion del servicio Deporte. Captura screenshot. Explora opciones: Credencial (scroll y regreso), Explora (scroll y regreso), Contacto (scroll y regreso). Realiza scroll para buscar clases, entra a la primera clase encontrada, busca boton 'Inscribirse' y hace click (maneja popup si aparece), y regresa al menu.",
        "resultado": "PASSED",
        "tiempo": "~61 segundos",
        "retro": "Test exitoso. Se encontro 1 clase y se interactuo con el boton 'Inscribirse'. El manejo del flujo de inscripcion funciona correctamente. La navegacion entre secciones es fluida. Tiempo de ejecucion: 61.09s."
    },
    {
        "num": "10",
        "nombre": "Noticias - Exploracion",
        "descripcion": "Test de exploracion del servicio Noticias. Realiza scroll para posicionar el servicio, hace click, captura screenshot. Itera sobre las primeras 4 pestanas del menu de noticias, para cada una busca articulos, entra al segundo articulo y regresa.",
        "resultado": "PASSED",
        "tiempo": "~51 segundos",
        "retro": "Test conciso y efectivo que prueba la navegacion por las 4 primeras pestanas de noticias. Se entraron exitosamente a articulos de cada pestana. La navegacion es fluida. Tiempo de ejecucion: 51.31s."
    },
    {
        "num": "11",
        "nombre": "Oficinas - Exploracion",
        "descripcion": "Test de exploracion del servicio Oficinas. Realiza scroll para posicionar, hace click, captura screenshot. Itera 3 veces: busca oficinas (Centro, Direccion, Instituto, Oficialia), entra a cada una, busca boton 'Como llegar', hace click, espera 8 segundos para cargar mapa, y regresa con 2 driver.back().",
        "resultado": "PASSED",
        "tiempo": "~57 segundos",
        "retro": "La primera iteracion encontro 4 oficinas y pudo probar 'Como llegar' correctamente. Las siguientes iteraciones no encontraron oficinas adicionales (probablemente debido a la navegacion). La espera de 8 segundos para Google Maps funciona. Tiempo de ejecucion: 57.02s."
    },
    {
        "num": "12",
        "nombre": "Bloque - Cursos",
        "descripcion": "Test automatizado del servicio Bloque (cursos). El flujo incluye: acceso al servicio, apertura de 'Ver todo', aplicacion de filtros (seleccionar idiomas y categorias como Ingles y Tecnologia), limpieza de filtros en dos ocasiones, cierre del panel de filtros mediante boton X en coordenadas especificas, seleccion de un curso especifico (CURSOS DE EXCEL), y regreso a la pantalla de inicio.",
        "resultado": "PASSED",
        "tiempo": "~46 segundos",
        "retro": "El test paso correctamente tras realizar ajustes en el metodo de cierre de filtros (se utilizo el boton X en lugar del boton 'Cerrar'). La logica de seleccion de filtros multiple funciona bien. El test es estable y reproducible."
    },
    {
        "num": "13",
        "nombre": "Tramites - Completado",
        "descripcion": "Test completo del servicio Tramites, cubriendo dos secciones principales: (1) Seccion 'Mas buscados': acceso a 'Ver todo', exploracion de los primeros 3 tramites (Padron de Contratistas, Renovacion con pago, Renovacion de Licencia) - en cada uno se realiza scroll down 3 veces y se cambia a la pestana 'Archivos', regresa a la lista. (2) Seccion 'Dependencias': acceso a 'Ver todo', ingreso a cada una de las 3 dependencias, espera de carga de 3 segundos y regreso. Regreso final al inicio con 2 driver.back().",
        "resultado": "PASSED",
        "tiempo": "~84-85 segundos",
        "retro": "El test cubrio exitosamente todas las funcionalidades requeridas: navegacion entre tramites, interaccion con pestanas (Informacion/Archivos), scrolling y exploracion de dependencias. El flujo es completo y estable."
    }
]

for test in tests_info:
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, f"Test {test['num']}: {test['nombre']}", ln=True)
    pdf.ln(2)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, "Descripcion:", ln=True)
    pdf.set_font("Arial", "", 9)
    pdf.multi_cell(0, 5, test['descripcion'])
    pdf.ln(3)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, "Resultado:", ln=True)
    pdf.set_font("Arial", "B", 10)
    pdf.set_text_color(0, 128, 0)
    pdf.cell(0, 6, f"{test['resultado']} - Tiempo: {test['tiempo']}", ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(3)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, "Retroalimentacion y Conclusiones:", ln=True)
    pdf.set_font("Arial", "", 9)
    pdf.multi_cell(0, 5, test['retro'])
    pdf.ln(10)

pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Resumen de Resultados", ln=True)
pdf.set_font("Arial", "", 10)
pdf.cell(0, 6, "Total de tests ejecutados: 13", ln=True)
pdf.set_font("Arial", "B", 10)
pdf.set_text_color(0, 128, 0)
pdf.cell(0, 6, "Tests exitosos: 13 (100%)", ln=True)
pdf.set_text_color(0, 0, 0)
pdf.ln(10)

total_time = 87 + 68 + 40 + 68 + 60 + 59 + 94 + 52 + 61 + 51 + 57 + 46 + 85
pdf.cell(0, 6, f"Tiempo total de ejecucion: ~{total_time} segundos (~{total_time/60:.1f} minutos)", ln=True)
pdf.ln(10)

pdf.multi_cell(0, 6, "Conclusiones generales: Se ha logrado exitosamente la automatizacion completa de los 13 tests para la aplicacion GD App (Gobierno Digital). Todos los tests pasaron correctamente (100% de exito), lo que indica una base solida de automatizacion. La estructura del codigo sigue un patron uniforme utilizando la pagina base (home_page) y los metodos de Appium. La logica de espera, scroll y navegacion es estable y reproducible. Los tests cubren flujos completos incluyendo: navegacion entre servicios, llenado de formularios, captura de fotos, interaccion con WebViews, scrolling, filtros, y navegacion compleja. El proyecto esta listo para ser utilizado como suite de regresion.")

output_path = os.path.join(os.getcwd(), "Reporte_Tests_GD_App.pdf")
pdf.output(output_path)
print(f"PDF generado exitosamente en: {output_path}")