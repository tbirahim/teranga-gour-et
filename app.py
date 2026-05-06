import streamlit as st

# Configuration
st.set_page_config(page_title="AWA'S HOUSE | THE ULTIMATE LUXE", layout="wide")

# ---------------------------------------------------------
# DESIGN "MALADE MENTAL" (FOCUS SUR L'ESTHÉTIQUE)
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Playfair+Display:ital,wght@0,900;1,900&family=Outfit:wght@100;400;900&display=swap');

    /* Fond animé subtil */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 100%);
        color: white;
        font-family: 'Outfit', sans-serif;
    }

    /* HEADER EXPLOSIF */
    .hero-section {
        padding: 120px 0;
        text-align: center;
        background: url('https://images.unsplash.com/photo-1618220179428-22790b461013?w=1600');
        background-size: cover;
        background-attachment: fixed;
        border-radius: 0 0 100px 100px;
        box-shadow: inset 0 0 200px #000;
        margin-bottom: 60px;
    }

    .main-title {
        font-family: 'Syncopate', sans-serif;
        font-size: 8vw;
        font-weight: 700;
        text-transform: uppercase;
        line-height: 0.8;
        background: linear-gradient(45deg, #D4AF37, #FFFFFF, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 10px 20px rgba(212,175,55,0.3));
    }

    /* BARRE DE SERVICES GLASSMORPHISM */
    .service-grid {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: -100px auto 60px;
        max-width: 90%;
    }

    .service-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 30px;
        border-radius: 30px;
        text-align: center;
        flex: 1;
        transition: 0.4s;
    }

    .service-card:hover {
        background: rgba(212, 175, 55, 0.1);
        transform: translateY(-10px);
    }

    /* SECTION TITRES */
    .section-label {
        font-family: 'Playfair Display', serif;
        font-size: 60px;
        font-weight: 900;
        font-style: italic;
        margin-bottom: 40px;
        color: #D4AF37;
    }

    /* CARTES PRODUITS NÉON-GOLD */
    .product-box {
        position: relative;
        border-radius: 40px;
        overflow: hidden;
        background: #000;
        border: 1px solid #222;
        transition: 0.6s cubic-bezier(0.23, 1, 0.32, 1);
        margin-bottom: 30px;
    }

    .product-box:hover {
        border-color: #D4AF37;
        box-shadow: 0 0 40px rgba(212, 175, 55, 0.2);
    }

    .product-box img {
        width: 100%;
        height: 450px;
        object-fit: cover;
        opacity: 0.7;
        transition: 0.6s;
    }

    .product-box:hover img {
        opacity: 1;
        transform: scale(1.05);
    }

    .price-overlay {
        position: absolute;
        bottom: 20px;
        left: 20px;
        font-family: 'Syncopate', sans-serif;
        font-size: 20px;
        background: #D4AF37;
        color: black;
        padding: 5px 15px;
        font-weight: 700;
    }

    /* BOUTON MALADE */
    div.stButton > button {
        background: transparent !important;
        color: white !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 50px !important;
        font-family: 'Syncopate', sans-serif !important;
        font-size: 10px !important;
        padding: 15px 0 !important;
        width: 100% !important;
        transition: 0.4s !important;
        text-transform: uppercase !important;
    }

    div.stButton > button:hover {
        background: #D4AF37 !important;
        color: black !important;
        box-shadow: 0 0 30px #D4AF37 !important;
    }

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# STRUCTURE CONSERVÉE (FORME OK)
# ---------------------------------------------------------

# 1. HEADER
st.markdown("""
<div class="hero-section">
    <div class="main-title">AWA'S HOUSE</div>
    <p style="letter-spacing:10px; color:white; opacity:0.6; margin-top:20px;">L'EMPIRE DE L'ÉLÉGANCE</p>
</div>
""", unsafe_allow_html=True)

# 2. SERVICES (Glassmorphism)
st.markdown("""
<div class="service-grid">
    <div class="service-card">
        <div style="font-size:30px;">🛡️</div>
        <div style="font-weight:900; letter-spacing:2px; margin-top:10px;">PRESTIGE</div>
    </div>
    <div class="service-card">
        <div style="font-size:30px;">✨</div>
        <div style="font-weight:900; letter-spacing:2px; margin-top:10px;">QUALITÉ</div>
    </div>
    <div class="service-card">
        <div style="font-size:30px;">💎</div>
        <div style="font-weight:900; letter-spacing:2px; margin-top:10px;">EXCLUSIF</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 3. NOS MEILLEURES VENTES
st.markdown("<div class='section-label'>Meilleures Ventes</div>", unsafe_allow_html=True)

ventes = [
    {"n": "Voile Jersey", "p": "1.500", "i": "https://images.unsplash.com/photo-1584030373081-f37b7bb4fa8e?w=800"},
    {"n": "Parfum Oud", "p": "3.500", "i": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=800"},
    {"n": "Pashmina", "p": "2.500", "i": "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?w=800"},
    {"n": "Pince Premium", "p": "500", "i": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=800"}
]

cols_v = st.columns(4)
for i, prod in enumerate(ventes):
    with cols_v[i]:
        st.markdown(f"""
        <div class="product-box">
            <img src="{prod['i']}">
            <div class="price-overlay">{prod['p']}</div>
            <div style="padding:20px; font-weight:900; letter-spacing:2px;">{prod['n'].upper()}</div>
        </div>
        """, unsafe_allow_html=True)
        st.button("ACQUÉRIR", key=f"v_{i}")

st.markdown("<br><br><br>", unsafe_allow_html=True)

# 4. NOS VOILES (Catalogue)
st.markdown("<div class='section-label'>Nos Voiles</div>", unsafe_allow_html=True)

catalogue = [
    {"n": "Soie de Luxe", "p": "3.500", "i": "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=1000"},
    {"n": "Chouchou Satin", "p": "500", "i": "https://images.unsplash.com/photo-1605810756711-645391a61044?w=1000"}
]

c1, c2 = st.columns(2)
for i, p in enumerate(catalogue):
    target = c1 if i == 0 else c2
    with target:
        st.markdown(f"""
        <div class="product-box">
            <img src="{p['i']}" style="height:600px;">
            <div class="price-overlay">{p['p']} FCFA</div>
            <div style="padding:30px;">
                <h1 style="font-family:Playfair Display; font-style:italic; margin:0;">{p['n']}</h1>
                <p style="opacity:0.5; letter-spacing:2px;">COLLECTION LIMITÉE</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("SÉLECTIONNER CETTE PIÈCE", key=f"c_{i}")

# 5. FOOTER
st.markdown("""
<div style="text-align:center; padding:100px 0; border-top:1px solid #333; margin-top:100px;">
    <h1 style="font-family:Syncopate; font-weight:700; color:#D4AF37;">AWA'S HOUSE</h1>
    <p style="letter-spacing:15px; opacity:0.3;">DUBAI • DAKAR • PARIS</p>
</div>
""", unsafe_allow_html=True)
