import streamlit as st

# Configuration de la page
st.set_page_config(page_title="AWA'S HOUSE | LUXE RADIANT", layout="wide")

# ---------------------------------------------------------
# DESIGN "RADIANT" (ULTRA-MODERNE & ATTIRANT)
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');

    /* Fond avec dégradé doux et chic */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top right, #FFF5F7 0%, #FFFFFF 50%, #F9F0FF 100%);
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #2D2D2D;
    }

    /* Animation du titre principal */
    @keyframes tracking-in-expand {
      0% { letter-spacing: -0.5em; opacity: 0; }
      40% { opacity: 0.6; }
      100% { opacity: 1; }
    }

    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(3rem, 8vw, 6rem);
        background: linear-gradient(to right, #D4AF37, #FF8AAE, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        text-align: center;
        animation: tracking-in-expand 1.5s cubic-bezier(0.215, 0.610, 0.355, 1.000) both;
        margin-bottom: 0;
    }

    /* Cartes Produits "Cloud Style" */
    .product-card {
        background: white;
        border-radius: 30px;
        padding: 10px;
        box-shadow: 0 20px 40px rgba(255, 138, 174, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.5);
        transition: all 0.4s ease-in-out;
        text-align: center;
        margin-bottom: 25px;
    }

    .product-card:hover {
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 30px 60px rgba(212, 175, 55, 0.2);
    }

    .img-container {
        border-radius: 25px;
        overflow: hidden;
        height: 400px;
        margin-bottom: 15px;
    }

    .img-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: 0.6s;
    }

    /* Bouton "Shopping Express" */
    div.stButton > button {
        background: linear-gradient(90deg, #D4AF37 0%, #FFB444 100%);
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 15px 30px !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 10px 20px rgba(212, 175, 55, 0.3);
        transition: 0.3s !important;
        width: 100%;
    }

    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 30px rgba(255, 138, 174, 0.4);
        background: linear-gradient(90deg, #FF8AAE 0%, #D4AF37 100%);
    }

    /* Menu Horizontal Custom */
    .nav-bar {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 40px;
    }

    .nav-item {
        padding: 10px 25px;
        border-radius: 20px;
        background: white;
        color: #D4AF37;
        font-weight: 600;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# CONTENU DE LA PAGE
# ---------------------------------------------------------

# Header Flashy
st.markdown('<h1 class="main-title">Awa\'s House</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:18px; color:#888; margin-top:-20px; letter-spacing:4px;">L\'ÉCLAT DE VOTRE BEAUTÉ</p>', unsafe_allow_html=True)

# Tabs pour une navigation fluide
tab1, tab2, tab3 = st.tabs(["✨ NOUVEAUTÉS", "💎 COLLECTION", "🛒 MON PANIER"])

with tab1:
    # Banner Hero
    st.image("https://images.unsplash.com/photo-1502716119720-b23a93e5fe1b?w=1600&q=80", use_container_width=True, caption="Collection Sahara Bloom 2026")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div style="background:#FFF0F3; padding:40px; border-radius:30px; border-left:10px solid #FF8AAE;">
            <h2 style="font-family:Playfair Display; color:#FF8AAE;">Soyez Irrésistible</h2>
            <p style="font-size:18px;">Nos tissus sont importés de Dubaï et travaillés à la main pour un tombé parfait. Ne portez pas juste un vêtement, portez une émotion.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.image("https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=800")

with tab2:
    st.markdown("<h2 style='text-align:center; font-family:Playfair Display;'>Le Shop</h2>", unsafe_allow_html=True)
    
    produits = [
        {"nom": "Abaya Silk Royal", "prix": "85.000", "img": "https://images.unsplash.com/photo-1621184455862-c163dfb30e0f?w=600"},
        {"nom": "Voile de Mariée", "prix": "150.000", "img": "https://images.unsplash.com/photo-1583939003579-730e3918a45a?w=600"},
        {"nom": "Parfum Nuit d'Orient", "prix": "45.000", "img": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=600"},
        {"nom": "Coffret Bijoux Awa", "prix": "25.000", "img": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=600"}
    ]

    col1, col2 = st.columns(2)
    
    for i, p in enumerate(produits):
        target_col = col1 if i % 2 == 0 else col2
        with target_col:
            st.markdown(f"""
            <div class="product-card">
                <div class="img-container">
                    <img src="{p['img']}">
                </div>
                <h3 style="font-family:Playfair Display; margin-bottom:0;">{p['nom']}</h3>
                <p style="color:#D4AF37; font-weight:800; font-size:22px;">{p['prix']} FCFA</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"AJOUTER AU PANIER 🛍️", key=f"shop_{i}"):
                st.balloons()
                st.toast("Merveilleux choix ! Ajouté.", icon="💖")
            st.markdown("<br>", unsafe_allow_html=True)

with tab3:
    st.markdown("<div style='text-align:center; padding:100px;'><h3>🛍️ Votre panier attend vos coups de cœur...</h3></div>", unsafe_allow_html=True)

# Footer Pink Gold
st.markdown("""
<div style='background: linear-gradient(90deg, #FF8AAE, #D4AF37); padding:20px; border-radius:50px 50px 0 0; text-align:center; color:white; font-weight:bold;'>
    REJOIGNEZ LA MAISON AWA SUR INSTAGRAM @AWASHOUSE_OFFICIEL
</div>
""", unsafe_allow_html=True)
