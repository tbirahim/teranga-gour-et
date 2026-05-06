import streamlit as st

# Configuration
st.set_page_config(page_title="AWA'S HOUSE | LUXURY HUB", layout="wide")

# ---------------------------------------------------------
# LE DESIGN "MAJESTIC" (CSS HAUTE COUTURE)
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,wght@0,400;0,900;1,400&family=Montserrat:wght@100;300;400;600&display=swap');

    /* Variables de couleurs */
    :root {
        --gold: #D4AF37;
        --dark: #0A0A0A;
        --cream: #F5F5F0;
    }

    /* Fond principal avec un dégradé subtil */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 100%);
        color: white;
        font-family: 'Montserrat', sans-serif;
    }

    /* Sidebar Ultra Dark */
    [data-testid="stSidebar"] {
        background-color: #000000 !important;
        border-right: 1px solid var(--gold);
    }

    /* HEADER TITRE MAGALINE */
    .mag-header {
        text-align: center;
        padding: 60px 0;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3);
        margin-bottom: 40px;
    }

    .mag-title {
        font-family: 'Bodoni Moda', serif;
        font-size: 100px;
        font-weight: 900;
        letter-spacing: -5px;
        color: var(--gold);
        line-height: 0.8;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .mag-subtitle {
        font-family: 'Montserrat', sans-serif;
        font-size: 14px;
        letter-spacing: 10px;
        text-transform: uppercase;
        color: white;
        opacity: 0.8;
    }

    /* CARTES PRODUITS GLASSMORPHISM */
    .product-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(212, 175, 55, 0.2);
        border-radius: 0px; /* Style minimaliste chic */
        padding: 0px;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        margin-bottom: 30px;
    }

    .product-card:hover {
        border-color: var(--gold);
        transform: translateY(-10px);
        background: rgba(212, 175, 55, 0.05);
    }

    .product-img {
        width: 100%;
        height: 450px;
        object-fit: cover;
        filter: grayscale(40%);
        transition: 0.5s;
    }

    .product-card:hover .product-img {
        filter: grayscale(0%);
        transform: scale(1.05);
    }

    .product-info {
        padding: 20px;
        text-align: center;
    }

    .product-name {
        font-family: 'Bodoni Moda', serif;
        font-size: 24px;
        margin-bottom: 5px;
    }

    .product-price {
        color: var(--gold);
        font-family: 'Bodoni Moda', serif;
        font-style: italic;
        font-size: 20px;
    }

    /* BOUTON LUXE */
    div.stButton > button {
        background: transparent !important;
        color: var(--gold) !important;
        border: 1px solid var(--gold) !important;
        border-radius: 0px !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        font-size: 12px !important;
        padding: 12px 20px !important;
        width: 100% !important;
        transition: 0.4s !important;
    }

    div.stButton > button:hover {
        background: var(--gold) !important;
        color: black !important;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.4) !important;
    }

    /* Masquer les éléments inutiles de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# NAVIGATION SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:white; text-align:center;'>AWA'S</h2>", unsafe_allow_html=True)
    page = st.radio("SÉLECTION", ["L'ÉDITO", "BOUTIQUE", "PANIER"], label_visibility="collapsed")
    st.markdown("<br><br><br><p style='text-align:center; color:#444;'>Dakar | Paris | Dubai</p>", unsafe_allow_html=True)

# ---------------------------------------------------------
# CONTENU
# ---------------------------------------------------------

# Header Type Magazine
st.markdown("""
<div class="mag-header">
    <div class="mag-title">Awa's House</div>
    <div class="mag-subtitle">Maison de Couture & Raffinement</div>
</div>
""", unsafe_allow_html=True)

if page == "L'ÉDITO":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://images.unsplash.com/photo-1618220179428-22790b461013?w=1200", use_container_width=True)
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-family:Bodoni Moda;'>L'Élégance Pure</h1>", unsafe_allow_html=True)
        st.write("""
        Plus qu'une boutique, une vision. Nous redéfinissons la pudeur par le prisme du luxe. 
        Chaque pièce de notre nouvelle collection "Sahara Glow" est une ode à la féminité sereine.
        """)
        st.markdown("<h2 style='color:#D4AF37;'>✨</h2>", unsafe_allow_html=True)

elif page == "BOUTIQUE":
    # Liste de produits
    produits = [
        {"nom": "Kaftan Signature Noir", "prix": "75.000", "img": "https://images.unsplash.com/photo-1567344231471-4571aebc888a?w=600"},
        {"nom": "Voile de Soie Brute", "prix": "12.500", "img": "https://images.unsplash.com/photo-1584030373081-f37b7bb4fa8e?w=600"},
        {"nom": "Abaya Perle d'Orient", "prix": "45.000", "img": "https://images.unsplash.com/photo-1621184455862-c163dfb30e0f?w=600"},
        {"nom": "Parfum d'Oud Or", "prix": "35.000", "img": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=600"}
    ]

    cols = st.columns(2) # 2 par ligne pour garder le côté "Grand Luxe"
    
    for i, p in enumerate(produits):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="product-card">
                <img src="{p['img']}" class="product-img">
                <div class="product-info">
                    <div class="product-name">{p['nom']}</div>
                    <div class="product-price">{p['prix']} FCFA</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"SÉLECTIONNER — {p['nom']}", key=f"btn_{i}"):
                st.toast(f"{p['nom']} ajouté à votre collection.", icon="💎")

elif page == "PANIER":
    st.markdown("<h1 style='font-family:Bodoni Moda; text-align:center;'>Votre Sélection Privée</h1>", unsafe_allow_html=True)
    st.info("Votre panier est en attente de validation.")
    st.markdown("<br><center><button style='background:white; color:black; border:none; padding:15px 40px; font-weight:bold; letter-spacing:2px;'>COMMANDER MAINTENANT</button></center>", unsafe_allow_html=True)

# Footer
st.markdown("<br><br><p style='text-align:center; opacity:0.3; font-size:10px; letter-spacing:3px;'>MADE FOR AWA'S HOUSE LUXURY HUB © 2026</p>", unsafe_allow_html=True)
