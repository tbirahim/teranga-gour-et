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
    {"n": "Voile Jersey", "p": "1.500", "i": "https://images.unsplash.com/photo-1583939003579-730e3918a45a?w=400"},
    {"n": "Parfum Oud", "p": "3.500", "i": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=400"},
    {"n": "Pashmina", "p": "2.500", "i": "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?w=400"},
    {"n": "Pince Premium", "p": "500", "i": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=400"}
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
