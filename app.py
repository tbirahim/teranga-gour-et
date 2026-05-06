import streamlit as st

# Configuration de la page
st.set_page_config(page_title="AWA'S HOUSE | EXCLUSIVE", page_icon="✨", layout="wide")

# --- GESTION DU PANIER ---
if 'cart' not in st.session_state:
    st.session_state.cart = []

def add_to_cart(name, price):
    st.session_state.cart.append({"nom": name, "prix": price})
    st.toast(f"💎 {name} ajouté au panier")

# ---------------------------------------------------------
# LE DESIGN "MALADE MENTAL" - LUXE & IMPACT
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Playfair+Display:ital,wght@0,900;1,900&family=Outfit:wght@100;300;600&display=swap');

    /* Fond Premium */
    [data-testid="stAppViewContainer"] {
        background: #0A0A0A;
        color: white;
        font-family: 'Outfit', sans-serif;
    }

    /* HEADER STYLE "MAGAZINE" */
    .hero-banner {
        background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                    url('https://images.unsplash.com/photo-1618220179428-22790b461013?w=1600');
        background-size: cover;
        background-position: center;
        height: 450px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-radius: 0 0 80px 80px;
        border-bottom: 3px solid #D4AF37;
        margin-bottom: 60px;
    }

    .main-title {
        font-family: 'Syncopate', sans-serif;
        font-size: 8vw;
        letter-spacing: -2px;
        background: linear-gradient(to right, #D4AF37, #FFF, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }

    /* SERVICES EN VERRE (GLASSMORPHISM) */
    .service-container {
        display: flex;
        justify-content: space-around;
        gap: 20px;
        margin: -100px auto 80px;
        max-width: 90%;
    }
    .service-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 40px 20px;
        border-radius: 30px;
        text-align: center;
        flex: 1;
        transition: 0.4s ease;
    }
    .service-card:hover { transform: translateY(-10px); border-color: #D4AF37; box-shadow: 0 20px 40px rgba(212,175,55,0.2); }

    /* TITRES DE SECTIONS */
    .section-header {
        font-family: 'Playfair Display', serif;
        font-size: 60px;
        font-style: italic;
        color: #D4AF37;
        margin: 60px 0 40px 5%;
        border-left: 4px solid white;
        padding-left: 20px;
    }

    /* CARTES PRODUITS NÉON-GOLD */
    .product-box {
        position: relative;
        border-radius: 40px;
        overflow: hidden;
        background: #111;
        border: 1px solid #222;
        transition: 0.5s;
    }
    .product-box:hover { border-color: #D4AF37; transform: scale(1.02); }
    
    .product-box img {
        width: 100%;
        height: 450px;
        object-fit: cover;
        opacity: 0.7;
        transition: 0.5s;
    }
    .product-box:hover img { opacity: 1; }

    .price-overlay {
        position: absolute;
        top: 20px;
        right: 20px;
        background: #D4AF37;
        color: black;
        padding: 5px 15px;
        font-weight: 900;
        font-family: 'Syncopate', sans-serif;
        border-radius: 10px;
    }

    /* BOUTONS STYLE "MALADE" */
    div.stButton > button {
        background: transparent !important;
        color: white !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 100px !important;
        font-family: 'Syncopate', sans-serif !important;
        font-size: 10px !important;
        padding: 15px 0 !important;
        width: 100% !important;
        margin-top: 10px !important;
        transition: 0.4s !important;
    }
    div.stButton > button:hover {
        background: #D4AF37 !important;
        color: black !important;
        box-shadow: 0 0 30px rgba(212,175,55,0.6) !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# STRUCTURE DU SITE
# ---------------------------------------------------------

# 1. HEADER
st.markdown('<div class="hero-banner"><h1 class="main-title">AWA\'S HOUSE</h1><p style="letter-spacing:10px; opacity:0.6;">L\'EMPIRE DU VOILE</p></div>', unsafe_allow_html=True)

# 2. SERVICES
st.markdown("""
<div class="service-container">
    <div class="service-card"><div style="font-size:30px;">🏺</div><div style="font-weight:900; margin-top:10px; letter-spacing:2px;">PRESTIGE</div></div>
    <div class="service-card"><div style="font-size:30px;">🛍️</div><div style="font-weight:900; margin-top:10px; letter-spacing:2px;">RETRAIT</div></div>
    <div class="service-card"><div style="font-size:30px;">🚚</div><div style="font-weight:900; margin-top:10px; letter-spacing:2px;">LIVRAISON</div></div>
</div>
""", unsafe_allow_html=True)

# 3. PANIER (SIDEBAR)
with st.sidebar:
    st.markdown("<h2 style='color:#D4AF37; font-family:Syncopate;'>VOTRE PANIER</h2>", unsafe_allow_html=True)
    if not st.session_state.cart:
        st.write("Le panier est vide.")
    else:
        total = 0
        for i, item in enumerate(st.session_state.cart):
            st.write(f"🔹 **{item['nom']}** ({item['prix']} FCFA)")
            total += int(item['prix'].replace(".", ""))
        st.markdown("---")
        st.subheader(f"TOTAL : {total:,} FCFA")
        
        nom = st.text_input("Nom Complet")
        adresse = st.text_input("Adresse de Livraison")
        
        if st.button("🚀 VALIDER LA COMMANDE"):
            if nom and adresse:
                # Préparation message WhatsApp
                liste_achats = "%0A".join([f"- {i['nom']} ({i['prix']} FCFA)" for i in st.session_state.cart])
                msg = f"Bonjour Awa's House, je commande :%0A{liste_achats}%0A%0ATotal : {total:,} FCFA%0A%0ANom : {nom}%0AAdresse : {adresse}"
                st.markdown(f'<meta http-equiv="refresh" content="0;URL=https://wa.me/22177XXXXXXX?text={msg}">', unsafe_allow_html=True)
            else:
                st.error("Remplissez vos infos !")
        if st.button("Vider le panier"):
            st.session_state.cart = []
            st.rerun()

# 4. MEILLEURES VENTES
st.markdown("<div class='section-header'>Les Meilleurs</div>", unsafe_allow_html=True)
v_cols = st.columns(4)
ventes = [
    {"n": "Voile Jersey", "p": "1.500", "i": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtowp8MI_nAZn_iJYDd3KFlcwXUuwvehdnAQ&s"},
    {"n": "Parfum et Huile", "p": "3.500", "i": "https://png.pngtree.com/thumb_back/fw800/background/20220930/pngtree-luxury-fragrance-and-perfume-bottles-at-night-parfum-oils-candle-light-photo-image_48968006.jpg"},
    {"n": "Voile de Pashmina", "p": "2.500", "i": "data:image/jpeg;base64,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"},
    {"n": "Voile Pince", "p": "500", "i": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_HXRM9e7jU1TXsPsIx4tL-qeXJOm3m7zPvpn3mPqbPw&s"}
]

for idx, p in enumerate(ventes):
    with v_cols[idx]:
        st.markdown(f'<div class="product-box"><div class="price-overlay">{p["p"]}</div><img src="{p["i"]}"><div style="padding:15px; font-weight:600;">{p["n"]}</div></div>', unsafe_allow_html=True)
        st.button(f"Prendre {p['n']}", key=f"v_{idx}", on_click=add_to_cart, args=(p['n'], p['p']))

# 5. NOS VOILES (Catalogue Complet)
st.markdown("<div class='section-header'>Nos Voiles</div>", unsafe_allow_html=True)
c_cols = st.columns(2)
voiles = [
    {"n": "Cachemire", "p": "1.500", "i": "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=800"},
    {"n": "Jersey Noir", "p": "1.500", "i": "https://images.unsplash.com/photo-1584030373081-f37b7bb4fa8e?w=800"},
    {"n": "Soie Royale", "p": "3.500", "i": "https://images.unsplash.com/photo-1533090481720-856c6e3c1fdc?w=800"},
    {"n": "Chouchou Satin", "p": "500", "i": "https://images.unsplash.com/photo-1605810756711-645391a61044?w=800"}
]

for idx, p in enumerate(voiles):
    target = c_cols[0] if idx % 2 == 0 else c_cols[1]
    with target:
        st.markdown(f"""
        <div class="product-box">
            <div class="price-overlay">{p['p']} FCFA</div>
            <img src="{p['i']}" style="height:600px;">
            <div style="padding:30px;">
                <h1 style="font-family:Playfair Display; font-style:italic; font-size:40px; margin:0; color:#D4AF37;">{p['n']}</h1>
                <p style="opacity:0.5; letter-spacing:5px; font-size:10px;">COLLECTION EXCLUSIVE</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"AJOUTER {p['n'].upper()}", key=f"c_{idx}", on_click=add_to_cart, args=(p['n'], p['p']))

# 6. FOOTER
st.markdown('<div style="text-align:center; padding:100px 0; border-top:1px solid #222; margin-top:100px;"><h1 style="font-family:Syncopate; color:#D4AF37;">AWA\'S HOUSE</h1><p style="letter-spacing:15px; opacity:0.3;">DAKAR • DUBAI • PARIS</p></div>', unsafe_allow_html=True)
