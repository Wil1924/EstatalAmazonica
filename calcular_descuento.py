# Wilman Tasinchano

def calcular_descuento(monto_total, porcentaje_descuento=20):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.
    
    Args:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (float, optional): El porcentaje de descuento a aplicar.
            Por defecto es 20.
    
    Returns:
        float: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamadas a la función desde el programa principal
monto_compra_1 = 100
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1
print("Monto total de la compra: $", monto_compra_1)
print("Descuento aplicado: $", descuento_1)
print("Monto final a pagar después del descuento: $", monto_final_1)

monto_compra_2 = 200
descuento_2 = calcular_descuento(monto_compra_2)
monto_final_2 = monto_compra_2 - descuento_2
print("\nMonto total de la compra: $", monto_compra_2)
print("Porcentaje de descuento aplicado: 20%")
print("Descuento aplicado: $", descuento_2)
print("Monto final a pagar después del descuento: $", monto_final_2)
