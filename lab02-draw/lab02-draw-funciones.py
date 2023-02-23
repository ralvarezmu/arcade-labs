import arcade

def dibujar_arbol() :
    """Dibuja un arbol"""
    altura = 60
    base = 20
    centrado_derecha = 100
    centrado_izquierda = 320

    return (arcade.draw_rectangle_filled(centrado_derecha, centrado_izquierda, base, altura, arcade.csscolor.SIENNA))

def dibujar_sol() :
    """Dibuja un sol"""
    diametro = 50
    radio = diametro/2
    centrado_derecha = 500
    centrado_izquierda = 500

    return(arcade.draw_circle_filled(centrado_derecha, centrado_izquierda, radio, arcade.csscolor.YELLOW))

def dibujar_hojas() :
    """Dibuja las hojas del arbol"""
    diametro = 60
    centrado_derecha = 100
    centrado_izquierda = 350

    return(arcade.draw_circle_filled(centrado_derecha, centrado_izquierda, diametro/2, arcade.csscolor.GREEN))

def dibujar_messi() :
    """Dibuja a Messi"""

    # Cabeza de Messi
    diametro = 60
    centrado_derecha_cabeza = 200
    centrado_izquierda_cabeza = 420

    # Cuerpo de Messi
    altura = 60
    base = 20
    centrado_derecha_c = 200
    centrado_izquierda_c = 410

    # Dibujar piernas de Messi
    # Se dibuja con lineas

    return(arcade.draw_rectangle_filled(centrado_derecha_c, centrado_izquierda_c, base, altura, arcade.csscolor.MAROON))




arcade.open_window(600, 600, "hola")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

dibujar_arbol()

dibujar_sol()

dibujar_hojas()

dibujar_messi()

arcade.finish_render()


arcade.run()

