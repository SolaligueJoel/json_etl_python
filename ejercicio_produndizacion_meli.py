import json
import requests
import matplotlib.pyplot as plt



def fetch(locacion):
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20{}%20&limit=50'.format(locacion)
    response = requests.get(url)
    data_json = response.json()
    new_data = data_json["results"]
    
    #Filtrando lista en pesos
    new_list = [{"price":x["price"], "condition":x["condition"]} for x in new_data if x.get("currency_id") == "ARS"]
    print("\n*********************\nImprimiendo DataSet\n*********************\n",new_list)
    return new_list



def transform(new_data,min,max):
    #Realizando listas por valor minimo, intermedio y maximo
    precio_min = [x["price"] for x in new_data if x.get("price")< min]
    precio_min_max = [x["price"] for x in new_data if x.get("price")>min and x.get("price")< max]
    precio_max = [x["price"] for x in new_data if x.get("price")>max]
    print("\n*********************\nImprimiendo Listas segun precio: Min, Inter. y Max\n*********************\n",precio_min,precio_min_max,precio_max)
    print("\n*********************\nImprimiendo Cantidad de elementos\n*********************\n",[len(precio_min),len(precio_min_max),len(precio_max)])
    return [len(precio_min),len(precio_min_max),len(precio_max)]




def report(data):
    #Pie Plot
    fig = plt.figure()
    fig.suptitle('Precios Alquileres en {}'.format(locacion))

    ax = fig.add_subplot()

    label = ['Valor Minimo','Valor Intermedio','Valor Maximo']
    colors = ['#90EE90','#F1C40F','#B03A2E']

    ax.pie(data, labels = label, wedgeprops={'edgecolor':'black'}, autopct='%0.0f%%', colors=colors)
    ax.axis('equal')

    plt.show()



if __name__ == '__main__':
    locacion = 'Bariloche'
    min = 2500
    max = 7000

    dataset = fetch(locacion)
    data = transform(dataset,min,max)
    report(data)
    
