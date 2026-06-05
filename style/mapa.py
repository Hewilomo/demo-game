def mapa():
    linea_horizontal = '-' * 10
    linea_vertical = '|' + ' ' * 8 + '|'  # '|        |'
    
    mapa_completo = f"""
{linea_horizontal}
{linea_vertical}
{linea_vertical}
{linea_vertical}
{linea_vertical}
{linea_vertical}
{linea_horizontal}
"""
    return mapa_completo