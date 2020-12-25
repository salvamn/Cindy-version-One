# Cindy-version-One

<h1> Cindy Asistente Virtual </h1>

Esta aplicacion es un asistente de voz como tambien puede funcionar sin hablarle, de momento se encuentra en su primera version, todos el codigo esta en un unico script y se espera en las proximas versiones separar el codigo en distintos scripts, arreglar bugs y comentar la app.

<h2> Librerias Usadas </h2>

<ol>
  <ul>reconocimiento de voz: Speech Recognition y Pyaudio <a href='https://pypi.org/project/SpeechRecognition'>Link</a></ul>
  <ul>Interfaz: Tkinter</ul>
  <ul>Imagenes: Pillow <a href='https://pillow.readthedocs.io/en/stable/'>Link</a></ul>
  <ul>Musica: Mixer de Pygame <a href='https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.get_busy'>Link</a></ul>
  <ul>Para acceder a directorios y abrir programas: subprocess y getpass </ul>
  <ul>Voz de Cindy: pyttsx3 <a href='https://pypi.org/project/pyttsx3/'>Link</a></ul>
  <ul>Ejecucion simultanea: Threading</ul>
</ol>  
  
  <h2>Imagen de la Interfaz</h2>
  
  ![cindyimg](https://user-images.githubusercontent.com/61121429/103034120-e9f15f00-4542-11eb-8670-eea4929b01b0.PNG)


<h2> Como funciona Cindy </h2>

Lo primero que se debe hacer es instalar la libreria Pyaudio, esta libreria se instala mediante `pip install pyaudio` en el caso de que no puedas instalar pyaudio mediante pip tendras que descargar el archivo whl desde <a href="https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio">aca</a>, para buscar el archivo simplemente presionas `ctrl + f` y buscas pyaudio y le das clic a la primera coincidencia, luego de eso descargas el archivo correspondiente a tu version de windows y python, cuando ya lo tengas te diriges a la carpeta donde descargaste el archivo abres un cmd y escribes pip install y el nombre del archivo.

El segundo paso es instalar `pip install SpeechRecognition` esta libreria necesita de pyaudio para poder usar su funcionalidad spech to text que es de habla a texto, tambien esta libreria en el caso de que no quieras usar el microfono le puedes pasar un archivo de audio y funciona de la misma manera, ojo para que esto funcione necesitas estar conectado a internet.

¿ Como funciona speech recognition ?

```
import speech_recognition as sr # Importamos speech_recognition y le damos un alias de sr.

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source: # Se abre el microfono y se procede hablar.
    print("Say something!")
    audio = r.listen(source) # Se escucha el audio
    
try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio)) # Se pasa el audio a texto con la api de google y luego se imprime.
except sr.UnknownValueError: # Manejamos errores en el caso de que se genere alguno.
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
```

bueno ahora ya puedes pasar el habla a texto con ese simple codigo.


<h2> Pygame y su funcion Mixer </h2>

ahora lo que haremos es acceder a la carpeta musica o music dependiendo el idioma de tu sistema operativo, primero instalaremos pygame `pip install pygame` luego importaremos `pygame y su funcion mixer`.

primero necesitamos la ruta asi que crearemos una variable directorio y le pasaremos la ruta hacia dicha carpeta en mi caso es la siguiente

`directorio = r"C:\Users\nombre_usuario\Music"`

ahora toca elegir la extension de nuestras canciones aasi que crearemos una variable extension y le asignaremos .mp3

`extension = ".mp3"`

el siguiente paso mediante una lista por comprension vamos a listar nuestra carpeta y la recorreremos y al vez iremos agregando todos los archivos con extension mp3 a nuestra lista canciones, de esta manera ya tenemos todos lo nombres de las canciones de la carpeta musica.

`canciones = [cancion for cancion in os.listdir(directorio) if cancion.lower().endswith(extension)] # Pasamos todos los caracteres de las canciones a minusculas`

ya tenemos todas las canciones ahora solo hace falta reproducirlas, para esto utilizaremos mixer de pygame esto se puede hacer de muchas formas pero ahora veremos solo una que es la de pasarle una cancion aleatoria usando el modulo random.

```
import random

numero_aleatorio = random.randrange(0,len(canciones)) # Generamos un numero

directorio = rf"C:\Users\nombre_usuario\Music\{canciones[numero_aleatorio - 1]}" # Le pasamos la lista al directorio y a la lista el numero aleatorio
mixer.init() # Iniciamos mixer
mixer.music.load(directorio) # Cargamos la cancion
mixer.music.set_volume(0.7) # Ajustamos el volumen
mixer.music.play() # Reproducimos la cancion
```

Listo ya tenemos nuestro reproductor de musica.

