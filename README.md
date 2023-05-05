# ENTREGA 5 - Contar las palabras de "Don Quijote de La Mancha" con Spark

Vamos a hacer un programa que cuente las palabras de un fichero dado, en este caso del libro "Don Quijote de La Mancha". Para ello vamos a seguir los siguientes pasos:

    - Genera una programa que estraiga de forma aleatoria un porcentaje de las líneas de un fichero: se leen el fichero por líneas y se "tira un dado". Si el dado es menor que el porcentaje la línea se graba en el fichero de salida
    - Con ese programa genera un fichero que se llame quijote_s05.txt
    - Haz que programa de contar palabras y pruébalo con el fichero quijote_s05.txt. Copia la salida y ponla en un fichero llamado out_quijote_s05.txt
    - Prueba el programa con el libro completo. Copia la salida en un fichero llamado out_quijote.txt
    - Ahora debes probar el programa en el cluster. Crea una carpeta word_count en tu directorio del cluster:
        - copia el fichero de datos (quijote.txt) y tu programa en tu directorio home del cluster.
        - copia el fichero de datos en el sistema de ficheros hdfs
        - ejecuta el programa con el programa con el fichero en hdfs Copia la salida en un fichero que se llame out_hdfs.txt Haz una captura del interfaz gráfico de spark con la ejecución de tu programa. 


# SOLUCION
- quijote.txt       -> Contiene el libro "Don Quijote de La Mancha" para contar las palabras
- porcentaje.py     -> Extrae de forma aleatoria un porcentaje de las líneas del fichero de entrada y las copia en un fichero llamado quijote_s05.txt
- contarPalabras.py -> Cuenta las palabras del contenido del archivo que se le pase como parámetro (quijote.txt / quijote_s05-txt) y escribe el número de la solución en un archivo .txt 
