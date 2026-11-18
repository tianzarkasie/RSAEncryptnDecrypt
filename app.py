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
# 2. CUSTOM CSS (TOP NAVBAR + STICKY HERO + RISING GLASS CONTAINER + SWITCH)
# ==============================================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

:root {
    --bg-obsidian: #07080b;
    --orange-core: #ff5500;
    --orange-bright: #ff8533;
    --silver-light: #f8fafc;
    --silver-mid: #94a3b8;
}

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: var(--bg-obsidian) !important;
    color: var(--silver-light);
}

.stApp {
    background-color: #07080b !important;
}

/* Sembunyikan toolbar & footer bawaan Streamlit */
header[data-testid="stHeader"], footer, #MainMenu {
    display: none !important;
}

.block-container {
    padding-top: 0.75rem !important;
    padding-bottom: 5rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    max-width: 1220px !important;
}

/* ============================================================================
   1. TOP NAVBAR STICKY (4 MENU PALING ATAS DENGAN HOVER SMOOTH)
   ============================================================================ */
div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:first-of-type {
    position: sticky;
    top: 0.65rem;
    z-index: 999;
    background: rgba(12, 14, 20, 0.78);
    backdrop-filter: blur(18px) saturate(150%);
    -webkit-backdrop-filter: blur(18px) saturate(150%);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 999px;
    padding: 6px 10px;
    margin-bottom: 0.5rem;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.65);
}

/* Tombol di dalam Top Navbar */
div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:first-of-type button {
    border-radius: 999px !important;
    font-size: 0.86rem !important;
    font-weight: 600 !important;
    padding: 0.42rem 0.9rem !important;
    border: 1px solid transparent !important;
    transition: all 0.3s cubic-bezier(0.22, 1, 0.36, 1) !important;
}

/* Navbar Item Tidak Aktif + Efek Hover */
div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:first-of-type button[kind="secondary"] {
    background: transparent !important;
    color: #94a3b8 !important;
}

div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:first-of-type button[kind="secondary"]:hover {
    background: rgba(255, 255, 255, 0.08) !important;
    color: #ffffff !important;
    border-color: rgba(255, 133, 51, 0.45) !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 16px rgba(255, 94, 20, 0.22) !important;
}

/* Navbar Item Aktif */
div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:first-of-type button[kind="primary"] {
    background: linear-gradient(135deg, #ff5500 0%, #ff8533 100%) !important;
    color: #ffffff !important;
    box-shadow: 0 4px 18px rgba(255, 94, 20, 0.45) !important;
}

/* ============================================================================
   2. STICKY HERO BACKGROUND (DIAM DI TEMPAT SAAT DI-SCROLL)
   ============================================================================ */
.hero-sticky-stage {
    position: sticky;
    top: 4.4rem;
    z-index: 1;
    height: 54vh;
    min-height: 390px;
    max-height: 490px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    overflow: hidden;
    border-radius: 28px;
    padding: 1.5rem 1rem 4.5rem 1rem;
    background:
        linear-gradient(125deg, rgba(255, 255, 255, 0.045) 0%, rgba(255, 255, 255, 0.01) 30%, transparent 55%),
        radial-gradient(ellipse at 50% 105%, rgba(255, 94, 20, 0.28) 0%, rgba(148, 163, 184, 0.07) 40%, transparent 72%),
        #07080b;
}

.hero-badge {
    position: relative;
    z-index: 2;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(22, 25, 34, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 999px;
    padding: 5px 14px 5px 6px;
    font-size: 0.76rem;
    color: #cbd5e1;
    margin-bottom: 1rem;
}

.hero-badge-pill {
    background: linear-gradient(135deg, #ff5500, #ff8533);
    color: #fff;
    font-weight: 700;
    font-size: 0.68rem;
    padding: 3px 10px;
    border-radius: 999px;
    letter-spacing: 0.04em;
}

.hero-title-text {
    position: relative;
    z-index: 2;
    font-size: clamp(2.3rem, 4.8vw, 3.9rem);
    font-weight: 700;
    line-height: 1.12;
    letter-spacing: -0.035em;
    background: linear-gradient(180deg, #ffffff 15%, #e2e8f0 55%, #94a3b8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
}

/* Cincin Lengkungan Oranye-Silver di Bawah Judul */
.hero-arc {
    position: absolute;
    bottom: -275px;
    left: 50%;
    transform: translateX(-50%);
    width: 740px;
    height: 430px;
    border-radius: 50%;
    background: linear-gradient(
        90deg,
        #1e293b 0%,
        #94a3b8 16%,
        #ff6a1a 36%,
        #ff944d 52%,
        #e2e8f0 74%,
        #334155 100%
    );
    padding: 15px;
    box-shadow:
        0 -16px 60px rgba(255, 102, 26, 0.4),
        0 -4px 20px rgba(226, 232, 240, 0.2),
        inset 0 4px 16px rgba(255, 255, 255, 0.45);
    pointer-events: none;
    z-index: 0;
}

.hero-arc::after {
    content: "";
    display: block;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: radial-gradient(circle at 50% 0%, #14161d 0%, #07080b 68%);
}

/* ============================================================================
   3. RISING GLASS DISPLAY CONTAINER (NAIK MENUTUPI & MEM-BLUR HERO SAAT SCROLL)
   ============================================================================ */
div[data-testid="stVerticalBlockBorderWrapper"] {
    position: relative !important;
    z-index: 20 !important;
    margin-top: -85px !important;
    background: rgba(11, 13, 19, 0.72) !important;
    backdrop-filter: blur(26px) saturate(145%) !important;
    -webkit-backdrop-filter: blur(26px) saturate(145%) !important;
    border: 1px solid rgba(255, 255, 255, 0.14) !important;
    border-radius: 28px !important;
    padding: 1.75rem 2rem 2.25rem 2rem !important;
    box-shadow:
        0 -24px 60px rgba(0, 0, 0, 0.78),
        0 25px 70px rgba(0, 0, 0, 0.85),
        inset 0 1px 0 rgba(255, 255, 255, 0.15) !important;
}

/* ============================================================================
   4. CENTER SWITCH BUTTON (ENCRYPT / DECRYPT) DENGAN HOVER & SLIDING PILL
   ============================================================================ */
div[data-testid="stRadio"] {
    display: flex !important;
    justify-content: center !important;
    width: 100% !important;
    margin-bottom: 1.5rem !important;
}

div[data-testid="stRadio"] > div[role="radiogroup"] {
    position: relative !important;
    display: inline-flex !important;
    flex-direction: row !important;
    background: rgba(16, 18, 26, 0.95) !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 999px !important;
    padding: 5px !important;
    gap: 0 !important;
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.55), inset 0 1px 3px rgba(0, 0, 0, 0.65) !important;
}

/* Kapsul Warna Bergerak */
div[data-testid="stRadio"] > div[role="radiogroup"]::before {
    content: "";
    position: absolute;
    top: 5px;
    left: 5px;
    width: calc(50% - 5px);
    height: calc(100% - 10px);
    border-radius: 999px;
    transition: transform 0.42s cubic-bezier(0.22, 1, 0.36, 1),
                background 0.42s ease,
                box-shadow 0.42s ease;
    z-index: 0;
}

/* Aktif: Encrypt (Oranye Menyala) */
div[data-testid="stRadio"] > div[role="radiogroup"]:has(label:nth-child(1) input:checked)::before {
    transform: translateX(0%);
    background: linear-gradient(135deg, #ff5500 0%, #ff8533 100%);
    box-shadow: 0 0 22px rgba(255, 94, 20, 0.65), inset 0 1px 1px rgba(255, 255, 255, 0.45);
}

/* Aktif: Decrypt (Silver-Cyan Metalik) */
div[data-testid="stRadio"] > div[role="radiogroup"]:has(label:nth-child(2) input:checked)::before {
    transform: translateX(100%);
    background: linear-gradient(135deg, #38bdf8 0%, #94a3b8 60%, #e2e8f0 100%);
    box-shadow: 0 0 22px rgba(56, 189, 248, 0.55), inset 0 1px 1px rgba(255, 255, 255, 0.6);
}

div[data-testid="stRadio"] > div[role="radiogroup"] > label {
    position: relative;
    z-index: 1;
    width: 150px;
    justify-content: center;
    align-items: center;
    margin: 0 !important;
    padding: 9px 20px !important;
    border-radius: 999px;
    cursor: pointer;
    background: transparent !important;
    transition: transform 0.25s ease;
}

/* Sembunyikan bulatan radio default */
div[data-testid="stRadio"] > div[role="radiogroup"] > label > div:first-child {
    display: none !important;
}

div[data-testid="stRadio"] > div[role="radiogroup"] > label p {
    font-size: 0.94rem !important;
    font-weight: 600 !important;
    color: #94a3b8 !important;
    margin: 0 !important;
    transition: color 0.25s ease, transform 0.25s ease;
}

/* Hover pada opsi switch */
div[data-testid="stRadio"] > div[role="radiogroup"] > label:hover p {
    color: #ffffff !important;
    transform: scale(1.05);
}

div[data-testid="stRadio"] > div[role="radiogroup"] > label:has(input:checked) p {
    color: #ffffff !important;
    font-weight: 700 !important;
    text-shadow: 0 1px 4px rgba(0, 0, 0, 0.35);
}

/* ============================================================================
   5. KARTU DETAIL & INPUT HORIZONTAL SCROLL
   ============================================================================ */
.block-header {
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    color: #94a3b8;
    margin-bottom: 6px;
    margin-top: 6px;
    display: flex;
    align-items: center;
    gap: 7px;
}

.dot-orange {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #ff6a1a;
    box-shadow: 0 0 8px #ff6a1a;
    display: inline-block;
}

.dot-silver {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #38bdf8;
    box-shadow: 0 0 8px #38bdf8;
    display: inline-block;
}

.mono-scroll {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.88rem;
    background: rgba(7, 8, 12, 0.9);
    border: 1px solid rgba(255, 255, 255, 0.12);
    color: #f1f5f9;
    padding: 11px 14px;
    border-radius: 12px;
    overflow-x: auto;
    white-space: nowrap;
    margin-bottom: 10px;
    scrollbar-width: thin;
    scrollbar-color: #475569 rgba(7, 8, 12, 0.9);
}

.mono-scroll::-webkit-scrollbar {
    height: 5px;
}
.mono-scroll::-webkit-scrollbar-thumb {
    background: #475569;
    border-radius: 999px;
}

div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
    background-color: rgba(7, 8, 12, 0.92) !important;
    color: #f8fafc !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 12px !important;
    font-family: 'JetBrains Mono', monospace !important;
    overflow-x: auto !important;
    white-space: nowrap !important;
}

div[data-testid="stTextInput"] input:focus,
div[data-testid="stNumberInput"] input:focus {
    border-color: #ff6a1a !important;
    box-shadow: 0 0 0 2px rgba(255, 106, 26, 0.25) !important;
}

/* Tombol Aksi di dalam Card */
div[data-testid="stVerticalBlockBorderWrapper"] button[kind="primary"] {
    background: linear-gradient(135deg, #ff5500 0%, #ff8533 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    box-shadow: 0 8px 24px rgba(255, 94, 20, 0.35) !important;
    transition: all 0.25s ease !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 12px 30px rgba(255, 94, 20, 0.55) !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] button[kind="secondary"] {
    background: rgba(24, 28, 38, 0.9) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(255, 255, 255, 0.16) !important;
    border-radius: 12px !important;
    transition: all 0.25s ease !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] button[kind="secondary"]:hover {
    border-color: #ff8533 !important;
    color: #ffffff !important;
}

.stat-tile {
    background: rgba(9, 11, 16, 0.88);
    border: 1px solid rgba(255, 255, 255, 0.09);
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

.info-box {
    background: rgba(14, 17, 25, 0.88);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-left: 4px solid #ff6a1a;
    border-radius: 14px;
    padding: 16px 18px;
    margin-bottom: 12px;
}
</style>
""",
    unsafe_allow_html=True,
)

# ==============================================================================
# 3. LOGIKA INTI KRIPTOGRAFI RSA
# ==============================================================================
OFFSET = 27


def is_prime(n: int) -> bool:
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
if "nav_page" not in st.session_state:
  st.session_state.nav_page = "Kalkulator RSA"
if "enc_result" not in st.session_state:
  st.session_state.enc_result = None
if "dec_result" not in st.session_state:
  st.session_state.dec_result = None
if "mode_selector" not in st.session_state:
  st.session_state.mode_selector = "Encrypt"

# ==============================================================================
# 5. TOP NAVBAR (4 MENU PALING ATAS)
# ==============================================================================
nav_cols = st.columns(4, gap="small")
nav_items = [
    ("🔐 Kalkulator RSA", "Kalkulator RSA"),
    ("⚙️ Proses RSA", "Proses RSA"),
    ("ℹ️ Information", "Information"),
    ("📘 Documentation", "Documentation"),
]

for col, (label, page_key) in zip(nav_cols, nav_items):
  with col:
    is_active = st.session_state.nav_page == page_key
    if st.button(
        label,
        key=f"top_nav_{page_key}",
        use_container_width=True,
        type="primary" if is_active else "secondary",
    ):
      st.session_state.nav_page = page_key
      st.rerun()

# ==============================================================================
# 6. STICKY HERO STAGE (TETAP DIAM SAAT HALAMAN DI-SCROLL)
# ==============================================================================
st.markdown(
    """
<div class="hero-sticky-stage">
    <div class="hero-badge">
        <span class="hero-badge-pill">RSA STUDIO</span>
        <span>Asymmetric Block Cipher • ASCII Offset (-27)</span>
    </div>
    <h1 class="hero-title-text">RSA Encrypt &amp; Decrypt</h1>
    <div class="hero-arc"></div>
</div>
""",
    unsafe_allow_html=True,
)

# ==============================================================================
# 7. RISING GLASS DISPLAY CONTAINER (NAIK & MEM-BLUR HERO SAAT SCROLL)
# ==============================================================================
with st.container(border=True):
  # --------------------------------------------------------------------------
  # HALAMAN 1: KALKULATOR RSA (SWITCH ENCRYPT / DECRYPT DI TENGAH)
  # --------------------------------------------------------------------------
  if st.session_state.nav_page == "Kalkulator RSA":
    selected_mode = st.radio(
        "Switch Mode",
        options=["Encrypt", "Decrypt"],
        horizontal=True,
        label_visibility="collapsed",
        key="mode_selector",
    )

    # === MODE ENCRYPT ===
    if selected_mode == "Encrypt":
      col_left, col_right = st.columns([1.05, 1], gap="large")

      with col_left:
        st.markdown(
            '<div class="block-header"><span class="dot-orange"></span> Blok 1'
            " · Teks Asli (Plaintext)</div>",
            unsafe_allow_html=True,
        )
        teks_input = st.text_input(
            "Teks Asli",
            value="halooo",
            placeholder="Masukkan teks ASCII (32–126)...",
            label_visibility="collapsed",
            key="enc_text_val",
        )

        st.markdown(
            '<div class="block-header"><span class="dot-orange"></span> Blok 2'
            " · Digit Bilangan Prima p &amp; q (1–24)</div>",
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

        st.write("")
        if st.button(
            "⚡ Generate Kunci & Enkripsi",
            type="primary",
            use_container_width=True,
        ):
          if not teks_input:
            st.error("Teks asli tidak boleh kosong.")
          elif digit_p == 1 and digit_q == 1:
            st.error(
                "Kombinasi 1 digit untuk p dan q menghasilkan n ≤ 35 (syarat"
                " blok 3-digit: n > 999)."
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

        enc_res = st.session_state.enc_result
        cipher_str = (
            " ".join(enc_res["blok_cipher"])
            if enc_res
            else "Hasil blok ciphertext akan muncul di sini..."
        )
        st.markdown(
            f"""
                    <div class="block-header" style="margin-top:14px;"><span class="dot-orange"></span> Blok 3 · Hasil Ciphertext (Cᵢ)</div>
                    <div class="mono-scroll" style="color:#ff8533; font-weight:600; border-color:rgba(255,106,26,0.35);">
                        {cipher_str}
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
              "↗ Kirim Ciphertext & Kunci ke Switch Decrypt",
              use_container_width=True,
              on_click=copy_to_decrypt,
          )

      with col_right:
        st.markdown(
            '<div class="block-header"><span class="dot-orange"></span> Detail'
            " Parameter &amp; Kunci RSA</div>",
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
                f'<div class="stat-tile"><div class="stat-title">n (p ×'
                f' q)</div><div'
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
                        <div class="stat-tile" style="padding:3rem 1.2rem; text-align:center; color:#64748b;">
                            Masukkan teks dan jumlah digit bilangan prima di sebelah kiri, lalu klik <b>Generate Kunci &amp; Enkripsi</b> untuk melihat nilai <i>p, q, n, m, e, d</i>, kode ASCII, dan pasangan kunci.
                        </div>
                        """,
              unsafe_allow_html=True,
          )

    # === MODE DECRYPT ===
    else:
      d_left, d_right = st.columns([1.05, 1], gap="large")

      with d_left:
        st.markdown(
            '<div class="block-header"><span class="dot-silver"></span> Blok 1'
            " · Masukkan Teks Cipher (Pisahkan Spasi)</div>",
            unsafe_allow_html=True,
        )
        cipher_in = st.text_input(
            "Teks Cipher",
            placeholder="Contoh: 407 436 812",
            label_visibility="collapsed",
            key="dec_cipher_val",
        )

        st.markdown(
            '<div class="block-header"><span class="dot-silver"></span> Blok 2'
            " · Nilai d &amp; n (Bersebelahan &amp; Scrollable)</div>",
            unsafe_allow_html=True,
        )
        col_d, col_n = st.columns(2, gap="medium")
        with col_d:
          d_in = st.text_input(
              "Nilai d", placeholder="Masukkan nilai d...", key="dec_d_val"
          )
          if d_in.strip():
            st.markdown(
                f'<div class="mono-scroll" style="font-size:0.76rem;'
                f' padding:6px 10px;">d: {d_in.strip()}</div>',
                unsafe_allow_html=True,
            )
        with col_n:
          n_in = st.text_input(
              "Nilai n", placeholder="Masukkan nilai n...", key="dec_n_val"
          )
          if n_in.strip():
            st.markdown(
                f'<div class="mono-scroll" style="font-size:0.76rem;'
                f' padding:6px 10px;">n: {n_in.strip()}</div>',
                unsafe_allow_html=True,
            )

        st.write("")
        if st.button(
            "🔓 Dekripsi Ciphertext", type="primary", use_container_width=True
        ):
          blok_c = cipher_in.strip().split()
          if not blok_c or not all(b.isdigit() for b in blok_c):
            st.error(
                "Format ciphertext tidak valid. Masukkan angka yang dipisah"
                " spasi."
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
                      f"Hasil dekripsi blok ({p_i}) > 999. Periksa kembali"
                      " nilai d dan n."
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
            '<div class="block-header"><span class="dot-silver"></span> Hasil'
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
                        <div class="stat-tile" style="padding:3rem 1.2rem; text-align:center; color:#64748b;">
                            Masukkan blok ciphertext beserta nilai <b>d</b> dan <b>n</b> di sebelah kiri, lalu klik <b>Dekripsi Ciphertext</b> untuk melihat blok plaintext, hasil Pᵢ 2-digit, dan teks aslinya.
                        </div>
                        """,
              unsafe_allow_html=True,
          )

  # --------------------------------------------------------------------------
  # HALAMAN 2: PROSES RSA
  # --------------------------------------------------------------------------
  elif st.session_state.nav_page == "Proses RSA":
    st.markdown("### ⚙️ Alur Kerja Algoritma RSA")
    st.write(
        "RSA (*Rivest–Shamir–Adleman*) mengamankan pesan menggunakan pasangan"
        " kunci asimetris berdasarkan kesulitan faktorisasi bilangan prima"
        " besar."
    )

    p1, p2 = st.columns(2, gap="large")
    with p1:
      st.markdown(
          """
            <div class="info-box">
                <b>1. Pemilihan Dua Bilangan Prima (p dan q)</b><br>
                Memilih dua bilangan prima acak berbeda (<i>p ≠ q</i>) sesuai panjang digit yang diminta.
            </div>
            <div class="info-box">
                <b>2. Menghitung Modulus (n) &amp; Totient (m)</b><br>
                • <b>n = p × q</b> (syarat <i>n &gt; 999</i> untuk menampung blok 3-digit).<br>
                • <b>m = φ(n) = (p − 1)(q − 1)</b>.
            </div>
            <div class="info-box">
                <b>3. Menentukan Eksponen e dan d</b><br>
                • Memilih <b>e</b> acak di mana <i>1 &lt; e &lt; m</i> dan <i>PBB(e, m) = 1</i>.<br>
                • Menghitung <b>d</b> sebagai invers modular sehingga <b>(e × d) mod m = 1</b>.
            </div>
            """,
          unsafe_allow_html=True,
      )
    with p2:
      st.markdown(
          """
            <div class="info-box" style="border-left-color:#38bdf8;">
                <b>4. Pengkodean 2-Digit (-27) &amp; Blok 3-Digit (Pᵢ)</b><br>
                Setiap karakter ASCII (32–126) dikurangi <b>27</b> agar seragam menjadi 2 digit (05–99), digabung, lalu dipotong per <b>3 digit</b>.
            </div>
            <div class="info-box" style="border-left-color:#38bdf8;">
                <b>5. Enkripsi Blok (Cᵢ)</b><br>
                Setiap blok <i>Pᵢ</i> dihitung dengan perpangkatan modular: <b>Cᵢ = Pᵢᵉ mod n</b>.
            </div>
            <div class="info-box" style="border-left-color:#38bdf8;">
                <b>6. Dekripsi &amp; Pemulihan Karakter</b><br>
                Menghitung <b>Pᵢ = Cᵢᵈ mod n</b>, memformat ulang ke 3 digit, melepas nol padding di blok akhir, memecah per <b>2 digit</b>, lalu menambah <b>27</b>.
            </div>
            """,
          unsafe_allow_html=True,
      )

  # --------------------------------------------------------------------------
  # HALAMAN 3: INFORMATION
  # --------------------------------------------------------------------------
  elif st.session_state.nav_page == "Information":
    st.markdown("### ℹ️ Informasi Sistem & Tim Pengembang")
    i1, i2 = st.columns([1.3, 1], gap="large")
    with i1:
      st.markdown(
          """
            <div class="info-box">
                <b>Tentang RSA Encrypt &amp; Decrypt Studio</b><br><br>
                Aplikasi web interaktif untuk simulasi kriptografi asimetris RSA dengan pembangkit bilangan prima acak hingga 24 digit menggunakan uji primalitas deterministik <i>Miller-Rabin</i> serta skema pengkodean blok 3-digit berbasis ASCII Offset (-27).
            </div>
            """,
          unsafe_allow_html=True,
      )
    with i2:
      st.markdown(
          """
            <div class="stat-tile">
                <div class="stat-title">Anggota 1 · NRP 002</div>
                <div class="stat-val-orange">Christian Zarkasie</div>
            </div>
            <div class="stat-tile">
                <div class="stat-title">Anggota 2 · NRP 005</div>
                <div class="stat-val-orange">Clifton Pratomo</div>
            </div>
            <div class="stat-tile">
                <div class="stat-title">Anggota 3 · NRP 042</div>
                <div class="stat-val-orange">I Nyoman Tisna Satya Wijaya</div>
            </div>
            """,
          unsafe_allow_html=True,
      )

  # --------------------------------------------------------------------------
  # HALAMAN 4: DOCUMENTATION
  # --------------------------------------------------------------------------
  elif st.session_state.nav_page == "Documentation":
    st.markdown("### 📘 Dokumentasi Teknis")
    st.markdown("""
        | Fungsi | Parameter | Keluaran | Keterangan |
        | :--- | :--- | :--- | :--- |
        | `generate_random_prime` | `digits`, `exclude` | `int` | Menghasilkan bilangan prima acak 1–24 digit menggunakan uji Miller-Rabin. |
        | `generate_random_e` | `m` | `int` | Memilih eksponen $1 < e < m$ yang relatif prima terhadap $m$. |
        | `teks_ke_blok3` | `teks` | `(ascii, kode_2d, blok_3)` | Mengurangi kode ASCII sebesar `27` menjadi 2 digit, lalu memecahnya menjadi blok 3 digit. |
        | `blok3_ke_teks_detail` | `blok_3` | `(kode_2d, ascii, teks)` | Menghapus nol padding di blok terakhir, memecah per 2 digit, dan mengembalikan `+27`. |
        """)
