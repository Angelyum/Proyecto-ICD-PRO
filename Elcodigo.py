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
    if tasita["dolar_today"] != None :
        precio = float(tasita["dolar_today"])
        dia = tasita["day"]
        mes = tasita["month"]
        
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
    plp.xlabel("Fecha", fontsize=20)
    plp.ylabel("CUPxUSD", fontsize=20)
    plp.fill_between(dias[:35], prices[:35], alpha=0.2, color="#4C00FF")
    plp.grid(True)
    plp.show()
    
    plp.figure(figsize=(16, 7))
    plp.plot(dias[35:], prices[35:], "o-", color="#4C00FF", linewidth=3)
    plp.xticks(dias[35:], sticks[35:], rotation=45, ha="right")
    plp.title("Evolución Informal del Dólar en Cuba (Resto de días)", fontsize=20)
    plp.xlabel("Fecha", fontsize = 20)
    plp.ylabel("CUPxUSD", fontsize = 20)
    plp.fill_between(dias[35:], prices[35:], alpha=0.2, color="#4C00FF")
    plp.grid(True)
    plp.show()

def tasa_de_cambio():
    plp.figure(figsize=(16, 7))
    plp.plot(dias[:35], prices[:35], "o-", color="#4C00FF", linewidth=3)
    plp.xticks(dias[:35], sticks[:35], rotation=45, ha="right")
    plp.title("Evolución Informal del Dólar en Cuba (Primeros 35 días)", fontsize=20)
    plp.xlabel("Fecha", fontsize=20)
    plp.ylabel("CUPxUSD", fontsize=20)
    plp.grid(True)
    plp.show()
    
    plp.figure(figsize=(16, 7))
    plp.plot(dias[35:], prices[35:], "o-", color="#4C00FF", linewidth=3)
    plp.xticks(dias[35:], sticks[35:], rotation=45, ha="right")
    plp.title("Evolución Informal del Dólar en Cuba (Resto de días)", fontsize=20)
    plp.xlabel("Fecha", fontsize=20)
    plp.ylabel("CUPxUSD", fontsize=20)
    plp.grid(True)
    plp.show()

#Grafica de promedio calle promedio mipyme 

mip_dict = cajson("mipymes.json")
websites = cajson("Tiendasonline usd.json")

def saca_todo():
    todpro = []
    for mipyme in mip_dict["mipymes"]:
            for producto in mipyme["product"]:
                proty = producto["type"]
                todpro.append(proty)
    todpro = elirep(todpro)
    
    return 

saca_todo()


# Datos de las mipymes de la calle

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
# Datos de las pag web
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
 
#La gráfica de comparación de precios   
    
def comparar_mxw():

    plp.figure(figsize=(14,6))
    x = np.arange(len(todpro))  
    ancho = 0.40
    plp.bar(x - ancho/2,prom,ancho,label = "Mypimes", color = "#4B1D91", )
    plp.bar(x + ancho/2,prom2,ancho,label = "Webs(CUP)", color = "#00A1A8")
    plp.xticks(x,todpro, ha = "right", rotation = 30)
    plp.grid(True, alpha = 0.3)
    plp.ylim(0,3000)
    plp.title("Comparacion: Promedio de precios de productos (Mipyme vs Web)", fontsize = 20)
    plp.xlabel("Productos", fontsize = 15)
    plp.ylabel("Precios", fontsize = 15)
    plp.legend()
    plp.tight_layout()
    plp.show()
    
# Cod para los datos de la gráfica de heatmap * disponibilidad
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
    plp.xticks(np.arange(len(todpro)) + 0.5, todpro, rotation=45, fontsize=9, ha="right")
    c = plp.Rectangle((0,0), 1, 1, facecolor="cyan", edgecolor="black")
    b = plp.Rectangle((0,0), 1, 1, facecolor="deeppink", edgecolor="black")
    plp.legend([c, b], ["Disponible", "No Disponible"], loc="upper right", fontsize=12)
    plp.grid(True, alpha = 0.4, color = "black")
    plp.tight_layout()            
    plp.show()


#DAtos para frecu de marcas     
colores = [ "#2E0854", "#4B0082", "#483D8B", "#6A5ACD", "#7B68EE", "#9370DB", "#8A2BE2", "#9400D3", "#9932CC", "#BA55D3", "#DA70D6", "#DDA0DD", "#EE82EE", "#E6E6FA", "#F8F8FF"]

# LA grafica de TOP ,mas vistas, FALLIDA YUDI DIJO QUE NO!!!!
def frecu_brand(n):

    
    cuenbrand = {}
    for mipyme in mip_dict["mipymes"]:
        for producto in mipyme["product"]:
            marca = producto["brand"]
            
            if marca and marca.strip() and marca != None :
                if marca in cuenbrand:
                    cuenbrand[marca] += 1
                else:
                    cuenbrand[marca] = 1    
    

    elems = list(cuenbrand.items())
    for i in range(len(elems)):
        for j in range(i + 1, len(elems)):
            if elems[i][1] < elems[j][1]:
                elems[i], elems[j] = elems[j], elems[i]
        top = elems[:n]
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

# La grafica para ver que productos tiene cada mipyme

def Mipyme_productos():
    print("\n" + "·"*70)
    print("PRODUCTOS POR MIPYME")
    print("·"*70)
    print("\nMIPYMES")
    i = 1  
    for mipyme in mip_dict["mipymes"]:
        if "names" in mipyme:
            nombre = mipyme["names"]
        print(f"{i}. {nombre}")
        i = i + 1
    entrada = input("\nEscriba el numero de la mipyme: ")
    id_mipyme = int(entrada)
    if id_mipyme < 1 or id_mipyme > len(mip_dict["mipymes"]):
        print(f"Error: El número debe estar entre 1 y {len(mip_dict["mipymes"])}")
    else:
        mipyele = mip_dict["mipymes"][id_mipyme - 1]
        if "names" in mipyele:
            mipyname = mipyele["names"]
        
        print(f"\nSeleccionaste: {mipyname}")

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
            if marca and marca.strip() and marca is not None:
                marcas_mipy.append(marca)
            else:
                marcas_mipy.append("?")  

    medias_web = []
    for tipo_producto in prod_type:
        precios_web_raw = saca_prodw(tipo_producto)
        precios_web_validos = [p for p in precios_web_raw if p is not None and p > 0]
        
        if precios_web_validos:
            precios_web_cup = [conv_usd(p) for p in precios_web_validos]
            media_web = np.mean(precios_web_cup)
        else:
            media_web = 0
        medias_web.append(media_web)
    
    print(f"\nAnalizando: {mipyname}")
    print(f"Productos encontrados: {len(prod_type)}")
    plp.figure(figsize=(14, 8))
    x_pos = range(len(prod_type))
    bars = plp.bar(x_pos, precios_mip, color=colores, edgecolor="black", linewidth=1)
    plp.plot(x_pos, medias_web, "o-", color="#003366", linewidth=2.5, markersize=8, 
             label="Promedio Web (USD→CUP)", alpha=0.9)
    
    
    for i, media in enumerate(medias_web):
        if media > 0:  
            plp.text(i, media + max(precios_mip)*0.02, 
                    f"{int(media)}", 
                    ha="center", va="bottom", 
                    fontsize=9, color="#003366", fontweight="bold",
                    bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8))
    
    plp.title(f"PRECIOS EN: {mipyname}", fontsize=18, fontweight="bold", pad=20)
    plp.xlabel("Productos", fontsize=13)
    plp.ylabel("Precio (CUP)", fontsize=13)
    plp.xticks(x_pos, prod_type, rotation=45, ha="right", fontsize=10)
    for i in range(len(bars)):
        bar = bars[i]
        precio = precios_mip[i]
        marca = marcas_mipy[i]
        altura = bar.get_height()
        plp.text(bar.get_x() + bar.get_width()/2, altura + max(precios_mip)*0.01,
                f"{int(precio)}", ha="center", va="bottom", fontsize=9, fontweight="bold")
        plp.text(bar.get_x() + bar.get_width()/2, -max(precios_mip)*0.05,
                marca[:10], ha="center", va="top", fontsize=7, color="gray", rotation=90)
    
    plp.legend(loc="upper right")
    plp.grid(True, alpha=0.2,)
    plp.tight_layout()
    plp.show()
    
# GRafica pastel para disponibilidasd de marcas

def dispo_marcas():
  
    marcas_mipymes = []
    for mipyme in mip_dict["mipymes"]:
        for producto in mipyme["product"]:
            marca = producto.get("brand")
            if marca is not None: 
                marcas_mipymes.append(marca)
    
    marcas_webs = []
    for website in websites["websites"]:
        for categoria in website["products_by_type"]:
            for producto in website["products_by_type"][categoria]:
                marca = producto.get("brand")
                if marca is not None: 
                    marcas_webs.append(marca)

    marcas_mipymes = elirep(marcas_mipymes)
    marcas_webs = elirep(marcas_webs)
    
    solo_mipymes = []
    for marca in marcas_mipymes:
        if marca not in marcas_webs:
            solo_mipymes.append(marca)
    
    solo_webs = []
    for marca in marcas_webs:
        if marca not in marcas_mipymes:
            solo_webs.append(marca)
    
    en_ambos = []
    for marca in marcas_mipymes:
        if marca in marcas_webs:
            en_ambos.append(marca)
    
    plp.figure(figsize=(10, 8))
    datos = [len(solo_mipymes), len(solo_webs), len(en_ambos)]
    etiquetas = ["Solo Mipymes", "Solo Webs", "En Ambos"]
    colores = ["#4B1D91", "#00A1A8", "#9370DB"]
    wedges, texts, autotexts = plp.pie(datos, labels=etiquetas, colors=colores,
                                      autopct="%1.1f%%", startangle=90,
                                      textprops={"fontsize": 12})
    for autotext in autotexts:
        autotext.set_color("white")
        autotext.set_fontweight("bold")
        autotext.set_fontsize(11)
    plp.title("Disponibilidad de Marcas: Mipymes vs Webs", 
              fontsize=16, fontweight="bold", pad=20)
    plp.tight_layout()
    plp.show()
    
    print("\n MARCAS ENCONTRADAS:")
    print(f"Solo en Mipymes: {len(solo_mipymes)}")
    print(f"Solo en Webs: {len(solo_webs)}")
    print(f"En ambos: {len(en_ambos)}")
