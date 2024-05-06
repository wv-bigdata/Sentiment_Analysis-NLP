import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from translate import Translator

# Inicializa el analizador de sentimientos VADER
analyzer = SentimentIntensityAnalyzer()

# Inicializa el traductor
translator = Translator(from_lang='es', to_lang='en')

# Función para traducir texto del español al inglés
def translate_to_english(text):
    translation = translator.translate(text)
    return translation

# Función para analizar los sentimientos de un texto
def analyze_sentiment(text):
    # Traduce el texto al inglés
    english_text = translate_to_english(text)

    # Obtiene el puntaje de sentimiento
    sentiment_score = analyzer.polarity_scores(english_text)

    # Determina la polaridad del sentimiento
    if sentiment_score['compound'] >= 0.05:
        return "Positivo"
    elif sentiment_score['compound'] <= -0.05:
        return "Negativo"
    else:
        return "Neutral"

# Configura el título de la aplicación
st.title("Análisis de Sentimientos")

# Agrega un área de texto para que el usuario ingrese su texto
user_input = st.text_area("Ingrese el comentario para analizar su sentimiento:")

# Agrega un botón para realizar el análisis de sentimientos
if st.button("Analizar"):
    # Si el usuario ingresa texto, realiza el análisis de sentimientos
    if user_input:
        # Realiza el análisis de sentimientos
        sentimiento = analyze_sentiment(user_input)
        
        # Muestra el resultado al usuario
        st.write("El sentimiento del texto es:", sentimiento)
    else:
        st.write("Por favor, ingrese un comentario antes de analizar.")

# Pie de página
st.caption("Aplicación análisis de sentimientos de comentarios, desarrollado por Wilbert Vong - Big Data Architect.")
