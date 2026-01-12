import json 
import matplotlib.pyplot as plp
import numpy as np

def promedio(lista):
    return sum(lista) / len(lista)

def cajson(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

# Función para mostrar nombres y productos
def mostdata(mipdat):
    for mipyme in mipdat:
        print("Nombre:", mipyme["names"])
        for producto in mipyme["product"]:
            print(" -", producto["type"], ":", producto["brand"])
        print("___________________________")

# Función para crear lista de productos
def listpro(mipdat):
    productos = []
    for mipyme in mipdat:
        for producto in mipyme["product"]:
            productos.append([producto["type"], producto["brand"]])
    return productos

# Función para quitar repetidos
def elirep(lista):
    sin_repetidos = []
    for item in lista:
        if item not in sin_repetidos:
            sin_repetidos.append(item)
    return sin_repetidos
# Saca los elementos de listas en listas para mis funciones de mierda
def sacador(x):
    listita = []
    for i in x:
        for j in i:
            listita.append(j)
    return listita        
# Convertidor de dolares 
def conv_usd(produc_price):
    ult_val = prices[-1]
    cambio = float(ult_val)*float(produc_price)
    return cambio   
    
#Datos para el cambio de la moneda 
prices = []  
dias = []       
sticks = []  

tasa_json = cajson("TASA_eltoque.json")
datos = tasa_json["data"]

pos_act = 0
for tasita in datos:
    if tasita["data"]["dolar_today"] != None :
        precio = float(tasita["data"]["dolar_today"])
        dia = tasita["data"]["day"]
        mes = tasita["data"]["month"]
        
        prices.append(precio)
        dias.append(pos_act) 
        sticks.append(f"{dia}/{mes}")
        pos_act += 1

#Gráficos de comportamiento de la moneda
     
def tasa_de_cambio_big():
    plp.figure(figsize=(16, 7))
    plp.plot(dias[:35], prices[:35], "o-", color="#4C00FF", linewidth=3)
    plp.xticks(dias[:35], sticks[:35], rotation=45, ha="right")
    plp.title("Evolución Informal del Dólar en Cuba (Primeros 35 días)", fontsize=20)
    plp.xlabel("Fecha", fontsize=15)
    plp.ylabel("CUPxUSD", fontsize=15)
    plp.fill_between(dias[:35], prices[:35], alpha=0.2, color="#4C00FF")
    plp.grid(True)
    plp.show()
    
    plp.figure(figsize=(16, 7))
    plp.plot(dias[35:], prices[35:], "o-", color="#4C00FF", linewidth=3)
    plp.xticks(dias[35:], sticks[35:], rotation=45, ha="right")
    plp.title("Evolución Informal del Dólar en Cuba (Resto de días)", fontsize=20)
    plp.xlabel("Fecha", fontsize=15)
    plp.ylabel("CUPxUSD", fontsize=15)
    plp.fill_between(dias[35:], prices[35:], alpha=0.2, color="#4C00FF")
    plp.grid(True)
    plp.show()

def tasa_de_cambio():
    plp.figure(figsize=(16, 7))
    plp.plot(dias[:35], prices[:35], "o-", color="#4C00FF", linewidth=3)
    plp.xticks(dias[:35], sticks[:35], rotation=45, ha="right")
    plp.title("Evolución Informal del Dólar en Cuba (Primeros 35 días)", fontsize=20)
    plp.xlabel("Fecha", fontsize=15)
    plp.ylabel("CUPxUSD", fontsize=15)
    plp.grid(True)
    plp.show()
    
    plp.figure(figsize=(16, 7))
    plp.plot(dias[35:], prices[35:], "o-", color="#4C00FF", linewidth=3)
    plp.xticks(dias[35:], sticks[35:], rotation=45, ha="right")
    plp.title("Evolución Informal del Dólar en Cuba (Resto de días)", fontsize=20)
    plp.xlabel("Fecha", fontsize=35)
    plp.ylabel("CUPxUSD", fontsize=35)
    plp.grid(True)
    plp.show()

#Grafica de promedio calle promedio mipyme 

mip_dict = cajson("mipymes.json")
websites = cajson("Tiendasonline usd.json")

#Datos de las pag

def saca_prodm(pro_req):
    priceslist = []
    for mipyme in mip_dict["mipymes"]:
        pro_mxp = []
        for producto in mipyme["product"]:
            if producto["type"] == pro_req:
                pro_mxp.append(float(producto["price"]))
                                
        
        priceslist.append(pro_mxp)
    
            
    priceslist = sacador(priceslist)
    return priceslist
 
todpro = []
for mipyme in mip_dict["mipymes"]:
        for producto in mipyme["product"]:
            proty = producto["type"]
            todpro.append(proty)
todpro = elirep(todpro)

prom = []
for elemento in todpro:
    pro = promedio(saca_prodm(elemento))
    prom.append(pro)
    
def saca_prodw(pro_req):
    priceslist = []
    for website in websites["websites"]:
        pro_wb = []  
        for categoria in website["products_by_type"]:
            if categoria == pro_req:  
                for producto in website["products_by_type"][categoria]:
                    precio = producto["price"]
                    if precio is not None:
                        pro_wb.append(float(precio))
        priceslist.append(pro_wb)
    return sacador(priceslist)

prom2 = []
for elemento in todpro:
    pro = np.mean(saca_prodw(elemento))
    prom2.append(conv_usd(pro))
    
#La grafica   
    
def comparame_esta():

    plp.figure(figsize=(14,6))
    x = np.arange(len(todpro))  
    ancho = 0.40
    plp.bar(x - ancho/2,prom,ancho,label = "Mypimes", color = "#4B1D91", )
    plp.bar(x + ancho/2,prom2,ancho,label = "Webs(CUP)", color = "#00A1A8")
    plp.xticks(x,todpro, ha = "right", rotation = 30)
    plp.grid(True, alpha = 0.3)
    plp.ylim(0,2500)
    plp.title("Comparacion: Promedio de precios de productos (Mipyme vs Web)", fontsize = 20)
    plp.xlabel("Productos", fontsize = 15)
    plp.ylabel("Precios", fontsize = 15)
    plp.legend()
    plp.tight_layout()
    plp.show()
    
# Cod para los datos de la grafica de heatmap * disponibilidad
mipy_name = []
for mipymes in mip_dict["mipymes"]:
    mipy_name.append(mipymes["names"])


matriz = []
for mipyme in mip_dict["mipymes"]:
    fila = []
    tosca_nmod = [p["type"] for p in mipyme["product"]]
    
    for producto in todpro:
        if producto in tosca_nmod:
            fila.append(0)
        else:
            fila.append(1)   
        
    matriz.append(fila)


matriz_np = np.array(matriz)
# LA grafica de heatmap
def heatmap():
    plp.figure(figsize=(16,8))
    mapita = plp.pcolormesh(matriz_np, cmap = "cool", edgecolors = "black",linewidth=1, antialiased=True )
    plp.title("Disponibilidad de productos por Mipyme", fontsize = 15, fontweight = 16, pad = 20)
    plp.xlabel("Productos", fontsize = 18)
    plp.ylabel("Mipymes", fontsize = 18)
    plp.yticks(np.arange(len(mipy_name)) + 0.5, mipy_name, fontsize=9)
    plp.xticks(np.arange(len(todpro)) + 0.5, todpro, rotation=45, fontsize=9, ha='right')
    c = plp.Rectangle((0,0), 1, 1, facecolor='cyan', edgecolor='black')
    b = plp.Rectangle((0,0), 1, 1, facecolor='deeppink', edgecolor='black')
    plp.legend([c, b], ['Disponible', 'No Disponible'], loc='upper right', fontsize=12)
    plp.grid(True, alpha = 0.4, color = "black")
    plp.tight_layout()            
    plp.show()


#DAtos para frecu de marcas     
cuenbrand = {}
for mipyme in mip_dict["mipymes"]:
    for producto in mipyme["product"]:
        marca = producto["brand"]
        
        if marca and marca.strip() and marca != "?" and marca != "nose":
            if marca in cuenbrand:
                cuenbrand[marca] += 1
            else:
                cuenbrand[marca] = 1    
colores = [ "#2E0854", "#4B0082", "#483D8B", "#6A5ACD", "#7B68EE", "#9370DB", "#8A2BE2", "#9400D3", "#9932CC", "#BA55D3", "#DA70D6", "#DDA0DD", "#EE82EE", "#E6E6FA", "#F8F8FF"]

# LA grafica de TOP ,mas vistas
def frecu_brand():
   
    items = list(cuenbrand.items())
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][1] < items[j][1]:
                items[i], items[j] = items[j], items[i]
    top = items[:15]
    marcas = [m[0] for m in top]
    frecuencias = [m[1] for m in top]

    plp.figure(figsize=(12, 8))
    plp.barh(marcas, frecuencias, color=colores, edgecolor="blue")
    for i, valor in enumerate(frecuencias):
        plp.text(valor + 0.5, i, str(valor), va="center", fontweight="bold")
    plp.title("Marcas mas frecuentes en Mipymes", fontsize=24, pad=15, fontweight="bold")
    plp.xlabel("Cantidad")
    plp.ylabel("Marca")
    plp.gca().invert_yaxis()
    plp.tight_layout()
    plp.grid(True, alpha=0.3)
    plp.show()

# La grafica donde eliges lo que quieres ver 

def interactua_capo():
    print("\n" + "·"*70)
    print("PRODUCTOS POR MIPYME")
    print("·"*70)
    print("\nMIPYMES DISPONIBLES")
    i = 1  
    for mipyme in mip_dict["mipymes"]:
        if "names" in mipyme:
            nombre = mipyme["names"]
        print(f"{i}. {nombre}")
        i = i + 1
    entrada = input("\nEscriba el numero de la mipyme: ")
    id_mipyme = int(entrada)
    if id_mipyme < 1 or id_mipyme > len(mip_dict["mipymes"]):
        print(f"Error: El número debe estar entre 1 y {len(mip_dict['mipymes'])}")
    else:
        mipyele = mip_dict["mipymes"][id_mipyme - 1]
        if "names" in mipyele:
            mipyname = mipyele["names"]
        
        print(f"\n¡Perfecto! Seleccionaste: {mipyname}")

    prod_type = []
    precios_mip = []
    marcas_mipy = []

    for producto in mipyele["product"]:
        tipo = producto["type"]
        precio = producto["price"]
        marca = producto.get("brand", "Sin marca")
        
        if precio:
            prod_type.append(tipo)
            precios_mip.append(float(precio))
            marcas_mipy.append(marca)
        

    if not prod_type:
        print(f"La mipyme '{mipyname}' no tiene productos con precio")
        

    print(f"\nAnalizando: {mipyname}")
    print(f"Productos encontrados: {len(prod_type)}")
    plp.figure(figsize=(14, 8))
    x_pos = range(len(prod_type))
    bars = plp.bar(x_pos, precios_mip, color=colores, edgecolor='black', linewidth=1)
    plp.title(f'PRECIOS EN: {mipyname}', fontsize=18, fontweight='bold', pad=20)
    plp.xlabel('Productos', fontsize=13)
    plp.ylabel('Precio (CUP)', fontsize=13)
    plp.xticks(x_pos, prod_type, rotation=45, ha='right', fontsize=10)
    for bar, precio, marca in zip(bars, precios_mip, marcas_mipy):
        altura = bar.get_height()
        plp.text(bar.get_x() + bar.get_width()/2, altura + max(precios_mip)*0.01,
                f'{int(precio)}', ha='center', va='bottom', fontsize=9, fontweight='bold')
        plp.text(bar.get_x() + bar.get_width()/2, -max(precios_mip)*0.05,
                marca[:10], ha='center', va='top', fontsize=7, color='gray', rotation=90)
    plp.grid(True, alpha=0.2,)
    plp.tight_layout()
    plp.show()

tasa_de_cambio()
interactua_capo()
frecu_brand()
heatmap()
comparame_esta()

