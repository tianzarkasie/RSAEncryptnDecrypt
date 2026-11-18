import math
import random
import streamlit as st

# ==============================================================================
# KONFIGURASI HALAMAN & CUSTOM CSS
# ==============================================================================
st.set_page_config(
    page_title="RSA Cryptography Studio | Kriptografi",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --bg-main: #0b0f19;
    --bg-card: #111827;
    --bg-card-hover: #162033;
    --bg-sub: #0d1322;
    --border-subtle: rgba(148, 163, 184, 0.16);
    --accent-enc: #38bdf8;
    --accent-enc-glow: rgba(56, 189, 248, 0.22);
    --accent-dec: #a78bfa;
    --accent-dec-glow: rgba(167, 139, 250, 0.22);
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background-color: var(--bg-main);
    color: var(--text-primary);
}

.stApp {
    background: radial-gradient(circle at 15% 10%, rgba(56, 189, 248, 0.08), transparent 35%),
                radial-gradient(circle at 85% 15%, rgba(167, 139, 250, 0.08), transparent 35%),
                #0b0f19;
}

/* Sembunyikan header bawaan Streamlit */
header[data-testid="stHeader"] {
    background: transparent;
}
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1360px;
}

/* Top Navbar */
.top-navbar {
    background: rgba(17, 24, 39, 0.85);
    backdrop-filter: blur(12px);
    border: 1px solid var(--border-subtle);
    border-radius: 16px;
    padding: 14px 22px;
    margin-bottom: 1.5rem;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
}

.team-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    align-items: center;
}

.team-badge {
    background: rgba(30, 41, 59, 0.9);
    border: 1px solid rgba(148, 163, 184, 0.2);
    color: #e2e8f0;
    padding: 5px 12px;
    border-radius: 999px;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.01em;
    transition: all 0.25s ease;
}

.team-badge:hover {
    border-color: #38bdf8;
    color: #38bdf8;
    transform: translateY(-1px);
}

/* Hero Title */
.hero-box {
    text-align: center;
    padding: 0.5rem 1rem 1.5rem 1rem;
}

.hero-title {
    font-size: 2.35rem;
    font-weight: 800;
    background: linear-gradient(135deg, #f8fafc 20%, #38bdf8 60%, #a78bfa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.4rem;
    letter-spacing: -0.02em;
}

.hero-desc {
    color: var(--text-secondary);
    font-size: 1rem;
    max-width: 760px;
    margin: 0 auto;
    line-height: 1.6;
}

/* Interactive Bubble Card Wrapper */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(180deg, rgba(17, 24, 39, 0.95), rgba(13, 19, 34, 0.98)) !important;
    border: 1px solid rgba(148, 163, 184, 0.18) !important;
    border-radius: 20px !important;
    padding: 1.25rem !important;
    transition: transform 0.35s cubic-bezier(0.22, 1, 0.36, 1),
                box-shadow 0.35s ease,
                border-color 0.35s ease !important;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-4px);
    border-color: rgba(56, 189, 248, 0.5) !important;
    box-shadow: 0 18px 40px -15px rgba(56, 189, 248, 0.22) !important;
}

/* Sub-blok di dalam Card */
.sub-block {
    background: #0b1120;
    border: 1px solid rgba(148, 163, 184, 0.15);
    border-radius: 14px;
    padding: 14px 16px;
    margin-bottom: 12px;
    transition: border-color 0.25s ease;
}

.sub-block:hover {
    border-color: rgba(148, 163, 184, 0.35);
}

.sub-block-title {
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #94a3b8;
    margin-bottom: 8px;
}

/* Horizontal Scrollable Box untuk Angka Panjang (d, n, ciphertext, ascii) */
.scroll-mono-box {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.88rem;
    background: #060a14;
    border: 1px solid rgba(56, 189, 248, 0.25);
    color: #e2e8f0;
    padding: 10px 14px;
    border-radius: 10px;
    overflow-x: auto;
    white-space: nowrap;
    scrollbar-width: thin;
    scrollbar-color: #334155 #060a14;
}

.scroll-mono-box::-webkit-scrollbar {
    height: 6px;
}
.scroll-mono-box::-webkit-scrollbar-track {
    background: #060a14;
    border-radius: 6px;
}
.scroll-mono-box::-webkit-scrollbar-thumb {
    background: #334155;
    border-radius: 6px;
}

/* Input teks d dan n agar bisa digeser horizontal saat angka panjang */
input[type="text"] {
    font-family: 'JetBrains Mono', monospace !important;
    overflow-x: auto !important;
    white-space: nowrap !important;
}

/* Parameter Grid */
.param-item {
    background: #0b1120;
    border: 1px solid rgba(148, 163, 184, 0.14);
    border-radius: 10px;
    padding: 8px 12px;
    margin-bottom: 8px;
}

.param-label {
    font-size: 0.74rem;
    color: #94a3b8;
    font-weight: 600;
}

.param-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.86rem;
    color: #38bdf8;
    font-weight: 600;
    overflow-x: auto;
    white-space: nowrap;
    padding-bottom: 2px;
}

.param-value-purple {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.86rem;
    color: #c4b5fd;
    font-weight: 600;
    overflow-x: auto;
    white-space: nowrap;
    padding-bottom: 2px;
}

/* Step Card untuk Halaman Proses RSA */
.step-card {
    background: #111827;
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-left: 4px solid #38bdf8;
    border-radius: 14px;
    padding: 18px 20px;
    margin-bottom: 14px;
}
.step-card-dec {
    background: #111827;
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-left: 4px solid #a78bfa;
    border-radius: 14px;
    padding: 18px 20px;
    margin-bottom: 14px;
}
</style>
""",
    unsafe_allow_html=True,
)

# ==============================================================================
# LOGIKA INTI KRIPTOGRAFI RSA (SESUAI NOTEBOOK COLAB)
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
  """Mengembalikan list blok 3 digit menjadi (list kode 2-digit Pi, list ASCII, teks asli)."""
  if not blok_3:
    return [], [], ""

  blok_bersih = blok_3.copy()
  total_digit = len(blok_bersih) * 3

  # Lepas padding nol di blok terakhir berdasarkan paritas panjang digit
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
          f"Hasil kode ASCII ({kode_ascii}) di luar rentang karakter cetak"
          " (32-126)."
      )
    ascii_list.append(str(kode_ascii))
    karakter.append(chr(kode_ascii))

  return kode_2digit, ascii_list, "".join(karakter)


# ==============================================================================
# STATE MANAGEMENT
# ==============================================================================
if "active_mode" not in st.session_state:
  st.session_state.active_mode = (
      "enkripsi"  # "enkripsi" | "dekripsi" | "seimbang"
  )
if "enc_result" not in st.session_state:
  st.session_state.enc_result = None
if "dec_result" not in st.session_state:
  st.session_state.dec_result = None
if "nav_page" not in st.session_state:
  st.session_state.nav_page = "Kalkulator RSA"


# ==============================================================================
# NAVBAR & HEADER IDENTITAS
# ==============================================================================
st.markdown(
    """
<div class="top-navbar">
    <div style="display:flex; align-items:center; gap:10px;">
        <span style="font-size:1.3rem;">🔐</span>
        <span style="font-weight:800; font-size:1.05rem; letter-spacing:-0.01em;">RSA CRYPTOGRAPHY LAB</span>
    </div>
    <div class="team-badges">
        <span class="team-badge">👤 Christian Zarkasie (002)</span>
        <span class="team-badge">👤 Clifton Pratomo (005)</span>
        <span class="team-badge">👤 I Nyoman Tisna Satya Wijaya (042)</span>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# Navigasi Halaman Utama
nav_cols = st.columns([1, 1, 1, 1])
pages = [
    ("🧮 Kalkulator RSA", "Kalkulator RSA"),
    ("⚙️ Proses RSA", "Proses RSA"),
    ("ℹ️ Information", "Information"),
    ("📘 Documentation", "Documentation"),
]

for col, (label, page_name) in zip(nav_cols, pages):
  with col:
    is_current = st.session_state.nav_page == page_name
    if st.button(
        label,
        key=f"nav_{page_name}",
        use_container_width=True,
        type="primary" if is_current else "secondary",
    ):
      st.session_state.nav_page = page_name
      st.rerun()

# Judul & Deskripsi Aplikasi
st.markdown(
    """
<div class="hero-box">
    <div class="hero-title">Simulasi & Kalkulator Kriptografi RSA</div>
    <div class="hero-desc">
        Platform interaktif untuk pembangkitan kunci asimetris bilangan prima hingga 24 digit, 
        pengkodean blok 3-digit berbasis ASCII Offset (-27), serta proses enkripsi dan dekripsi pesan secara real-time.
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ==============================================================================
# HALAMAN 1: KALKULATOR RSA (DUA CARD INTERAKTIF ENKRIPSI & DEKRIPSI)
# ==============================================================================
if st.session_state.nav_page == "Kalkulator RSA":
  # Rasio lebar kolom dinamis saat bubble card Enkripsi atau Dekripsi diklik
  if st.session_state.active_mode == "enkripsi":
    col_widths = [2.25, 1.0]
  elif st.session_state.active_mode == "dekripsi":
    col_widths = [1.0, 2.25]
  else:
    col_widths = [1.0, 1.0]

  col_enc, col_dec = st.columns(col_widths, gap="large")

  # --------------------------------------------------------------------------
  # DIV 1: CARD ENKRIPSI
  # --------------------------------------------------------------------------
  with col_enc:
    with st.container(border=True):
      hdr_l, hdr_r = st.columns([3, 1.4])
      with hdr_l:
        st.markdown("### 🔒 Enkripsi Pesan")
        st.caption(
            "Ubah teks asli menjadi blok ciphertext menggunakan kunci publik."
        )
      with hdr_r:
        if st.session_state.active_mode != "enkripsi":
          if st.button(
              "⤢ Perbesar Enkripsi",
              key="expand_enc",
              use_container_width=True,
          ):
            st.session_state.active_mode = "enkripsi"
            st.rerun()
        else:
          st.markdown(
              "<div style='text-align:right; color:#38bdf8; font-size:0.8rem;"
              " font-weight:700; padding-top:8px;'>● MODE FOKUS</div>",
              unsafe_allow_html=True,
          )

      st.markdown("---")

      # --- 3 BLOK UTAMA ENKRIPSI ---
      # BLOK 1: Teks Asli
      st.markdown(
          '<div class="sub-block"><div class="sub-block-title">Blok 1 · Teks'
          " Asli (Plaintext)</div>",
          unsafe_allow_html=True,
      )
      teks_input = st.text_input(
          "Masukkan teks (ASCII 32–126)",
          value="halooo",
          placeholder="Contoh: Halo Dunia 123!",
          key="enc_teks_input",
          label_visibility="collapsed",
      )
      st.markdown("</div>", unsafe_allow_html=True)

      # BLOK 2: Nilai Digit p dan q (1 blok berisi 2 input bersebelahan)
      st.markdown(
          '<div class="sub-block"><div class="sub-block-title">Blok 2 ·'
          " Panjang Digit Bilangan Prima (p & q)</div>",
          unsafe_allow_html=True,
      )
      pq_col1, pq_col2 = st.columns(2, gap="medium")
      with pq_col1:
        digit_p = st.number_input(
            "Digit Prima p (1–24)",
            min_value=1,
            max_value=24,
            value=4,
            step=1,
            key="digit_p_input",
        )
      with pq_col2:
        digit_q = st.number_input(
            "Digit Prima q (1–24)",
            min_value=1,
            max_value=24,
            value=4,
            step=1,
            key="digit_q_input",
        )
      st.markdown("</div>", unsafe_allow_html=True)

      # Tombol Eksekusi Enkripsi
      if st.button(
          "⚡ Generate Kunci & Enkripsi",
          type="primary",
          use_container_width=True,
          key="btn_run_enc",
      ):
        st.session_state.active_mode = "enkripsi"
        if not teks_input:
          st.error("Teks asli tidak boleh kosong.")
        elif digit_p == 1 and digit_q == 1:
          st.error(
              "Kombinasi 1 digit untuk p dan q menghasilkan n ≤ 35 (harus n >"
              " 999 untuk blok 3-digit). Gunakan minimal 2 digit pada salah"
              " satu prima."
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
      cipher_preview = (
          " ".join(enc_res["blok_cipher"])
          if enc_res
          else "Belum ada ciphertext — tekan tombol di atas."
      )
      st.markdown(
          f"""
            <div class="sub-block" style="margin-top:12px;">
                <div class="sub-block-title">Blok 3 · Hasil Ciphertext (Cᵢ)</div>
                <div class="scroll-mono-box" style="border-color: rgba(56, 189, 248, 0.45); color: #38bdf8; font-weight:600;">
                    {cipher_preview}
                </div>
            </div>
            """,
          unsafe_allow_html=True,
      )

      if enc_res:
        # Tombol bantu untuk salin cepat ke form dekripsi
        if st.button(
            "📤 Kirim Ciphertext & Kunci ke Panel Dekripsi",
            use_container_width=True,
            key="send_to_dec",
        ):
          st.session_state.dec_cipher_input = " ".join(enc_res["blok_cipher"])
          st.session_state.dec_d_input = str(enc_res["d"])
          st.session_state.dec_n_input = str(enc_res["n"])
          st.session_state.active_mode = "dekripsi"
          st.rerun()

        st.markdown("#### 📊 Detail Parameter & Kunci RSA")

        # Parameter p, q, n, m, e, d
        p_col1, p_col2 = st.columns(2)
        with p_col1:
          st.markdown(
              f'<div class="param-item"><div class="param-label">p yang'
              f' terpilih</div><div class="param-value">{enc_res["p"]}</div></div>',
              unsafe_allow_html=True,
          )
          st.markdown(
              f'<div class="param-item"><div class="param-label">n (p ×'
              f' q)</div><div class="param-value">{enc_res["n"]}</div></div>',
              unsafe_allow_html=True,
          )
          st.markdown(
              f'<div class="param-item"><div class="param-label">e (Eksponen'
              f' Publik)</div><div class="param-value">{enc_res["e"]}</div></div>',
              unsafe_allow_html=True,
          )
        with p_col2:
          st.markdown(
              f'<div class="param-item"><div class="param-label">q yang'
              f' terpilih</div><div class="param-value">{enc_res["q"]}</div></div>',
              unsafe_allow_html=True,
          )
          st.markdown(
              f'<div class="param-item"><div class="param-label">m = φ(n) ='
              f' (p-1)(q-1)</div><div class="param-value">{enc_res["m"]}</div></div>',
              unsafe_allow_html=True,
          )
          st.markdown(
              f'<div class="param-item"><div class="param-label">d (Eksponen'
              f' Privat)</div><div class="param-value">{enc_res["d"]}</div></div>',
              unsafe_allow_html=True,
          )

        # Kode ASCII & Blok Plaintext
        st.markdown(
            f"""
                <div class="param-item">
                    <div class="param-label">Kode ASCII Asli</div>
                    <div class="param-value" style="color:#e2e8f0;">{' '.join(enc_res['ascii_asli'])}</div>
                </div>
                <div class="param-item">
                    <div class="param-label">Kode 2-Digit (ASCII - 27) & Blok Plaintext (Pᵢ)</div>
                    <div class="param-value" style="color:#93c5fd;">
                        2-Digit: {' '.join(enc_res['kode_2digit'])} &nbsp;|&nbsp; Blok 3-Digit: {' '.join(enc_res['blok_plain'])}
                    </div>
                </div>
                """,
            unsafe_allow_html=True,
        )

        # Kunci Privat (e, n) & Kunci Publik (d, n) sesuai spesifikasi sketsa
        k_col1, k_col2 = st.columns(2)
        with k_col1:
          st.markdown(
              f"""
                    <div class="param-item" style="border-color: rgba(56, 189, 248, 0.35);">
                        <div class="param-label">Kunci Privat (e, n)</div>
                        <div class="param-value">({enc_res['e']}, {enc_res['n']})</div>
                    </div>
                    """,
              unsafe_allow_html=True,
          )
        with k_col2:
          st.markdown(
              f"""
                    <div class="param-item" style="border-color: rgba(167, 139, 250, 0.35);">
                        <div class="param-label">Kunci Publik (d, n)</div>
                        <div class="param-value-purple">({enc_res['d']}, {enc_res['n']})</div>
                    </div>
                    """,
              unsafe_allow_html=True,
          )

  # --------------------------------------------------------------------------
  # DIV 2: CARD DEKRIPSI
  # --------------------------------------------------------------------------
  with col_dec:
    with st.container(border=True):
      dhdr_l, dhdr_r = st.columns([3, 1.4])
      with dhdr_l:
        st.markdown("### 🔓 Dekripsi Pesan")
        st.caption(
            "Kembalikan blok ciphertext menjadi teks asli menggunakan d dan n."
        )
      with dhdr_r:
        if st.session_state.active_mode != "dekripsi":
          if st.button(
              "⤢ Perbesar Dekripsi",
              key="expand_dec",
              use_container_width=True,
          ):
            st.session_state.active_mode = "dekripsi"
            st.rerun()
        else:
          st.markdown(
              "<div style='text-align:right; color:#a78bfa; font-size:0.8rem;"
              " font-weight:700; padding-top:8px;'>● MODE FOKUS</div>",
              unsafe_allow_html=True,
          )

      st.markdown("---")

      # BLOK 1: Input Teks Cipher
      st.markdown(
          '<div class="sub-block"><div class="sub-block-title">Blok 1 ·'
          " Masukkan Teks Cipher (Pisahkan Spasi)</div>",
          unsafe_allow_html=True,
      )
      cipher_input = st.text_input(
          "Blok Ciphertext",
          placeholder="Contoh: 407 436 912",
          key="dec_cipher_input",
          label_visibility="collapsed",
      )
      st.markdown("</div>", unsafe_allow_html=True)

      # BLOK 2: Input d dan n bersebelahan (dengan horizontal scroll untuk angka panjang)
      st.markdown(
          '<div class="sub-block"><div class="sub-block-title">Blok 2 · Input'
          " Nilai d dan n (Bersebelahan & Scrollable)</div>",
          unsafe_allow_html=True,
      )
      dn_col1, dn_col2 = st.columns(2, gap="medium")
      with dn_col1:
        d_input_str = st.text_input(
            "Nilai d",
            placeholder="Masukkan nilai d...",
            key="dec_d_input",
        )
        if d_input_str.strip():
          st.markdown(
              f'<div class="scroll-mono-box" style="font-size:0.76rem;'
              f' padding:6px 10px; border-color:rgba(167,139,250,0.3);">d:'
              f" {d_input_str.strip()}</div>",
              unsafe_allow_html=True,
          )
      with dn_col2:
        n_input_str = st.text_input(
            "Nilai n",
            placeholder="Masukkan nilai n...",
            key="dec_n_input",
        )
        if n_input_str.strip():
          st.markdown(
              f'<div class="scroll-mono-box" style="font-size:0.76rem;'
              f' padding:6px 10px; border-color:rgba(167,139,250,0.3);">n:'
              f" {n_input_str.strip()}</div>",
              unsafe_allow_html=True,
          )
      st.markdown("</div>", unsafe_allow_html=True)

      # Tombol Eksekusi Dekripsi
      if st.button(
          "🗝️ Dekripsi Ciphertext",
          type="primary",
          use_container_width=True,
          key="btn_run_dec",
      ):
        st.session_state.active_mode = "dekripsi"
        blok_c = cipher_input.strip().split()
        if not blok_c or not all(b.isdigit() for b in blok_c):
          st.error("Format ciphertext tidak valid. Masukkan angka dipisah spasi.")
        elif (
            not d_input_str.strip().isdigit()
            or not n_input_str.strip().isdigit()
        ):
          st.error("Nilai d dan n harus berupa bilangan bulat positif.")
        else:
          try:
            d_val = int(d_input_str.strip())
            n_val = int(n_input_str.strip())
            blok_plain_dec = []

            for c_str in blok_c:
              c_i = int(c_str)
              p_i = pow(c_i, d_val, n_val)
              if p_i > 999:
                raise ValueError(
                    f"Hasil dekripsi blok ({p_i}) melebihi 3 digit. Periksa"
                    " kembali nilai d dan n."
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

      # OUTPUT DEKRIPSI
      dec_res = st.session_state.dec_result
      if dec_res:
        st.markdown("#### 📄 Hasil Dekripsi")

        # 1. Teks asli berupa blok (3-digit Pi)
        st.markdown(
            f"""
                <div class="sub-block">
                    <div class="sub-block-title">Blok Plaintext Terdekripsi (Pᵢ - Blok 3 Digit)</div>
                    <div class="scroll-mono-box" style="border-color: rgba(167, 139, 250, 0.45); color: #c4b5fd; font-weight:600;">
                        {' '.join(dec_res['blok_plain'])}
                    </div>
                </div>
                """,
            unsafe_allow_html=True,
        )

        # 2. Hasil Pi setelah diubah menjadi 2 digit
        st.markdown(
            f"""
                <div class="sub-block">
                    <div class="sub-block-title">Hasil Pᵢ Setelah Diubah Menjadi 2 Digit (Sebelum +27)</div>
                    <div class="scroll-mono-box" style="color: #e2e8f0;">
                        {' '.join(dec_res['pi_2digit'])}
                    </div>
                    <div style="font-size:0.75rem; color:#94a3b8; margin-top:6px;">
                        Kode ASCII (+27): <span style="font-family:'JetBrains Mono', monospace; color:#cbd5e1;">{' '.join(dec_res['ascii_dec'])}</span>
                    </div>
                </div>
                """,
            unsafe_allow_html=True,
        )

        # 3. Teks Asli Final
        st.markdown(
            f"""
                <div class="sub-block" style="border-color: rgba(52, 211, 153, 0.45); background: rgba(6, 78, 59, 0.2);">
                    <div class="sub-block-title" style="color:#6ee7b7;">Teks Asli Berhasil Dipulihkan</div>
                    <div class="scroll-mono-box" style="border-color: rgba(52, 211, 153, 0.45); color: #34d399; font-size:1.05rem; font-weight:700;">
                        {dec_res['hasil_teks']}
                    </div>
                </div>
                """,
            unsafe_allow_html=True,
        )
      else:
        st.markdown(
            """
                <div class="sub-block" style="margin-top:12px;">
                    <div class="sub-block-title">Hasil Dekripsi</div>
                    <div style="color:#64748b; font-size:0.86rem;">
                        Masukkan blok ciphertext beserta nilai d dan n, lalu klik tombol <b>Dekripsi Ciphertext</b> untuk melihat blok Pᵢ, kode 2-digit, dan teks aslinya.
                    </div>
                </div>
                """,
            unsafe_allow_html=True,
        )


# ==============================================================================
# HALAMAN 2: PROSES RSA (KONSEPTUAL & ALUR MATEMATIS - TANPA KODE)
# ==============================================================================
elif st.session_state.nav_page == "Proses RSA":
  st.markdown("## ⚙️ Bagaimana Algoritma RSA Bekerja?")
  st.write(
      "RSA (*Rivest–Shamir–Adleman*) adalah algoritma kriptografi asimetris"
      " yang menggunakan sepasang kunci berbeda untuk mengunci (enkripsi) dan"
      " membuka pesan (dekripsi). Keamanannya bertumpu pada sulitnya"
      " memfaktorkan hasil perkalian dua bilangan prima raksasa."
  )

  p_col1, p_col2 = st.columns(2, gap="large")

  with p_col1:
    st.markdown("### 🔑 Tahap 1: Pembangkitan Kunci")
    st.markdown(
        """
        <div class="step-card">
            <b>1. Pemilihan Dua Bilangan Prima (p dan q)</b><br>
            Sistem memilih dua bilangan prima acak yang berbeda (<i>p ≠ q</i>) sesuai jumlah digit yang ditentukan pengguna.
        </div>
        <div class="step-card">
            <b>2. Menghitung Modulus (n)</b><br>
            Kedua bilangan prima dikalikan: <b>n = p × q</b>. Nilai <i>n</i> menjadi batas atas ruang aritmetika modulo dan harus lebih besar dari 999 agar mampu menampung blok 3-digit.
        </div>
        <div class="step-card">
            <b>3. Menghitung Fungsi Totient Euler (m)</b><br>
            Menghitung banyaknya bilangan bulat positif di bawah <i>n</i> yang relatif prima dengannya: <b>m = φ(n) = (p − 1)(q − 1)</b>.
        </div>
        <div class="step-card">
            <b>4. Menentukan Eksponen e dan Invers Modular d</b><br>
            • Memilih bilangan acak <b>e</b> (1 &lt; e &lt; m) yang koprim dengan <i>m</i> (PBB(e, m) = 1).<br>
            • Menghitung <b>d</b> sebagai invers perkalian modular dari <i>e</i> terhadap <i>m</i>, sehingga memenuhi <b>(e × d) mod m = 1</b>.
        </div>
        """,
        unsafe_allow_html=True,
    )

  with p_col2:
    st.markdown("### 🔄 Tahap 2: Pengkodean, Enkripsi & Dekripsi")
    st.markdown(
        """
        <div class="step-card-dec">
            <b>1. Konversi Karakter ke Kode 2-Digit (Offset -27)</b><br>
            Setiap karakter teks (ASCII 32–126) dikurangi <b>27</b> sehingga seluruh karakter—baik 2 digit maupun 3 digit—seragam menjadi tepat <b>2 digit (05–99)</b>.
        </div>
        <div class="step-card-dec">
            <b>2. Pembentukan Blok Plaintext 3-Digit (Pᵢ)</b><br>
            Seluruh kode 2-digit digabungkan menjadi satu deret angka panjang, lalu dipotong per <b>3 digit</b>. Jika blok terakhir kurang dari 3 digit, ditambahkan angka nol di depan.
        </div>
        <div class="step-card-dec">
            <b>3. Proses Enkripsi Menjadi Ciphertext (Cᵢ)</b><br>
            Setiap blok <i>Pᵢ</i> dihitung dengan perpangkatan modular: <b>Cᵢ = Pᵢᵉ mod n</b>. Hasilnya berupa deretan angka acak yang tidak terbaca.
        </div>
        <div class="step-card-dec">
            <b>4. Proses Dekripsi & Pemulihan Teks</b><br>
            Setiap blok <i>Cᵢ</i> dikembalikan dengan rumus <b>Pᵢ = Cᵢᵈ mod n</b>, diformat ulang ke 3 digit, dibersihkan nol tambahannya, dipecah kembali per <b>2 digit</b>, lalu ditambah <b>27</b> untuk mendapatkan karakter ASCII semula.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==============================================================================
# HALAMAN 3: INFORMATION
# ==============================================================================
elif st.session_state.nav_page == "Information":
  st.markdown("## ℹ️ Informasi Aplikasi & Tim Pengembang")

  info_c1, info_c2 = st.columns([1.4, 1], gap="large")
  with info_c1:
    with st.container(border=True):
      st.markdown("### Tentang Proyek")
      st.write(
          "Aplikasi web ini dikembangkan untuk memvisualisasikan implementasi"
          " kriptografi kunci publik **RSA** secara utuh—mulai dari"
          " pembangkitan bilangan prima acak hingga 24 digit, transformasi"
          " teks ke blok numerik, hingga pemulihan pesan asli."
      )
      st.markdown("""
            **Fitur Utama Sistem:**
            * **Pembangkit Prima Multi-Digit (1–24 Digit):** Menggunakan uji primalitas deterministik *Miller-Rabin* untuk menjamin keakuratan bilangan prima besar secara instan.
            * **Skema Pengkodean ASCII Offset (-27):** Menjaga konsistensi huruf kapital, huruf kecil, angka, spasi, dan simbol cetak (ASCII 32–126) tanpa risiko ambiguitas saat pemotongan blok.
            * **Antarmuka Fokus Dinamis:** Kartu Enkripsi dan Dekripsi yang dapat diperbesar secara interaktif sesuai kebutuhan pengguna.
            """)

  with info_c2:
    with st.container(border=True):
      st.markdown("### Anggota Kelompok")
      st.markdown(
          """
            <div class="param-item">
                <div class="param-label">Anggota 1 · NRP 002</div>
                <div class="param-value" style="color:#f8fafc;">Christian Zarkasie</div>
            </div>
            <div class="param-item">
                <div class="param-label">Anggota 2 · NRP 005</div>
                <div class="param-value" style="color:#f8fafc;">Clifton Pratomo</div>
            </div>
            <div class="param-item">
                <div class="param-label">Anggota 3 · NRP 042</div>
                <div class="param-value" style="color:#f8fafc;">I Nyoman Tisna Satya Wijaya</div>
            </div>
            """,
          unsafe_allow_html=True,
      )


# ==============================================================================
# HALAMAN 4: DOCUMENTATION
# ==============================================================================
elif st.session_state.nav_page == "Documentation":
  st.markdown("## 📘 Dokumentasi Teknis & Panduan Penggunaan")

  with st.container(border=True):
    st.markdown("### 1. Panduan Penggunaan")
    st.markdown("""
        **A. Melakukan Enkripsi:**
        1. Buka tab **Kalkulator RSA** dan klik kartu **Enkripsi Pesan** (atau tombol *Perbesar Enkripsi*).
        2. Masukkan teks pada **Blok 1** (mendukung seluruh karakter ASCII cetak 32–126).
        3. Tentukan jumlah digit bilangan prima `p` dan `q` pada **Blok 2** (1–24 digit; pastikan perkalian `n = p × q > 999`).
        4. Tekan **Generate Kunci & Enkripsi**. Hasil ciphertext muncul pada **Blok 3**, disertai rincian `p, q, n, m, e, d`, kode ASCII, serta pasangan kunci.
        5. Gunakan tombol **Kirim Ciphertext & Kunci ke Panel Dekripsi** untuk menguji dekripsi secara otomatis.

        **B. Melakukan Dekripsi:**
        1. Masukkan deretan angka ciphertext yang dipisahkan spasi pada **Blok 1**.
        2. Masukkan nilai `d` dan `n` pada **Blok 2** (kolom dapat digeser secara horizontal apabila angka berdigit panjang).
        3. Tekan **Dekripsi Ciphertext** untuk melihat blok 3-digit $P_i$, hasil konversi 2-digit $P_i$, serta teks asli yang dipulihkan.
        """)

  with st.container(border=True):
    st.markdown("### 2. Spesifikasi Arsitektur Fungsi")
    st.markdown("""
        | Nama Fungsi | Input | Output | Deskripsi Tugas |
        | :--- | :--- | :--- | :--- |
        | `generate_random_prime(digits, exclude)` | `digits: int`, `exclude: int` | `int` | Menghasilkan bilangan prima acak 1–24 digit dengan optimasi lompatan ganjil. |
        | `generate_random_e(m)` | `m: int` | `int` | Memilih eksponen $1 < e < m$ yang memenuhi $\\text{PBB}(e, m) = 1$. |
        | `teks_ke_blok3(teks)` | `teks: str` | `(ascii, kode_2d, blok_3)` | Mengurangi ASCII dengan `OFFSET = 27` menjadi 2 digit, lalu memecahnya menjadi blok 3-digit. |
        | `blok3_ke_teks_detail(blok_3)` | `blok_3: list[str]` | `(kode_2d, ascii, teks)` | Menghapus nol padding di blok akhir berdasarkan paritas digit, memecah per 2 digit, dan menambah `+27`. |
        """)
