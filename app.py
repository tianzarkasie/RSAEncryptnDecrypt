import html
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
# 2. CUSTOM CSS
# ==============================================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

:root {
    --bg: #07080b;
    --orange: #ff5e14;
    --orange-soft: #ff8533;
    --blue: #38bdf8;
    --indigo: #818cf8;
    --silver-1: #f1f5f9;
    --silver-2: #cbd5e1;
    --silver-3: #94a3b8;
    --silver-4: #64748b;
    --card: rgba(16, 19, 27, 0.78);
    --line: rgba(255, 255, 255, 0.09);
}

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--silver-1);
    scroll-behavior: smooth;
}

.stApp {
    background:
        radial-gradient(ellipse 70% 40% at 50% 0%, rgba(255, 94, 20, 0.10), transparent 70%),
        radial-gradient(ellipse 50% 30% at 100% 40%, rgba(56, 189, 248, 0.05), transparent 70%),
        var(--bg) !important;
    overflow-x: hidden;
}

header[data-testid="stHeader"], footer { visibility: hidden; height: 0; }

.block-container {
    padding-top: 0 !important;
    padding-bottom: 3rem !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    max-width: 1240px !important;
}

/* Offset anchor supaya tidak tertutup navbar */
.anchor { display: block; position: relative; top: -90px; visibility: hidden; height: 0; }

/* ============================================================================
   NAVBAR (FIXED, GLASS)
   ============================================================================ */
.topnav {
    position: fixed;
    top: 14px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 9999;
    width: min(1180px, calc(100% - 28px));
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    padding: 9px 12px 9px 18px;
    background: rgba(12, 14, 20, 0.72);
    backdrop-filter: blur(22px) saturate(150%);
    -webkit-backdrop-filter: blur(22px) saturate(150%);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 999px;
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

.nav-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 700;
    font-size: 0.98rem;
    letter-spacing: -0.01em;
    color: #fff !important;
    text-decoration: none !important;
}

.nav-logo {
    width: 28px; height: 28px;
    border-radius: 9px;
    display: grid; place-items: center;
    background: linear-gradient(135deg, #ff5500, #ff8533);
    box-shadow: 0 0 16px rgba(255, 94, 20, 0.6);
    font-size: 0.8rem; font-weight: 800; color: #fff;
}

.nav-links { display: flex; align-items: center; gap: 2px; }

.nav-links a {
    position: relative;
    padding: 8px 15px;
    font-size: 0.86rem;
    font-weight: 500;
    color: var(--silver-3) !important;
    text-decoration: none !important;
    border-radius: 999px;
    transition: color 0.25s ease, background 0.25s ease;
}

.nav-links a:hover {
    color: #fff !important;
    background: rgba(255, 255, 255, 0.07);
}

.nav-links a::after {
    content: "";
    position: absolute;
    left: 50%; bottom: 3px;
    width: 0; height: 2px;
    border-radius: 2px;
    background: linear-gradient(90deg, #ff5e14, #ff8533);
    transition: width 0.3s ease, left 0.3s ease;
}
.nav-links a:hover::after { width: 38%; left: 31%; }

.nav-cta {
    padding: 8px 18px;
    font-size: 0.84rem;
    font-weight: 600;
    color: #fff !important;
    text-decoration: none !important;
    border-radius: 999px;
    background: linear-gradient(135deg, #ff5500, #ff8533);
    box-shadow: 0 6px 20px rgba(255, 94, 20, 0.4);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    white-space: nowrap;
}
.nav-cta:hover { transform: translateY(-1px); box-shadow: 0 10px 26px rgba(255, 94, 20, 0.6); }

@media (max-width: 820px) {
    .nav-links { display: none; }
}

/* ============================================================================
   HERO
   ============================================================================ */
.hero {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    overflow: hidden;
    margin: 0 -1.5rem 2rem -1.5rem;
    padding: 9.5rem 1rem 6.5rem 1rem;
    background:
        linear-gradient(125deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.01) 28%, transparent 55%),
        radial-gradient(ellipse at 50% 120%, rgba(255, 94, 20, 0.32) 0%, rgba(148, 163, 184, 0.08) 40%, transparent 70%);
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.hero-arc {
    position: absolute;
    bottom: -330px; left: 50%;
    transform: translateX(-50%);
    width: 820px; max-width: 120%; height: 440px;
    border-radius: 50%;
    background: linear-gradient(90deg, #1e293b 0%, #94a3b8 14%, #ff6a1a 35%, #ff944d 52%, #e2e8f0 74%, #334155 100%);
    padding: 14px;
    box-shadow: 0 -18px 65px rgba(255, 102, 26, 0.4), 0 -4px 24px rgba(226, 232, 240, 0.2), inset 0 4px 18px rgba(255, 255, 255, 0.45);
    pointer-events: none;
}
.hero-arc::after {
    content: ""; display: block; width: 100%; height: 100%;
    border-radius: 50%;
    background: radial-gradient(circle at 50% 0%, #14161d 0%, #07080b 68%);
}

.hero-pill {
    position: relative; z-index: 2;
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(24, 26, 34, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 999px;
    padding: 5px 14px 5px 6px;
    font-size: 0.78rem; color: var(--silver-2);
    margin-bottom: 1.2rem;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
}
.hero-pill b {
    background: linear-gradient(135deg, #ff5e14, #ff8c42);
    color: #fff; font-size: 0.7rem; font-weight: 700;
    padding: 3px 10px; border-radius: 999px;
}

.hero-title {
    position: relative; z-index: 2;
    font-size: clamp(2.4rem, 5.4vw, 4.3rem);
    font-weight: 700; line-height: 1.1; letter-spacing: -0.035em;
    background: linear-gradient(180deg, #ffffff 15%, #e2e8f0 55%, #94a3b8 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin: 0 0 0.9rem 0; padding: 0;
}

.hero-sub {
    position: relative; z-index: 2;
    max-width: 640px;
    font-size: 1rem; line-height: 1.65;
    color: var(--silver-3);
}

/* ============================================================================
   SWITCH ENCRYPT / DECRYPT
   ============================================================================ */
div[data-testid="stRadio"] { display: flex; justify-content: center; margin: 0.5rem 0 1.6rem 0; }

div[data-testid="stRadio"] > div[role="radiogroup"] {
    position: relative;
    display: inline-flex !important;
    flex-direction: row !important;
    gap: 0 !important;
    background: rgba(15, 17, 24, 0.92);
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 999px;
    padding: 6px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.55), inset 0 1px 2px rgba(0, 0, 0, 0.6);
    isolation: isolate;
}

/* Kapsul yang bergeser (berada DI BELAKANG label) */
div[data-testid="stRadio"] > div[role="radiogroup"]::before {
    content: "";
    position: absolute;
    top: 6px; left: 6px;
    width: 160px;
    height: calc(100% - 12px);
    border-radius: 999px;
    z-index: -1;
    pointer-events: none;
    transition: transform 0.5s cubic-bezier(0.22, 1, 0.36, 1), background 0.45s ease, box-shadow 0.45s ease;
}

div[data-testid="stRadio"] > div[role="radiogroup"]:has(label:nth-of-type(1) input:checked)::before {
    transform: translateX(0);
    background: linear-gradient(135deg, #ff5500 0%, #ff8533 100%);
    box-shadow: 0 0 26px rgba(255, 94, 20, 0.65), inset 0 1px 1px rgba(255, 255, 255, 0.45);
}

div[data-testid="stRadio"] > div[role="radiogroup"]:has(label:nth-of-type(2) input:checked)::before {
    transform: translateX(160px);
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 60%, #a5b4fc 100%);
    box-shadow: 0 0 26px rgba(56, 189, 248, 0.55), inset 0 1px 1px rgba(255, 255, 255, 0.55);
}

div[data-testid="stRadio"] > div[role="radiogroup"] > label {
    position: relative;
    width: 160px;
    justify-content: center;
    align-items: center;
    margin: 0 !important;
    padding: 11px 0 !important;
    border-radius: 999px;
    cursor: pointer;
    background: transparent !important;
}

div[data-testid="stRadio"] > div[role="radiogroup"] > label > div:first-child { display: none !important; }

div[data-testid="stRadio"] > div[role="radiogroup"] > label > div:last-child {
    width: 100%; display: flex; justify-content: center;
}

div[data-testid="stRadio"] > div[role="radiogroup"] > label p {
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    color: var(--silver-3) !important;
    margin: 0 !important;
    transition: color 0.3s ease, transform 0.25s ease;
}

/* Hover pada tombol yang belum aktif: teks menyala + sedikit membesar */
div[data-testid="stRadio"] > div[role="radiogroup"] > label:hover p {
    color: #ffffff !important;
    transform: scale(1.06);
}

div[data-testid="stRadio"] > div[role="radiogroup"] > label:has(input:checked) p {
    color: #ffffff !important;
    font-weight: 700 !important;
    text-shadow: 0 1px 4px rgba(0, 0, 0, 0.35);
}

/* Efek hover pada seluruh switch: cahaya mengikuti sisi yang disorot */
div[data-testid="stRadio"] > div[role="radiogroup"]:hover {
    border-color: rgba(255, 255, 255, 0.28);
}

/* ============================================================================
   KARTU (st.container(key="card_...")) 
   ============================================================================ */
[class*="st-key-card"] {
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 16px 18px 12px 18px;
    margin-bottom: 14px;
    transition: border-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
}
[class*="st-key-card"]:hover {
    border-color: rgba(255, 115, 36, 0.4);
    transform: translateY(-2px);
    box-shadow: 0 14px 34px rgba(0, 0, 0, 0.45);
}
.mode-decrypt [class*="st-key-card"]:hover { border-color: rgba(56, 189, 248, 0.4); }

.card-label {
    display: flex; align-items: center; gap: 8px;
    font-size: 0.76rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.07em;
    color: var(--silver-3);
    margin-bottom: 6px;
}
.dot { width: 7px; height: 7px; border-radius: 50%; }
.dot.o { background: #ff6a1a; box-shadow: 0 0 8px #ff6a1a; }
.dot.b { background: #38bdf8; box-shadow: 0 0 8px #38bdf8; }

.mono-scroll {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.88rem;
    background: rgba(7, 8, 12, 0.88);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: var(--silver-1);
    padding: 11px 14px;
    border-radius: 12px;
    overflow-x: auto;
    white-space: nowrap;
    scrollbar-width: thin;
    scrollbar-color: #475569 rgba(7, 8, 12, 0.88);
    transition: border-color 0.25s ease;
}
.mono-scroll:hover { border-color: rgba(255, 255, 255, 0.25); }
.mono-scroll::-webkit-scrollbar { height: 5px; }
.mono-scroll::-webkit-scrollbar-thumb { background: #475569; border-radius: 999px; }

/* Input */
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
    background-color: rgba(7, 8, 12, 0.9) !important;
    color: #f8fafc !important;
    border: 1px solid rgba(255, 255, 255, 0.14) !important;
    border-radius: 12px !important;
    font-family: 'JetBrains Mono', monospace !important;
    transition: border-color 0.25s ease, box-shadow 0.25s ease !important;
}
div[data-testid="stTextInput"] input:hover,
div[data-testid="stNumberInput"] input:hover { border-color: rgba(255, 255, 255, 0.3) !important; }
div[data-testid="stTextInput"] input:focus,
div[data-testid="stNumberInput"] input:focus {
    border-color: #ff6a1a !important;
    box-shadow: 0 0 0 2px rgba(255, 106, 26, 0.25) !important;
}
.mode-decrypt div[data-testid="stTextInput"] input:focus {
    border-color: #38bdf8 !important;
    box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.25) !important;
}
div[data-testid="stWidgetLabel"] p { color: var(--silver-3) !important; font-size: 0.82rem !important; }

/* Tombol */
div[data-testid="stButton"] > button[kind="primary"] {
    background: linear-gradient(135deg, #ff5500 0%, #ff8533 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    padding: 0.65rem 1.2rem !important;
    box-shadow: 0 8px 25px rgba(255, 94, 20, 0.38) !important;
    transition: transform 0.25s ease, box-shadow 0.25s ease !important;
}
div[data-testid="stButton"] > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 12px 32px rgba(255, 94, 20, 0.58) !important;
}
.mode-decrypt div[data-testid="stButton"] > button[kind="primary"] {
    background: linear-gradient(135deg, #0ea5e9 0%, #818cf8 100%) !important;
    box-shadow: 0 8px 25px rgba(56, 189, 248, 0.35) !important;
}
.mode-decrypt div[data-testid="stButton"] > button[kind="primary"]:hover {
    box-shadow: 0 12px 32px rgba(56, 189, 248, 0.55) !important;
}
div[data-testid="stButton"] > button[kind="secondary"] {
    background: rgba(30, 34, 46, 0.85) !important;
    color: var(--silver-1) !important;
    border: 1px solid rgba(255, 255, 255, 0.16) !important;
    border-radius: 12px !important;
    font-weight: 500 !important;
    transition: all 0.25s ease !important;
}
div[data-testid="stButton"] > button[kind="secondary"]:hover {
    border-color: #ff8533 !important;
    color: #fff !important;
    transform: translateY(-1px) !important;
}

/* Tile parameter */
.tile {
    background: rgba(9, 11, 16, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 10px 14px;
    margin-bottom: 10px;
    transition: border-color 0.25s ease, background 0.25s ease;
}
.tile:hover { border-color: rgba(255, 133, 51, 0.45); background: rgba(255, 94, 20, 0.05); }
.tile-t { font-size: 0.72rem; color: var(--silver-3); font-weight: 600; margin-bottom: 3px; }
.tile-v {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.88rem; font-weight: 600;
    overflow-x: auto; white-space: nowrap;
    scrollbar-width: thin;
}
.tile-v.o { color: #ff8533; }
.tile-v.s { color: #e2e8f0; }
.tile-v.b { color: #38bdf8; }

.empty-note { padding: 3.5rem 1rem; text-align: center; color: var(--silver-4); font-size: 0.9rem; line-height: 1.7; }

/* ============================================================================
   SEKSI INFO (CARA KERJA & TIM)
   ============================================================================ */
.sec-head { text-align: center; margin: 3.2rem 0 1.4rem 0; }
.sec-head h2 {
    font-size: clamp(1.5rem, 3vw, 2.1rem); font-weight: 700; letter-spacing: -0.025em;
    color: #fff; margin: 0 0 0.4rem 0; padding: 0;
}
.sec-head p { color: var(--silver-3); font-size: 0.95rem; margin: 0; }

.grid { display: grid; gap: 14px; }
.grid.g4 { grid-template-columns: repeat(4, 1fr); }
.grid.g3 { grid-template-columns: repeat(3, 1fr); }
@media (max-width: 900px) { .grid.g4 { grid-template-columns: repeat(2, 1fr); } .grid.g3 { grid-template-columns: 1fr; } }
@media (max-width: 520px) { .grid.g4 { grid-template-columns: 1fr; } }

.info-card {
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 20px;
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
}
.info-card:hover {
    transform: translateY(-4px);
    border-color: rgba(255, 115, 36, 0.45);
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.5), 0 0 30px rgba(255, 94, 20, 0.1);
}
.info-card .step {
    width: 32px; height: 32px; border-radius: 10px;
    display: grid; place-items: center;
    background: linear-gradient(135deg, #ff5500, #ff8533);
    font-weight: 700; font-size: 0.9rem; color: #fff;
    margin-bottom: 12px;
}
.info-card h4 { margin: 0 0 6px 0; font-size: 1rem; font-weight: 600; color: #fff; }
.info-card p { margin: 0; font-size: 0.86rem; line-height: 1.6; color: var(--silver-3); }
.info-card code {
    font-family: 'JetBrains Mono', monospace; font-size: 0.8rem;
    color: #ff8533; background: rgba(255, 94, 20, 0.1);
    padding: 1px 6px; border-radius: 6px;
}

.member { text-align: center; }
.member .avatar {
    width: 56px; height: 56px; border-radius: 50%;
    margin: 0 auto 12px auto;
    display: grid; place-items: center;
    background: linear-gradient(135deg, #1e293b, #475569);
    border: 2px solid rgba(255, 133, 51, 0.5);
    font-weight: 700; font-size: 1.1rem; color: #fff;
    transition: transform 0.35s ease, box-shadow 0.35s ease;
}
.member:hover .avatar { transform: scale(1.1) rotate(-4deg); box-shadow: 0 0 24px rgba(255, 94, 20, 0.55); }
.member .nim { font-family: 'JetBrains Mono', monospace; color: #ff8533; font-size: 0.82rem; margin-top: 4px; }

.footer {
    margin-top: 3rem; padding-top: 1.4rem;
    border-top: 1px solid rgba(255, 255, 255, 0.07);
    text-align: center; font-size: 0.82rem; color: var(--silver-4);
}

@media (prefers-reduced-motion: reduce) {
    * { transition: none !important; animation: none !important; }
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
  """Uji primalitas deterministik Miller-Rabin."""
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
    return random.choice([p for p in (2, 3, 5, 7) if p != exclude])

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
  """Memilih e acak dengan 1 < e < m dan PBB(e, m) = 1."""
  if m <= 10000:
    kandidat = [e for e in range(3, m, 2) if math.gcd(e, m) == 1]
    if not kandidat:
      kandidat = [e for e in range(2, m) if math.gcd(e, m) == 1]
    return random.choice(kandidat)

  while True:
    e = random.randrange(3, m, 2)
    if math.gcd(e, m) == 1:
      return e


def teks_ke_blok3(teks: str):
  """Teks -> kode 2 digit (ASCII - 27) -> blok 3 digit."""
  ascii_asli, kode_2digit = [], []
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


def blok3_ke_teks_detail(blok_3):
  """Blok 3 digit -> (kode 2-digit, ASCII asli, teks asli)."""
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
  ascii_list, karakter = [], []
  for k2 in kode_2digit:
    kode_ascii = int(k2) + OFFSET
    if kode_ascii < 32 or kode_ascii > 126:
      raise ValueError(f"Kode ASCII ({kode_ascii}) di luar rentang cetak (32-126).")
    ascii_list.append(str(kode_ascii))
    karakter.append(chr(kode_ascii))

  return kode_2digit, ascii_list, "".join(karakter)


# ==============================================================================
# 4. SESSION STATE
# ==============================================================================
st.session_state.setdefault("enc_result", None)
st.session_state.setdefault("dec_result", None)
st.session_state.setdefault("mode_selector", "Encrypt")

# Streamlit menghapus state widget yang tidak ditampilkan. Baris ini menjaga
# isi input tetap ada saat pengguna berpindah antara tab Encrypt dan Decrypt.
for _k in (
    "enc_text_val", "in_digit_p", "in_digit_q",
    "dec_cipher_val", "dec_d_val", "dec_n_val",
):
  if _k in st.session_state:
    st.session_state[_k] = st.session_state[_k]


def card_label(text: str, color: str = "o") -> None:
  st.markdown(
      f'<div class="card-label"><span class="dot {color}"></span>{text}</div>',
      unsafe_allow_html=True,
  )


def tile(title: str, value: str, tone: str = "s", extra_style: str = "") -> str:
  return (
      f'<div class="tile" style="{extra_style}"><div class="tile-t">{title}</div>'
      f'<div class="tile-v {tone}">{html.escape(str(value))}</div></div>'
  )


# ==============================================================================
# 5. NAVBAR
# ==============================================================================
st.markdown(
    """
<nav class="topnav">
    <a class="nav-brand" href="#beranda" target="_self">
        <span class="nav-logo">R</span> RSA Studio
    </a>
    <div class="nav-links">
        <a href="#beranda" target="_self">Beranda</a>
        <a href="#workspace" target="_self">Enkripsi &amp; Dekripsi</a>
        <a href="#cara-kerja" target="_self">Cara Kerja</a>
        <a href="#tim" target="_self">Tim</a>
    </div>
    <a class="nav-cta" href="#workspace" target="_self">Mulai Sekarang</a>
</nav>
""",
    unsafe_allow_html=True,
)

# ==============================================================================
# 6. HERO
# ==============================================================================
st.markdown(
    """
<span id="beranda" class="anchor"></span>
<div class="hero">
    <div class="hero-pill"><b>RSA ENGINE</b><span>Kriptografi asimetris dengan offset −27</span></div>
    <h1 class="hero-title">RSA Encrypt &amp; Decrypt</h1>
    <div class="hero-sub">
        Bangkitkan kunci publik dan privat, enkripsi pesan teks, lalu dekripsi kembali
        dengan rincian setiap langkahnya.
    </div>
    <div class="hero-arc"></div>
</div>
<span id="workspace" class="anchor"></span>
""",
    unsafe_allow_html=True,
)

# ==============================================================================
# 7. SWITCH ENCRYPT / DECRYPT
# ==============================================================================
selected_mode = st.radio(
    "Pilih Mode",
    options=["Encrypt", "Decrypt"],
    horizontal=True,
    label_visibility="collapsed",
    key="mode_selector",
)

# Tema biru untuk mode Decrypt (tanpa membungkus widget)
st.markdown(
    f"""<style>
    {'' if selected_mode == 'Encrypt' else '''
    [class*="st-key-card"]:hover { border-color: rgba(56,189,248,0.4) !important; }
    div[data-testid="stTextInput"] input:focus { border-color:#38bdf8 !important; box-shadow:0 0 0 2px rgba(56,189,248,0.25) !important; }
    div[data-testid="stButton"] > button[kind="primary"] { background: linear-gradient(135deg,#0ea5e9 0%,#818cf8 100%) !important; box-shadow:0 8px 25px rgba(56,189,248,0.35) !important; }
    div[data-testid="stButton"] > button[kind="primary"]:hover { box-shadow:0 12px 32px rgba(56,189,248,0.55) !important; }
    '''}
    </style>""",
    unsafe_allow_html=True,
)

# ==============================================================================
# 8. MODE ENCRYPT
# ==============================================================================
if selected_mode == "Encrypt":
  col_left, col_right = st.columns([1.08, 1], gap="large")

  with col_left:
    with st.container(key="card_plain"):
      card_label("Blok 1 · Teks asli (plaintext)")
      teks_input = st.text_input(
          "Teks Asli",
          value="halooo",
          placeholder="Masukkan pesan (ASCII 32–126)...",
          label_visibility="collapsed",
          key="enc_text_val",
      )

    with st.container(key="card_digits"):
      card_label("Blok 2 · Panjang digit prima p &amp; q (1–24 digit)")
      c_p, c_q = st.columns(2, gap="medium")
      with c_p:
        digit_p = st.number_input(
            "Digit prima p", min_value=1, max_value=24, value=4, step=1, key="in_digit_p"
        )
      with c_q:
        digit_q = st.number_input(
            "Digit prima q", min_value=1, max_value=24, value=4, step=1, key="in_digit_q"
        )

    if st.button(
        "⚡ Buat kunci & enkripsi pesan", type="primary", use_container_width=True
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
          blok_cipher = [str(pow(int(p_i), e_val, n_val)) for p_i in blok_plain]

          st.session_state.enc_result = {
              "p": p_val, "q": q_val, "n": n_val, "m": m_val,
              "e": e_val, "d": d_val,
              "ascii_asli": ascii_asli, "kode_2digit": kode_2digit,
              "blok_plain": blok_plain, "blok_cipher": blok_cipher,
          }
        except ValueError as err:
          st.error(str(err))

    enc_res = st.session_state.enc_result
    cipher_str = (
        " ".join(enc_res["blok_cipher"])
        if enc_res
        else "Hasil blok ciphertext akan muncul di sini..."
    )
    with st.container(key="card_cipher"):
      card_label("Blok 3 · Hasil ciphertext (Cᵢ)")
      st.markdown(
          f'<div class="mono-scroll" style="color:#ff8533;font-weight:600;'
          f'border-color:rgba(255,106,26,0.35);margin-bottom:6px;">{cipher_str}</div>',
          unsafe_allow_html=True,
      )

    if enc_res:

      def copy_to_decrypt():
        r = st.session_state.enc_result
        st.session_state.dec_cipher_val = " ".join(r["blok_cipher"])
        st.session_state.dec_d_val = str(r["d"])
        st.session_state.dec_n_val = str(r["n"])
        st.session_state.mode_selector = "Decrypt"

      st.button(
          "↗ Kirim ciphertext & kunci ke tab Decrypt",
          use_container_width=True,
          on_click=copy_to_decrypt,
      )

  with col_right:
    with st.container(key="card_params"):
      card_label("Parameter matematis &amp; kunci")
      if enc_res:
        g1, g2 = st.columns(2)
        with g1:
          st.markdown(
              tile("p terpilih", enc_res["p"], "o")
              + tile("n (p × q)", enc_res["n"], "s")
              + tile("e (eksponen publik)", enc_res["e"], "o"),
              unsafe_allow_html=True,
          )
        with g2:
          st.markdown(
              tile("q terpilih", enc_res["q"], "o")
              + tile("m = (p − 1)(q − 1)", enc_res["m"], "s")
              + tile("d (eksponen privat)", enc_res["d"], "o"),
              unsafe_allow_html=True,
          )

        st.markdown(
            tile("Kode ASCII asli", " ".join(enc_res["ascii_asli"]), "s")
            + tile("Kode 2 digit (−27)", " ".join(enc_res["kode_2digit"]), "s")
            + tile("Blok plaintext 3 digit (Pᵢ)", " ".join(enc_res["blok_plain"]), "s"),
            unsafe_allow_html=True,
        )

        k1, k2 = st.columns(2)
        with k1:
          st.markdown(
              tile(
                  "Kunci publik (e, n)",
                  f"({enc_res['e']}, {enc_res['n']})",
                  "o",
                  "border-color:rgba(255,106,26,0.35);",
              ),
              unsafe_allow_html=True,
          )
        with k2:
          st.markdown(
              tile(
                  "Kunci privat (d, n)",
                  f"({enc_res['d']}, {enc_res['n']})",
                  "s",
                  "border-color:rgba(226,232,240,0.28);",
              ),
              unsafe_allow_html=True,
          )
      else:
        st.markdown(
            '<div class="empty-note">Masukkan teks dan jumlah digit prima di sebelah kiri, '
            "lalu tekan <b>Buat kunci &amp; enkripsi pesan</b> untuk melihat nilai "
            "<i>p, q, n, m, e, d</i>, kode ASCII, dan pasangan kunci.</div>",
            unsafe_allow_html=True,
        )

# ==============================================================================
# 9. MODE DECRYPT
# ==============================================================================
else:
  d_left, d_right = st.columns([1.05, 1], gap="large")

  with d_left:
    with st.container(key="card_cipher_in"):
      card_label("Blok 1 · Teks cipher (pisahkan dengan spasi)", "b")
      cipher_in = st.text_input(
          "Teks Cipher",
          placeholder="Contoh: 407 436 812",
          label_visibility="collapsed",
          key="dec_cipher_val",
      )

    with st.container(key="card_dn"):
      card_label("Blok 2 · Nilai d &amp; n", "b")
      col_d, col_n = st.columns(2, gap="medium")
      with col_d:
        d_in = st.text_input("Nilai d", placeholder="Masukkan d...", key="dec_d_val")
      with col_n:
        n_in = st.text_input("Nilai n", placeholder="Masukkan n...", key="dec_n_val")

    if st.button("🔓 Dekripsi ciphertext", type="primary", use_container_width=True):
      blok_c = cipher_in.strip().split()
      if not blok_c or not all(b.isdigit() for b in blok_c):
        st.error("Format ciphertext tidak valid. Masukkan angka yang dipisah spasi.")
      elif not d_in.strip().isdigit() or not n_in.strip().isdigit():
        st.error("Nilai d dan n harus berupa bilangan bulat positif.")
      else:
        try:
          d_val = int(d_in.strip())
          n_val = int(n_in.strip())
          blok_plain_dec = []

          for c_str in blok_c:
            p_i = pow(int(c_str), d_val, n_val)
            if p_i > 999:
              raise ValueError(
                  f"Hasil dekripsi blok ({p_i}) > 999. Periksa kembali nilai d dan n."
              )
            blok_plain_dec.append(f"{p_i:03d}")

          pi_2digit, ascii_dec, hasil_teks = blok3_ke_teks_detail(blok_plain_dec)
          st.session_state.dec_result = {
              "blok_plain": blok_plain_dec,
              "pi_2digit": pi_2digit,
              "ascii_dec": ascii_dec,
              "hasil_teks": hasil_teks,
          }
        except Exception as err:
          st.session_state.dec_result = None
          st.error(f"Dekripsi gagal: {err}")

  with d_right:
    with st.container(key="card_dec_out"):
      card_label("Hasil dekripsi &amp; pemulihan blok", "b")
      dec_res = st.session_state.dec_result
      if dec_res:
        st.markdown(
            f"""
            <div class="tile"><div class="tile-t">Blok plaintext 3 digit (Pᵢ)</div>
                <div class="mono-scroll" style="color:#38bdf8;font-weight:600;">{' '.join(dec_res['blok_plain'])}</div></div>
            <div class="tile"><div class="tile-t">Pᵢ menjadi 2 digit (sebelum +27)</div>
                <div class="mono-scroll">{' '.join(dec_res['pi_2digit'])}</div></div>
            <div class="tile"><div class="tile-t">Kode ASCII asli (+27)</div>
                <div class="mono-scroll" style="color:#94a3b8;">{' '.join(dec_res['ascii_dec'])}</div></div>
            <div class="tile" style="border-color:rgba(56,189,248,0.45);background:rgba(56,189,248,0.07);">
                <div class="tile-t" style="color:#38bdf8;">Teks asli final</div>
                <div class="mono-scroll" style="color:#fff;font-size:1.05rem;font-weight:700;border-color:rgba(56,189,248,0.4);">{html.escape(dec_res['hasil_teks'])}</div></div>
            """,
            unsafe_allow_html=True,
        )
      else:
        st.markdown(
            '<div class="empty-note">Masukkan blok ciphertext beserta nilai <b>d</b> dan '
            "<b>n</b> di sebelah kiri, lalu tekan <b>Dekripsi ciphertext</b> untuk melihat "
            "blok plaintext, konversi Pᵢ 2 digit, dan teks aslinya.</div>",
            unsafe_allow_html=True,
        )

# ==============================================================================
# 10. CARA KERJA
# ==============================================================================
st.markdown(
    """
<span id="cara-kerja" class="anchor"></span>
<div class="sec-head">
    <h2>Cara kerja</h2>
    <p>Empat langkah dari teks biasa sampai ciphertext.</p>
</div>
<div class="grid g4">
    <div class="info-card"><div class="step">1</div><h4>Ubah teks ke blok</h4>
        <p>Setiap karakter jadi kode ASCII, dikurangi 27 sehingga tersisa 2 digit, lalu digabung dan dipotong menjadi blok 3 digit.</p></div>
    <div class="info-card"><div class="step">2</div><h4>Bangkitkan kunci</h4>
        <p>Pilih dua prima acak <code>p</code> dan <code>q</code>, hitung <code>n = p × q</code> dan <code>m = (p−1)(q−1)</code>, lalu cari <code>e</code> dan <code>d</code>.</p></div>
    <div class="info-card"><div class="step">3</div><h4>Enkripsi</h4>
        <p>Setiap blok plaintext dihitung dengan <code>C = P^e mod n</code>. Hasilnya adalah deretan angka ciphertext.</p></div>
    <div class="info-card"><div class="step">4</div><h4>Dekripsi</h4>
        <p>Dengan <code>P = C^d mod n</code> blok kembali ke bentuk semula, lalu ditambah 27 dan dikonversi kembali menjadi huruf.</p></div>
</div>
""",
    unsafe_allow_html=True,
)

# ==============================================================================
# 11. TIM
# ==============================================================================
st.markdown(
    """
<span id="tim" class="anchor"></span>
<div class="sec-head">
    <h2>Tim pembuat</h2>
    <p>Dikerjakan oleh tiga orang.</p>
</div>
<div class="grid g3">
    <div class="info-card member"><div class="avatar">CZ</div><h4>Christian Zarkasie</h4><div class="nim">(002)</div></div>
    <div class="info-card member"><div class="avatar">CP</div><h4>Clifton Pratomo</h4><div class="nim">(005)</div></div>
    <div class="info-card member"><div class="avatar">NT</div><h4>I Nyoman Tisna Satya Wijaya</h4><div class="nim">(042)</div></div>
</div>
<div class="footer">RSA Studio · Kriptografi asimetris dengan offset −27</div>
""",
    unsafe_allow_html=True,
)
