import streamlit as st

# Configuration de la page
st.set_page_config(page_title="AWA'S HOUSE | PRESTIGE", layout="wide")

# ---------------------------------------------------------
# LE DESIGN "ULTRA-VIBRANT" (CSS HAUTE PERFORMANCE)
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Italiana&family=Outfit:wght@100;300;600;900&display=swap');

    /* Fond avec animation de gradient Mesh */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(at 0% 0%, #ffffff 0%, #fdfbfb 50%, #ebedee 100%);
        font-family: 'Outfit', sans-serif;
    }

    /* HEADER TITRE - EFFET MIROIR */
    .brand-container {
        text-align: center;
        padding: 100px 0;
        perspective: 1000px;
    }

    .main-logo {
        font-family: 'Italiana', serif;
        font-size: 120px;
        font-weight: 400;
        color: #1a1a1a;
        letter-spacing: 25px;
        text-transform: uppercase;
        position: relative;
        display: inline-block;
        margin-bottom: 0;
        background: linear-gradient(to bottom, #1a1a1a 50%, #D4AF37 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* CARTES PRODUITS - EFFET "FIBRE DE VERRE" */
    .product-box {
        position: relative;
        background: rgba(255, 255, 255, 0.7);
        border: 1px solid rgba(212, 175, 55, 0.1);
        border-radius: 40px;
        overflow: hidden;
        transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
        margin-bottom: 50px;
    }

    .product-box:hover {
        transform: scale(1.02) rotate(1deg);
        box-shadow: 0 50px 80px rgba(212, 175, 55, 0.15);
        border-color: #D4AF37;
    }

    .product-img-vibe {
        width: 100%;
        height: 600px;
        object-fit: cover;
        transition: 0.8s;
        filter: sepia(20%) contrast(1.1);
    }

    .product-box:hover .product-img-vibe {
        filter: sepia(0%) contrast(1.2);
        transform: scale(1.1);
    }

    /* TEXTE DYNAMIQUE */
    .floating-price {
        position: absolute;
        top: 30px;
        right: 30px;
        background: white;
        padding: 10px 20px;
        border-radius: 50px;
        font-weight: 900;
        font-size: 14px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }

    .product-info-panel {
        padding: 30px;
        background: white;
        text-align: left;
    }

    .product-name-modern {
        font-family: 'Italiana', serif;
        font-size: 35px;
        color: #1a1a1a;
        margin: 0;
    }

    /* BOUTON ULTRA-DESIGN */
    div.stButton > button {
        background: #1a1a1a !important;
        color: white !important;
        border: none !important;
        border-radius: 0 30px 0 30px !important; /* Forme asymétrique */
        padding: 20px 40px !important;
        font-weight: 600 !important;
        letter-spacing: 3px !important;
        transition: 0.5s !important;
        width: 100% !important;
    }

    div.stButton > button:hover {
        background: #D4AF37 !important;
        border-radius: 30px 0 30px 0 !important;
        box-shadow: 0 15px 30px rgba(212, 175, 55, 0.4) !important;
    }

    /* BARRE DE NAVIGATION MINIMALISTE */
    .nav-pill {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin-top: -50px;
        margin-bottom: 80px;
    }
    .nav-link {
        font-size: 11px;
        font-weight: 900;
        letter-spacing: 4px;
        text-transform: uppercase;
        color: #888;
        cursor: pointer;
        transition: 0.3s;
    }
    .nav-link:hover { color: #D4AF37; }

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# CONTENU DE LA MAISON
# ---------------------------------------------------------

# Header "Malade Mental"
st.markdown("""
<div class="brand-container">
    <div class="main-logo">AWA'S</div>
    <div style="font-size: 12px; letter-spacing: 15px; color: #D4AF37; text-transform: uppercase; margin-top: -20px;">
        The Luxury Experience
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation Flottante
st.markdown("""
<div class="nav-pill">
    <div class="nav-link">L'ORIGINE</div>
    <div class="nav-link" style="color:#1a1a1a; border-bottom: 2px solid #D4AF37;">BOUTIQUE</div>
    <div class="nav-link">SUR MESURE</div>
</div>
""", unsafe_allow_html=True)

# GRID PRODUITS
# Liste basée sur tes produits (Chouchou, Cachemire, Jersey, Soie, Pashmina, Parfum)
items = [
    {"n": "SOIE IMPÉRIALE", "p": "3.500", "img": "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=1000"},
    {"n": "JERSEY PREMIUM", "p": "1.500", "img": "https://images.unsplash.com/photo-1584030373081-f37b7bb4fa8e?w=1000"},
    {"n": "PASHMINA LUXE", "p": "2.500", "img": "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?w=1000"},
    {"n": "CHOUCHOU SATIN", "p": "500", "img": "https://images.unsplash.com/photo-1605810756711-645391a61044?w=1000"},
    {"n": "CACHEMIRE PUR", "p": "3.500", "img": "https://images.unsplash.com/photo-1533090481720-856c6e3c1fdc?w=1000"},
    {"n": "OUD SIGNATURE", "p": "5.500", "img": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=1000"}
]

# Affichage en colonnes alternées pour un look "Branding de Mode"
for i in range(0, len(items), 2):
    col1, col2 = st.columns(2, gap="large")
    
    for idx, col in enumerate([col1, col2]):
        item = items[i + idx]
        with col:
            st.markdown(f"""
            <div class="product-box">
                <div class="floating-price">{item['p']} FCFA</div>
                <img src="{item['img']}" class="product-img-vibe">
                <div class="product-info-panel">
                    <div class="product-name-modern">{item['n']}</div>
                    <p style="font-size:12px; color:#888; letter-spacing:1px; margin-top:10px;">
                        Matière d'exception sélectionnée pour sa brillance et sa douceur incomparable. 
                        Un incontournable de la garde-robe Awa's House.
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.button(f"ACQUÉRIR LA PIÈCE - {item['n']}", key=f"btn_{i+idx}")

# Footer Magnétique
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="background: #1a1a1a; padding: 100px 50px; border-radius: 100px 100px 0 0; text-align: center;">
    <h2 style="font-family: 'Italiana'; color: white; font-size: 50px;">AWA'S HOUSE</h2>
    <p style="color: #D4AF37; letter-spacing: 5px;">DAKAR • PARIS • DUBAI</p>
    <div style="margin-top: 50px; display: flex; justify-content: center; gap: 30px; color: white; opacity: 0.5; font-size: 12px;">
        <span>INSTAGRAM</span>
        <span>WHATSAPP</span>
        <span>TIKTOK</span>
    </div>
</div>
""", unsafe_allow_html=True)
