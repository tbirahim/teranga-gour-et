import streamlit as st

# Configuration de la page pour un look "Atelier"
st.set_page_config(page_title="Awa's House | Maison de Qualité", page_icon="✨", layout="wide")

# ---------------------------------------------------------
# DESIGN "ELITE" - MINIMALISME ET ÉLÉGANCE
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,600;1,400&family=Montserrat:wght@200;400;600&display=swap');

    /* Fond Ivoire très doux */
    [data-testid="stAppViewContainer"] {
        background-color: #FCFAFB;
        font-family: 'Montserrat', sans-serif;
    }

    /* Header avec effet parallaxe inversé */
    .hero-banner {
        background: linear-gradient(rgba(255,255,255,0.4), rgba(255,255,255,0.4)), 
                    url('https://images.unsplash.com/photo-1520006403993-4744f0c846a1?q=80&w=2000');
        background-size: cover;
        background-position: center;
        height: 450px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-radius: 0 0 100px 100px;
        box-shadow: inset 0 0 100px rgba(0,0,0,0.05);
        margin-bottom: 50px;
    }

    .brand-name {
        font-family: 'Cormorant Garamond', serif;
        font-size: 85px;
        font-weight: 300;
        color: #2C2C2C;
        letter-spacing: 12px;
        text-transform: uppercase;
        margin-bottom: 0;
    }

    /* Icônes de service modernisées */
    .service-container {
        display: flex;
        justify-content: space-around;
        padding: 40px 0;
        background: white;
        border-radius: 30px;
        margin: 20px 0 50px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.02);
    }
    
    .service-card {
        text-align: center;
        flex: 1;
    }
    .service-icon { font-size: 30px; margin-bottom: 10px; }
    .service-text { font-size: 12px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; color: #888; }

    /* Grille de produits façon "Catalogue de Mode" */
    .product-wrapper {
        background: white;
        padding: 15px;
        border-radius: 5px;
        transition: 0.5s;
        border-bottom: 1px solid #eee;
    }

    .product-wrapper:hover {
        box-shadow: 0 20px 40px rgba(0,0,0,0.05);
        transform: translateY(-5px);
    }

    .product-label {
        font-family: 'Cormorant Garamond', serif;
        font-size: 26px;
        font-style: italic;
        margin-top: 15px;
        color: #1a1a1a;
    }

    .product-price {
        font-family: 'Montserrat', sans-serif;
        font-size: 14px;
        letter-spacing: 2px;
        color: #D4AF37;
        font-weight: 600;
        margin-bottom: 20px;
    }

    /* Bouton d'achat discret et chic */
    div.stButton > button {
        background-color: #1a1a1a !important;
        color: white !important;
        border: none !important;
        border-radius: 0px !important;
        padding: 10px 25px !important;
        font-size: 11px !important;
        letter-spacing: 2px !important;
        transition: 0.4s !important;
    }

    div.stButton > button:hover {
        background-color: #D4AF37 !important;
        transform: scale(1.02);
    }
    
    /* Footer */
    .footer-custom {
        text-align: center;
        padding: 60px;
        font-size: 12px;
        color: #aaa;
        letter-spacing: 1px;
    }

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# STRUCTURE DE L'INTERFACE
# ---------------------------------------------------------

# 1. HERO SECTION
st.markdown("""
<div class="hero-banner">
    <div class="brand-name">Awa's House</div>
    <div style="font-size: 14px; letter-spacing: 5px; color: #555; text-transform: uppercase;">
        Élégance • Qualité • Raffinement
    </div>
</div>
""", unsafe_allow_html=True)

# 2. SERVICES (Repris de ton aperçu mais en plus chic)
st.markdown("""
<div class="service-container">
    <div class="service-card">
        <div class="service-icon">🏺</div>
        <div class="service-text">À votre service</div>
    </div>
    <div class="service-card">
        <div class="service-icon">🛍️</div>
        <div class="service-text">Retrait en magasin</div>
    </div>
    <div class="service-card">
        <div class="service-icon">🚚</div>
        <div class="service-text">Livraison à domicile</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 3. LES MEILLEURES VENTES
st.markdown("<h2 style='font-family:Cormorant Garamond; font-size:45px; text-align:center; font-weight:300;'>Nos Meilleures Ventes</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888; margin-bottom:50px;'>Une sélection de nos pièces les plus convoitées</p>", unsafe_allow_html=True)

# Liste des produits basés sur ton image
ventes = [
    {"n": "Voile Jersey", "p": "1 500", "i": "https://images.unsplash.com/photo-1584030373081-f37b7bb4fa8e?w=600"},
    {"n": "Parfum & Huile", "p": "3 500", "i": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=600"},
    {"n": "Pashmina Luxe", "p": "2 500", "i": "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?w=600"},
    {"n": "Pince Premium", "p": "500", "i": "https://images.unsplash.com/photo-1605810756711-645391a61044?w=600"}
]

cols_ventes = st.columns(4)
for idx, prod in enumerate(ventes):
    with cols_ventes[idx]:
        st.markdown(f"""
        <div class="product-wrapper">
            <img src="{prod['i']}" style="width:100%; height:250px; object-fit:cover;">
            <div class="product-label">{prod['n']}</div>
            <div class="product-price">{prod['p']} FCFA</div>
        </div>
        """, unsafe_allow_html=True)
        st.button("AJOUTER AU PANIER", key=f"v_{idx}")

st.markdown("<br><br><br>", unsafe_allow_html=True)

# 4. NOS VOILES (Section Catalogue)
st.markdown("<h2 style='font-family:Cormorant Garamond; font-size:45px; font-weight:300; padding-left:20px;'>Nos Voiles</h2>", unsafe_allow_html=True)

catalogue = [
    {"n": "Cachemire Doux", "p": "3 500", "i": "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=600"},
    {"n": "Soie d'Orient", "p": "1 500", "i": "https://images.unsplash.com/photo-1533090481720-856c6e3c1fdc?w=600"},
    {"n": "Chouchou Satin", "p": "500", "i": "https://images.unsplash.com/photo-1605810756711-645391a61044?w=600"},
    {"n": "Jersey Premium", "p": "1 500", "i": "https://images.unsplash.com/photo-1584030373081-f37b7bb4fa8e?w=600"}
]

# Affichage en 2x2 pour un look plus aéré
c1, c2 = st.columns(2)
for i, p in enumerate(catalogue):
    target = c1 if i < 2 else c2
    with target:
        st.markdown(f"""
        <div style="margin-bottom:40px;">
            <img src="{p['i']}" style="width:100%; height:400px; object-fit:cover; border-radius:5px;">
            <div style="display:flex; justify-content:space-between; align-items:baseline; padding:10px 0;">
                <span class="product-label">{p['n']}</span>
                <span class="product-price">{p['p']} FCFA</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("VOIR LE PRODUIT", key=f"c_{i}")

# 5. FOOTER (Repris de ton image)
st.markdown("""
<div class="footer-custom">
    <p>Awa's House - ÉLÉGANCE ÉMOI | © 2026</p>
    <p style="font-size:10px; text-transform:uppercase;">Conditions générales de ventes • Politique de confidentialité</p>
</div>
""", unsafe_allow_html=True)
