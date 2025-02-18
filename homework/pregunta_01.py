# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

"""
La información requerida para este laboratio esta almacenada en el
archivo "files/input.zip" ubicado en la carpeta raíz.
Descomprima este archivo.

Como resultado se creara la carpeta "input" en la raiz del
repositorio, la cual contiene la siguiente estructura de archivos:


```
train/
    negative/
        0000.txt
        0001.txt
        ...
    positive/
        0000.txt
        0001.txt
        ...
    neutral/
        0000.txt
        0001.txt
        ...
test/
    negative/
        0000.txt
        0001.txt
        ...
    positive/
        0000.txt
        0001.txt
        ...
    neutral/
        0000.txt
        0001.txt
        ...
```

A partir de esta informacion escriba el código que permita generar
dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
del repositorio.

Estos archivos deben tener la siguiente estructura:

* phrase: Texto de la frase. hay una frase por cada archivo de texto.
* sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
    o "neutral". Este corresponde al nombre del directorio donde se
    encuentra ubicado el archivo.

Cada archivo tendria una estructura similar a la siguiente:

```
|    | phrase                                                                                                                                                                 | target   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
|  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
|  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
|  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
|  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
```


"""
import os
import zipfile
import pandas as pd

def descomprimir_archivo():
    zip = "files/input.zip"
    salida = "input"
    
    with zipfile.ZipFile(zip, 'r') as ref:
        ref.extractall()
    
    print("Archivo descomprimido correctamente en la carpeta existente 'input'.")

def verificar_estructura():
    bp = "input"
    if not os.path.exists(bp):
        print("Error: La carpeta 'input' no existe después de la extracción.")
        return False
    for dtb in ["train", "test"]:
        dtbp = os.path.join(bp, dtb)
        if not os.path.exists(dtbp):
            print(f"Error: La carpeta '{dtb}' no existe en 'input'.")
            return False
        for sentiment in ["positive", "negative", "neutral"]:
            stmp = os.path.join(dtbp, sentiment)
            if not os.path.exists(stmp):
                print(f"Advertencia: La carpeta '{sentiment}' no existe en '{dtb}'.")
    return True

def procesar_datos():
    if not verificar_estructura():
        return
    
    dtsets = {"train": [], "test": []}
    bp = "input"
    
    for dtb in ["train", "test"]:
        dtbp = os.path.join(bp, dtb)
        for sentiment in ["positive", "negative", "neutral"]:
            stmp = os.path.join(dtbp, sentiment)
            if not os.path.exists(stmp):
                continue  # Evita errores si la carpeta no existe
            for file_name in os.listdir(stmp):
                file_path = os.path.join(stmp, file_name)
                with open(file_path, "r", encoding="utf-8") as file:
                    text = file.read().strip()
                    dtsets[dtb].append([text, sentiment])
    
    # Guardar en CSV
    output = "files/output"
    os.makedirs(output, exist_ok=True)
    
    for dtb, data in dtsets.items():
        df = pd.DataFrame(data, columns=["phrase", "target"])
        df.to_csv(os.path.join(output, f"{dtb}_dataset.csv"), index=False, encoding="utf-8")
    
    print("Archivos CSV generados correctamente.")

def pregunta_01():
    descomprimir_archivo()
    procesar_datos()

# Ejecutar la función
pregunta_01()
