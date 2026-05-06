import streamlit as st

# Configuration de la page
st.set_page_config(page_title="AWA'S HOUSE | E-SHOP", layout="wide")

# --- INITIALISATION DU PANIER ---
if 'cart' not in st.session_state:
    st.session_state.cart = []

# ---------------------------------------------------------
# DESIGN "MALADE MENTAL" - DARK & GOLD (CSS INTACT)
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Playfair+Display:ital,wght@0,900;1,900&family=Outfit:wght@100;300;900&display=swap');

    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #1a1a1a 0%, #050505 100%);
        color: white;
        font-family: 'Outfit', sans-serif;
    }

    .main-title {
        font-family: 'Syncopate', sans-serif;
        font-size: 7vw;
        background: linear-gradient(to right, #D4AF37, #FFF, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }

    .card-modern {
        position: relative;
        border-radius: 50px;
        overflow: hidden;
        background: #000;
        transition: 0.6s ease;
        margin-bottom: 20px;
        border: 1px solid #222;
    }

    .card-modern img {
        width: 100%;
        height: 450px;
        object-fit: cover;
        opacity: 0.7;
    }

    .tag-price {
        position: absolute;
        top: 20px;
        left: 20px;
        background: #D4AF37;
        color: black;
        padding: 5px 15px;
        font-weight: 900;
        border-radius: 10px;
    }

    /* Style du Panier */
    .cart-summary {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #D4AF37;
    }

    div.stButton > button {
        background: transparent !important;
        color: white !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 100px !important;
        font-family: 'Syncopate', sans-serif !important;
        width: 100% !important;
        transition: 0.4s !important;
    }

    div.stButton > button:hover {
        background: #D4AF37 !important;
        color: black !important;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGIQUE D'ACHAT ---
def add_to_cart(name, price):
    st.session_state.cart.append({"nom": name, "prix": price})
    st.toast(f"✅ {name} ajouté au panier !")

# ---------------------------------------------------------
# STRUCTURE DU SITE
# ---------------------------------------------------------

# 1. HEADER & PANIER (SIDEBAR)
with st.sidebar:
    st.markdown("<h2 style='color:#D4AF37; font-family:Syncopate;'>VOTRE PANIER</h2>", unsafe_allow_html=True)
    if not st.session_state.cart:
        st.write("Le panier est vide.")
    else:
        total = 0
        for i, item in enumerate(st.session_state.cart):
            col_item, col_del = st.columns([4, 1])
            col_item.write(f"**{item['nom']}**\n{item['prix']} FCFA")
            if col_del.button("❌", key=f"del_{i}"):
                st.session_state.cart.pop(i)
                st.rerun()
            total += int(item['prix'].replace(".", ""))
        
        st.markdown("---")
        st.markdown(f"### TOTAL : {total:,} FCFA")
        
        if st.button("🚀 FINALISER LA COMMANDE"):
            st.session_state.checkout = True

st.markdown("<h1 class='main-title'>AWA'S HOUSE</h1>", unsafe_allow_html=True)

# 2. PRODUITS (MEILLEURES VENTES)
st.markdown("<h2 style='color:#D4AF37; font-style:italic;'>Les Essentiels</h2>", unsafe_allow_html=True)
ventes = [
    {"n": "Voile Jersey", "p": "1.500", "i": "https://images.unsplash.com/photo-1583939003579-730e3918a45a?w=600"},
    {"n": "Parfum Oud", "p": "3.500", "i": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=600"}
]

cols = st.columns(2)
for i, p in enumerate(ventes):
    with cols[i]:
        st.markdown(f'<div class="card-modern"><div class="tag-price">{p["p"]}</div><img src="{p["i"]}"></div>', unsafe_allow_html=True)
        st.button(f"COMMANDER {p['n'].upper()}", key=f"v_{i}", on_click=add_to_cart, args=(p['n'], p['p']))

# 3. CATALOGUE "NOS VOILES"
st.markdown("<h2 style='color:#D4AF37; font-style:italic; margin-top:50px;'>Nos Voiles</h2>", unsafe_allow_html=True)
voiles = [
    {"n": "Cachemire", "p": "1.500", "i": "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=800"},
    {"n": "Jersey Noir", "p": "1.500", "i": "https://images.unsplash.com/photo-1584030373081-f37b7bb4fa8e?w=800"}
]

cols2 = st.columns(2)
for i, p in enumerate(voiles):
    with cols2[i]:
        st.markdown(f'<div class="card-modern"><div class="tag-price">{p["p"]}</div><img src="{p["i"]}"></div>', unsafe_allow_html=True)
        st.button(f"AJOUTER {p['n'].upper()}", key=f"cat_{i}", on_click=add_to_cart, args=(p['n'], p['p']))

# --- SECTION CHECKOUT (FORMULAIRE) ---
if 'checkout' in st.session_state and st.session_state.checkout:
    st.markdown("---")
    st.markdown("<h2 style='color:#D4AF37; text-align:center;'>FINALISATION DE LA COMMANDE</h2>", unsafe_allow_html=True)
    
    with st.form("order_form"):
        nom = st.text_input("Nom Complet")
        tel = st.text_input("Numéro de Téléphone (WhatsApp)")
        adresse = st.text_area("Adresse de Livraison")
        
        # Préparation du message WhatsApp
        items_list = "\\n".join([f"- {item['nom']} ({item['prix']} FCFA)" for item in st.session_state.cart])
        msg = f"Bonjour Awa's House, je souhaite commander :\\n{items_list}\\n\\nNom : {nom}\\nAdresse : {adresse}"
        
        # Lien WhatsApp (remplace le numéro par le tien)
        whatsapp_url = f"https://wa.me/22177XXXXXXX?text={msg.replace(' ', '%20')}"
        
        submit = st.form_submit_button("VALIDER SUR WHATSAPP")
        if submit:
            if nom and tel and adresse:
                st.markdown(f'<meta http-equiv="refresh" content="0;URL={whatsapp_url}">', unsafe_allow_html=True)
                st.success("Redirection vers WhatsApp...")
            else:
                st.error("Veuillez remplir tous les champs.")
