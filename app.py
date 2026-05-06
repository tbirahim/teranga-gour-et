import streamlit as st
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="Awa's House - Voiles Élégants",
    page_icon="🧕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personnalisé
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f8f9fa;
    }
    
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        text-align: center;
        color: white;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    
    .header-container h1 {
        font-size: 2.5em;
        margin-bottom: 10px;
    }
    
    .big-title {
        font-size: 2em;
        color: #333;
        text-align: center;
        margin: 40px 0;
        font-weight: bold;
    }
    
    .section-title {
        font-size: 1.8em;
        color: #667eea;
        margin: 30px 0 20px 0;
        text-align: center;
        border-bottom: 3px solid #667eea;
        padding-bottom: 10px;
    }
    
    .service-container {
        display: flex;
        justify-content: space-around;
        margin: 40px 0;
        flex-wrap: wrap;
    }
    
    .service-item {
        text-align: center;
        padding: 20px;
        background: white;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 10px;
        flex: 1;
        min-width: 200px;
    }
    
    .service-item h3 {
        color: #667eea;
        margin-top: 10px;
    }
    
    .voile-card {
        background: white;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: transform 0.3s, box-shadow 0.3s;
        cursor: pointer;
    }
    
    .voile-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    
    .voile-name {
        font-weight: bold;
        color: #333;
        margin: 10px 0 5px 0;
    }
    
    .voile-price {
        color: #667eea;
        font-size: 1.2em;
        font-weight: bold;
    }
    
    .footer {
        background: #333;
        color: white;
        text-align: center;
        padding: 20px;
        margin-top: 50px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# En-tête
st.markdown("""
<div class="header-container">
    <h1>🧕 Awa's House</h1>
    <p>Voiles élégants, qualité et raffinement</p>
</div>
""", unsafe_allow_html=True)

# Navigation
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🏠 Accueil", use_container_width=True):
        st.session_state.page = "accueil"
with col2:
    if st.button("⭐ Meilleures ventes", use_container_width=True):
        st.session_state.page = "meilleures"
with col3:
    if st.button("📦 Tous les articles", use_container_width=True):
        st.session_state.page = "articles"

st.divider()

# Titre principal
st.markdown("""
<h2 class="big-title">Élégance, qualité et raffinement tout est au rendez-vous.</h2>
""", unsafe_allow_html=True)

# Section Services
st.markdown("<h2 class='section-title'>Nos Services</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

services = [
    {"icon": "🏪", "titre": "Nos voiles à votre service", "desc": "Large sélection de voiles de qualité"},
    {"icon": "🤝", "titre": "Retrait en magasin", "desc": "Sans contact et sécurisé"},
    {"icon": "🚚", "titre": "Livraison à domicile", "desc": "Livraison sans contact"}
]

for idx, service in enumerate(services):
    with [col1, col2, col3][idx]:
        st.markdown(f"""
        <div class="service-item">
            <h2>{service['icon']}</h2>
            <h3>{service['titre']}</h3>
            <p>{service['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# Meilleures ventes
st.markdown("<h2 class='section-title'>Nos Meilleures Ventes</h2>", unsafe_allow_html=True)

best_voiles = [
    {"nom": "Jersey Voile", "prix": "1500 FCFA", "emoji": "👗"},
    {"nom": "Parfum et Huile", "prix": "500-3000 FCFA", "emoji": "🧴"},
    {"nom": "Pashmina Voile", "prix": "2500-3500 FCFA", "emoji": "🧣"},
    {"nom": "Voile Pincé", "prix": "500 FCFA/boîte", "emoji": "📌"}
]

cols = st.columns(4)
for idx, voile in enumerate(best_voiles):
    with cols[idx]:
        st.markdown(f"""
        <div class="voile-card">
            <h2>{voile['emoji']}</h2>
            <p class="voile-name">{voile['nom']}</p>
            <p class="voile-price">{voile['prix']}</p>
            <button style="background-color: #667eea; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Voir plus</button>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# Tous les articles
st.markdown("<h2 class='section-title'>Tous Nos Voiles</h2>", unsafe_allow_html=True)

all_voiles = [
    {"nom": "Cachemire", "prix": "1500 FCFA", "emoji": "🧥"},
    {"nom": "Pashmina", "prix": "1500 FCFA", "emoji": "🧣"},
    {"nom": "Soie", "prix": "1500 FCFA", "emoji": "✨"},
    {"nom": "Chochou", "prix": "500 FCFA", "emoji": "🎀"},
    {"nom": "Cachemire Premium", "prix": "2000 FCFA", "emoji": "👑"},
    {"nom": "Jersey", "prix": "1500 FCFA", "emoji": "👕"}
]

cols = st.columns(3)
for idx, voile in enumerate(all_voiles):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="voile-card">
            <h2>{voile['emoji']}</h2>
            <p class="voile-name">{voile['nom']}</p>
            <p class="voile-price">{voile['prix']}</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# Formulaire de contact
st.markdown("<h2 class='section-title'>Nous Contacter</h2>", unsafe_allow_html=True)

with st.form("contact_form"):
    nom = st.text_input("Votre nom")
    email = st.text_input("Votre email")
    message = st.text_area("Votre message")
    submitted = st.form_submit_button("Envoyer", use_container_width=True)
    
    if submitted:
        st.success("✅ Merci ! Votre message a été envoyé.")

st.divider()

# Footer
st.markdown("""
<div class="footer">
    <p><strong>© 2025 - Awa's House | Élégance Emoi</strong></p>
    <p>Conditions générales de ventes | Politique de confidentialité</p>
</div>
""", unsafe_allow_html=True)
