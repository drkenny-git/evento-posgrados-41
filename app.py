from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
from datetime import datetime
import os
from pathlib import Path

app = Flask(__name__)

# Archivo Excel para guardar los registros
EXCEL_FILE = 'registros_asistencia.xlsx'

# Lista de programas de maestría - EDITA ESTA LISTA CON TUS PROGRAMAS
PROGRAMAS = {
    'director1': 'Maestría en Comercio Exterior y Gestión Logística',
    'director2': 'Maestría en Administración de Empresas: Mención en Innovación y Dirección Estratégica',
    'director3': 'Maestría en Gerencia Tributaria',
    'director4': 'Maestría en Transformación Digital e Innovación',
    'director5': 'Maestría en Gestión del Talento Humano',
    'director6': 'Maestría en Gestión de la Calidad de la Información y Documentación',
    'director7': 'Maestría en Gestión de Proyectos',
    'director8': 'Maestría en Producción y Operaciones Industriales',
    'director9': 'Maestría en Seguridad Salud e Higiene Industrial',
    'director10': 'Maestría en Diseño, Desarrollo y Gestión de Productos',
    'director11': 'Maestría en Ingeniería Mecánica',
    'director12': 'Maestría en Ingeniería Automotriz con mención en negocios automotrices',
    'director13': 'Especialización Sistemas Fotovoltaicos',
    'director14': 'Maestría en Electricidad',
    'director15': 'Maestría en Automatización para la Industria 4.0',
    'director16': 'Maestría en Software',
    'director17': 'Maestría en Construcción de Estructuras Sismorresistentes',
    'director18': 'Maestría en Sistemas Hidráulicos Urbanos de Abastecimiento y Protección',
    'director19': 'Maestría en Vialidad y Transporte',
    'director20': 'Maestría en Analítica de datos',
    'director21': 'Especialización en Visualización de datos',
    'director22': 'Maestría en Sistemas de Información Geográfica',
    'director23': 'Maestría en Ingeniería Biomédica',
    'director24': 'Maestría en Seguridad de la Información',
    'director25': 'Maestría en Recursos Naturales Renovables',
    'director26': 'Maestría en Agroecología',
    'director27': 'Maestría en Productos Farmacéuticos Naturales',
    'director28': 'Maestría en Biotecnología Molecular',
    'director29': 'Maestría en Gestión de la Calidad de la Leche y Derivados',
    'director30': 'Maestría en Gestión Ambiental y Ecoinnovación',
    'director31': 'Maestría en Actividad Física, mención entrenamiento deportivo',
    'director32': 'Maestría en Gestión Cultural',
    'director33': 'Maestría en Antropología',
    'director34': 'Maestría en Filosofía, mención ética, política y sociedad',
    'director35': 'Maestría en Psicología con mención en: Niñez adolescencia y Diversidad',
    'director36': 'Maestría en Desarrollo Local',
    'director37': 'Maestría en Educación Especial',
    'director38': 'Maestría en Innovación en Educación',
    'director39': 'Maestría en Tecnologías de la Información y Comunicación para la Educación',
    'director40': 'Maestría en Educación Intercultural Bilingüe',
    'director41': 'Maestría en Intervención Psicopedagógica en Educación Infantil',
    'director42': 'Maestría en Neuroeducación',
    'director43': 'Maestría en Pedagogía de la enseñanza religiosa',
    'director44': 'Maestría en Educación con mención en Desarrollo del Pensamiento',
}


def inicializar_excel():
    """Crea el archivo Excel si no existe"""
    if not os.path.exists(EXCEL_FILE):
        df = pd.DataFrame(columns=['Programa', 'Registro', 'Email'])
        df.to_excel(EXCEL_FILE, index=False)


def registrar_asistencia(programa, email=None):
    """Registra la asistencia en el archivo Excel"""
    inicializar_excel()

    # Leer el archivo actual
    df = pd.read_excel(EXCEL_FILE)

    # Crear nuevo registro
    nuevo_registro = {
        'Programa': programa,
        'Registro': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Email': email if email else 'No proporcionado'
    }

    # Agregar el nuevo registro
    df = pd.concat([df, pd.DataFrame([nuevo_registro])], ignore_index=True)

    # Guardar en Excel
    df.to_excel(EXCEL_FILE, index=False)


@app.route('/')
def index():
    """Página de inicio - lista todos los links disponibles"""
    return render_template('index.html', programas=PROGRAMAS)


@app.route('/<director_id>')
def registro_director(director_id):
    """Página de registro para cada director"""
    if director_id not in PROGRAMAS:
        return "Link no válido", 404

    programa = PROGRAMAS[director_id]

    # Registrar la visita automáticamente (sin email)
    registrar_asistencia(programa)

    return render_template('registro.html', programa=programa, director_id=director_id)


@app.route('/api/guardar_email', methods=['POST'])
def guardar_email():
    """API para guardar el email cuando el estudiante lo proporciona"""
    data = request.get_json()
    director_id = data.get('director_id')
    email = data.get('email', '').strip()

    if director_id not in PROGRAMAS:
        return jsonify({'error': 'Director no válido'}), 400

    if email:
        programa = PROGRAMAS[director_id]
        registrar_asistencia(programa, email)
        return jsonify({'success': True, 'message': 'Email registrado correctamente'})

    return jsonify({'error': 'Email no proporcionado'}), 400


@app.route('/directores')
def links_directores():
    """Página para que TODOS los directores vean y copien sus links"""
    return render_template('links_directores.html', programas=PROGRAMAS)


@app.route('/admin/descargar')
def descargar_registros():
    """Descarga el archivo Excel con todos los registros"""
    if os.path.exists(EXCEL_FILE):
        return send_file(EXCEL_FILE, as_attachment=True,
                         download_name=f'registros_asistencia_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx')
    return "No hay registros disponibles", 404


@app.route('/admin/estadisticas')
def estadisticas():
    """Muestra estadísticas de asistencia"""
    if not os.path.exists(EXCEL_FILE):
        return render_template('estadisticas.html', stats=None)

    df = pd.read_excel(EXCEL_FILE)

    # Calcular estadísticas
    stats = {
        'total_registros': len(df),
        'con_email': len(df[df['Email'] != 'No proporcionado']),
        'sin_email': len(df[df['Email'] == 'No proporcionado']),
        'por_programa': df['Programa'].value_counts().to_dict()
    }

    return render_template('estadisticas.html', stats=stats)


if __name__ == '__main__':
    inicializar_excel()
    # Para desarrollo local
    app.run(debug=True, host='0.0.0.0', port=5000)
