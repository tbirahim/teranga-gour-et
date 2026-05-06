import streamlit as st

st.set_page_config(page_title="Awa's House", layout="wide")

# ------------------------
# DATA PRODUITS
# ------------------------
produits = [
    {"nom": "Jersey Premium", "prix": 1500, "image": "https://via.placeholder.com/200", "categorie": "Voile"},
    {"nom": "Pashmina Luxe", "prix": 3000, "image": "https://via.placeholder.com/200", "categorie": "Voile"},
    {"nom": "Soie Élégante", "prix": 3500, "image": "https://via.placeholder.com/200", "categorie": "Voile"},
    {"nom": "Chouchou Satin", "prix": 500, "image": "https://via.placeholder.com/200", "categorie": "Accessoire"},
    {"nom": "Parfum Oud", "prix": 2500, "image": "https://via.placeholder.com/200", "categorie": "Beauté"},
]

# ------------------------
# PANIER
# ------------------------
if "panier" not in st.session_state:
    st.session_state.panier = []

# ------------------------
# SIDEBAR
# ------------------------
st.sidebar.title("🧕 Awa's House")
page = st.sidebar.radio("Navigation", ["Accueil", "Boutique", "Panier"])

# ------------------------
# ACCUEIL
# ------------------------
if page == "Accueil":
    st.title("✨ Awa's House")
    st.subheader("Élégance • Qualité • Raffinement")
    st.image("https://via.placeholder.com/800x300")
    st.write("Bienvenue dans votre boutique de voiles et accessoires.")

# ------------------------
# BOUTIQUE
# ------------------------
elif page == "Boutique":
    st.title("🛍️ Nos Produits")

    # Filtre catégorie
    categories = list(set([p["categorie"] for p in produits]))
    filtre = st.selectbox("Filtrer par catégorie", ["Tous"] + categories)

    cols = st.columns(3)

    for i, p in enumerate(produits):
        if filtre == "Tous" or p["categorie"] == filtre:
            with cols[i % 3]:
                st.image(p["image"])
                st.subheader(p["nom"])
                st.write(f"{p['prix']} FCFA")

                if st.button(f"Ajouter au panier 🛒 {p['nom']}", key=i):
                    st.session_state.panier.append(p)
                    st.success("Ajouté au panier !")

# ------------------------
# PANIER
# ------------------------
elif page == "Panier":
    st.title("🛒 Votre Panier")

    if len(st.session_state.panier) == 0:
        st.warning("Votre panier est vide")
    else:
        total = 0

        for i, item in enumerate(st.session_state.panier):
            col1, col2 = st.columns([3,1])

            with col1:
                st.write(f"{item['nom']} - {item['prix']} FCFA")

            with col2:
                if st.button("❌", key=f"remove_{i}"):
                    st.session_state.panier.pop(i)
                    st.rerun()

            total += item["prix"]

        st.markdown("---")
        st.subheader(f"Total : {total} FCFA")

        # Simulation paiement
        if st.button("Payer 💳"):
            st.success("Paiement simulé réussi ✅")

# ------------------------
# FOOTER
# ------------------------
st.markdown("---")
st.write("© 2025 - Awa's House | Boutique Pro")
