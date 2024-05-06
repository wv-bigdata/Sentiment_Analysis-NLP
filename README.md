# Sentiment Analysis

---

### Creador:
- Wilbert Vong

---

**Este trabajo consiste en la aplicación del modelo pre entrenado vaderSentiment para determinar el sentimiento en comentarios.**

**El proceso de Sentiment Analysis es el proceso de analizar texto digital para determinar si el tono emocional del mensaje es positivo, negativo o neutral.**

**Hoy en día, las empresas tienen grandes volúmenes de datos de texto, como correos electrónicos, transcripciones de chats de atención al cliente, comentarios de redes sociales y reseñas. El proceso de Sentiment Analysis pueden escanear este texto para determinar automáticamente la actitud del autor hacia un tema. Las empresas utilizan esto para mejorar el servicio al cliente y aumentar la reputación de la marca.**

**Funcionamiento**:

*Tokenización*:   El texto se divide en palabras o frases más pequeñas, conocidas como tokens. Cada token es una unidad individual de texto que se puede analizar de manera independiente.

*Segmentación*: El OCR identifica y separa los caracteres individuales o palabras en la imagen.

*Puntuación de sentimiento*: Para cada token en el texto. Esta puntuación representa cuán positivo, negativo o neutral es el sentimiento asociado con ese token.

*Ponderación de las puntuaciones*: Después de asignar una puntuación de sentimiento a cada token, estas puntuaciones se ponderan para calcular una puntuación general de sentimiento para todo el texto.

*Clasificación del sentimiento*: Basándose en la puntuación general de sentimiento calculada, el texto se clasifica en una de las tres categorías principales: positivo, negativo o neutral. Esta clasificación se realiza utilizando umbrales predefinidos para determinar en qué rango cae la puntuación de sentimiento.

---

**Usos prácticos**:

*Análisis de opiniones de clientes*: Las empresas pueden utilizar el Sentiment Analysis para comprender las opiniones de los clientes sobre sus productos o servicios.

*Detección de tendencias y opiniones en redes sociales*: El Sentiment Analysis puede ayudar a las empresas y a los especialistas en marketing a monitorizar las redes sociales para detectar tendencias y opiniones sobre temas específicos relacionados con su industria o marca.

*Gestión de la reputación en línea*: Las organizaciones pueden utilizar el Sentiment Analysis para gestionar su reputación en línea, identificando y abordando rápidamente comentarios negativos o críticas que puedan afectar su imagen pública.

*Predicción de tendencias del mercado*: El Sentiment Analysis puede ayudar a predecir tendencias del mercado al analizar el sentimiento general del público en relación con ciertos productos, servicios o temas.

*Análisis de comentarios en encuestas y formularios*: Las organizaciones pueden utilizar el análisis de sentimientos para analizar los comentarios recopilados en encuestas, formularios de retroalimentación u otros medios de comunicación con los clientes. Esto les permite identificar temas comunes, patrones de comportamiento y áreas de preocupación entre sus clientes, lo que puede informar decisiones empresariales y estrategias de mejora de productos o servicios.

---

*El modelo pre entrenado aplicado en este trabajo fue [vaderSentiment](https://github.com/cjhutto/vaderSentiment).*

---

## Notebooks

[vaderSentiment- Sentiment Analysis](https://colab.research.google.com/drive/1lluSnAJm1NMy8mkEa2Qyj5TcBtbu4oqY?usp=sharing)

---

## Aplicación web con el modelo preentrenado vaderSentiment.

Luego de desarrollar en el entorno de Google Colab el proceso de Sentiment Analysis con el modelo preentrenado vaderSentiment, he creado una aplicación web para utilizarla en un entorno amigable. Para poder acceder a ella, haz click [aquí.](https://sentimentanalysis-nlp-wv-bigdata.streamlit.app/)
