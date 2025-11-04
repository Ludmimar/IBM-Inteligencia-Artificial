"""
╔═══════════════════════════════════════════════════════════════╗
║          TIENDA AURELION - SISTEMA DE GESTIÓN                 ║
║          Sistema de Inventario Interactivo                    ║
║          Sprint 1 - Introducción a la IA - IBM                ║
║                                                               ║
║          Autor: Martos Ludmila                                ║
║          DNI: 34811650                                        ║
╚═══════════════════════════════════════════════════════════════╝

Programa interactivo para gestionar el inventario de la Tienda Aurelion.
Permite consultar, buscar, agregar y actualizar productos de manera eficiente.
"""

import csv
import os
from typing import List, Dict, Optional

# Constantes
# Detectar automáticamente la ruta correcta del CSV
def obtener_ruta_csv():
    """Obtiene la ruta correcta del CSV independientemente de desde dónde se ejecute."""
    rutas_posibles = [
        "../datos/tienda_aurelion.csv",  # Ejecutando desde programas/
        "datos/tienda_aurelion.csv",      # Ejecutando desde Sprint-1/
        "Sprint-1/datos/tienda_aurelion.csv"  # Ejecutando desde raíz del repo
    ]
    for ruta in rutas_posibles:
        if os.path.exists(ruta):
            return ruta
    return "../datos/tienda_aurelion.csv"  # Por defecto

ARCHIVO_CSV = obtener_ruta_csv()
UMBRAL_STOCK_BAJO = 20


def limpiar_pantalla():
    """Limpia la pantalla de la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_banner():
    """Muestra el banner principal de la aplicación."""
    print("\n" + "═" * 70)
    print("              ⚔️  TIENDA AURELION - SISTEMA DE GESTIÓN ⚔️")
    print("                   Inventario de Artículos Mágicos")
    print("═" * 70 + "\n")


def cargar_datos() -> List[Dict]:
    """
    Carga los datos del archivo CSV y los convierte en una lista de diccionarios.
    
    Returns:
        Lista de diccionarios donde cada diccionario representa un producto.
        Retorna lista vacía si hay error al cargar.
    """
    productos = []
    
    try:
        with open(ARCHIVO_CSV, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    # Convertir campos numéricos a enteros
                    fila['id'] = int(fila['id'])
                    fila['precio'] = int(fila['precio'])
                    fila['stock'] = int(fila['stock'])
                    productos.append(fila)
                except (ValueError, KeyError) as e:
                    print(f"⚠️  Advertencia: Error al procesar fila: {e}")
                    continue
        
        print(f"✅ Se cargaron {len(productos)} productos correctamente.\n")
        return productos
    
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{ARCHIVO_CSV}'")
        print("   Por favor, asegúrate de que el archivo existe en el directorio actual.\n")
        return []
    except Exception as e:
        print(f"❌ Error inesperado al cargar datos: {e}\n")
        return []


def guardar_datos(productos: List[Dict]) -> bool:
    """
    Guarda la lista de productos en el archivo CSV.
    
    Args:
        productos: Lista de diccionarios con los productos.
    
    Returns:
        True si se guardó correctamente, False en caso contrario.
    """
    try:
        if not productos:
            print("⚠️  No hay productos para guardar.")
            return False
        
        # Obtener nombres de columnas del primer producto
        columnas = list(productos[0].keys())
        
        with open(ARCHIVO_CSV, 'w', encoding='utf-8', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(productos)
        
        print("✅ Datos guardados correctamente.\n")
        return True
    
    except Exception as e:
        print(f"❌ Error al guardar datos: {e}\n")
        return False


def validar_entrada_numerica(mensaje: str, minimo: int = 0, maximo: Optional[int] = None) -> int:
    """
    Solicita al usuario un número y valida que esté en el rango especificado.
    
    Args:
        mensaje: Mensaje a mostrar al usuario.
        minimo: Valor mínimo permitido.
        maximo: Valor máximo permitido (opcional).
    
    Returns:
        Número entero validado.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"⚠️  El valor debe ser mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"⚠️  El valor debe ser menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("⚠️  Por favor, ingresa un número válido.")


def mostrar_producto(producto: Dict, mostrar_indice: bool = False, indice: int = 0):
    """
    Muestra la información de un producto de forma formateada.
    
    Args:
        producto: Diccionario con los datos del producto.
        mostrar_indice: Si True, muestra el número de índice.
        indice: Número de índice a mostrar.
    """
    if mostrar_indice:
        print(f"\n{'─' * 70}")
        print(f"  Producto #{indice + 1}")
    print(f"{'─' * 70}")
    print(f"  🆔 ID:          {producto['id']}")
    print(f"  📦 Nombre:      {producto['nombre']}")
    print(f"  🏷️  Categoría:   {producto['categoria']}")
    print(f"  💰 Precio:      {producto['precio']} monedas de oro")
    print(f"  📊 Stock:       {producto['stock']} unidades", end="")
    
    # Alerta de stock bajo
    if producto['stock'] <= UMBRAL_STOCK_BAJO:
        print(" ⚠️  ¡STOCK BAJO!")
    else:
        print()
    
    print(f"  📝 Descripción: {producto['descripcion']}")
    print(f"  🏪 Proveedor:   {producto['proveedor']}")
    print(f"{'─' * 70}")


def listar_todos_productos(productos: List[Dict]):
    """Muestra todos los productos del inventario."""
    limpiar_pantalla()
    mostrar_banner()
    print("📋 LISTADO COMPLETO DE PRODUCTOS\n")
    
    if not productos:
        print("⚠️  No hay productos en el inventario.\n")
        return
    
    for i, producto in enumerate(productos):
        mostrar_producto(producto, mostrar_indice=True, indice=i)
    
    print(f"\n📊 Total de productos: {len(productos)}")


def buscar_por_categoria(productos: List[Dict]):
    """Busca y muestra productos de una categoría específica."""
    limpiar_pantalla()
    mostrar_banner()
    print("🏷️  BUSCAR POR CATEGORÍA\n")
    
    # Obtener categorías únicas
    categorias = sorted(set(p['categoria'] for p in productos))
    
    print("Categorías disponibles:")
    for i, cat in enumerate(categorias, 1):
        print(f"  {i}. {cat}")
    
    print(f"\n{'─' * 70}\n")
    categoria = input("Ingresa el nombre de la categoría: ").strip()
    
    # Buscar productos
    resultados = [p for p in productos if p['categoria'].lower() == categoria.lower()]
    
    if resultados:
        print(f"\n✅ Se encontraron {len(resultados)} producto(s) en la categoría '{categoria}':\n")
        for i, producto in enumerate(resultados):
            mostrar_producto(producto, mostrar_indice=True, indice=i)
    else:
        print(f"\n❌ No se encontraron productos en la categoría '{categoria}'.")


def buscar_por_id(productos: List[Dict]):
    """Busca un producto por su ID."""
    limpiar_pantalla()
    mostrar_banner()
    print("🆔 BUSCAR POR ID\n")
    
    id_buscar = validar_entrada_numerica("Ingresa el ID del producto: ", minimo=1)
    
    # Buscar producto
    for producto in productos:
        if producto['id'] == id_buscar:
            print("\n✅ Producto encontrado:\n")
            mostrar_producto(producto)
            return
    
    print(f"\n❌ No se encontró ningún producto con ID {id_buscar}.")


def buscar_por_nombre(productos: List[Dict]):
    """Busca productos por nombre (búsqueda parcial)."""
    limpiar_pantalla()
    mostrar_banner()
    print("📦 BUSCAR POR NOMBRE\n")
    
    nombre = input("Ingresa el nombre (o parte del nombre) a buscar: ").strip().lower()
    
    if not nombre:
        print("⚠️  Debes ingresar un nombre para buscar.")
        return
    
    # Buscar productos que contengan el texto en el nombre
    resultados = [p for p in productos if nombre in p['nombre'].lower()]
    
    if resultados:
        print(f"\n✅ Se encontraron {len(resultados)} producto(s):\n")
        for i, producto in enumerate(resultados):
            mostrar_producto(producto, mostrar_indice=True, indice=i)
    else:
        print(f"\n❌ No se encontraron productos con '{nombre}' en el nombre.")


def buscar_por_rango_precios(productos: List[Dict]):
    """Busca productos dentro de un rango de precios."""
    limpiar_pantalla()
    mostrar_banner()
    print("💰 BUSCAR POR RANGO DE PRECIOS\n")
    
    precio_min = validar_entrada_numerica("Ingresa el precio mínimo: ", minimo=0)
    precio_max = validar_entrada_numerica("Ingresa el precio máximo: ", minimo=precio_min)
    
    # Buscar productos en el rango
    resultados = [p for p in productos if precio_min <= p['precio'] <= precio_max]
    
    if resultados:
        print(f"\n✅ Se encontraron {len(resultados)} producto(s) entre {precio_min} y {precio_max} monedas:\n")
        for i, producto in enumerate(resultados):
            mostrar_producto(producto, mostrar_indice=True, indice=i)
    else:
        print(f"\n❌ No se encontraron productos en ese rango de precios.")


def productos_bajo_stock(productos: List[Dict]):
    """Muestra productos con stock bajo que necesitan reabastecimiento."""
    limpiar_pantalla()
    mostrar_banner()
    print("⚠️  PRODUCTOS CON BAJO STOCK\n")
    
    print(f"Umbral de stock bajo: {UMBRAL_STOCK_BAJO} unidades\n")
    
    # Filtrar productos con stock bajo
    resultados = [p for p in productos if p['stock'] <= UMBRAL_STOCK_BAJO]
    
    if resultados:
        print(f"⚠️  Se encontraron {len(resultados)} producto(s) con stock bajo:\n")
        for i, producto in enumerate(sorted(resultados, key=lambda x: x['stock'])):
            mostrar_producto(producto, mostrar_indice=True, indice=i)
        print(f"\n💡 Sugerencia: Contacta a los proveedores para reabastecer estos productos.")
    else:
        print("✅ ¡Excelente! Todos los productos tienen stock adecuado.")


def estadisticas_inventario(productos: List[Dict]):
    """Muestra estadísticas generales del inventario."""
    limpiar_pantalla()
    mostrar_banner()
    print("📊 ESTADÍSTICAS DEL INVENTARIO\n")
    
    if not productos:
        print("⚠️  No hay productos para analizar.\n")
        return
    
    # Calcular estadísticas
    total_productos = len(productos)
    stock_total = sum(p['stock'] for p in productos)
    valor_total = sum(p['precio'] * p['stock'] for p in productos)
    categorias_unicas = len(set(p['categoria'] for p in productos))
    proveedores_unicos = len(set(p['proveedor'] for p in productos))
    
    # Producto más caro y más barato
    producto_mas_caro = max(productos, key=lambda x: x['precio'])
    producto_mas_barato = min(productos, key=lambda x: x['precio'])
    
    # Precio promedio
    precio_promedio = sum(p['precio'] for p in productos) / total_productos
    
    # Stock promedio
    stock_promedio = stock_total / total_productos
    
    # Productos por categoría
    productos_por_categoria = {}
    for producto in productos:
        cat = producto['categoria']
        productos_por_categoria[cat] = productos_por_categoria.get(cat, 0) + 1
    
    # Mostrar estadísticas
    print(f"{'═' * 70}")
    print("  ESTADÍSTICAS GENERALES")
    print(f"{'═' * 70}")
    print(f"  📦 Total de productos:        {total_productos}")
    print(f"  🏷️  Categorías únicas:         {categorias_unicas}")
    print(f"  🏪 Proveedores únicos:        {proveedores_unicos}")
    print(f"  📊 Stock total:               {stock_total} unidades")
    print(f"  💰 Valor total inventario:    {valor_total:,} monedas de oro")
    print(f"{'─' * 70}")
    print(f"  💵 Precio promedio:           {precio_promedio:.2f} monedas")
    print(f"  📈 Stock promedio:            {stock_promedio:.2f} unidades")
    print(f"{'═' * 70}\n")
    
    print(f"{'═' * 70}")
    print("  PRODUCTOS DESTACADOS")
    print(f"{'═' * 70}")
    print(f"  💎 Producto más caro:")
    print(f"     • {producto_mas_caro['nombre']}")
    print(f"     • Precio: {producto_mas_caro['precio']} monedas")
    print(f"{'─' * 70}")
    print(f"  🎯 Producto más económico:")
    print(f"     • {producto_mas_barato['nombre']}")
    print(f"     • Precio: {producto_mas_barato['precio']} monedas")
    print(f"{'═' * 70}\n")
    
    print(f"{'═' * 70}")
    print("  PRODUCTOS POR CATEGORÍA")
    print(f"{'═' * 70}")
    for cat, cantidad in sorted(productos_por_categoria.items(), key=lambda x: x[1], reverse=True):
        barra = "█" * (cantidad * 3)
        print(f"  {cat:20s} │ {barra} {cantidad}")
    print(f"{'═' * 70}")


def buscar_por_proveedor(productos: List[Dict]):
    """Busca productos de un proveedor específico."""
    limpiar_pantalla()
    mostrar_banner()
    print("🏪 BUSCAR POR PROVEEDOR\n")
    
    # Obtener proveedores únicos
    proveedores = sorted(set(p['proveedor'] for p in productos))
    
    print("Proveedores disponibles:")
    for i, prov in enumerate(proveedores, 1):
        print(f"  {i}. {prov}")
    
    print(f"\n{'─' * 70}\n")
    proveedor = input("Ingresa el nombre del proveedor: ").strip()
    
    # Buscar productos
    resultados = [p for p in productos if p['proveedor'].lower() == proveedor.lower()]
    
    if resultados:
        print(f"\n✅ Se encontraron {len(resultados)} producto(s) del proveedor '{proveedor}':\n")
        for i, producto in enumerate(resultados):
            mostrar_producto(producto, mostrar_indice=True, indice=i)
        
        # Estadísticas del proveedor
        stock_total = sum(p['stock'] for p in resultados)
        valor_total = sum(p['precio'] * p['stock'] for p in resultados)
        print(f"\n{'═' * 70}")
        print(f"  📊 Estadísticas del proveedor '{proveedor}':")
        print(f"  • Total productos: {len(resultados)}")
        print(f"  • Stock total: {stock_total} unidades")
        print(f"  • Valor total: {valor_total:,} monedas de oro")
        print(f"{'═' * 70}")
    else:
        print(f"\n❌ No se encontraron productos del proveedor '{proveedor}'.")


def agregar_producto(productos: List[Dict]):
    """Permite agregar un nuevo producto al inventario."""
    limpiar_pantalla()
    mostrar_banner()
    print("➕ AGREGAR NUEVO PRODUCTO\n")
    
    print(f"{'═' * 70}\n")
    
    # Generar nuevo ID
    nuevo_id = max(p['id'] for p in productos) + 1 if productos else 1
    
    # Solicitar datos del nuevo producto
    print(f"🆔 ID asignado automáticamente: {nuevo_id}\n")
    
    nombre = input("📦 Nombre del producto: ").strip()
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return
    
    # Mostrar categorías existentes
    categorias = sorted(set(p['categoria'] for p in productos))
    if categorias:
        print("\n🏷️  Categorías existentes:")
        for cat in categorias:
            print(f"   • {cat}")
    
    categoria = input("\n🏷️  Categoría: ").strip()
    if not categoria:
        print("❌ La categoría no puede estar vacía.")
        return
    
    precio = validar_entrada_numerica("💰 Precio (monedas de oro): ", minimo=1)
    stock = validar_entrada_numerica("📊 Stock inicial (unidades): ", minimo=0)
    
    descripcion = input("📝 Descripción: ").strip()
    if not descripcion:
        print("❌ La descripción no puede estar vacía.")
        return
    
    # Mostrar proveedores existentes
    proveedores = sorted(set(p['proveedor'] for p in productos))
    if proveedores:
        print("\n🏪 Proveedores existentes:")
        for prov in proveedores:
            print(f"   • {prov}")
    
    proveedor = input("\n🏪 Proveedor: ").strip()
    if not proveedor:
        print("❌ El proveedor no puede estar vacío.")
        return
    
    # Crear nuevo producto
    nuevo_producto = {
        'id': nuevo_id,
        'nombre': nombre,
        'categoria': categoria,
        'precio': precio,
        'stock': stock,
        'descripcion': descripcion,
        'proveedor': proveedor
    }
    
    # Confirmar antes de agregar
    print(f"\n{'═' * 70}")
    print("  CONFIRMAR NUEVO PRODUCTO")
    print(f"{'═' * 70}")
    mostrar_producto(nuevo_producto)
    
    confirmacion = input("\n¿Deseas agregar este producto? (s/n): ").strip().lower()
    
    if confirmacion == 's':
        productos.append(nuevo_producto)
        if guardar_datos(productos):
            print("✅ Producto agregado exitosamente al inventario.")
    else:
        print("❌ Operación cancelada. El producto no fue agregado.")


def actualizar_stock(productos: List[Dict]):
    """Permite actualizar el stock de un producto existente."""
    limpiar_pantalla()
    mostrar_banner()
    print("🔄 ACTUALIZAR STOCK DE PRODUCTO\n")
    
    id_buscar = validar_entrada_numerica("Ingresa el ID del producto: ", minimo=1)
    
    # Buscar producto
    producto_encontrado = None
    for producto in productos:
        if producto['id'] == id_buscar:
            producto_encontrado = producto
            break
    
    if not producto_encontrado:
        print(f"\n❌ No se encontró ningún producto con ID {id_buscar}.")
        return
    
    # Mostrar producto actual
    print("\n📦 Producto encontrado:\n")
    mostrar_producto(producto_encontrado)
    
    print(f"\n{'═' * 70}\n")
    print(f"Stock actual: {producto_encontrado['stock']} unidades\n")
    print("Opciones:")
    print("  1. Agregar stock (recibir mercancía)")
    print("  2. Reducir stock (venta)")
    print("  3. Establecer stock nuevo (inventario)")
    print("  4. Cancelar")
    
    opcion = validar_entrada_numerica("\nSelecciona una opción: ", minimo=1, maximo=4)
    
    if opcion == 4:
        print("❌ Operación cancelada.")
        return
    
    if opcion == 1:
        cantidad = validar_entrada_numerica("\nCantidad a agregar: ", minimo=1)
        nuevo_stock = producto_encontrado['stock'] + cantidad
        accion = f"agregaron {cantidad} unidades"
    elif opcion == 2:
        cantidad = validar_entrada_numerica(
            "\nCantidad a reducir: ", 
            minimo=1, 
            maximo=producto_encontrado['stock']
        )
        nuevo_stock = producto_encontrado['stock'] - cantidad
        accion = f"redujeron {cantidad} unidades"
    else:  # opcion == 3
        nuevo_stock = validar_entrada_numerica("\nNuevo stock: ", minimo=0)
        accion = f"estableció en {nuevo_stock} unidades"
    
    # Confirmar actualización
    print(f"\n{'═' * 70}")
    print(f"  Stock actual:  {producto_encontrado['stock']} unidades")
    print(f"  Stock nuevo:   {nuevo_stock} unidades")
    if nuevo_stock <= UMBRAL_STOCK_BAJO:
        print(f"  ⚠️  ADVERTENCIA: Stock bajo (≤ {UMBRAL_STOCK_BAJO})")
    print(f"{'═' * 70}")
    
    confirmacion = input("\n¿Confirmar actualización? (s/n): ").strip().lower()
    
    if confirmacion == 's':
        producto_encontrado['stock'] = nuevo_stock
        if guardar_datos(productos):
            print(f"✅ Stock actualizado exitosamente. Se {accion}.")
    else:
        print("❌ Operación cancelada. El stock no fue modificado.")


def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print("\n" + "╔" + "═" * 68 + "╗")
    print("║" + " " * 25 + "MENÚ PRINCIPAL" + " " * 29 + "║")
    print("╠" + "═" * 68 + "╣")
    print("║  🔍 CONSULTAS Y BÚSQUEDAS                                        ║")
    print("║     1. Listar todos los productos                               ║")
    print("║     2. Buscar por categoría                                     ║")
    print("║     3. Buscar por ID                                            ║")
    print("║     4. Buscar por nombre                                        ║")
    print("║     5. Buscar por rango de precios                              ║")
    print("║     6. Ver productos con bajo stock                             ║")
    print("║     7. Ver estadísticas del inventario                          ║")
    print("║     8. Buscar por proveedor                                     ║")
    print("╠" + "═" * 68 + "╣")
    print("║  ✏️  GESTIÓN DE INVENTARIO                                       ║")
    print("║     9. Agregar nuevo producto                                   ║")
    print("║    10. Actualizar stock de producto                             ║")
    print("╠" + "═" * 68 + "╣")
    print("║     0. Salir del sistema                                        ║")
    print("╚" + "═" * 68 + "╝\n")


def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input("\n📌 Presiona Enter para continuar...")


def main():
    """Función principal del programa."""
    limpiar_pantalla()
    mostrar_banner()
    
    print("Cargando datos del inventario...\n")
    productos = cargar_datos()
    
    if not productos:
        print("❌ No se pudieron cargar los productos. Verifica el archivo CSV.")
        return
    
    pausar()
    
    # Bucle principal del menú
    while True:
        limpiar_pantalla()
        mostrar_banner()
        mostrar_menu()
        
        opcion = validar_entrada_numerica("Selecciona una opción: ", minimo=0, maximo=10)
        
        if opcion == 0:
            limpiar_pantalla()
            mostrar_banner()
            print("╔" + "═" * 68 + "╗")
            print("║" + " " * 15 + "¡Gracias por usar Tienda Aurelion!" + " " * 18 + "║")
            print("║" + " " * 20 + "¡Que tengas un gran día! ⚔️" + " " * 21 + "║")
            print("╚" + "═" * 68 + "╝\n")
            break
        elif opcion == 1:
            listar_todos_productos(productos)
        elif opcion == 2:
            buscar_por_categoria(productos)
        elif opcion == 3:
            buscar_por_id(productos)
        elif opcion == 4:
            buscar_por_nombre(productos)
        elif opcion == 5:
            buscar_por_rango_precios(productos)
        elif opcion == 6:
            productos_bajo_stock(productos)
        elif opcion == 7:
            estadisticas_inventario(productos)
        elif opcion == 8:
            buscar_por_proveedor(productos)
        elif opcion == 9:
            agregar_producto(productos)
        elif opcion == 10:
            actualizar_stock(productos)
        
        pausar()


if __name__ == "__main__":
    main()

