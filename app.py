"""評等分類蛇 — Streamlit 外殼：讀取 game.html，把 Supabase 設定塞進去後顯示。"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="評等分類蛇", page_icon="🐍", layout="centered")

# 把 Streamlit 自己的選單、頁尾和多餘留白藏起來，讓遊戲畫面更乾淨
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding-top: 0.5rem; padding-bottom: 0; max-width: 560px;}
    </style>
    """,
    unsafe_allow_html=True,
)


def get_secret(*names: str) -> str:
    """依序找 secrets 裡的設定；找不到就回傳空字串（遊戲仍可單機玩）。"""
    try:
        for name in names:
            if name in st.secrets:
                return str(st.secrets[name])
    except Exception:
        pass
    return ""


supabase_url = get_secret("SUPABASE_URL")
supabase_key = get_secret("SUPABASE_KEY", "SUPABASE_ANON_KEY")

html = Path(__file__).with_name("game.html").read_text(encoding="utf-8")
html = html.replace("__SUPABASE_URL__", supabase_url.rstrip("/"))
html = html.replace("__SUPABASE_KEY__", supabase_key)

components.html(html, height=1500, scrolling=True)
