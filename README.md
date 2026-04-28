# Linear Regression Interactive Workspace

這是一個基於 Streamlit 開發的互動式線性回歸教學工具。使用者可以動態調整線性回歸的參數，並即時觀察資料分布與回歸線的變化。

## 功能特點 (Features)
- **即時參數調整**: 透過滑桿調整斜率 ($m$) 與截距 ($b$)。
- **動態隨機資料**: 可調整隨機噪音 (Noise) 的大小，觀察資料點的離散程度。
- **視覺化呈現**: 使用 Matplotlib 繪製高品質圖表，包含：
  - 藍色散佈圖：代表生成的隨機資料點。
  - 紅色直線：代表目前參數下的線性回歸模型。
- **直觀佈局**: 參數調整面板位於圖表下方，提供更好的操作體驗。

## 快速開始 (Quick Start)

### 1. 安裝環境需求
請確保您的系統已安裝 Python 3.8+，並執行以下指令安裝必要套件：

```bash
pip install streamlit numpy matplotlib
```

### 2. 執行應用程式
在專案目錄下執行：

```bash
python -m streamlit run regression_app.py
```

執行後，瀏覽器會自動開啟網頁界面（預設為 http://localhost:8501 ）。

## 部署說明 (Deployment - Live Demo)

本專案可以直接部署於 **Streamlit Community Cloud**:
1. 登入 [Streamlit Cloud](https://share.streamlit.io/)。
2. 連結 GitHub 並選擇本儲存庫 (`DIC7-ML`)。
3. 設定 Main file path 為 `regression_app.py`。
4. 點擊 Deploy 即可完成部署。

## 檔案說明 (File Structure)
- `regression_app.py`: 主要的 Streamlit 應用程式程式碼。
- `chatlog.md`: 本專案的開發過程對話紀錄。
- `README.md`: 專案介紹與安裝指南。

## 預覽圖片 (Preview)
![Linear Regression Preview](https://github.com/user-attachments/assets/your-screenshot-here.png)
*(請自行在 GitHub 上傳圖片後替換連結)*
