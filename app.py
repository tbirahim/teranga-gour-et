import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Awa's House | Boutique Officielle", page_icon="✨", layout="wide")

# --- INITIALISATION DU PANIER ---
if 'cart' not in st.session_state:
    st.session_state.cart = []

# ---------------------------------------------------------
# DESIGN "PRESTIGE" - RETOUR À TA FORME ORIGINALE
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;600&family=Montserrat:wght@300;600&display=swap');

    [data-testid="stAppViewContainer"] {
        background-color: #FCFAFB;
        font-family: 'Montserrat', sans-serif;
    }

    /* Ta structure de Header */
    .hero-banner {
        background: linear-gradient(rgba(255,255,255,0.5), rgba(255,255,255,0.5)), 
                    url('https://images.unsplash.com/photo-1520006403993-4744f0c846a1?q=80&w=2000');
        background-size: cover;
        height: 350px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-bottom: 2px solid #D4AF37;
        margin-bottom: 40px;
    }

    .brand-name {
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(40px, 8vw, 80px);
        letter-spacing: 10px;
        color: #1a1a1a;
        text-transform: uppercase;
    }

    /* Ta barre de services horizontale */
    .service-bar {
        display: flex;
        justify-content: space-around;
        padding: 30px;
        background: white;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        margin-bottom: 50px;
    }
    .service-item { text-align: center; }
    .service-icon { font-size: 24px; margin-bottom: 5px; }
    .service-label { font-size: 10px; letter-spacing: 2px; font-weight: 600; color: #888; text-transform: uppercase; }

    /* Titres de sections */
    .section-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 40px;
        text-align: center;
        margin-bottom: 40px;
        color: #1a1a1a;
    }

    /* Cartes produits pro */
    .product-card {
        background: white;
        padding: 10px;
        border-radius: 10px;
        transition: 0.3s;
        border-bottom: 1px solid #eee;
    }
    .product-card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.05); }
    
    .price-tag { color: #D4AF37; font-weight: 600; font-size: 14px; margin-top: 10px; }

    /* Boutons de commande */
    div.stButton > button {
        background-color: #1a1a1a !important;
        color: white !important;
        border-radius: 5px !important;
        border: none !important;
        width: 100% !important;
        font-size: 11px !important;
        letter-spacing: 1px !important;
    }
    div.stButton > button:hover { background-color: #D4AF37 !important; }

</style>
""", unsafe_allow_html=True)

# --- FONCTION PANIER ---
def add_item(name, price):
    st.session_state.cart.append({"nom": name, "prix": price})
    st.toast(f"✨ {name} ajouté !")

# ---------------------------------------------------------
# STRUCTURE DE TA PAGE
# ---------------------------------------------------------

# 1. HEADER (L'entrée du magasin)
st.markdown('<div class="hero-banner"><div class="brand-name">Awa\'s House</div><div style="letter-spacing:5px; font-size:12px; color:#555;">QUALITÉ & ÉLÉGANCE</div></div>', unsafe_allow_html=True)

# 2. SERVICES (Tes icônes)
st.markdown("""
<div class="service-bar">
    <div class="service-item"><div class="service-icon">🏺</div><div class="service-label">Prestige</div></div>
    <div class="service-item"><div class="service-icon">🛍️</div><div class="service-label">Retrait</div></div>
    <div class="service-item"><div class="service-icon">🚚</div><div class="service-label">Livraison</div></div>
</div>
""", unsafe_allow_html=True)

# 3. PANIER (SIDEBAR)
with st.sidebar:
    st.markdown("## 🛒 Votre Commande")
    if not st.session_state.cart:
        st.write("Le panier est vide.")
    else:
        total = 0
        for i, item in enumerate(st.session_state.cart):
            st.write(f"**{item['nom']}** - {item['prix']} FCFA")
            total += int(item['prix'].replace(".", ""))
        st.markdown("---")
        st.subheader(f"Total: {total:,} FCFA")
        
        nom = st.text_input("Nom complet")
        adresse = st.text_input("Adresse de livraison")
        
        if st.button("🚀 Commander via WhatsApp"):
            if nom and adresse:
                # Lien WhatsApp
                items_text = "%0A".join([f"- {i['nom']} ({i['prix']} FCFA)" for i in st.session_state.cart])
                msg = f"Bonjour Awa's House, je souhaite commander :%0A{items_text}%0A%0ATotal : {total:,} FCFA%0A%0ANom : {nom}%0AAdresse : {adresse}"
                st.markdown(f'<meta http-equiv="refresh" content="0;URL=https://wa.me/22177XXXXXXX?text={msg}">', unsafe_allow_html=True)
            else:
                st.warning("Remplissez vos infos !")
        if st.button("Vider le panier"):
            st.session_state.cart = []
            st.rerun()

# 4. MEILLEURES VENTES
st.markdown('<div class="section-title">Nos Meilleures Ventes</div>', unsafe_allow_html=True)
v_cols = st.columns(4)
ventes = [
    {"n": "Voile Jersey", "p": "1.500", "i": "https://images.unsplash.com/photo-1583939003579-730e3918a45a?w=400"},
    {"n": "Parfum Oud", "p": "3.500", "i": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=400"},
    {"n": "Pashmina", "p": "2.500", "i": "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?w=400"},
    {"n": "Pince Premium", "p": "500", "i": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=400"}
]

for idx, p in enumerate(ventes):
    with v_cols[idx]:
        st.markdown(f'<div class="product-card"><img src="{p["i"]}" style="width:100%; border-radius:5px;"><div style="font-weight:600; margin-top:10px;">{p["n"]}</div><div class="price-tag">{p["p"]} FCFA</div></div>', unsafe_allow_html=True)
        st.button(f"Prendre {p['n']}", key=f"v_{idx}", on_click=add_item, args=(p['n'], p['p']))

# 5. NOS VOILES (Section Catalogue)
st.markdown('<br><br><div class="section-title">Catalogue Voiles</div>', unsafe_allow_html=True)
c_cols = st.columns(2)
voiles = [
    {"n": "Cachemire", "p": "1.500", "i": "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=800"},
    {"n": "Jersey", "p": "1.500", "i": "https://images.unsplash.com/photo-1584030373081-f37b7bb4fa8e?w=800"},
    {"n": "Soie Royale", "p": "3.500", "i": "https://images.unsplash.com/photo-1533090481720-856c6e3c1fdc?w=800"},
    {"n": "Chouchou Satin", "p": "500", "i": "https://images.unsplash.com/photo-1605810756711-645391a61044?w=800"}
]

for idx, p in enumerate(voiles):
    target = c_cols[0] if idx % 2 == 0 else c_cols[1]
    with target:
        st.markdown(f'<div class="product-card"><img src="{p["i"]}" style="width:100%; height:400px; object-fit:cover; border-radius:5px;"><div style="font-size:20px; font-family:Cormorant Garamond; font-weight:600; margin-top:15px;">{p["n"]}</div><div class="price-tag">{p["p"]} FCFA</div></div>', unsafe_allow_html=True)
        st.button(f"Ajouter {p['n']} au panier", key=f"c_{idx}", on_click=add_item, args=(p['n'], p['p']))

# 6. FOOTER
st.markdown('<div style="text-align:center; padding:50px; color:#aaa; font-size:10px; letter-spacing:2px;">AWA\'S HOUSE © 2026 • DAKAR • PARIS</div>', unsafe_allow_html=True)
