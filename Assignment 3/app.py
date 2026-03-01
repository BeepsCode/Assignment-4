from flask import Flask, request, jsonify, render_template, redirect, url_for

# ... (tus listas iniciales productos_db = [] etc.) ...

# Ruta 1: Mostrar el formulario (GET)
@app.route('/nuevo_producto')
def formulario_producto():
    return render_template('nuevo_producto.html')

# Ruta 2: Recibir los datos del formulario (POST)
@app.route('/crear_producto_web', methods=['POST'])
def crear_producto_web():
    # IMPORTANTE: Cuando viene de un formulario HTML, usamos request.form 
    # en lugar de request.get_json()
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precio = float(request.form.get('precio')) # Convertimos a número
    moneda = request.form.get('moneda')
    stock = int(request.form.get('stock'))     # Convertimos a entero
    categoria = request.form.get('categoria')

    nuevo_prod = {
        "id": 100 + len(productos_db) + 1,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "moneda": moneda,
        "stock": stock,
        "categoria": categoria
    }
    
    productos_db.append(nuevo_prod)
    
    # Después de guardar, redirigimos al usuario a la lista de productos
    return redirect(url_for('ver_productos'))