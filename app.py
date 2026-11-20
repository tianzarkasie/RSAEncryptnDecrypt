import html
import json
import math
import random

import streamlit as st
import streamlit.components.v1 as components

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
    --bg: #0a0c11;
    --orange: #ff5a1f;
    --orange-soft: #ffa24a;
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
    background: linear-gradient(135deg, #ff5a1f, #ffa24a);
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
    background: linear-gradient(90deg, #ff5a1f, #ffa24a);
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
    background: linear-gradient(135deg, #ff5a1f, #ffa24a);
    box-shadow: 0 6px 20px rgba(255, 94, 20, 0.4);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    white-space: nowrap;
}
.nav-cta:hover { transform: translateY(-1px); box-shadow: 0 10px 26px rgba(255, 94, 20, 0.6); }

@media (max-width: 820px) {
    .nav-links { display: none; }
}

/* ============================================================================
   BACKGROUND TETAP (FIXED) - TIDAK ikut ter-scroll, hanya tertutup sheet
   ============================================================================ */
.bg-fixed {
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    text-align: center;
    padding: 22vh 1rem 0 1rem;
    background:
        radial-gradient(rgba(255, 255, 255, 0.07) 1px, transparent 1.4px) 0 0 / 26px 26px,
        linear-gradient(125deg, rgba(255, 255, 255, 0.055) 0%, rgba(255, 255, 255, 0.012) 28%, transparent 55%),
        radial-gradient(ellipse 80% 55% at 50% 108%, rgba(255, 94, 20, 0.38) 0%, rgba(148, 163, 184, 0.09) 42%, transparent 72%),
        radial-gradient(ellipse 60% 40% at 15% 20%, rgba(56, 189, 248, 0.07), transparent 70%);
}

.hero-arc {
    position: absolute;
    bottom: -300px; left: 50%;
    transform: translateX(-50%);
    width: 900px; max-width: 130%; height: 470px;
    border-radius: 50%;
    background: linear-gradient(90deg, #1e293b 0%, #94a3b8 14%, #ff6a2b 35%, #ff944d 52%, #e2e8f0 74%, #334155 100%);
    padding: 14px;
    box-shadow: 0 -18px 70px rgba(255, 102, 26, 0.45), 0 -4px 24px rgba(226, 232, 240, 0.22), inset 0 4px 18px rgba(255, 255, 255, 0.45);
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
    background: linear-gradient(135deg, #ff5a1f, #ff8c42);
    color: #fff; font-size: 0.7rem; font-weight: 700;
    padding: 3px 10px; border-radius: 999px;
}

.hero-title {
    position: relative; z-index: 2;
    font-size: clamp(2.4rem, 5.4vw, 4.4rem);
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

/* Ruang kosong agar background terlihat penuh sebelum sheet naik menutupinya */
.hero-spacer { height: 88vh; min-height: 560px; }

/* ============================================================================
   SHEET KONTEN: naik menutupi background + mem-blur (z-index di atas background)
   ============================================================================ */
.st-key-sheet {
    position: relative;
    z-index: 2;
    background: rgba(8, 9, 13, 0.58);
    backdrop-filter: blur(30px) saturate(150%);
    -webkit-backdrop-filter: blur(30px) saturate(150%);
    border: 1px solid rgba(255, 255, 255, 0.13);
    border-radius: 32px;
    padding: 2rem 2rem 2.2rem 2rem;
    box-shadow: 0 -24px 70px rgba(0, 0, 0, 0.7), inset 0 1px 0 rgba(255, 255, 255, 0.16);
}
@media (max-width: 640px) { .st-key-sheet { padding: 1.2rem 0.9rem 1.5rem 0.9rem; border-radius: 24px; } }

/* ============================================================================
   SWITCH ENCRYPT / DECRYPT (dua tombol, kapsul bergeser, selalu di tengah)
   ============================================================================ */
.st-key-switchwrap {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    width: 100% !important;
    margin: 0.2rem 0 2rem 0;
}

.st-key-switchwrap [data-testid="stHorizontalBlock"] {
    position: relative;
    isolation: isolate;
    box-sizing: border-box;
    display: flex !important;
    flex-wrap: nowrap !important;
    gap: 0 !important;
    width: 100%;
    max-width: 440px;
    margin: 0 auto;
    padding: 7px;
    background: rgba(15, 17, 24, 0.92);
    border: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 999px;
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.6), inset 0 1px 2px rgba(0, 0, 0, 0.6);
    transition: border-color 0.3s ease;
}
.st-key-switchwrap [data-testid="stHorizontalBlock"]:hover { border-color: rgba(255, 255, 255, 0.34); }

/* Kapsul bergerak: tepat setengah dari area dalam */
.st-key-switchwrap [data-testid="stHorizontalBlock"]::before {
    content: "";
    position: absolute;
    top: 7px; bottom: 7px; left: 7px;
    width: calc(50% - 7px);
    border-radius: 999px;
    z-index: -1;
    pointer-events: none;
    transition: transform 0.5s cubic-bezier(0.22, 1, 0.36, 1), background 0.45s ease, box-shadow 0.45s ease;
}

.st-key-switchwrap [data-testid="stColumn"] {
    flex: 1 1 0 !important;
    width: 50% !important;
    min-width: 0 !important;
}
.st-key-switchwrap [data-testid="stElementContainer"],
.st-key-switchwrap [data-testid="stButton"] { width: 100% !important; }

.st-key-switchwrap div[data-testid="stButton"] > button[kind],
.st-key-switchwrap div[data-testid="stButton"] > button[kind]:hover,
.st-key-switchwrap div[data-testid="stButton"] > button[kind]:focus,
.st-key-switchwrap div[data-testid="stButton"] > button[kind]:active {
    width: 100% !important;
    min-height: 0 !important;
    padding: 0.95rem 0 !important;
    background: transparent !important;
    border: none !important;
    border-radius: 999px !important;
    box-shadow: none !important;
    transform: none !important;
    outline: none !important;
}
.st-key-switchwrap div[data-testid="stButton"] > button[kind] p {
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    color: var(--silver-3) !important;
    margin: 0 !important;
    transition: color 0.3s ease, transform 0.25s ease;
}
.st-key-switchwrap div[data-testid="stButton"] > button[kind]:hover p {
    color: #ffffff !important;
    transform: scale(1.08);
}

/* Hilangkan ikon tautan di judul & rapikan teks agar semuanya di tengah */
h1 a, h2 a, h3 a, h4 a, [data-testid="stHeaderActionElements"] { display: none !important; }
.sec-head, .info-card { text-align: center; }
.info-card .step { margin-left: auto; margin-right: auto; }
.info-card h4 { text-align: center; }

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
.dot.o { background: #ff6a2b; box-shadow: 0 0 8px #ff6a2b; }
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
    border-color: #ff6a2b !important;
    box-shadow: 0 0 0 2px rgba(255, 106, 26, 0.25) !important;
}
.mode-decrypt div[data-testid="stTextInput"] input:focus {
    border-color: #38bdf8 !important;
    box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.25) !important;
}
div[data-testid="stWidgetLabel"] p { color: var(--silver-3) !important; font-size: 0.82rem !important; }

/* Tombol */
div[data-testid="stButton"] > button[kind="primary"] {
    background: linear-gradient(135deg, #ff5a1f 0%, #ffa24a 100%) !important;
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
    border-color: #ffa24a !important;
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
.tile-v.o { color: #ffa24a; }
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
    background: linear-gradient(135deg, #ff5a1f, #ffa24a);
    font-weight: 700; font-size: 0.9rem; color: #fff;
    margin-bottom: 12px;
}
.info-card h4 { margin: 0 0 6px 0; font-size: 1rem; font-weight: 600; color: #fff; }
.info-card p { margin: 0; font-size: 0.86rem; line-height: 1.6; color: var(--silver-3); }
.info-card code {
    font-family: 'JetBrains Mono', monospace; font-size: 0.8rem;
    color: #ffa24a; background: rgba(255, 94, 20, 0.1);
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
.member .nim { font-family: 'JetBrains Mono', monospace; color: #ffa24a; font-size: 0.82rem; margin-top: 4px; }

.footer {
    margin-top: 3rem; padding-top: 1.4rem;
    border-top: 1px solid rgba(255, 255, 255, 0.07);
    text-align: center; font-size: 0.82rem; color: var(--silver-4);
}


/* ============================================================================
   TEMA ALA SITUS HOSTING: announcement bar, dropdown, CTA, perks, FAQ, footer
   ============================================================================ */
.announce {
    position: fixed; top: 0; left: 0; right: 0; z-index: 10000;
    height: 36px; display: flex; align-items: center; justify-content: center; gap: 8px;
    background: linear-gradient(90deg, #e84a00, #ff6a2b 40%, #ffa24a 70%, #e84a00);
    font-size: 0.8rem; font-weight: 600; color: #fff;
    box-shadow: 0 4px 20px rgba(255, 94, 20, 0.35);
}
.announce a { color: #fff !important; text-decoration: underline !important; text-underline-offset: 3px; }
.announce .badge { background: rgba(0,0,0,.28); border-radius: 999px; padding: 2px 9px; font-size: .68rem; letter-spacing: .05em; }
.topnav { top: 16px !important; }
.anchor { top: -100px !important; }

.nav-item { position: relative; }
.nav-item > a .caret { display: inline-block; margin-left: 5px; font-size: .6rem; transition: transform .25s ease; opacity: .7; }
.nav-item:hover > a .caret { transform: rotate(180deg); }
.dd-wrap {
    position: absolute; top: 100%; left: 50%;
    padding-top: 14px; min-width: 270px;
    opacity: 0; visibility: hidden;
    transform: translate(-50%, 10px);
    transition: opacity .25s ease, transform .25s ease, visibility .25s;
}
.nav-item:hover .dd-wrap { opacity: 1; visibility: visible; transform: translate(-50%, 0); }
.dd {
    background: rgba(12, 14, 20, 0.96);
    border: 1px solid rgba(255,255,255,.13);
    border-radius: 18px; padding: 8px;
    box-shadow: 0 24px 60px rgba(0,0,0,.65);
    backdrop-filter: blur(20px);
}
.dd a { display: flex !important; align-items: center; gap: 12px; padding: 10px 12px !important; border-radius: 12px !important; }
.dd a::after { display: none !important; }
.dd a:hover { background: rgba(255,94,20,.1) !important; }
.dd .ic {
    width: 34px; height: 34px; flex: none; border-radius: 10px; display: grid; place-items: center;
    background: rgba(255,94,20,.14); border: 1px solid rgba(255,133,51,.3); font-size: .95rem;
}
.dd b { display: block; color: #fff; font-size: .86rem; font-weight: 600; }
.dd small { display: block; color: var(--silver-3); font-size: .74rem; font-weight: 400; margin-top: 1px; }

.hero-cta { position: relative; z-index: 3; display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; margin-top: 1.6rem; }
.hero-cta a { pointer-events: auto; text-decoration: none !important; font-weight: 600; font-size: .95rem; border-radius: 14px; padding: 13px 26px; transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease; }
.btn-fire { color: #fff !important; background: linear-gradient(135deg, #ff5a1f, #ffa24a); box-shadow: 0 10px 30px rgba(255,94,20,.45); }
.btn-fire:hover { transform: translateY(-3px); box-shadow: 0 16px 40px rgba(255,94,20,.65); }
.btn-ghost { color: #e2e8f0 !important; background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.18); }
.btn-ghost:hover { transform: translateY(-3px); border-color: #ffa24a; color: #fff !important; }
.hero-chips { position: relative; z-index: 2; display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; margin-top: 1.3rem; max-width: 720px; }
.hero-chips span { font-size: .78rem; color: var(--silver-2); background: rgba(255,255,255,.05); border: 1px solid rgba(255,255,255,.1); padding: 5px 12px; border-radius: 999px; }
.hero-chips span::before { content: "✓ "; color: #ffa24a; font-weight: 700; }

.sec-eyebrow { display: inline-block; font-size: .72rem; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: #ffa24a; margin-bottom: .6rem; }

.pillar { text-align: left !important; }
.pillar .ico { font-size: 1.5rem; margin-bottom: 10px; }
.pillar ul { list-style: none; padding: 0; margin: 14px 0 16px 0; }
.pillar li { font-size: .84rem; color: var(--silver-2); padding: 3px 0; }
.pillar li::before { content: "✓"; color: #ffa24a; font-weight: 700; margin-right: 8px; }
.pillar .more { font-size: .86rem; font-weight: 600; color: #ffa24a !important; text-decoration: none !important; }
.pillar .more:hover { color: #fff !important; }

.panel-grid { display: grid; grid-template-columns: 1.05fr 1fr; gap: 18px; align-items: stretch; }
@media (max-width: 900px) { .panel-grid { grid-template-columns: 1fr; } }
.panel-list { display: grid; gap: 10px; }
.panel-list div { text-align: left; background: var(--card); border: 1px solid var(--line); border-radius: 14px; padding: 13px 16px; font-size: .9rem; color: var(--silver-1); transition: all .25s ease; }
.panel-list div:hover { border-color: rgba(255,115,36,.5); transform: translateX(6px); background: rgba(255,94,20,.07); }
.panel-list div::before { content: "▸"; color: #ffa24a; margin-right: 10px; }
.console {
    background: #05060a; border: 1px solid rgba(255,255,255,.1); border-radius: 18px; overflow: hidden;
    font-family: 'JetBrains Mono', monospace; font-size: .8rem; text-align: left;
    box-shadow: 0 20px 50px rgba(0,0,0,.55);
}
.console .bar { display: flex; gap: 7px; padding: 11px 14px; background: rgba(255,255,255,.04); border-bottom: 1px solid rgba(255,255,255,.07); }
.console .bar i { width: 10px; height: 10px; border-radius: 50%; background: #ff5f56; }
.console .bar i:nth-child(2) { background: #ffbd2e; } .console .bar i:nth-child(3) { background: #27c93f; }
.console .body { padding: 16px 18px; line-height: 1.9; color: var(--silver-2); }
.console .o { color: #ffa24a; } .console .g { color: #4ade80; } .console .m { color: var(--silver-4); }

.grid.g2x3 { grid-template-columns: repeat(3, 1fr); }
@media (max-width: 900px) { .grid.g2x3 { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 520px) { .grid.g2x3 { grid-template-columns: 1fr; } }
.perk .ico { width: 44px; height: 44px; margin: 0 auto 12px auto; border-radius: 14px; display: grid; place-items: center; font-size: 1.25rem;
    background: linear-gradient(135deg, rgba(255,94,20,.2), rgba(255,133,51,.06)); border: 1px solid rgba(255,133,51,.35); }

.stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-top: 1rem; }
.stat { text-align: center; padding: 16px 8px; border-radius: 16px; background: var(--card); border: 1px solid var(--line); transition: all .3s ease; }
.stat:hover { border-color: rgba(255,115,36,.5); transform: translateY(-3px); }
.stat b { display: block; font-size: 1.7rem; font-weight: 800; background: linear-gradient(180deg,#fff,#ffa24a); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.stat span { font-size: .78rem; color: var(--silver-3); }

.faq { max-width: 820px; margin: 0 auto; display: grid; gap: 10px; text-align: left; }
.faq details { background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 0 18px; transition: border-color .25s ease, background .25s ease; }
.faq details:hover { border-color: rgba(255,115,36,.4); }
.faq details[open] { border-color: rgba(255,115,36,.55); background: rgba(255,94,20,.05); }
.faq summary { cursor: pointer; list-style: none; display: flex; align-items: center; gap: 12px; padding: 16px 0; font-weight: 600; font-size: .95rem; color: #fff; }
.faq summary::-webkit-details-marker { display: none; }
.faq summary::before { content: "+"; width: 24px; height: 24px; flex: none; display: grid; place-items: center; border-radius: 8px; background: rgba(255,94,20,.18); color: #ffa24a; font-weight: 700; transition: transform .3s ease; }
.faq details[open] summary::before { content: "–"; transform: rotate(180deg); }
.faq p { margin: 0 0 16px 36px; font-size: .88rem; line-height: 1.7; color: var(--silver-3); }

.cta-banner {
    position: relative; overflow: hidden; text-align: center; margin-top: 3rem; padding: 2.6rem 1.5rem;
    border-radius: 26px; border: 1px solid rgba(255,133,51,.35);
    background: radial-gradient(ellipse at 50% 120%, rgba(255,94,20,.45), transparent 65%), linear-gradient(135deg, rgba(255,94,20,.12), rgba(15,17,24,.9));
}
.cta-banner h3 { margin: 0 0 .5rem 0; font-size: clamp(1.4rem, 3vw, 2rem); font-weight: 700; color: #fff; letter-spacing: -.02em; }
.cta-banner p { margin: 0 0 1.4rem 0; color: var(--silver-2); font-size: .95rem; }
.cta-banner a { display: inline-block; text-decoration: none !important; font-weight: 600; padding: 13px 28px; border-radius: 14px; }

.mega-footer { display: grid; grid-template-columns: 1.6fr 1fr 1fr 1fr; gap: 28px; text-align: left; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,.08); }
@media (max-width: 760px) { .mega-footer { grid-template-columns: 1fr 1fr; } }
.mega-footer h5 { margin: 0 0 12px 0; font-size: .78rem; text-transform: uppercase; letter-spacing: .1em; color: #fff; }
.mega-footer a { display: block; padding: 4px 0; font-size: .86rem; color: var(--silver-3) !important; text-decoration: none !important; transition: color .2s ease, transform .2s ease; }
.mega-footer a:hover { color: #ffa24a !important; transform: translateX(4px); }
.mega-footer p { font-size: .86rem; line-height: 1.7; color: var(--silver-3); margin: 10px 0 0 0; }
.copyright { margin-top: 2rem; padding-top: 1.2rem; border-top: 1px solid rgba(255,255,255,.06); text-align: center; font-size: .8rem; color: var(--silver-4); }


/* ============================================================================
   RESPONSIF (HP, tablet, desktop) - tidak boleh ada scroll horizontal
   ============================================================================ */
html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
    max-width: 100vw;
    overflow-x: hidden;
}
.block-container, .st-key-sheet { box-sizing: border-box; max-width: 100%; }
.st-key-sheet { overflow-x: clip; }
.st-key-sheet img, .st-key-sheet iframe { max-width: 100%; }

@media (max-width: 820px) {
    .block-container { padding-left: 0.8rem !important; padding-right: 0.8rem !important; }
    .topnav { width: calc(100% - 20px); padding: 7px 8px 7px 12px; top: 10px !important; }
    .nav-cta { padding: 8px 14px; font-size: 0.8rem; }
    .anchor { top: -90px !important; }
    .hero-spacer { height: 78vh; min-height: 460px; }
    .bg-fixed { padding-top: 18vh; }
    .hero-sub { font-size: 0.92rem; padding: 0 0.5rem; }
    .hero-cta a { padding: 12px 20px; font-size: 0.88rem; }
    .sec-head { margin: 2.4rem 0 1.1rem 0; }
    .grid { gap: 10px; }
    .panel-list div:hover { transform: none; }
    .mega-footer { grid-template-columns: 1fr 1fr; gap: 20px; }
    .mega-footer > div:first-child { grid-column: 1 / -1; }
    .cta-banner { padding: 2rem 1rem; border-radius: 20px; }
}
@media (max-width: 640px) {
    .stats { gap: 8px; }
    .stat { padding: 12px 4px; }
    .stat b { font-size: 1.35rem; }
    .stat span { font-size: 0.68rem; line-height: 1.3; display: block; }
    .st-key-switchwrap { margin-bottom: 1.4rem; }
    .st-key-switchwrap div[data-testid="stButton"] > button[kind] { padding: 0.8rem 0 !important; }
    .st-key-switchwrap div[data-testid="stButton"] > button[kind] p { font-size: 1rem !important; }
    [class*="st-key-card"] { padding: 12px 12px 8px 12px; }
    .console { font-size: 0.72rem; }
    .console .body { padding: 12px 14px; overflow-x: auto; white-space: nowrap; }
    .faq p { margin-left: 0; }
    .faq summary { font-size: 0.9rem; }
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
# Nilai input disimpan di key "sv_*" (bukan key widget) lalu disinkronkan lewat
# on_change, sehingga isi tetap ada saat pindah tab tanpa error session_state.
st.session_state.setdefault("sv_enc_text", "halooo")
st.session_state.setdefault("sv_digit_p", 4)
st.session_state.setdefault("sv_digit_q", 4)
st.session_state.setdefault("sv_dec_cipher", "")
st.session_state.setdefault("sv_dec_d", "")
st.session_state.setdefault("sv_dec_n", "")


def sync(name: str) -> None:
  st.session_state["sv_" + name] = st.session_state["w_" + name]


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


def copy_tile(
    title: str,
    value,
    tone: str = "s",
    big: bool = False,
    highlight: bool = False,
) -> None:
  """Kotak nilai dengan tombol Salin (clipboard). Nilai panjang bisa digeser."""
  value = str(value)
  colors = {"o": "#ffa24a", "s": "#e2e8f0", "b": "#38bdf8"}
  accent = "#38bdf8" if st.session_state.mode_selector == "Decrypt" else "#ffa24a"
  accent_rgb = "56,189,248" if accent == "#38bdf8" else "255,133,51"
  border = f"rgba({accent_rgb},0.5)" if highlight else "rgba(255,255,255,0.09)"
  bg = f"rgba({accent_rgb},0.08)" if highlight else "rgba(9,11,16,0.85)"
  size = "1.05rem" if big else "0.88rem"
  safe_js = json.dumps(value).replace("</", "<\\/")
  doc = f"""<!doctype html><html><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700&family=JetBrains+Mono:wght@500;600;700&display=swap');
*{{box-sizing:border-box}}
html,body{{margin:0;background:transparent;font-family:'Inter',sans-serif;overflow:hidden}}
.tile{{background:{bg};border:1px solid {border};border-radius:12px;padding:9px 12px 10px 14px;transition:border-color .25s,background .25s}}
.tile:hover{{border-color:rgba({accent_rgb},.55)}}
.top{{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:5px}}
.t{{font-size:.72rem;font-weight:600;color:{accent if highlight else '#94a3b8'};white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
button{{display:inline-flex;align-items:center;gap:5px;cursor:pointer;font:600 .7rem 'Inter',sans-serif;color:#e2e8f0;
 background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-radius:999px;padding:4px 11px;transition:all .2s}}
button:hover{{background:{accent};border-color:{accent};color:#fff;transform:translateY(-1px)}}
button.ok{{background:#16a34a;border-color:#16a34a;color:#fff}}
.v{{font-family:'JetBrains Mono',monospace;font-size:{size};font-weight:{700 if big else 600};color:{'#fff' if big else colors.get(tone,'#e2e8f0')};
 white-space:nowrap;overflow-x:auto;padding-bottom:3px;scrollbar-width:thin;scrollbar-color:#475569 transparent}}
.v::-webkit-scrollbar{{height:5px}}.v::-webkit-scrollbar-thumb{{background:#475569;border-radius:999px}}
</style></head><body>
<div class="tile"><div class="top"><span class="t">{html.escape(title)}</span>
<button id="b" type="button"><span id="i">⧉</span><span id="l">Salin</span></button></div>
<div class="v">{html.escape(value)}</div></div>
<script>
const text={safe_js};
const b=document.getElementById('b'),l=document.getElementById('l'),i=document.getElementById('i');
function fallback(t){{const a=document.createElement('textarea');a.value=t;a.style.position='fixed';a.style.opacity='0';
 document.body.appendChild(a);a.select();let ok=false;try{{ok=document.execCommand('copy')}}catch(e){{}}document.body.removeChild(a);return ok}}
b.addEventListener('click',async()=>{{
 let ok=false;
 try{{await navigator.clipboard.writeText(text);ok=true}}catch(e){{ok=fallback(text)}}
 l.textContent=ok?'Tersalin':'Gagal';i.textContent=ok?'✓':'!';b.classList.toggle('ok',ok);
 setTimeout(()=>{{l.textContent='Salin';i.textContent='⧉';b.classList.remove('ok')}},1600);
}});
</script></body></html>"""
  if hasattr(st, "iframe"):  # Streamlit terbaru (components.html sudah deprecated)
    st.iframe(doc, height=84)
  else:
    components.html(doc, height=84)


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
        <div class="nav-item"><a href="#workspace" target="_self">Alat<span class="caret">▼</span></a>
            <div class="dd-wrap"><div class="dd">
                <a href="#workspace" target="_self"><span class="ic">🔒</span><span><b>Enkripsi</b><small>Bangkitkan kunci &amp; sandikan pesan</small></span></a>
                <a href="#workspace" target="_self"><span class="ic">🔓</span><span><b>Dekripsi</b><small>Pulihkan teks dari ciphertext</small></span></a>
                <a href="#fitur" target="_self"><span class="ic">🔑</span><span><b>Pasangan kunci</b><small>Kunci publik (e, n) &amp; privat (d, n)</small></span></a>
            </div></div></div>
        <div class="nav-item"><a href="#cara-kerja" target="_self">Belajar<span class="caret">▼</span></a>
            <div class="dd-wrap"><div class="dd">
                <a href="#cara-kerja" target="_self"><span class="ic">📘</span><span><b>Cara kerja RSA</b><small>Empat langkah dari teks ke cipher</small></span></a>
                <a href="#keunggulan" target="_self"><span class="ic">⚡</span><span><b>Keunggulan</b><small>Fitur utama RSA Studio</small></span></a>
                <a href="#faq" target="_self"><span class="ic">❓</span><span><b>FAQ</b><small>Pertanyaan yang sering muncul</small></span></a>
            </div></div></div>
        <div class="nav-item"><a href="#fitur" target="_self">Fitur</a></div>
        <div class="nav-item"><a href="#tim" target="_self">Tim</a></div>
    </div>
    <a class="nav-cta" href="#workspace" target="_self">Mulai Sekarang</a>
</nav>
""",
    unsafe_allow_html=True,
)

# ==============================================================================
# 6. BACKGROUND TETAP + TEMA MODE
# ==============================================================================
selected_mode = st.session_state.mode_selector  # callback tombol sudah dijalankan


def set_mode(mode: str) -> None:
  st.session_state.mode_selector = mode


st.markdown(
    """
<div class="bg-fixed">
    <div class="hero-pill"><b>RSA ENGINE</b><span>Kriptografi asimetris dengan offset −27</span></div>
    <h1 class="hero-title">RSA Encrypt &amp; Decrypt</h1>
    <div class="hero-sub">
        Bangkitkan kunci publik dan privat, enkripsi pesan teks, lalu dekripsi kembali
        dengan rincian setiap langkahnya.
    </div>
    <div class="hero-cta">
        <a class="btn-fire" href="#workspace" target="_self">Mulai Enkripsi</a>
        <a class="btn-ghost" href="#cara-kerja" target="_self">Pelajari Cara Kerja</a>
    </div>
    <div class="hero-arc"></div>
</div>
<div class="hero-spacer"><span id="beranda" class="anchor"></span></div>
""",
    unsafe_allow_html=True,
)

_thumb = ".st-key-switchwrap [data-testid=\"stHorizontalBlock\"]::before{"
_btn = ".st-key-switchwrap .st-key-%s div[data-testid=\"stButton\"] > button[kind] p{color:#fff !important;font-weight:700 !important;text-shadow:0 1px 4px rgba(0,0,0,.35);}"
if selected_mode == "Decrypt":
  theme_css = (
      _thumb
      + "transform:translateX(100%);background:linear-gradient(135deg,#38bdf8 0%,#818cf8 60%,#a5b4fc 100%);"
      "box-shadow:0 0 28px rgba(56,189,248,.55),inset 0 1px 1px rgba(255,255,255,.55);}"
      + _btn % "sw_dec"
      + '[class*="st-key-card"]:hover{border-color:rgba(56,189,248,.4) !important;}'
      "div[data-testid=\"stTextInput\"] input:focus{border-color:#38bdf8 !important;box-shadow:0 0 0 2px rgba(56,189,248,.25) !important;}"
      "div[data-testid=\"stButton\"] > button[kind=\"primary\"]{background:linear-gradient(135deg,#0ea5e9 0%,#818cf8 100%) !important;box-shadow:0 8px 25px rgba(56,189,248,.35) !important;}"
      "div[data-testid=\"stButton\"] > button[kind=\"primary\"]:hover{box-shadow:0 12px 32px rgba(56,189,248,.55) !important;}"
  )
else:
  theme_css = (
      _thumb
      + "transform:translateX(0);background:linear-gradient(135deg,#ff5a1f 0%,#ffa24a 100%);"
      "box-shadow:0 0 28px rgba(255,94,20,.65),inset 0 1px 1px rgba(255,255,255,.45);}"
      + _btn % "sw_enc"
  )
st.markdown(f"<style>{theme_css}</style>", unsafe_allow_html=True)

# ==============================================================================
# 7. SHEET KONTEN (z-index di atas background, memburamkan background saat naik)
# ==============================================================================
with st.container(key="sheet"):
  st.markdown('<span id="workspace" class="anchor"></span>', unsafe_allow_html=True)

  with st.container(key="switchwrap"):
    sc1, sc2 = st.columns(2, gap="small")
    with sc1:
      st.button(
          "Encrypt", key="sw_enc", on_click=set_mode, args=("Encrypt",),
          use_container_width=True,
      )
    with sc2:
      st.button(
          "Decrypt", key="sw_dec", on_click=set_mode, args=("Decrypt",),
          use_container_width=True,
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
            value=st.session_state.sv_enc_text,
            placeholder="Masukkan pesan (ASCII 32–126)...",
            label_visibility="collapsed",
            key="w_enc_text",
            on_change=sync,
            args=("enc_text",),
        )

      with st.container(key="card_digits"):
        card_label("Blok 2 · Panjang digit prima p &amp; q (1–24 digit)")
        c_p, c_q = st.columns(2, gap="medium")
        with c_p:
          digit_p = st.number_input(
              "Digit prima p", min_value=1, max_value=24, step=1,
              value=int(st.session_state.sv_digit_p), key="w_digit_p",
              on_change=sync, args=("digit_p",),
          )
        with c_q:
          digit_q = st.number_input(
              "Digit prima q", min_value=1, max_value=24, step=1,
              value=int(st.session_state.sv_digit_q), key="w_digit_q",
              on_change=sync, args=("digit_q",),
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
        if enc_res:
          copy_tile("Ciphertext (Cᵢ)", cipher_str, "o", highlight=True)
        else:
          st.markdown(
              '<div class="mono-scroll" style="color:#ffa24a;font-weight:600;'
              'border-color:rgba(255,106,26,0.35);margin-bottom:6px;">'
              f"{cipher_str}</div>",
              unsafe_allow_html=True,
          )

      if enc_res:

        def copy_to_decrypt():
          r = st.session_state.enc_result
          st.session_state.sv_dec_cipher = " ".join(r["blok_cipher"])
          st.session_state.sv_dec_d = str(r["d"])
          st.session_state.sv_dec_n = str(r["n"])
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
            copy_tile("p terpilih", enc_res["p"], "o")
            copy_tile("n (p × q)", enc_res["n"], "s")
            copy_tile("e (eksponen publik)", enc_res["e"], "o")
          with g2:
            copy_tile("q terpilih", enc_res["q"], "o")
            copy_tile("m = (p − 1)(q − 1)", enc_res["m"], "s")
            copy_tile("d (eksponen privat)", enc_res["d"], "o")

          copy_tile("Kode ASCII asli", " ".join(enc_res["ascii_asli"]), "s")
          copy_tile("Kode 2 digit (−27)", " ".join(enc_res["kode_2digit"]), "s")
          copy_tile("Blok plaintext 3 digit (Pᵢ)", " ".join(enc_res["blok_plain"]), "s")

          k1, k2 = st.columns(2)
          with k1:
            copy_tile("Kunci publik (e, n)", f"({enc_res['e']}, {enc_res['n']})", "o", highlight=True)
          with k2:
            copy_tile("Kunci privat (d, n)", f"({enc_res['d']}, {enc_res['n']})", "s")
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
            value=st.session_state.sv_dec_cipher,
            placeholder="Contoh: 407 436 812",
            label_visibility="collapsed",
            key="w_dec_cipher",
            on_change=sync,
            args=("dec_cipher",),
        )

      with st.container(key="card_dn"):
        card_label("Blok 2 · Nilai d &amp; n", "b")
        col_d, col_n = st.columns(2, gap="medium")
        with col_d:
          d_in = st.text_input(
              "Nilai d", value=st.session_state.sv_dec_d, placeholder="Masukkan d...",
              key="w_dec_d", on_change=sync, args=("dec_d",),
          )
        with col_n:
          n_in = st.text_input(
              "Nilai n", value=st.session_state.sv_dec_n, placeholder="Masukkan n...",
              key="w_dec_n", on_change=sync, args=("dec_n",),
          )

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
          copy_tile("Blok plaintext 3 digit (Pᵢ)", " ".join(dec_res["blok_plain"]), "b")
          copy_tile("Pᵢ menjadi 2 digit (sebelum +27)", " ".join(dec_res["pi_2digit"]), "s")
          copy_tile("Kode ASCII asli (+27)", " ".join(dec_res["ascii_dec"]), "s")
          copy_tile("Teks asli final", dec_res["hasil_teks"], "b", big=True, highlight=True)
        else:
          st.markdown(
              '<div class="empty-note">Masukkan blok ciphertext beserta nilai <b>d</b> dan '
              "<b>n</b> di sebelah kiri, lalu tekan <b>Dekripsi ciphertext</b> untuk melihat "
              "blok plaintext, konversi Pᵢ 2 digit, dan teks aslinya.</div>",
              unsafe_allow_html=True,
          )

  # ==============================================================================
  # 10. KEUNGGULAN, FITUR, CARA KERJA, TIM, FAQ, CTA, FOOTER
  # ==============================================================================
  st.markdown(
      """
  <span id="keunggulan" class="anchor"></span>
  <div class="sec-head">
      <span class="sec-eyebrow">Satu alat, tiga kebutuhan</span>
      <h2>Enkripsi RSA yang mudah dipahami.</h2>
      <p>Dari membangkitkan kunci sampai memulihkan pesan, semuanya dalam satu halaman.</p>
  </div>
  <div class="grid g3">
      <div class="info-card pillar"><div class="ico">🔒</div><h4>Enkripsi</h4>
          <p>Ubah teks menjadi blok angka lalu sandikan dengan kunci publik.</p>
          <ul><li>Prima acak 1–24 digit</li><li>Uji prima Miller-Rabin</li><li>Rincian p, q, n, m, e, d</li></ul>
          <a class="more" href="#workspace" target="_self">Buka enkripsi →</a></div>
      <div class="info-card pillar"><div class="ico">🔓</div><h4>Dekripsi</h4>
          <p>Pulihkan pesan asli dari ciphertext dengan kunci privat.</p>
          <ul><li>Tempel cipher, d, dan n</li><li>Lihat tiap langkah konversi</li><li>Pesan error yang jelas</li></ul>
          <a class="more" href="#workspace" target="_self">Buka dekripsi →</a></div>
      <div class="info-card pillar"><div class="ico">🔑</div><h4>Manajemen kunci</h4>
          <p>Pasangan kunci tampil lengkap dan siap disalin.</p>
          <ul><li>Kunci publik (e, n)</li><li>Kunci privat (d, n)</li><li>Kirim ke tab Decrypt</li></ul>
          <a class="more" href="#fitur" target="_self">Lihat fitur →</a></div>
  </div>

  <span id="fitur" class="anchor"></span>
  <div class="sec-head">
      <span class="sec-eyebrow">Panel kerja</span>
      <h2>Panel yang langsung bisa dipakai.</h2>
      <p>Dirancang supaya kamu fokus pada angkanya, bukan pada antarmukanya.</p>
  </div>
  <div class="panel-grid">
      <div class="panel-list">
          <div>Switch Encrypt/Decrypt dengan kapsul yang bergeser mulus</div>
          <div>Hasil kunci, blok, dan ciphertext tersusun rapi per kartu</div>
          <div>Nilai panjang tetap rapi dan bisa digeser ke samping</div>
          <div>Kirim ciphertext dan kunci ke tab Decrypt otomatis</div>
          <div>Rincian ASCII, kode 2 digit, dan blok 3 digit</div>
      </div>
      <div class="console">
          <div class="bar"><i></i><i></i><i></i></div>
          <div class="body">
              <span class="m">$</span> rsa --encrypt <span class="o">"halooo"</span><br>
              <span class="m">›</span> prima p, q dibangkitkan <span class="g">✓</span><br>
              <span class="m">›</span> n = p × q, m = (p−1)(q−1) <span class="g">✓</span><br>
              <span class="m">›</span> e dipilih, d dihitung <span class="g">✓</span><br>
              <span class="m">›</span> ciphertext berhasil dibuat <span class="g">✓</span><br>
              <span class="o">▍</span>
          </div>
      </div>
  </div>

  <div class="sec-head">
      <span class="sec-eyebrow">Keunggulan</span>
      <h2>Fitur yang membuat belajar RSA lebih cepat.</h2>
  </div>
  <div class="grid g4">
      <div class="info-card perk"><div class="ico">⚡</div><h4>Hasil instan</h4><p>Kunci dan ciphertext muncul begitu tombol ditekan.</p></div>
      <div class="info-card perk"><div class="ico">🧮</div><h4>Miller-Rabin</h4><p>Pengujian bilangan prima deterministik yang akurat.</p></div>
      <div class="info-card perk"><div class="ico">📏</div><h4>1–24 digit</h4><p>Pilih panjang prima sesuai kebutuhan latihanmu.</p></div>
        <div class="info-card perk"><div class="ico">🧾</div><h4>Langkah terperinci</h4><p>Setiap tahap konversi ditampilkan, bukan hanya hasil akhir.</p></div>
    </div>
  <div class="stats">
      <div class="stat"><b>24</b><span>digit prima maksimum</span></div>
      <div class="stat"><b>95</b><span>karakter ASCII didukung</span></div>
      <div class="stat"><b>3</b><span>digit per blok</span></div>
    </div>

  <span id="cara-kerja" class="anchor"></span>
  <div class="sec-head">
      <span class="sec-eyebrow">Cara kerja</span>
      <h2>Empat langkah dari teks sampai ciphertext.</h2>
  </div>
  <div class="grid g4">
      <div class="info-card"><div class="step">1</div><h4>Ubah teks ke blok</h4>
          <p>Setiap karakter jadi kode ASCII, dikurangi 27 sehingga tersisa 2 digit, lalu digabung dan dipotong menjadi blok 3 digit.</p></div>
      <div class="info-card"><div class="step">2</div><h4>Bangkitkan kunci</h4>
          <p>Pilih dua prima acak <code>p</code> dan <code>q</code>, hitung <code>n = p × q</code> dan <code>m = (p−1)(q−1)</code>, lalu cari <code>e</code> dan <code>d</code>.</p></div>
      <div class="info-card"><div class="step">3</div><h4>Enkripsi</h4>
          <p>Setiap blok plaintext dihitung dengan <code>C = P^e mod n</code>. Hasilnya adalah deretan angka ciphertext.</p></div>
      <div class="info-card"><div class="step">4</div><h4>Dekripsi</h4>
          <p>Dengan <code>P = C^d mod n</code> blok kembali ke bentuk semula, lalu ditambah 27 dan dikonversi menjadi huruf.</p></div>
  </div>

  <span id="tim" class="anchor"></span>
  <div class="sec-head">
      <span class="sec-eyebrow">Tim</span>
      <h2>Dibuat oleh tiga orang.</h2>
  </div>
  <div class="grid g3">
      <div class="info-card member"><div class="avatar">CZ</div><h4>Christian Zarkasie</h4><div class="nim">(002)</div></div>
      <div class="info-card member"><div class="avatar">CP</div><h4>Clifton Pratomo</h4><div class="nim">(005)</div></div>
      <div class="info-card member"><div class="avatar">NT</div><h4>I Nyoman Tisna Satya Wijaya</h4><div class="nim">(042)</div></div>
  </div>

  <span id="faq" class="anchor"></span>
  <div class="sec-head">
      <span class="sec-eyebrow">FAQ</span>
      <h2>Pertanyaan yang sering muncul.</h2>
      <p>Tidak menemukan jawabanmu? Tanyakan ke tim lewat dosen pembimbing.</p>
  </div>
  <div class="faq">
      <details><summary>Apakah ini aman untuk data sungguhan?</summary>
          <p>Tidak. Alat ini untuk belajar. Kunci RSA aman butuh bilangan prima jauh lebih panjang (sekitar 2048 bit) dan skema padding. Pembatasan 24 digit di sini sengaja dibuat agar hasilnya mudah diikuti.</p></details>
      <details><summary>Kenapa dikurangi 27 dan dibagi blok 3 digit?</summary>
          <p>Kode ASCII cetak (32–126) dikurangi 27 menjadi 5–99, sehingga selalu 2 digit. Digit digabung lalu dipotong per 3 agar setiap blok lebih kecil dari n (syarat n &gt; 999).</p></details>
      <details><summary>Mana kunci publik dan mana kunci privat?</summary>
          <p>Kunci publik adalah pasangan (e, n) untuk mengenkripsi. Kunci privat adalah (d, n) untuk mendekripsi. Bagikan hanya yang publik.</p></details>
      <details><summary>Kenapa hasil dekripsi gagal atau berbentuk aneh?</summary>
          <p>Biasanya nilai d atau n tidak cocok dengan kunci yang dipakai saat enkripsi, atau ciphertext terpotong. Gunakan tombol kirim ke tab Decrypt agar nilainya terisi otomatis.</p></details>
      <details><summary>Karakter apa saja yang didukung?</summary>
          <p>Huruf besar dan kecil, angka, spasi, dan tanda baca ASCII 32–126. Karakter di luar itu (misalnya emoji) akan ditolak dengan pesan error.</p></details>
  </div>

  <div class="cta-banner">
      <h3>Siap mencoba enkripsi RSA?</h3>
      <p>Bangkitkan kunci dan sandikan pesan pertamamu dalam hitungan detik.</p>
      <a class="btn-fire" href="#workspace" target="_self">Mulai Sekarang</a>
  </div>

  <div class="mega-footer">
      <div><div class="nav-brand"><span class="nav-logo">R</span> RSA Studio</div>
          <p>Alat belajar kriptografi asimetris dengan offset −27, dibuat untuk memahami RSA langkah demi langkah.</p></div>
      <div><h5>Alat</h5><a href="#workspace" target="_self">Enkripsi</a><a href="#workspace" target="_self">Dekripsi</a><a href="#fitur" target="_self">Pasangan kunci</a></div>
      <div><h5>Belajar</h5><a href="#cara-kerja" target="_self">Cara kerja</a><a href="#keunggulan" target="_self">Keunggulan</a><a href="#faq" target="_self">FAQ</a></div>
      <div><h5>Tim</h5><a href="#tim" target="_self">Christian Zarkasie</a><a href="#tim" target="_self">Clifton Pratomo</a><a href="#tim" target="_self">I Nyoman Tisna S. W.</a></div>
  </div>
  <div class="copyright">© 2026 RSA Studio · Dibuat untuk tujuan edukasi</div>
  """,
      unsafe_allow_html=True,
  )
