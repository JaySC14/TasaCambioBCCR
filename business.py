from data_access import BCCR 
from entities import TipoCambio
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
import os

class BusinessLogic:
    def __init__(self):
        self.bccr = BCCR()

    def consultar_tipo_cambio(self, fecha):
        try:
            tipo_cambio = self.bccr.obtener_tipo_cambio(fecha)
            tipo_cambio.tipo_cambio_compra = round(float(tipo_cambio.tipo_cambio_compra), 2)
            tipo_cambio.tipo_cambio_venta = round(float(tipo_cambio.tipo_cambio_venta), 2)
            return tipo_cambio
        except Exception as e:
            raise RuntimeError(f"Error al obtener los valores: {e}")
        
    def ultima_semana(self):
        hoy = datetime.today().date()
        inicio_semana = hoy - timedelta(days=hoy.weekday())
        fechas = []

        fecha_actual = inicio_semana
        while fecha_actual <= hoy:
            fechas.append(fecha_actual.strftime("%d/%m/%Y"))
            fecha_actual += timedelta(days=1)
        return fechas
    
    def ultimo_mes(self):
        hoy = datetime.today().date()
        primer_dia_del_mes = hoy.replace(day=1)
        fechas = []

        fecha_actual = primer_dia_del_mes
        while fecha_actual <= hoy:
            fechas.append(fecha_actual.strftime("%d/%m/%Y"))
            fecha_actual += timedelta(days=1)
        return fechas
    
    def ultimo_año(self):
        hoy = datetime.today()
        primer_dia_del_año = hoy.replace(month=1, day=1)
        fechas = []

        fecha_actual = primer_dia_del_año
        while fecha_actual <= hoy:
            fechas.append(fecha_actual.strftime("%d/%m/%Y"))
            fecha_actual += timedelta(days=1)
        return fechas
    
    def verificar_carpeta_reportes(self):
        carpeta_reportes = 'app/static/reportes'
        if not os.path.exists(carpeta_reportes):
            os.makedirs(carpeta_reportes)
            print(f'Carpeta {carpeta_reportes} creada exitosamente.')
        
    def generar_grafico(self,tipo_reporte, fechas, array_compra, array_venta):
        self.verificar_carpeta_reportes()
        fecha = datetime.today()
        fecha_str = fecha.strftime("%Y-%m-%d_%H-%M-%S")
        plt.plot(fechas, array_compra, marker='o', label='Compra') 
        plt.plot(fechas, array_venta, marker='o', label='Venta')  
        plt.xlabel('Fecha') 
        plt.xticks(rotation=45)
        plt.title('Tasa de Cambio')
        plt.legend() 
        ruta_grafico = f'reporte_{tipo_reporte}_{fecha_str}.png'
        plt.savefig(f'app/static/reportes/reporte_{tipo_reporte}_{fecha_str}.png')
        plt.close()
        return ruta_grafico