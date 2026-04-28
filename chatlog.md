# 對話紀錄與開發總結 (Chat Log)

## 專案目標
建立一個使用 Streamlit 的網頁應用程式，讓使用者能夠動態調整線性回歸的參數（斜率、截距、隨機分布大小），並即時觀察圖表變化。

## 對話紀錄摘要

### 1. 初始需求開發
- **需求**: 使用 Streamlit 建立線性回歸操作台。
- **功能**: 
  - 斜率 ($m$)、截距 ($b$) 調整。
  - 隨機 Noise 大小調整。
  - 固定生成 100 點隨機資料。
  - 使用 Matplotlib 進行視覺化。
- **開發檔案**: [regression_app.py](file:///c:/Users/user/Desktop/新增資料夾/regression_app.py)

### 2. 介面與佈局優化
- **需求**: 調整介面，將參數調整滑桿移至圖表下方，並縮小圖表尺寸以優化感官。
- **更新項目**:
  - `st.set_page_config` 改為 `centered` 佈局。
  - 使用 `st.container` 與 `st.columns` 將滑桿排列在圖表下方。
  - 縮小圖表 `figsize` 為 `(6, 4)`。

### 3. 文字與顯示修正
- **需求**: 圖表內的中文無法正常顯示，需改為英文。
- **更新項目**:
  - 將 Matplotlib 圖表中的 Title, X-axis label, Y-axis label 以及 Legend 全部改為英文。

### 4. 部署支援與 Live Demo 指南
- **需求**: 使用者詢問如何在 Streamlit 上建立 Live Demo，且部署後遇到 `ModuleNotFoundError`。
- **更新項目**:
  - 在 `README.md` 中新增 Streamlit Community Cloud 部署步驟。
  - **建立 `requirements.txt`**: 包含 `streamlit`, `numpy`, `matplotlib` 套件清單，解決雲端部署時的環境依賴問題。
  - 將所有檔案（包含新建立的 `requirements.txt`）push 至 GitHub 儲存庫。

---

## 目前狀態
- **檔案路徑**: `c:\Users\user\Desktop\新增資料夾\regression_app.py`
- **執行指令**: `python -m streamlit run regression_app.py`
- **預覽網址**: `http://localhost:8506` (本地) / [GitHub Repo](https://github.com/herny0207/DIC7-ML)
