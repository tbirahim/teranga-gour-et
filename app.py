import streamlit as st
import time

# Configuration de la page
st.set_page_config(page_title="Awa's House | Maison de Luxe", page_icon="👑", layout="wide")

# ---------------------------------------------------------
# DESIGN ULTRA-PRO & ATTRAYANT (CSS AVANCÉ)
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Montserrat:wght@300;400;600&family=Great+Vibes&display=swap');

    /* Fond et Police Générale */
    [data-testid="stAppViewContainer"] {
        background: #ffffff;
        font-family: 'Montserrat', sans-serif;
    }

    /* Hero Section (Bannière d'entrée) */
    .hero-container {
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                          url('https://images.unsplash.com/photo-1606293926075-69a00dbfde81?q=80&w=1920&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        height: 500px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: white;
        text-align: center;
        border-radius: 0 0 50px 50px;
        margin-bottom: 50px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }

    .hero-title {
        font-family: 'Great Vibes', cursive;
        font-size: 80px;
        margin-bottom: 0px;
        color: #D4AF37; /* Or */
    }

    .hero-subtitle {
        font-family: 'Cinzel', serif;
        font-size: 25px;
        letter-spacing: 5px;
        text-transform: uppercase;
    }

    /* Cartes Produits Stylées */
    .st-emotion-cache-1r6sl7u { /* Container des colonnes */
        padding: 10px;
    }

    .product-box {
        border-radius: 15px;
        overflow: hidden;
        background: white;
        padding-bottom: 20px;
        transition: 0.4s;
        border: 1px solid #f0f0f0;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }

    .product-box:hover {
        transform: scale(1.03);
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);
        border: 1px solid #D4AF37;
    }

    .product-price {
        color: #D4AF37;
        font-weight: bold;
        font-size: 20px;
        font-family: 'Cinzel', serif;
    }

    /* Boutons de Luxe */
    div.stButton > button {
        background: linear-gradient(135deg, #1a1a1a 0%, #333 100%);
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 10px 25px !important;
        font-weight: 600 !important;
        letter-spacing: 1px;
        transition: 0.3s !important;
        width: 80% !important;
        display: block;
        margin: 0 auto;
    }

    div.stButton > button:hover {
        background: #D4AF37 !important;
        color: black !important;
        box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4);
    }

    /* Sidebar élégante */
    [data-testid="stSidebar"] {
        background-color: #1a1a1a;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# DONNÉES & LOGIQUE
# ---------------------------------------------------------
if "panier" not in st.session_state:
    st.session_state.panier = {}

produits = [
    {"id": 1, "nom": "Voile Soie d'Or", "prix": 5500, "img": "https://images.unsplash.com/photo-1584030373081-f37b7bb4fa8e?w=500"},
    {"id": 2, "nom": "Abaya Crystal", "prix": 15000, "img": "https://images.unsplash.com/photo-1621184455862-c163dfb30e0f?w=500"},
    {"id": 3, "nom": "Oud Impérial", "prix": 8500, "img": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=500"},
    {"id": 4, "nom": "Coffret Prestige", "prix": 25000, "img": "https://images.unsplash.com/photo-1549465220-1a8b9238cd48?w=500"},
]

def add_to_cart(p_name, p_price):
    if p_name in st.session_state.panier:
        st.session_state.panier[p_name]['qty'] += 1
    else:
        st.session_state.panier[p_name] = {'price': p_price, 'qty': 1}
    st.toast(f"✅ {p_name} ajouté !", icon="✨")

# ---------------------------------------------------------
# STRUCTURE DE LA PAGE
# ---------------------------------------------------------

# Sidebar
with st.sidebar:
    st.markdown("<h1 style='color:#D4AF37;'>Awa's House</h1>", unsafe_allow_html=True)
    menu = st.radio("Navigation", ["La Maison", "Collection", "Mon Panier"])
    st.write("---")
    st.write("📍 Dakar, Plateau\n\n📞 +221 77 XXX XX XX")

# PAGE ACCUEIL (HERO SECTION)
if menu == "La Maison":
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">Awa's House</div>
        <div class="hero-subtitle">L'Excellence de la Pudeur</div>
        <p style="max-width:600px; margin-top:20px;">Découvrez des pièces uniques conçues pour la femme moderne qui ne fait aucun compromis entre foi et élégance.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1533090481720-856c6e3c1fdc?w=800", caption="Nouvelle Collection")
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.h3("L'art du détail")
        st.write("Chaque tissu est sélectionné avec soin, chaque perle est posée à la main. Notre mission est de vous faire briller.")
        if st.button("Voir la Collection"):
            st.info("Utilisez le menu à gauche pour naviguer !")

# PAGE BOUTIQUE
elif menu == "Collection":
    st.markdown("<h1 style='text-align:center; font-family:Cinzel;'>Nos Exclusivités</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Livraison express en 24h sur Dakar</p><br>", unsafe_allow_html=True)
    
    cols = st.columns(2) # 2 colonnes pour des images plus grandes et plus "impactantes"
    
    for i, p in enumerate(produits):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="product-box">
                <img src="{p['img']}" style="width:100%; height:350px; object-fit:cover;">
                <h3 style="font-family:Cinzel; margin-top:15px;">{p['nom']}</h3>
                <p class="product-price">{p['prix']} FCFA</p>
            </div>
            """, unsafe_allow_html=True)
            st.button(f"Acquérir - {p['nom']}", key=f"btn_{p['id']}", on_click=add_to_cart, args=(p['nom'], p['prix']))
            st.markdown("<br>", unsafe_allow_html=True)

# PAGE PANIER
elif menu == "Mon Panier":
    st.markdown("<h1 style='font-family:Cinzel;'>Votre Sélection</h1>", unsafe_allow_html=True)
    
    if not st.session_state.panier:
        st.write("Votre sélection est vide pour le moment.")
    else:
        total = 0
        for item, info in st.session_state.panier.items():
            sous_total = info['price'] * info['qty']
            total += sous_total
            st.markdown(f"""
            <div style="display:flex; justify-content:space-between; padding:10px; border-bottom:1px solid #eee;">
                <span><b>{item}</b> (x{info['qty']})</span>
                <span style="color:#D4AF37;">{sous_total} FCFA</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown(f"<h2 style='text-align:right;'>Total: {total} FCFA</h2>", unsafe_allow_html=True)
        if st.button("Passer la commande via WhatsApp 📲"):
            st.success("Redirection vers WhatsApp...")
            st.balloons()

# Footer
st.markdown("<br><br><div style='text-align:center; color:#aaa;'>— Awa's House Luxury —</div>", unsafe_allow_html=True)
