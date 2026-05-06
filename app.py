import streamlit as st
import time

# ------------------------
# CONFIGURATION DE LA PAGE
# ------------------------
st.set_page_config(page_title="Awa's House | Boutique Premium", page_icon="✨", layout="wide")

# ------------------------
# STYLE CSS PREMIUM
# ------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Poppins:wght@300;400;500&display=swap');

    /* Fond global et typographie */
    [data-testid="stAppViewContainer"] {
        background-color: #FCFBF9;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Titres élégants */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #1A1A1A;
    }

    /* Style des boutons Streamlit pour un effet Luxe */
    div.stButton > button:first-child {
        background-color: #1A1A1A;
        color: #FFFFFF;
        border: 1px solid #1A1A1A;
        border-radius: 0px; /* Bordures carrées pour un style éditorial/luxe */
        padding: 10px 24px;
        width: 100%;
        font-weight: 500;
        letter-spacing: 1px;
        text-transform: uppercase;
        font-size: 12px;
        transition: all 0.4s ease;
    }
    
    div.stButton > button:first-child:hover {
        background-color: #C59D5F;
        color: white;
        border-color: #C59D5F;
        transform: translateY(-2px);
        box-shadow: 0px 8px 15px rgba(197, 157, 95, 0.2);
    }

    /* Couleurs personnalisées pour les textes spécifiques */
    .brand-title {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 600;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }
    .brand-subtitle {
        text-align: center;
        color: #C59D5F;
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-size: 1.2rem;
        margin-top: -10px;
        margin-bottom: 40px;
    }
    .price-tag {
        color: #C59D5F;
        font-weight: 600;
        font-size: 1.2rem;
        margin-top: -10px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ------------------------
# DATA DES PRODUITS
# ------------------------
produits = [
    {"nom": "Voile Jersey Premium", "prix": 1500, "image": "https://images.unsplash.com/photo-1584030373081-f37b7bb4fa8e?auto=format&fit=crop&w=600&q=80", "desc": "Doux, extensible et opaque."},
    {"nom": "Pashmina Luxe", "prix": 3000, "image": "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?auto=format&fit=crop&w=600&q=80", "desc": "Chaud et élégant pour vos soirées."},
    {"nom": "Soie de Médine Élégante", "prix": 3500, "image": "https://images.unsplash.com/photo-1533090481720-856c6e3c1fdc?auto=format&fit=crop&w=600&q=80", "desc": "Le summum du raffinement."},
    {"nom": "Chouchou Satin Volumineux", "prix": 500, "image": "https://images.unsplash.com/photo-1605810756711-645391a61044?auto=format&fit=crop&w=600&q=80", "desc": "Protège vos cheveux avec style."},
    {"nom": "Extrait de Parfum Oud", "prix": 2500, "image": "https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=600&q=80", "desc": "Des notes boisées et orientales intenses."},
    {"nom": "Coffret Cadeau Awa", "prix": 8000, "image": "https://images.unsplash.com/photo-1549465220-1a8b9238cd48?auto=format&fit=crop&w=600&q=80", "desc": "Le cadeau parfait à offrir."}
]

# ------------------------
# LOGIQUE DU PANIER (SESSION STATE)
# ------------------------
if "panier" not in st.session_state:
    st.session_state.panier = {} # Dictionnaire pour gérer les quantités

def ajouter_au_panier(nom, prix):
    if nom in st.session_state.panier:
        st.session_state.panier[nom]["quantite"] += 1
    else:
        st.session_state.panier[nom] = {"prix": prix, "quantite": 1}
    st.toast(f"✨ {nom} ajouté à votre panier !", icon="🛍️")

# ------------------------
# SIDEBAR (MENU & RESUME PANIER)
# ------------------------
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #C59D5F;'>Menu</h2>", unsafe_allow_html=True)
    menu = st.radio("Navigation", ["Accueil", "Boutique", "Mon Panier"], label_visibility="collapsed")
    
    st.markdown("---")
    st.markdown("### 🛒 Résumé")
    total_articles = sum(item["quantite"] for item in st.session_state.panier.values())
    st.write(f"**Articles :** {total_articles}")
    if total_articles > 0:
        st.info("Allez dans 'Mon Panier' pour finaliser votre commande.")

# ------------------------
# HEADER GLOBAL
# ------------------------
st.markdown("<div class='brand-title'>Awa's House</div>", unsafe_allow_html=True)
st.markdown("<div class='brand-subtitle'>Élégance, Pudeur & Raffinement</div>", unsafe_allow_html=True)

# ------------------------
# PAGE: ACCUEIL
# ------------------------
if menu == "Accueil":
    # Image Hero (Bannière)
    st.image("https://images.unsplash.com/photo-1490481651871-ab68de25d43d?auto=format&fit=crop&w=1600&q=80", use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <h3 style='text-align:center;'>Bienvenue dans notre univers</h3>
        <p style='text-align:center; color:#555;'>
        Chez <b>Awa's House</b>, nous croyons que la modestie rime avec élégance. 
        Découvrez notre sélection rigoureuse de voiles haut de gamme, d'accessoires délicats 
        et de parfums enivrants, pensés pour sublimer votre quotidien.
        </p>
        """, unsafe_allow_html=True)

# ------------------------
# PAGE: BOUTIQUE
# ------------------------
elif menu == "Boutique":
    st.markdown("## 🛍️ Notre Collection")
    st.write("Trouvez la pièce parfaite parmi notre sélection de produits de qualité.")
    st.markdown("<br>", unsafe_allow_html=True)

    # Affichage en grille de 3 colonnes
    cols = st.columns(3, gap="large")

    for i, p in enumerate(produits):
        with cols[i % 3]:
            # Utilisation de st.container pour regrouper visuellement les infos
            with st.container():
                st.image(p['image'], use_container_width=True)
                st.markdown(f"### {p['nom']}")
                st.markdown(f"<p style='color:#777; font-size:0.9rem; margin-top:-10px;'>{p['desc']}</p>", unsafe_allow_html=True)
                st.markdown(f"<div class='price-tag'>{p['prix']} FCFA</div>", unsafe_allow_html=True)
                
                # Bouton natif qui appelle la fonction d'ajout
                st.button("Ajouter au panier", key=f"add_{i}", on_click=ajouter_au_panier, args=(p['nom'], p['prix']))
            st.markdown("<br>", unsafe_allow_html=True)

# ------------------------
# PAGE: PANIER
# ------------------------
elif menu == "Mon Panier":
    st.markdown("## 🛒 Votre Panier")
    
    if not st.session_state.panier:
        st.info("Votre panier est actuellement vide. Visitez la Boutique pour y ajouter des merveilles ! ✨")
    else:
        total = 0
        
        # Affichage propre sous forme de colonnes
        col_nom, col_qty, col_prix = st.columns([3, 1, 1])
        with col_nom: st.markdown("**Produit**")
        with col_qty: st.markdown("**Quantité**")
        with col_prix: st.markdown("**Sous-total**")
        
        st.markdown("---")
        
        for nom, details in st.session_state.panier.items():
            sous_total = details["prix"] * details["quantite"]
            total += sous_total
            
            c1, c2, c3 = st.columns([3, 1, 1])
            with c1: st.write(nom)
            with c2: st.write(f"x {details['quantite']}")
            with c3: st.write(f"{sous_total} FCFA")
            
        st.markdown("---")
        
        # Section Total
        st.markdown(f"<h3 style='text-align: right;'>Total à régler : <span style='color: #C59D5F;'>{total} FCFA</span></h3>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Bouton de paiement avec animation
        col_empty, col_pay = st.columns([2, 1])
        with col_pay:
            if st.button("Valider la commande 💳"):
                with st.spinner('Traitement de votre paiement en cours...'):
                    time.sleep(2) # Simulation de chargement
                st.success("Paiement validé avec succès ! Merci pour votre confiance ✅")
                st.balloons()
                # Optionnel : Vider le panier après paiement
                st.session_state.panier = {}
                st.rerun()

# ------------------------
# FOOTER GLOBAL
# ------------------------
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; font-size: 0.8rem;'>
    © 2026 - <b>Awa's House</b><br>
    Conçu avec élégance
</div>
""", unsafe_allow_html=True)
