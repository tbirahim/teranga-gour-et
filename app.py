import streamlit as st

st.set_page_config(page_title="Awa's House", layout="wide")

# ------------------------
# STYLE CSS PREMIUM
# ------------------------
st.markdown("""
<style>
body {
    background-color: #f8f8f8;
}

h1, h2, h3 {
    font-family: 'Segoe UI', sans-serif;
}

.product-card {
    background: white;
    padding: 15px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    transition: 0.3s;
}

.product-card:hover {
    transform: translateY(-5px);
}

.price {
    color: #c59d5f;
    font-weight: bold;
    font-size: 18px;
}

.button {
    background-color: black;
    color: white;
    padding: 8px;
    border-radius: 10px;
    text-align: center;
}

.header {
    text-align: center;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------
# DATA
# ------------------------
produits = [
    {"nom": "Jersey Premium", "prix": 1500, "image": "https://via.placeholder.com/300"},
    {"nom": "Pashmina Luxe", "prix": 3000, "image": "https://via.placeholder.com/300"},
    {"nom": "Soie Élégante", "prix": 3500, "image": "https://via.placeholder.com/300"},
    {"nom": "Chouchou Satin", "prix": 500, "image": "https://via.placeholder.com/300"},
    {"nom": "Parfum Oud", "prix": 2500, "image": "https://via.placeholder.com/300"},
]

if "panier" not in st.session_state:
    st.session_state.panier = []

# ------------------------
# HEADER
# ------------------------
st.markdown("<div class='header'><h1>🧕 Awa's House</h1><p>Élégance & Raffinement</p></div>", unsafe_allow_html=True)

menu = st.radio("", ["Accueil", "Boutique", "Panier"], horizontal=True)

# ------------------------
# ACCUEIL
# ------------------------
if menu == "Accueil":
    st.image("https://via.placeholder.com/1200x400")
    st.markdown("### Découvrez notre collection premium de voiles et accessoires")

# ------------------------
# BOUTIQUE
# ------------------------
elif menu == "Boutique":
    st.markdown("## 🛍️ Nos produits")

    cols = st.columns(3)

    for i, p in enumerate(produits):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="product-card">
                <img src="{p['image']}" width="100%">
                <h3>{p['nom']}</h3>
                <p class="price">{p['prix']} FCFA</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Ajouter 🛒", key=i):
                st.session_state.panier.append(p)

# ------------------------
# PANIER
# ------------------------
elif menu == "Panier":
    st.markdown("## 🛒 Votre panier")

    total = 0

    for i, item in enumerate(st.session_state.panier):
        st.write(f"{item['nom']} - {item['prix']} FCFA")
        total += item["prix"]

    st.markdown(f"### Total : {total} FCFA")

    if st.button("Paiement 💳"):
        st.success("Paiement validé ✅")

# ------------------------
# FOOTER
# ------------------------
st.markdown("---")
st.markdown("<center>© 2025 - Awa's House</center>", unsafe_allow_html=True)
