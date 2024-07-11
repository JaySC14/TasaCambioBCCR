# TasaCambioBCCR

## Descripción
Aplicación web en Flask que consulte el tipo  de cambio de compra y venta del Banco Central de Costa  Rica (BCCR) para una fecha específica, utilizando servicios  web SOAP. La aplicación debe permitir al usuario  seleccionar una fecha y mostrar los resultados redondeados a dos decimales con una interfaz atractiva.

## Instalación
Para configurar y ejecutar este proyecto localmente, sigue estos pasos:

1. **Clona** este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/JaySC14/TasaCambioBCCR.git
   cd TasaCambioBCCR

2. **Crea y Activa** un entorno virtual
py -m venv venv
source venv/Script/activate

3. **Instala** las dependencias
-pip install Flask
-pip install Zeep
-pip install lxml
-pip install matplotlib

Con estos pasos, los desarrolladores podrán clonar tu repositorio directamente desde GitHub y seguir instrucciones detalladas para configurar y ejecutar tu proyecto Flask en sus propias máquinas.

## Uso

1. Ejecuta la aplicación run.py

2. Abre tu navegador web y accede a http://localhost:5000.

3. En la aplicación, podrás:

- Seleccionar una fecha para consultar las tasas de cambio del Banco Central de Costa Rica.
- Ver las tasas de cambio de compra y venta para esa fecha.
- Generar un gráfico dinámico que muestra las tasas de cambio visualmente.

4. A continuación se muestra un ejemplo básico de cómo interactuar con la aplicación:

- Selecciona la fecha "2024-07-11".
- Haz click en el botón "Consultar tasas".
- Verás las tasas de compra y venta para esa fecha.
- Veras el titulo de "Generar Reporte"
- Haz click en el boton "Semanal","Mensual","Anual" segun tu necesidad
- El gráfico dinámico se actualizará automáticamente con los datos de la fecha seleccionada.
- ¡Explora las funcionalidades y disfruta utilizando la aplicación!

Si encuentras algún problema o deseas sugerir mejoras, no dudes en contactarme.

## Contribución
¡Bienvenido a contribuir a este proyecto! Agradecemos cualquier contribución que desees hacer para mejorar este proyecto.

Para contribuir, sigue estos pasos:

1. **Forkea** el repositorio en GitHub.
2. **Crea una rama** para tu contribución (`git checkout -b feature/nueva-funcionalidad`).
3. **Realiza tus cambios** y asegúrate de que el código siga las guías de estilo.
4. **Haz commit** de tus cambios (`git commit -am 'Agrega nueva funcionalidad'`).
5. **Envía tu Pull Request** explicando tus cambios y por qué deberían ser aceptados.

Agradecemos tu interés y esfuerzo en mejorar este proyecto. ¡Esperamos ver tus contribuciones!

## Licencia
Este proyecto está disponible bajo la [Licencia MIT](https://opensource.org/licenses/MIT). Ver `LICENSE` para más información.

## Contacto
Jason Sanabria Carvajal 
- jasonsanabria1409@gmail.com

## Notas Importantes

- A la hora de generar los reportes, estos se tomarán en cuenta desde el día actual hasta el inicio de ese mismo año, mes o semana respectivamente.
- Los reportes generados se almacenarán en la carpeta `app/static/reportes/` en formato .PNG.
- No se podrá seleccionar una fecha posterior al día actual a la hora de hacer las consultas de tasas de cambio ni se tomarán en cuenta en los reportes.

Estas restricciones aseguran que las consultas y los reportes estén basados en datos históricos válidos hasta el día actual, evitando errores debido a fechas futuras.

Para más detalles sobre cómo utilizar y configurar la aplicación, consulta la sección de [Uso](#uso) en este README.


Para generar un reporte:
1. Asegúrate de que la aplicación esté ejecutándose localmente según las instrucciones de la sección de Uso.
2. Accede a la funcionalidad de generación de reportes desde la interfaz de usuario de la aplicación.
3. Selecciona el tipo de reporte (por año, mes o semana).
4. El reporte se generará automáticamente y se guardará en la carpeta mencionada.

¡Explora esta funcionalidad y aprovecha al máximo los reportes generados por la aplicación!

Si tienes alguna pregunta o necesitas asistencia adicional, no dudes en [contactarme](#contacto).
