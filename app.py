import streamlit as st

# Configuration pour un affichage plein écran et élégant
st.set_page_config(page_title="Awa's House | Maison de Couture", layout="wide")

# ---------------------------------------------------------
# DESIGN "ATELIER LUXE" - CSS SUR MESURE
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,600;1,400&family=Montserrat:wght@100;300;400;600&display=swap');

    /* Fond Ivoire doux pour ne pas fatiguer l'oeil */
    [data-testid="stAppViewContainer"] {
        background-color: #FDFCFB;
        font-family: 'Montserrat', sans-serif;
    }

    /* En-tête type Magazine de Mode */
    .header-luxury {
        text-align: center;
        padding: 80px 0 40px 0;
        background: white;
        border-bottom: 1px solid #EEE;
        margin-bottom: 50px;
    }

    .brand-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 75px;
        font-weight: 300;
        letter-spacing: 15px;
        text-transform: uppercase;
        color: #1A1A1A;
        margin-bottom: 0;
    }

    /* Section Services (Inspirée de ton menu icônes) */
    .info-bar {
        display: flex;
        justify-content: space-around;
        padding: 30px;
        background: #FFF;
        margin: 20px auto;
        max-width: 1000px;
        border-radius: 100px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.03);
    }

    .info-item {
        text-align: center;
        font-size: 11px;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #888;
    }

    /* Grille de Produits - Espacement Pro */
    .product-box {
        background: white;
        padding: 0px;
        border-radius: 0px; /* Le carré fait plus "Luxe" que l'arrondi */
        transition: 0.5s;
        margin-bottom: 40px;
    }

    .product-box:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.08);
    }

    .product-img {
        width: 100%;
        height: 500px; /* Images hautes pour un look éditorial */
        object-fit: cover;
    }

    .product-text {
        padding: 20px 0;
        text-align: center;
    }

    .product-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 28px;
        font-style: italic;
        color: #1A1A1A;
    }

    .product-price {
        font-size: 14px;
        color: #D4AF37; /* Or Signature */
        font-weight: 600;
        margin-top: 5px;
    }

    /* Boutons Minimalistes */
    div.stButton > button {
        background-color: transparent !important;
        color: #1A1A1A !important;
        border: 1px solid #1A1A1A !important;
        border-radius: 0px !important;
        padding: 12px 30px !important;
        font-size: 10px !important;
        letter-spacing: 3px !important;
        width: 100% !important;
        transition: 0.3s !important;
    }

    div.stButton > button:hover {
        background-color: #1A1A1A !important;
        color: white !important;
    }

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# CONTENU (Basé sur tes produits réels)
# ---------------------------------------------------------

# 1. HEADER
st.markdown("""
<div class="header-luxury">
    <div class="brand-title">Awa's House</div>
    <p style="letter-spacing: 5px; color: #AAA; font-size: 12px;">ÉLÉGANCE • QUALITÉ • RAFFINEMENT</p>
</div>
""", unsafe_allow_html=True)

# 2. BARRE D'INFOS (Icônes de ton projet)
st.markdown("""
<div class="info-bar">
    <div class="info-item">🏪 Retrait en magasin</div>
    <div class="info-item">🚚 Livraison express</div>
    <div class="info-item">🛡️ Qualité Garantie</div>
</div>
""", unsafe_allow_html=True)

# 3. GALERIE DE PRODUITS
st.markdown("<h2 style='text-align:center; font-family:Cormorant Garamond; font-weight:300; margin: 60px 0;'>Nos Pièces Maîtresses</h2>", unsafe_allow_html=True)

# On utilise tes vrais noms de produits
produits = [
    {"nom": "Voile Jersey", "prix": "1 500", "img": "https://images.unsplash.com/photo-1584030373081-f37b7bb4fa8e?w=800"},
    {"nom": "Cachemire", "prix": "3 500", "img": "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=800"},
    {"nom": "Chouchou Satin", "prix": "500", "img": "https://images.unsplash.com/photo-1605810756711-645391a61044?w=800"},
    {"nom": "Soie de Luxe", "prix": "1 500", "img": "https://images.unsplash.com/photo-1533090481720-856c6e3c1fdc?w=800"},
    {"nom": "Pashmina", "prix": "2 500", "img": "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?w=800"},
    {"nom": "Parfum d'Oud", "prix": "3 500", "img": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=800"}
]

# Affichage en grille de 2 colonnes pour un effet "Grand Catalogue"
cols = st.columns(2)

for i, p in enumerate(produits):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="product-box">
            <img src="{p['img']}" class="product-img">
            <div class="product-text">
                <div class="product-title">{p['nom']}</div>
                <div class="product-price">{p['prix']} FCFA</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"SÉLECTIONNER {p['nom'].upper()}", key=f"btn_{i}"):
            st.toast(f"{p['nom']} ajouté à votre panier.")

# 4. FOOTER
st.markdown("""
<div style="text-align: center; padding: 100px 0 50px 0; border-top: 1px solid #EEE; margin-top: 50px;">
    <p style="font-family: Cormorant Garamond; font-size: 20px; font-style: italic;">Awa's House - Émotion Émoi</p>
    <p style="font-size: 10px; color: #AAA; letter-spacing: 2px;">DAKAR • PARIS • DUBAI</p>
</div>
""", unsafe_allow_html=True)
