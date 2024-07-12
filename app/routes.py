from flask import Flask, render_template, request, current_app as app
from datetime import date, datetime
from business import BusinessLogic

@app.route('/', methods=['GET', 'POST'])
def home():
    fecha_actual = date.today()
    fecha_seleccionada = None
    error = None
    tipo_cambio_compra = None
    tipo_cambio_venta = None

    if request.method == 'POST':
        fecha_seleccionada_str = request.form.get('fecha')
        if not fecha_seleccionada_str:
            error = "Debe seleccionar una fecha primero"
        else:
            fecha_seleccionada = datetime.strptime(fecha_seleccionada_str, '%Y-%m-%d').date()

            if fecha_seleccionada > fecha_actual:
                error = f"No puedes seleccionar una fecha posterior a {fecha_actual}"
            else:
                business_logic = BusinessLogic()
                fecha_seleccionada_str = fecha_seleccionada.strftime('%d/%m/%Y')
                try:
                    tipo_cambio = business_logic.obtener_tipo_cambio(fecha_seleccionada_str)
                    tipo_cambio_compra = tipo_cambio.tipo_cambio_compra
                    tipo_cambio_venta = tipo_cambio.tipo_cambio_venta
                except ConnectionError:
                    error = "Error de conexión al servicio de tipo de cambio"
                except ValueError:
                    error = "Error en el formato de fecha"
                except Exception as e:
                    error = f"Ha ocurrido un error: {str(e)}"
    return render_template('index.html', error=error, fecha_max=fecha_actual, tipo_cambio_compra=tipo_cambio_compra, tipo_cambio_venta=tipo_cambio_venta, fecha=fecha_seleccionada)

@app.route('/generar_reporte', methods=['POST'])
def generate_report():
    array_compra = []
    array_venta = []
    business_logic = BusinessLogic()
    report_type = request.form.get('tipo_reporte')

    if report_type == 'semanal':
        fechas = business_logic.ultima_semana()
    elif report_type == 'mensual':
        fechas = business_logic.ultimo_mes()
    elif report_type == 'anual':
        fechas = business_logic.ultimo_año()
    else:
        return "Tipo de reporte no válido"

    for fecha in fechas:
        tipo_cambio = business_logic.obtener_tipo_cambio(fecha)
        array_compra.append(tipo_cambio.tipo_cambio_compra)
        array_venta.append(tipo_cambio.tipo_cambio_venta)
    
    url_imagen = business_logic.generar_grafico(report_type, fechas, array_compra, array_venta)
    print(url_imagen)
    return render_template(f'grafico_{report_type}.html', url_imagen=url_imagen)



if __name__ == "__main__":
    app.run(debug=True)