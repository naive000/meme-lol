# DEX Screener App — 代幣詳情頁 4 子分頁全功能走查

> 掃描範圍：實機點進一個真實代幣（Solana 鏈「Anonymous Cat / ZCAT」，Raydium CLMM 交易對）的詳情頁，逐一點開底部 4 個子分頁：**Info / Chart+Txns / Chart / Txns**，以及共用於這些分頁頂部的 **Holders / Liquidity Providers / Maps** 列。方法沿用 Screener 分頁走查同一套：WDA accessibility tree 抓座標點擊，`wda.sh shot` 截圖後用 `crop.py` 去除頂部狀態列（時間/WiFi/電池）。截圖檔案存放於暫存區 `/tmp/claude-1000/-home-crazy-meme-lol/a86e65ed-f5aa-4767-bab6-b7715104d41f/scratchpad/shots/`（暫存，非版控，重開機或換 session 可能消失)。
>
> 本文件補足、並更正 `dex-screener-features.md` 原本對這 4 個子分頁「未逐一展開驗證，推測」的部分——這次全部實際點開驗證過。

---

## 子分頁 1：Info（預設進入頁）

截圖：`05_info_crop.png`（上半段統計）、`06_info_scroll1_crop.png`／`07_more.png`（下滑後：社群評價投票 + 專案介紹 + 換算器）

### 上半段（原本 round 1 就記錄過，這次確認無誤）
- 頭部：返回鍵、代幣圖示+名稱、分享、更多選項（⋯）
- 鏈徽章（Solana）→ DEX 徽章（Raydium）→ 交易對類型標籤（CLMM）
- PRICE USD / PRICE（原始計價幣，如 ZEC）
- LIQUIDITY（旁邊有🔒鎖圖示，代表流動性已鎖）/ FDV / MARKET CAP
- 時間區間分段：5M / 1H / 6H / 24H，各自漲跌 %
- TXNS 總筆數 + BUYS/SELLS 對比長條
- VOLUME 總量 + BUY VOL/SELL VOL 對比長條
- TRADERS 總人數 + BUYERS/SELLERS 對比長條
- Watchlist（收藏）/ Alerts（設價格提醒）按鈕
- Trade（跳轉外部 DEX 實際下單）
- Pair created：交易對創建至今時間（如「9d 8h ago」）

### 下滑後的新發現（round 1 沒記錄到，這次是本輪最大發現）

**① 「Audit」社群評價投票區塊 + 官方免責聲明**
- 區塊標題是「Audit」，右上角小字顯示彙整結果（如「No issues」）
- 底下有一段可展開的警語（預設收合成一行，點「More」展開／點「Less」收合）：
  > 「Warning! Audits may not be 100% accurate! They are not intended as advice and should be considered in conjunction with other factors. DEX Screener does not validate nor assume responsibility for the accuracy of data obtained from these external auditors.」
  （翻譯：**審計結果不保證 100% 準確，不算投資建議，DEX Screener 不對這些外部審計資料的準確性負責**）
- 再往下是 4 顆表情符號投票鈕，各自顯示目前票數：🚀（火箭/看漲，644 票）、🔥（熱門，44 票）、💩（大便/爛幣，83 票）、🚩（紅旗/檢舉詐騙，97 票）
- **實測發現且需要提醒使用者的關鍵點**：這 4 顆是**任何人都能按的即時投票鈕**，不需要登入帳號。測試時點了一下🚩（紅旗），App 跳出 Cloudflare Turnstile 人機驗證（自動秒過，沒有要求手動操作），驗證通過後**票數立刻從 97 變成 98**，畫面截圖見 `09_flag_result.png`。
  - ⚠️ **這代表這組投票數字只是「防機器人洗票」而已，門檻極低（不用登入、驗證機是自動過），完全可以被任何人（包含專案方自己）大量刷高「🚀看漲」票，或被競爭對手/黑粉刷高「🚩檢舉」票。不能當作可信的安全指標，最多是輔助參考。**
  - 這點連同官方自己寫的免責聲明「Audits may not be 100% accurate」，是這次掃描中最值得放進網站風險教學的素材：**連 App 官方都自己承認這數字不準，使用者更不該把它當成「這個幣安全/不安全」的唯一依據。**

**② 專案自介卡片**
- 大頭貼、專案名稱、一句話 slogan（如「The Cat Stays Anonymous. No Socials. Zcash Rewards.」）
- 「Metas」標籤（如「🐱 Cat」）——類似分類/主題標籤，方便同類型代幣被歸類搜尋到，跟 Screener 首頁「Metas」儀表板是同一套系統

**③ 內建換算計算機**
- 輸入任意數量的代幣（預設 1），下方自動換算成 USD 或原始計價幣（ZEC），有 USD/ZEC 切換鈕
- 純換算顯示用，不是下單介面（下單要用上面的 Trade 按鈕跳轉外部 DEX）

---

## 子分頁 2：Chart+Txns（上下分割視圖）

截圖：`10_charttxns_crop.png`

- **上半：TradingView 風格 K 線圖**（WebView，非原生元件，無法讀取內部文字，只能截圖記錄）
  - 頂部工具列：新增指標（+）、時間粒度（15m / 1h / 4h / 12h / D / W + 更多下拉）、圖表類型切換（K線/其他）、副圖指標切換、`fx` 函數編輯
  - 左側繪圖工具列：十字準星、趨勢線、水平線、通道、筆刷、文字標註、表情符號標記、測距尺、放大鏡、磁吸模式、鎖定繪圖等——完整專業看盤工具，小白幾乎用不到，只需要知道「這是看盤軟體 TradingView 的內嵌版」即可
  - 底部：Date Range 選擇器、目前時間戳、auto 即時更新開關
- **下半：資料表格**，由「Holders / Liquidity Providers / Maps」三顆按鈕切換（見下方共用區塊說明），預設不特別高亮任一顆時顯示的其實是 **Txns 交易紀錄表**（TXN 買賣圖示+時間 / USD 金額 / PRICE / TRADER 錢包縮寫，每欄都有篩選圖示）
- **更正 round 1 的舊記錄**：原本寫「下半三個子分頁 Txns / Top Traders / Holders」，這次實測**沒有找到「Top Traders」這個分頁**，正確應該是「Holders / Liquidity Providers / Maps」三顆切換鈕 + 一個預設不特別標記的 Txns 表格狀態，共 4 種表格內容、3 顆按鈕。

---

## 子分頁 3：Chart（全螢幕圖表）

截圖：`11_chart_crop.png`

- 跟 Chart+Txns 的上半圖表完全一樣（同一個 TradingView WebView），只是把下半的 Txns 表格拿掉，圖表區域變全螢幕
- 因為空間變大，左側繪圖工具列多顯示了幾顆平常被裁切掉的按鈕（鎖定繪圖、隱藏繪圖、垃圾桶清除、更多繪圖形狀）
- **更正 round 1 的舊記錄**：原本寫「未逐一展開驗證，推測為 Chart+Txns 拿掉下方交易表的精簡版」——這次確認**推測正確**，就是拿掉 Txns 表格的全螢幕看盤版。

---

## 子分頁 4：Txns（全螢幕交易紀錄）

截圖：`04_txns_crop.png`

- 跟 Chart+Txns 的下半 Txns 表格完全一樣，只是拿掉上半的圖表，表格變全螢幕，一次能看更多筆交易紀錄
- 表格上方一樣有「Holders (20,107) / Liquidity Providers / Maps」三顆切換鈕（跟 Chart+Txns 共用同一套邏輯）
- **更正 round 1 的舊記錄**：原本寫「未逐一展開驗證，推測為 Chart+Txns 下方表格的全螢幕版」——這次確認**推測正確**。

---

## 共用區塊：Holders / Liquidity Providers / Maps（出現在 Info / Chart+Txns / Txns 三個分頁）

這三顆按鈕在 Info 分頁是入口按鈕（點了跳轉），在 Chart+Txns／Txns 分頁則是**表格內容切換器**（點了原地替換下方表格），指向同一組資料：

1. **Holders**（截圖 `12_holders_crop.png`）：持有人排行榜，欄位 ADDRESS（錢包地址縮寫）/ %（佔總供應量比例）/ AMOUNT（持有數量，用長條圖視覺化佔比）/ VALUE（美元價值）。
   - 👉 **這是實用的風控檢查工具**：如果單一地址持有比例過高（例如第一名就佔 30%、50%），代表這顆幣被少數大戶掌控，隨時可能被倒貨砸盤（"rug pull" 常見前兆之一）。這次測試的樣本代幣第一大持有人只有 3.11%，相對分散。
2. **Liquidity Providers**（截圖 `13_lp_crop.png`）：流動性提供者名單。實測這個交易對顯示「Not available for this pair」——**代表這個功能不是每個交易對都有資料，取決於是哪個 DEX/哪條鏈**，不能保證每次點都看得到內容，這點要在網站上講清楚避免使用者以為是 App 壞掉。
3. **Maps**（截圖 `14_maps_crop.png`）：跳出一個全螢幕彈窗「XXX Maps」，裡面有兩個第三方服務可切換：**Bubblemaps**（氣泡圖，把持有人錢包用氣泡大小+連線視覺化，方便肉眼看出「哪些錢包其實是同一群人在互轉」，業界常用的抓內部人/團伙控盤工具）、**InsightX**（另一個類似的鏈上分析服務）。實測時內容還在 WebView loading 中沒有截到實際圖形，但功能定位很明確：**進階版的「持有人視覺化分析」，比單純看 Holders 排行榜更容易發現「假分散、實際上是同一批錢包」的手法**。

---

## 總結：這輪最值得放進網站的發現

按對「小白防詐騙」教育目標的重要性排序：

1. 🔴🔥 **Audit 投票區 + 官方免責聲明**：4 顆表情投票鈕人人可按、驗證機制形同虛設、票數可被刷。**這是最強的「不要迷信 App 內建安全分數」教材**，而且是 App 官方自己承認的（不是我們自己猜的）。
2. 🟡 **Holders 持有人排行榜**：教「看第一大持有人佔比」是一個具體、可操作的風控檢查步驟，比空泛講「要小心巨鯨」更有用。
3. 🟡 **Bubblemaps／InsightX 這類持有人視覺化工具**：值得一提「有更進階的免費工具可以抓團伙控盤」，但可以只是點名帶過，不必深入教怎麼操作（避免頁面過長，且這是第三方服務不是 DEX Screener 本身的功能）。
4. 🟢 **Liquidity Providers 可能顯示「Not available」**：提醒使用者這是正常現象，不是 bug。
5. 🟢 **Chart / Chart+Txns / Txns 三個分頁其實是同一組資料的不同排版組合**（圖表+表格的切換），不是三種不同功能——小白只要懂「Chart+Txns 是預設好用版，其他兩個是各自的全螢幕版」就夠了，不需要逐一詳細教。

以下項目評估後**不建議寫進網站**（避免頁面繼續變長，且屬於進階看盤工具，非小白必需）：
- TradingView 圖表左側繪圖工具列的各項細節（趨勢線、測距尺等專業看盤功能）
- 換算計算機（次要功能，Trade 按鈕才是真正下單入口）
- Metas 標籤系統的完整分類邏輯（跟 Screener 首頁 Metas 儀表板重複，之前已經決定不深入）
