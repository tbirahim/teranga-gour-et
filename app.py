import streamlit as st

# Configuration de la page
st.set_page_config(page_title="AWA'S HOUSE | ULTIMATE", layout="wide")

# ---------------------------------------------------------
# DESIGN "MALADE MENTAL" - DARK & GOLD EDITION
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Playfair+Display:ital,wght@0,900;1,900&family=Outfit:wght@100;300;900&display=swap');

    /* Fond Gradient Profond */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #1a1a1a 0%, #050505 100%);
        color: white;
        font-family: 'Outfit', sans-serif;
    }

    /* HEADER STYLE "MAGAZINE" */
    .hero-container {
        height: 60vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                    url('https://images.unsplash.com/photo-1618220179428-22790b461013?w=1600');
        background-size: cover;
        background-attachment: fixed;
        border-radius: 0 0 120px 120px;
        border-bottom: 2px solid #D4AF37;
        margin-bottom: 80px;
    }

    .main-title {
        font-family: 'Syncopate', sans-serif;
        font-size: 7vw;
        letter-spacing: -2px;
        background: linear-gradient(to right, #D4AF37, #FFF, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }

    /* BARRE DE SERVICES (FORME CONSERVÉE) */
    .service-flex {
        display: flex;
        justify-content: center;
        gap: 25px;
        margin: -120px auto 100px;
        max-width: 85%;
    }

    .service-item {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(212, 175, 55, 0.2);
        padding: 40px 20px;
        border-radius: 40px;
        text-align: center;
        flex: 1;
        transition: 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .service-item:hover {
        transform: scale(1.05);
        border-color: #D4AF37;
        box-shadow: 0 20px 40px rgba(212, 175, 55, 0.1);
    }

    /* SECTION LABELS */
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 70px;
        font-style: italic;
        font-weight: 900;
        color: #D4AF37;
        margin-bottom: 50px;
        padding-left: 5%;
        border-left: 5px solid white;
    }

    /* PRODUCT CARDS - "ELITE STYLE" */
    .card-modern {
        position: relative;
        border-radius: 50px;
        overflow: hidden;
        background: #000;
        transition: 0.6s ease;
        margin-bottom: 40px;
    }

    .card-modern img {
        width: 100%;
        height: 500px;
        object-fit: cover;
        opacity: 0.6;
        transition: 0.8s;
    }

    .card-modern:hover img {
        opacity: 1;
        transform: scale(1.1) rotate(1deg);
    }

    .tag-price {
        position: absolute;
        top: 30px;
        left: 30px;
        background: #D4AF37;
        color: black;
        font-family: 'Syncopate', sans-serif;
        padding: 8px 20px;
        font-weight: 700;
        border-radius: 0 20px 0 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }

    /* BOUTON MALADE MENTAL */
    div.stButton > button {
        background: transparent !important;
        color: white !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 100px !important;
        font-family: 'Syncopate', sans-serif !important;
        font-size: 10px !important;
        height: 60px !important;
        width: 100% !important;
        transition: 0.5s !important;
        letter-spacing: 3px !important;
    }

    div.stButton > button:hover {
        background: #D4AF37 !important;
        color: black !important;
        box-shadow: 0 0 50px rgba(212, 175, 55, 0.5) !important;
        transform: translateY(-5px) !important;
    }

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# STRUCTURE DU SITE
# ---------------------------------------------------------

# 1. HEADER
st.markdown("""
<div class="hero-container">
    <h1 class="main-title">AWA'S HOUSE</h1>
    <p style="letter-spacing:15px; font-weight:100; margin-top:20px;">LA PERFECTION DU VOILE</p>
</div>
""", unsafe_allow_html=True)

# 2. SERVICES
st.markdown("""
<div class="service-flex">
    <div class="service-item">
        <div style="font-size:40px;">🏪</div>
        <div style="font-weight:900; letter-spacing:3px; margin-top:15px; color:#D4AF37;">BOUTIQUE</div>
    </div>
    <div class="service-item">
        <div style="font-size:40px;">🚚</div>
        <div style="font-weight:900; letter-spacing:3px; margin-top:15px; color:#D4AF37;">LIVRAISON</div>
    </div>
    <div class="service-item">
        <div style="font-size:40px;">💎</div>
        <div style="font-weight:900; letter-spacing:3px; margin-top:15px; color:#D4AF37;">PREMIUM</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 3. NOS MEILLEURES VENTES
st.markdown("<div class='section-title'>Les Essentiels</div>", unsafe_allow_html=True)

meilleures_ventes = [
    {"n": "Voile Jersey", "p": "1.500", "i": "https://images.unsplash.com/photo-1583939003579-730e3918a45a?w=800"},
    {"n": "Parfum Oud", "p": "3.500", "i": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=800"},
    {"n": "Pashmina", "p": "2.500", "i": "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?w=800"},
    {"n": "Pince Premium", "p": "500", "i": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=800"}
]

col_v = st.columns(4)
for i, prod in enumerate(meilleures_ventes):
    with col_v[i]:
        st.markdown(f"""
        <div class="card-modern">
            <div class="tag-price">{prod['p']}</div>
            <img src="{prod['i']}">
            <div style="padding:25px; text-align:center;">
                <h3 style="font-family:Syncopate; font-size:16px;">{prod['n']}</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("AJOUTER", key=f"ventes_{i}")

st.markdown("<br><br><br>", unsafe_allow_html=True)

# 4. NOS VOILES (Catalogue mis à jour)
st.markdown("<div class='section-title'>Nos Voiles</div>", unsafe_allow_html=True)

# Ajout de Cachemire et Jersey comme demandé
nos_voiles = [
    {"n": "Cachemire", "p": "1.500", "i": "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=1000"},
    {"n": "Jersey", "p": "1.500", "i": "https://images.unsplash.com/photo-1584030373081-f37b7bb4fa8e?w=1000"},
    {"n": "Soie Royale", "p": "3.500", "i": "https://images.unsplash.com/photo-1533090481720-856c6e3c1fdc?w=1000"},
    {"n": "Chouchou Satin", "p": "500", "i": "https://images.unsplash.com/photo-1605810756711-645391a61044?w=1000"}
]

# Affichage en 2x2 pour un impact visuel maximal
c1, c2 = st.columns(2)
for i, p in enumerate(nos_voiles):
    target = c1 if i % 2 == 0 else c2
    with target:
        st.markdown(f"""
        <div class="card-modern">
            <div class="tag-price">{p['p']} FCFA</div>
            <img src="{p['i']}" style="height:650px;">
            <div style="padding:40px;">
                <h1 style="font-family:Playfair Display; font-style:italic; font-size:45px; margin:0;">{p['n']}</h1>
                <p style="letter-spacing:5px; opacity:0.5; font-size:12px; margin-top:10px;">ÉDITION PRESTIGE</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"SÉLECTIONNER {p['n'].upper()}", key=f"cat_{i}")

# 5. FOOTER
st.markdown("""
<div style="text-align:center; padding:120px 0; border-top:1px solid #333; margin-top:100px;">
    <h1 style="font-family:Syncopate; color:#D4AF37; font-size:40px;">AWA'S HOUSE</h1>
    <p style="letter-spacing:20px; opacity:0.2;">DAKAR • DUBAI • PARIS</p>
    <p style="margin-top:50px; font-size:12px; opacity:0.5;">© 2026 - TOUS DROITS RÉSERVÉS</p>
</div>
""", unsafe_allow_html=True)
