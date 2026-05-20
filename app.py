import streamlit as st
import pandas as pd

# ─── CONFIG ───────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Spotify · Alejandro",
    page_icon="🎵",
    layout="wide",
)

# ─── SPOTIFY THEME (CSS embutido no Python) ───────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

/* FUNDO GERAL */
html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background-color: #121212 !important;
    color: #FFFFFF !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* GRADIENTE VERDE NO TOPO (estilo Spotify) */
[data-testid="stMainBlockContainer"] {
    background: linear-gradient(180deg, #1a3d25 0%, #121212 380px) !important;
    padding-top: 2rem !important;
}

/* SIDEBAR PRETA */
[data-testid="stSidebar"] {
    background-color: #000000 !important;
    border-right: 1px solid #282828 !important;
}
[data-testid="stSidebar"] * {
    color: #B3B3B3 !important;
    font-family: 'DM Sans', sans-serif !important;
}
[data-testid="stSidebar"] label {
    color: #FFFFFF !important;
    font-weight: 600 !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
}

/* TITULO */
h1 {
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 700 !important;
    font-size: 3rem !important;
    letter-spacing: -0.04em !important;
    color: #FFFFFF !important;
}

h2, h3 {
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 700 !important;
    color: #FFFFFF !important;
}

/* SUBTITULO */
[data-testid="stSubheader"] p {
    color: #B3B3B3 !important;
    font-weight: 400 !important;
    letter-spacing: 0.05em !important;
    font-size: 0.9rem !important;
}

/* ARTISTA SELECIONADO */
[data-testid="stMarkdown"] h2 {
    color: #1DB954 !important;
    border-left: 4px solid #1DB954 !important;
    padding-left: 1rem !important;
    margin-top: 1.5rem !important;
}

code {
    background-color: #282828 !important;
    color: #1DB954 !important;
    border-radius: 4px !important;
    padding: 2px 8px !important;
}

/* CARDS DE MÚSICA */
[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
    background-color: #181818 !important;
    border-radius: 8px !important;
    padding: 1.2rem 1.5rem !important;
    margin-bottom: 0.75rem !important;
    border: 1px solid #282828 !important;
    transition: background 0.2s ease, border-color 0.2s ease !important;
}
[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"]:hover {
    background-color: #282828 !important;
    border-color: #1DB954 !important;
}

/* MÉTRICAS */
[data-testid="stMetric"] {
    background-color: #282828 !important;
    border-radius: 8px !important;
    padding: 0.8rem 1rem !important;
    border: 1px solid #333 !important;
}
[data-testid="stMetricLabel"] p {
    color: #B3B3B3 !important;
    font-size: 0.75rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
}
[data-testid="stMetricValue"] {
    color: #1DB954 !important;
    font-size: 1.3rem !important;
    font-weight: 700 !important;
}

/* DIVISOR */
hr {
    border-color: #282828 !important;
    margin: 1.5rem 0 !important;
}

/* BOTÃO SPOTIFY */
[data-testid="stLinkButton"] a {
    background-color: #1DB954 !important;
    color: #000000 !important;
    font-weight: 700 !important;
    border-radius: 500px !important;
    padding: 0.75rem 2rem !important;
    font-size: 0.875rem !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    border: none !important;
    transition: background 0.2s, transform 0.1s !important;
}
[data-testid="stLinkButton"] a:hover {
    background-color: #1ed760 !important;
    transform: scale(1.04) !important;
}

/* VIDEO */
[data-testid="stVideo"] {
    border-radius: 8px !important;
    overflow: hidden !important;
    margin-top: 0.5rem !important;
}

/* SCROLLBAR */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #121212; }
::-webkit-scrollbar-thumb { background: #535353; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #1DB954; }
</style>
""", unsafe_allow_html=True)
# ──────────────────────────────────────────────────────────────────────────────

### 1. Leia o Arquivo Dados_Artistas.csv e o Transforme em dataframe
df = pd.read_parquet("Dados_Artistas.parquet")

### 2. Coloque um titulo na pagina
st.title("Spotify")

### 3. Coloque subtitulo titulo na pagina
st.subheader("desenvolvido por Alejandro")

### 4. Coloque uma logo na sidebar(barra lateral)
st.sidebar.image("logo.png")

### 5. Não mexa abaixo, estamos criando uma selectbox, para selecionar o artista
artistas = st.sidebar.selectbox('Selecione o Artista', df['Artist'].unique())
df_artista = df[df['Artist'] == artistas]

### 6. Coloque Mais um subtitulo que mostre o artista que foi selecionado
st.markdown(
    f"## 🎵 Artista selecionado: `{artistas}`"
)

### 7. Não mexa aqui, pois esse é o for que vai percorer o dataframe
st.write('Aqui estão as músicas mais tocadas:')
for index, row in df_artista.iterrows():
        with st.container():
            st.markdown(f"### 🎵 **{row['Track']}**")
            
            col1, col2 = st.columns(2)
            col1.metric("🎵 Spotify Streams", f"{row['Stream']:,.0f}")
            col2.metric("📺 YouTube Views", f"{row['Views']:,.0f}")
            
            st.video(row['Url_youtube'])
            st.markdown("---")
st.link_button('Ouça no Spotify', url=row['Url_spotify'], type='primary')