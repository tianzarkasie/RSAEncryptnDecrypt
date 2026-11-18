import math
import random
import streamlit as st

# ==============================================================================
# 1. KONFIGURASI HALAMAN
# ==============================================================================
st.set_page_config(
    page_title="RSA Encrypt & Decrypt",
    page_icon="🟠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==============================================================================
# 2. CUSTOM CSS (OBSIDIAN BLACK + GLOWING ORANGE + METALLIC SILVER + PARALLAX BLUR)
# ==============================================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

:root {
    --bg-obsidian: #07080b;
    --orange-core: #ff5e14;
    --orange-bright: #ff8533;
    --orange-glow: rgba(255, 94, 20, 0.45);
    --silver-light: #f1f5f9;
    --silver-mid: #94a3b8;
    --silver-dark: #475569;
    --glass-surface: rgba(12, 14, 20, 0.72);
    --glass-border: rgba(226, 232, 240, 0.14);
}

/* Reset & Base */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: var(--bg-obsidian) !important;
    color: var(--silver-light);
    scroll-behavior: smooth;
}

.stApp {
    background-color: #07080b !important;
    overflow-x: hidden;
}

header[data-testid="stHeader"], footer {
    visibility: hidden;
    height: 0;
}

.block-container {
    padding-top: 0 !important;
    padding-bottom: 5rem !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    max-width: 1240px !important;
}

/* ============================================================================
   STICKY HERO BACKGROUND (TERTUTUP & MENJADI BLUR SAAT DI-SCROLL)
   ============================================================================ */
.hero-sticky-wrapper {
    position: sticky;
    top: 0;
    z-index: 1;
    height: 68vh;
    min-height: 490px;
    max-height: 620px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    overflow: hidden;
    padding: 2rem 1rem 5rem 1rem;
    /* Sinar cahaya diagonal halus seperti di gambar referensi */
    background:
        linear-gradient(125deg, rgba(255, 255, 255, 0.045) 0%, rgba(255, 255, 255, 0.01) 28%, transparent 55%),
        radial-gradient(ellipse at 50% 105%, rgba(255, 94, 20, 0.28) 0%, rgba(148, 163, 184, 0.08) 38%, transparent 70%),
        #07080b;
}

/* Lengkungan Cincin Oranye & Silver di Bagian Bawah Hero */
.hero-arc-ring {
    position: absolute;
    bottom: -270px;
    left: 50%;
    transform: translateX(-50%);
    width: 780px;
    height: 440px;
    border-radius: 50%;
    background: linear-gradient(
        90deg,
        #1e293b 0%,
        #94a3b8 14%,
        #ff6a1a 35%,
        #ff944d 52%,
        #e2e8f0 74%,
        #334155 100%
    );
    padding: 16px;
    box-shadow:
        0 -18px 65px rgba(255, 102, 26, 0.42),
        0 -4px 24px rgba(226, 232, 240, 0.22),
        inset 0 4px 18px rgba(255, 255, 255, 0.5);
    pointer-events: none;
    z-index: 0;
}

.hero-arc-ring::after {
    content: "";
    display: block;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: radial-gradient(circle at 50% 0%, #14161d 0%, #07080b 68%);
}

/* Badge Atas Kecil */
.hero-pill-tag {
    position: relative;
    z-index: 2;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(24, 26, 34, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 999px;
    padding: 5px 14px 5px 6px;
    font-size: 0.78rem;
    color: #cbd5e1;
    margin-bottom: 1.2rem;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
}

.hero-pill-dot {
    background: linear-gradient(135deg, #ff5e14, #ff8c42);
    color: #fff;
    font-weight: 700;
    font-size: 0.7rem;
    padding: 3px 10px;
    border-radius: 999px;
    letter-spacing: 0.03em;
}

/* Judul Utama Gradien Silver Metalik */
.hero-main-title {
    position: relative;
    z-index: 2;
    font-size: clamp(2.4rem, 5vw, 4.1rem);
    font-weight: 700;
    line-height: 1.12;
    letter-spacing: -0.035em;
    background: linear-gradient(180deg, #ffffff 15%, #e2e8f0 55%, #94a3b8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.85rem;
}

/* Subjudul Made By */
.hero-made-by {
    position: relative;
    z-index: 2;
    font-size: 0.92rem;
    color: #94a3b8;
    font-weight: 400;
    letter-spacing: 0.01em;
    max-width: 780px;
    line-height: 1.6;
}

.hero-made-by span {
    color: #e2e8f0;
    font-weight: 500;
}

.hero-made-by b {
    color: #ff8533;
    font-weight: 600;
}

/* ============================================================================
   PANEL KONTEN NAIK & MEM-BLUR BACKGROUND SAAT SCROLL
   ============================================================================ */
.glass-scroll-sheet {
    position: relative;
    z-index: 10;
    margin-top: -115px;
    background: rgba(10, 12, 17, 0.68);
    backdrop-filter: blur(26px) saturate(140%);
    -webkit-backdrop-filter: blur(26px) saturate(140%);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 28px;
    padding: 1.75rem 2rem 2.25rem 2rem;
    box-shadow:
        0 -20px 60px rgba(0, 0, 0, 0.75),
        0 25px 70px rgba(0, 0, 0, 0.85),
        inset 0 1px 0 rgba(255, 255, 255, 0.14);
}

/* ============================================================================
   SLIDING PILL NAVBAR (ENCRYPT / DECRYPT) DENGAN LINGKARAN BERWARNA BERGERAK
   ============================================================================ */
div[data-testid="stRadio"] {
    display: flex;
    justify-content: center;
    margin-bottom: 1.5rem;
}

div[data-testid="stRadio"] > div[role="radiogroup"] {
    position: relative;
    display: inline-flex !important;
    flex-direction: row !important;
    background: rgba(15, 17, 24, 0.92);
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 999px;
    padding: 6px;
    gap: 0 !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.55), inset 0 1px 2px rgba(0, 0, 0, 0.6);
}

/* Lingkaran / Kapsul Berwarna yang Bergeser Halus */
div[data-testid="stRadio"] > div[role="radiogroup"]::before {
    content: "";
    position: absolute;
    top: 6px;
    left: 6px;
    width: calc(50% - 6px);
    height: calc(100% - 12px);
    border-radius: 999px;
    transition: transform 0.45s cubic-bezier(0.22, 1, 0.36, 1),
                background 0.45s ease,
                box-shadow 0.45s ease;
    z-index: 0;
}

/* Posisi 1: Encrypt dipilih -> Kapsul Oranye Menyala */
div[data-testid="stRadio"] > div[role="radiogroup"]:has(label:nth-child(1) input:checked)::before {
    transform: translateX(0%);
    background: linear-gradient(135deg, #ff5500 0%, #ff8533 100%);
    box-shadow: 0 0 24px rgba(255, 94, 20, 0.65), inset 0 1px 1px rgba(255, 255, 255, 0.45);
}

/* Posisi 2: Decrypt dipilih -> Bergeser mulus & berubah warna Silver-Cyan/Amber */
div[data-testid="stRadio"] > div[role="radiogroup"]:has(label:nth-child(2) input:checked)::before {
    transform: translateX(100%);
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 55%, #e2e8f0 100%);
    box-shadow: 0 0 24px rgba(56, 189, 248, 0.55), inset 0 1px 1px rgba(255, 255, 255, 0.6);
}

/* Styling tiap item tombol Encrypt & Decrypt */
div[data-testid="stRadio"] > div[role="radiogroup"] > label {
    position: relative;
    z-index: 1;
    width: 155px;
    justify-content: center;
    align-items: center;
    margin: 0 !important;
    padding: 10px 22px !important;
    border-radius: 999px;
    cursor: pointer;
    transition: all 0.3s ease;
    background: transparent !important;
}

/* Sembunyikan lingkaran radio default bawaan browser */
div[data-testid="stRadio"] > div[role="radiogroup"] > label > div:first-child {
    display: none !important;
}

/* Teks di dalam tombol */
div[data-testid="stRadio"] > div[role="radiogroup"] > label p {
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.01em;
    color: #94a3b8 !important;
    transition: color 0.3s ease, transform 0.25s ease;
    margin: 0 !important;
}

/* Hover pada tombol yang tidak aktif */
div[data-testid="stRadio"] > div[role="radiogroup"] > label:hover p {
    color: #ffffff !important;
    transform: scale(1.04);
}

/* Teks tombol aktif */
div[data-testid="stRadio"] > div[role="radiogroup"] > label:has(input:checked) p {
    color: #ffffff !important;
    font-weight: 700 !important;
    text-shadow: 0 1px 4px rgba(0, 0, 0, 0.35);
}

/* ============================================================================
   KARTU & SUB-BLOK DI DALAM WORKSPACE
   ============================================================================ */
.glass-subcard {
    background: rgba(16, 19, 27, 0.78);
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 18px;
    padding: 16px 18px;
    margin-bottom: 14px;
    transition: border-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
}

.glass-subcard:hover {
    border-color: rgba(255, 115, 36, 0.38);
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.4);
}

.subcard-label {
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    color: #94a3b8;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 6px;
}

.subcard-label .dot-orange {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #ff6a1a;
    box-shadow: 0 0 8px #ff6a1a;
}

.subcard-label .dot-silver {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #38bdf8;
    box-shadow: 0 0 8px #38bdf8;
}

/* Kotak Output Angka Panjang (Bisa digeser horizontal) */
.mono-scroll {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.88rem;
    background: rgba(7, 8, 12, 0.88);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: #f1f5f9;
    padding: 11px 14px;
    border-radius: 12px;
    overflow-x: auto;
    white-space: nowrap;
    scrollbar-width: thin;
    scrollbar-color: #475569 rgba(7, 8, 12, 0.88);
}

.mono-scroll::-webkit-scrollbar {
    height: 5px;
}
.mono-scroll::-webkit-scrollbar-thumb {
    background: #475569;
    border-radius: 999px;
}

/* Input Streamlit Dark Metallic */
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
    background-color: rgba(7, 8, 12, 0.9) !important;
    color: #f8fafc !important;
    border: 1px solid rgba(255, 255, 255, 0.14) !important;
    border-radius: 12px !important;
    font-family: 'JetBrains Mono', monospace !important;
    overflow-x: auto !important;
    white-space: nowrap !important;
    transition: border-color 0.25s ease, box-shadow 0.25s ease !important;
}

div[data-testid="stTextInput"] input:focus,
div[data-testid="stNumberInput"] input:focus {
    border-color: #ff6a1a !important;
    box-shadow: 0 0 0 2px rgba(255, 106, 26, 0.25) !important;
}

/* Tombol Eksekusi Utama Oranye Menyala */
div[data-testid="stButton"] > button[kind="primary"] {
    background: linear-gradient(135deg, #ff5500 0%, #ff8533 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.2rem !important;
    box-shadow: 0 8px 25px rgba(255, 94, 20, 0.38) !important;
    transition: transform 0.25s ease, box-shadow 0.25s ease !important;
}

div[data-testid="stButton"] > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 12px 32px rgba(255, 94, 20, 0.58) !important;
}

/* Tombol Sekunder Silver */
div[data-testid="stButton"] > button[kind="secondary"] {
    background: rgba(30, 34, 46, 0.85) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(255, 255, 255, 0.16) !important;
    border-radius: 12px !important;
    font-weight: 500 !important;
    transition: all 0.25s ease !important;
}

div[data-testid="stButton"] > button[kind="secondary"]:hover {
    border-color: #ff8533 !important;
    color: #ffffff !important;
    transform: translateY(-1px) !important;
}

/* Grid Parameter RSA */
.stat-tile {
    background: rgba(9, 11, 16, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 10px 14px;
    margin-bottom: 10px;
}

.stat-title {
    font-size: 0.72rem;
    color: #94a3b8;
    font-weight: 600;
    margin-bottom: 3px;
}

.stat-val-orange {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.88rem;
    font-weight: 600;
    color: #ff8533;
    overflow-x: auto;
    white-space: nowrap;
}

.stat-val-silver {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.88rem;
    font-weight: 600;
    color: #e2e8f0;
    overflow-x: auto;
    white-space: nowrap;
}
</style>
""",
    unsafe_allow_html=True,
)

# ==============================================================================
# 3. LOGIKA INTI KRIPTOGRAFI RSA (SESUAI NOTEBOOK COLAB)
# ==============================================================================
OFFSET = 27


def is_prime(n: int) -> bool:
  """Uji primalitas deterministik Miller-Rabin (akurat 100% hingga > 24 digit)."""
  if n < 2:
    return False
  small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
  if n in small_primes:
    return True
  for p in small_primes:
    if n % p == 0:
      return False

  d = n - 1
  s = 0
  while d % 2 == 0:
    d //= 2
    s += 1

  for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41):
    if a >= n:
      break
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
      continue
    for _ in range(s - 1):
      x = pow(x, 2, n)
      if x == n - 1:
        break
    else:
      return False
  return True


def generate_random_prime(digits: int, exclude: int = None) -> int:
  """Menghasilkan bilangan prima acak (1 - 24 digit)."""
  if digits == 1:
    prima_1_digit = [p for p in [2, 3, 5, 7] if p != exclude]
    return random.choice(prima_1_digit)

  batas_bawah = 10 ** (digits - 1)
  batas_atas = (10**digits) - 1

  while True:
    kandidat = random.randint(batas_bawah, batas_atas)
    if kandidat % 2 == 0:
      kandidat += 1
      if kandidat > batas_atas:
        kandidat -= 2

    if kandidat != exclude and is_prime(kandidat):
      return kandidat


def generate_random_e(m: int) -> int:
  """Memilih nilai e secara acak di mana 1 < e < m dan PBB(e, m) = 1."""
  if m <= 10000:
    kandidat = [e for e in range(3, m, 2) if math.gcd(e, m) == 1]
    if not kandidat:
      kandidat = [e for e in range(2, m) if math.gcd(e, m) == 1]
    return random.choice(kandidat)

  while True:
    e = random.randrange(3, m, 2)
    if math.gcd(e, m) == 1:
      return e


def teks_ke_blok3(teks: str) -> tuple[list[str], list[str], list[str]]:
  """Mengubah teks (huruf besar/kecil) menjadi kode 2 digit lalu blok 3 digit."""
  ascii_asli = []
  kode_2digit = []

  for ch in teks:
    kode = ord(ch)
    if kode < 32 or kode > 126:
      raise ValueError(
          f"Karakter '{ch}' (ASCII {kode}) tidak didukung (hanya ASCII 32-126)."
      )
    ascii_asli.append(str(kode))
    kode_2digit.append(f"{kode - OFFSET:02d}")

  gabungan = "".join(kode_2digit)
  blok_3 = [gabungan[i : i + 3].zfill(3) for i in range(0, len(gabungan), 3)]
  return ascii_asli, kode_2digit, blok_3


def blok3_ke_teks_detail(
    blok_3: list[str],
) -> tuple[list[str], list[str], str]:
  """Mengembalikan list blok 3 digit menjadi (kode 2-digit Pi, ASCII asli, teks asli)."""
  if not blok_3:
    return [], [], ""

  blok_bersih = blok_3.copy()
  total_digit = len(blok_bersih) * 3

  if total_digit % 2 == 1:
    blok_bersih[-1] = blok_bersih[-1][1:]
  elif blok_bersih[-1].startswith("00"):
    blok_bersih[-1] = blok_bersih[-1][2:]

  gabungan = "".join(blok_bersih)
  if len(gabungan) % 2 != 0:
    raise ValueError("Panjang digit gabungan tidak valid.")

  kode_2digit = [gabungan[i : i + 2] for i in range(0, len(gabungan), 2)]
  ascii_list = []
  karakter = []

  for k2 in kode_2digit:
    kode_ascii = int(k2) + OFFSET
    if kode_ascii < 32 or kode_ascii > 126:
      raise ValueError(
          f"Kode ASCII ({kode_ascii}) di luar rentang cetak (32-126)."
      )
    ascii_list.append(str(kode_ascii))
    karakter.append(chr(kode_ascii))

  return kode_2digit, ascii_list, "".join(karakter)


# ==============================================================================
# 4. SESSION STATE
# ==============================================================================
if "enc_result" not in st.session_state:
  st.session_state.enc_result = None
if "dec_result" not in st.session_state:
  st.session_state.dec_result = None
if "mode_selector" not in st.session_state:
  st.session_state.mode_selector = "Encrypt"

# ==============================================================================
# 5. STICKY HERO SECTION (JUDUL, MADE BY, & CINCIN ORANYE-SILVER)
# ==============================================================================
st.markdown(
    """
<div class="hero-sticky-wrapper">
    <div class="hero-pill-tag">
        <span class="hero-pill-dot">RSA ENGINE</span>
        <span>Asymmetric Cryptography • Offset (-27)</span>
    </div>
    <h1 class="hero-main-title">RSA Encrypt &amp; Decrypt</h1>
    <div class="hero-made-by">
        Made by: 
        <span>Christian Zarkasie</span> <b>(002)</b> &nbsp;•&nbsp; 
        <span>Clifton Pratomo</span> <b>(005)</b> &nbsp;•&nbsp; 
        <span>I Nyoman Tisna Satya Wijaya</span> <b>(042)</b>
    </div>
    <div class="hero-arc-ring"></div>
</div>
""",
    unsafe_allow_html=True,
)

# ==============================================================================
# 6. GLASSMORPHISM SCROLL SHEET (NAIK MENUTUPI & MEM-BLUR HERO SAAT DI-SCROLL)
# ==============================================================================
st.markdown('<div class="glass-scroll-sheet">', unsafe_allow_html=True)

# 2-Item Sliding Pill Navbar (Encrypt | Decrypt)
selected_mode = st.radio(
    "Pilih Mode",
    options=["Encrypt", "Decrypt"],
    horizontal=True,
    label_visibility="collapsed",
    key="mode_selector",
)

# ==============================================================================
# TAMPILAN 1: ENCRYPT
# ==============================================================================
if selected_mode == "Encrypt":
  col_left, col_right = st.columns([1.08, 1], gap="large")

  with col_left:
    # BLOK 1: Teks Asli
    st.markdown(
        '<div class="glass-subcard"><div class="subcard-label"><span'
        ' class="dot-orange"></span> Blok 1 · Teks Asli (Plaintext)</div>',
        unsafe_allow_html=True,
    )
    teks_input = st.text_input(
        "Teks Asli",
        value="halooo",
        placeholder="Masukkan pesan (ASCII 32–126)...",
        label_visibility="collapsed",
        key="enc_text_val",
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # BLOK 2: Digit p dan q bersebelahan
    st.markdown(
        '<div class="glass-subcard"><div class="subcard-label"><span'
        ' class="dot-orange"></span> Blok 2 · Panjang Digit Prima p &amp;'
        " q (1–24 Digit)</div>",
        unsafe_allow_html=True,
    )
    c_p, c_q = st.columns(2, gap="medium")
    with c_p:
      digit_p = st.number_input(
          "Digit Prima p",
          min_value=1,
          max_value=24,
          value=4,
          step=1,
          key="in_digit_p",
      )
    with c_q:
      digit_q = st.number_input(
          "Digit Prima q",
          min_value=1,
          max_value=24,
          value=4,
          step=1,
          key="in_digit_q",
      )
    st.markdown("</div>", unsafe_allow_html=True)

    # Tombol Enkripsi
    if st.button(
        "⚡ Generate Kunci & Enkripsi Pesan",
        type="primary",
        use_container_width=True,
    ):
      if not teks_input:
        st.error("Teks asli tidak boleh kosong.")
      elif digit_p == 1 and digit_q == 1:
        st.error(
            "Kombinasi 1 digit untuk p dan q menghasilkan n ≤ 35 (syarat blok"
            " 3-digit: n > 999)."
        )
      else:
        try:
          ascii_asli, kode_2digit, blok_plain = teks_ke_blok3(teks_input)

          while True:
            p_val = generate_random_prime(int(digit_p))
            q_val = generate_random_prime(int(digit_q), exclude=p_val)
            n_val = p_val * q_val
            if n_val > 999:
              break

          m_val = (p_val - 1) * (q_val - 1)
          e_val = generate_random_e(m_val)
          d_val = pow(e_val, -1, m_val)
          blok_cipher = [
              str(pow(int(p_i), e_val, n_val)) for p_i in blok_plain
          ]

          st.session_state.enc_result = {
              "p": p_val,
              "q": q_val,
              "n": n_val,
              "m": m_val,
              "e": e_val,
              "d": d_val,
              "ascii_asli": ascii_asli,
              "kode_2digit": kode_2digit,
              "blok_plain": blok_plain,
              "blok_cipher": blok_cipher,
          }
        except ValueError as err:
          st.error(str(err))

    # BLOK 3: Hasil Ciphertext
    enc_res = st.session_state.enc_result
    cipher_str = (
        " ".join(enc_res["blok_cipher"])
        if enc_res
        else "Hasil blok ciphertext akan muncul di sini..."
    )
    st.markdown(
        f"""
        <div class="glass-subcard" style="margin-top:14px;">
            <div class="subcard-label"><span class="dot-orange"></span> Blok 3 · Hasil Ciphertext (Cᵢ)</div>
            <div class="mono-scroll" style="color:#ff8533; font-weight:600; border-color:rgba(255,106,26,0.35);">
                {cipher_str}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if enc_res:

      def copy_to_decrypt():
        st.session_state.dec_cipher_val = " ".join(enc_res["blok_cipher"])
        st.session_state.dec_d_val = str(enc_res["d"])
        st.session_state.dec_n_val = str(enc_res["n"])
        st.session_state.mode_selector = "Decrypt"

      st.button(
          "↗ Kirim Ciphertext & Kunci ke Tab Decrypt",
          use_container_width=True,
          on_click=copy_to_decrypt,
      )

  # Kolom Kanan: Rincian Parameter & Kunci
  with col_right:
    st.markdown(
        '<div class="glass-subcard" style="height:100%;"><div'
        ' class="subcard-label"><span class="dot-orange"></span> Parameter'
        " Matematis &amp; Kunci Terbentuk</div>",
        unsafe_allow_html=True,
    )
    if enc_res:
      g1, g2 = st.columns(2)
      with g1:
        st.markdown(
            f'<div class="stat-tile"><div class="stat-title">p yang'
            f' terpilih</div><div'
            f' class="stat-val-orange">{enc_res["p"]}</div></div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="stat-tile"><div class="stat-title">n (p × q)</div><div'
            f' class="stat-val-silver">{enc_res["n"]}</div></div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="stat-tile"><div class="stat-title">e (Eksponen'
            f' Publik)</div><div'
            f' class="stat-val-orange">{enc_res["e"]}</div></div>',
            unsafe_allow_html=True,
        )
      with g2:
        st.markdown(
            f'<div class="stat-tile"><div class="stat-title">q yang'
            f' terpilih</div><div'
            f' class="stat-val-orange">{enc_res["q"]}</div></div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="stat-tile"><div class="stat-title">m = (p − 1)(q −'
            f' 1)</div><div'
            f' class="stat-val-silver">{enc_res["m"]}</div></div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="stat-tile"><div class="stat-title">d (Eksponen'
            f' Privat)</div><div'
            f' class="stat-val-orange">{enc_res["d"]}</div></div>',
            unsafe_allow_html=True,
        )

      st.markdown(
          f"""
            <div class="stat-tile">
                <div class="stat-title">Kode ASCII Asli</div>
                <div class="stat-val-silver">{' '.join(enc_res['ascii_asli'])}</div>
            </div>
            <div class="stat-tile">
                <div class="stat-title">Kode 2-Digit (-27) &amp; Blok Plaintext 3-Digit (Pᵢ)</div>
                <div class="stat-val-silver">2-Digit: {' '.join(enc_res['kode_2digit'])} &nbsp;|&nbsp; Blok Pᵢ: {' '.join(enc_res['blok_plain'])}</div>
            </div>
            """,
          unsafe_allow_html=True,
      )

      k1, k2 = st.columns(2)
      with k1:
        st.markdown(
            f"""
                <div class="stat-tile" style="border-color:rgba(255,106,26,0.35);">
                    <div class="stat-title">Kunci Privat (e, n)</div>
                    <div class="stat-val-orange">({enc_res['e']}, {enc_res['n']})</div>
                </div>
                """,
            unsafe_allow_html=True,
        )
      with k2:
        st.markdown(
            f"""
                <div class="stat-tile" style="border-color:rgba(226,232,240,0.28);">
                    <div class="stat-title">Kunci Publik (d, n)</div>
                    <div class="stat-val-silver">({enc_res['d']}, {enc_res['n']})</div>
                </div>
                """,
            unsafe_allow_html=True,
        )
    else:
      st.markdown(
          """
            <div style="padding: 3.5rem 1rem; text-align:center; color:#64748b; font-size:0.9rem;">
                Masukkan teks dan jumlah digit bilangan prima di sebelah kiri, lalu tekan tombol <b>Generate Kunci &amp; Enkripsi Pesan</b> untuk melihat rincian nilai <i>p, q, n, m, e, d</i>, kode ASCII, serta pasangan kunci.
            </div>
            """,
          unsafe_allow_html=True,
      )
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# TAMPILAN 2: DECRYPT
# ==============================================================================
else:
  d_left, d_right = st.columns([1.05, 1], gap="large")

  with d_left:
    # BLOK 1: Input Ciphertext
    st.markdown(
        '<div class="glass-subcard"><div class="subcard-label"><span'
        ' class="dot-silver"></span> Blok 1 · Masukkan Teks Cipher (Pisahkan'
        " Spasi)</div>",
        unsafe_allow_html=True,
    )
    cipher_in = st.text_input(
        "Teks Cipher",
        placeholder="Contoh: 407 436 812",
        label_visibility="collapsed",
        key="dec_cipher_val",
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # BLOK 2: Input d dan n bersebelahan & bisa digeser horizontal jika panjang
    st.markdown(
        '<div class="glass-subcard"><div class="subcard-label"><span'
        ' class="dot-silver"></span> Blok 2 · Nilai d &amp; n (Bersebelahan'
        " &amp; Scrollable)</div>",
        unsafe_allow_html=True,
    )
    col_d, col_n = st.columns(2, gap="medium")
    with col_d:
      d_in = st.text_input(
          "Nilai d", placeholder="Masukkan d...", key="dec_d_val"
      )
      if d_in.strip():
        st.markdown(
            f'<div class="mono-scroll" style="font-size:0.76rem; padding:6px'
            f' 10px;">d: {d_in.strip()}</div>',
            unsafe_allow_html=True,
        )
    with col_n:
      n_in = st.text_input(
          "Nilai n", placeholder="Masukkan n...", key="dec_n_val"
      )
      if n_in.strip():
        st.markdown(
            f'<div class="mono-scroll" style="font-size:0.76rem; padding:6px'
            f' 10px;">n: {n_in.strip()}</div>',
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button(
        "🔓 Dekripsi Ciphertext", type="primary", use_container_width=True
    ):
      blok_c = cipher_in.strip().split()
      if not blok_c or not all(b.isdigit() for b in blok_c):
        st.error(
            "Format ciphertext tidak valid. Masukkan angka yang dipisah spasi."
        )
      elif not d_in.strip().isdigit() or not n_in.strip().isdigit():
        st.error("Nilai d dan n harus berupa bilangan bulat positif.")
      else:
        try:
          d_val = int(d_in.strip())
          n_val = int(n_in.strip())
          blok_plain_dec = []

          for c_str in blok_c:
            c_i = int(c_str)
            p_i = pow(c_i, d_val, n_val)
            if p_i > 999:
              raise ValueError(
                  f"Hasil dekripsi blok ({p_i}) > 999. Periksa kembali nilai d"
                  " dan n."
              )
            blok_plain_dec.append(f"{p_i:03d}")

          pi_2digit, ascii_dec, hasil_teks = blok3_ke_teks_detail(
              blok_plain_dec
          )
          st.session_state.dec_result = {
              "blok_plain": blok_plain_dec,
              "pi_2digit": pi_2digit,
              "ascii_dec": ascii_dec,
              "hasil_teks": hasil_teks,
          }
        except Exception as err:
          st.error(f"Dekripsi gagal: {err}")

  with d_right:
    st.markdown(
        '<div class="glass-subcard" style="height:100%;"><div'
        ' class="subcard-label"><span class="dot-silver"></span> Hasil'
        " Dekripsi &amp; Pemulihan Blok</div>",
        unsafe_allow_html=True,
    )
    dec_res = st.session_state.dec_result
    if dec_res:
      st.markdown(
          f"""
            <div class="stat-tile">
                <div class="stat-title">Teks Asli Berupa Blok (Blok Pᵢ 3-Digit)</div>
                <div class="mono-scroll" style="color:#38bdf8; font-weight:600;">{' '.join(dec_res['blok_plain'])}</div>
            </div>
            <div class="stat-tile">
                <div class="stat-title">Hasil Pᵢ Setelah Diubah Menjadi 2 Digit (Sebelum +27)</div>
                <div class="mono-scroll" style="color:#e2e8f0;">{' '.join(dec_res['pi_2digit'])}</div>
            </div>
            <div class="stat-tile">
                <div class="stat-title">Kode ASCII Asli (+27)</div>
                <div class="mono-scroll" style="color:#94a3b8;">{' '.join(dec_res['ascii_dec'])}</div>
            </div>
            <div class="stat-tile" style="border-color:rgba(255,106,26,0.45); background:rgba(255,94,20,0.08);">
                <div class="stat-title" style="color:#ff8533;">Teks Asli Final</div>
                <div class="mono-scroll" style="color:#ffffff; font-size:1.05rem; font-weight:700; border-color:rgba(255,106,26,0.4);">
                    {dec_res['hasil_teks']}
                </div>
            </div>
            """,
          unsafe_allow_html=True,
      )
    else:
      st.markdown(
          """
            <div style="padding: 3.5rem 1rem; text-align:center; color:#64748b; font-size:0.9rem;">
                Masukkan blok ciphertext serta nilai <b>d</b> dan <b>n</b> di sebelah kiri, lalu tekan <b>Dekripsi Ciphertext</b> untuk melihat blok plaintext, hasil konversi Pᵢ 2-digit, dan teks aslinya.
            </div>
            """,
          unsafe_allow_html=True,
      )
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # Tutup .glass-scroll-sheet
