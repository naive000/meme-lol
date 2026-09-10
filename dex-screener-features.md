# DEX Screener APP 完整功能文件

> 掃描日期：2026-09-10
> APP 版本：2.9.34.13 (23G71)（Menu > DEBUG > Application Version 讀出）
> 平台：iOS（實機掃描，非模擬器）
> 掃描範圍：底部 5 個 Tab 全部走過一輪；**Screener（首頁）Tab 做深度掃描**（本次任務重點），其餘 4 個 Tab 記錄首屏結構即可。

## 全域 UI 元素

- 底部固定 Tab Bar，5 個分頁：**Screener / Search / Watchlist / Alerts / Menu**
- 除 Menu 外，其餘分頁頂部多為「篩選/排序 chip 列」而非傳統導覽列
- 代幣列表項目（無論在哪個分頁看到）固定結構：左側代幣圖示 + 鏈圖示（如 Robinhood 葉子標）→ Ticker + 建立時間（新幣才顯示，如「10h」）→ 右側現價 + 1H% + 24H% → 第二行：專案全名 + LIQ/VOL/MCAP 三個數據 chip
- 多數清單為原生元件（可用 accessibility tree 直接讀出文字），但**代幣詳情頁的 K 線圖表是 WebView（TradingView 元件）**，無法用 accessibility tree 讀取，只能截圖判讀

---

## Tab 1：Screener（首頁，深度掃描）

### 頁面概覽
DEX Screener 的預設首頁，是一個可切換排序模式、可篩選鏈/DEX、依各種指標排序的代幣總表。小白最常用的頁面，功能也最密集。

### 功能清單

| # | 功能名稱 | 類型 | 說明 | 互動方式 | 備註 |
|---|---------|------|------|---------|------|
| 1 | Trending / New / Top | 頂部分段按鈕（3選1） | 三種排序邏輯：熱門 / 新上線 / 依量排行 | 點擊切換 | 見下方「排序模式」 |
| 2 | Trending 時間區間 | 下拉選單 | 5 minutes / 1 hour / 6 hours / 24 hours | 點 Trending chip 展開小面板 | 影響「熱門」的計算窗口 |
| 3 | Top 子模式 | 下拉選單 | Volume（依量）/ Txns（依筆數） | 點 Top chip 展開小面板 | |
| 4 | 統計橫條 | 靜態資訊 | 顯示 24H VOLUME / 24H TXNS / BLOCK 剛出的區塊秒數 | 純顯示 | Trending/New 模式下才出現 |
| 5 | 時間區間 chip（24H） | 篩選 chip | 控制清單價格變動百分比顯示的時間窗 | 點擊展開 | 在 Top 模式下的篩選列最左側 |
| 6 | 鏈別選擇器（如 Robinhood） | 篩選 chip + 全螢幕彈窗 | 選要看哪條鏈的代幣 | 點擊展開彈窗，含搜尋框 + 網格 | 已知選項：Solana／Robinhood／Base／BSC／Ethereum／Polygon／HyperEVM／PulseChain，可下拉看更多（彈窗顯示「8頁」可捲動，實際支援鏈數遠超過這8個） |
| 7 | All DEXes 篩選 | 篩選 chip | 篩特定 DEX（如只看 Uniswap） | 點擊展開（本次掃描時裝置意外跳轉，未完整記錄選項清單） | 建議網站標記「未完整驗證」 |
| 8 | Sort | 篩選 chip | 額外排序條件入口 | 點擊展開 | 未展開驗證，功能名稱明確 |
| 9 | Rank / Profile / Boosted / Ads | 篩選 chip（4個） | 列表顯示欄位開關，例如是否顯示排名數字、是否只看有填 Profile 資料的、是否為付費 Boosted、廣告位 | 點擊切換 | 這幾個是「顯示哪些欄位/類型」的 toggle，不是排序 |
| 10 | Market Cap / FDV / Txns / Buys / Sells | 排序欄位 chip（5個） | 點擊依該欄位排序代幣列表 | 點擊套用 | 與前面的篩選 chip 同在一條水平捲動列，只是位置在較右側 |
| 11 | Reset | 按鈕 chip | 清空所有篩選/排序，回到預設 | 點擊 | 篩選列最右端 |
| 12 | 代幣列表項目 | 卡片列表 | 每一列＝一個交易對，含價格/漲跌/流動性/量/市值 | 點擊進入代幣詳情頁 | 支援上下滑動載入更多（垂直捲動列顯示「11頁」，代表清單很長） |

### 排序模式細節（Trending / New / Top）

- **Trending**：依熱度排序，可選 5分/1小時/6小時/24小時 窗口。頁面上方會多一條「24H VOLUME / 24H TXNS / BLOCK 幾秒前」的全域統計列
- **New**：依新上線時間排序，欄位結構同 Trending，部分新幣列表項目會多顯示一個數字徽章（如「100」）。**事後查證：這不是安全分數**——比對 Search 分頁「熱門推薦」卡片牆上明確帶閃電圖示的「⚡10／⚡50／⚡100」Boost 標記，數字區間完全對得上，判斷是同一種東西，只是 accessibility tree 沒抓到閃電圖示，只留下數字，原始掃描誤判為安全分數。**這其實就是站內已經講過的「付費推廣 Boost 標記」**，不代表安全或推薦
- **Top**：依單一指標排行，子模式只有 Volume 和 Txns 兩種，此模式下才會出現「24H / 鏈別 / All DEXes / Sort / Rank / Profile / Boosted / Ads / Market Cap / FDV / Txns / Buys / Sells / Reset」完整篩選列

### 子頁面：代幣詳情頁

點擊任一代幣列表項目進入，頂部固定，底部有 4 個子分頁：**Info / Chart+Txns / Chart / Txns**

#### 子分頁 1：Info（預設）
- 頭部：返回鍵、代幣圖示+名稱、分享按鈕、更多選項（⋯）
- 交易對資訊：`TICKER / 計價幣種`，鏈徽章 → DEX 徽章（如 Robinhood → Uniswap V4）
- 大圖 Banner（項目方放的宣傳圖/梗圖）
- 社群連結列：Website / Twitter / Telegram +（更多，下拉）
- 價格區塊：PRICE USD（美元計價） / PRICE（原始計價幣種，如 USDG）
- 統計區塊：LIQUIDITY（流動性）/ FDV（完全稀釋市值）/ MARKET CAP（市值）
- 時間區間分段：5M / 1H / 6H / 24H，各自顯示漲跌%
- 交易統計：TXNS（總筆數）+ BUYS/SELLS 對比條；VOLUME + BUY VOL/SELL VOL 對比條；TRADERS + BUYERS/SELLERS 對比條
- 操作按鈕：Watchlist（加入關注）、Alerts（設價格提醒）、Trade（跳轉外部 DEX 進行實際交易）

#### 子分頁 2：Chart+Txns
- 上半：TradingView 風格 K 線圖（WebView），含：
  - 新增指標（+）
  - 時間粒度：1s / 1m / 5m / 15m / 1h / 4h / D（+更多下拉）
  - K線/面積圖切換
  - 左側繪圖工具列（畫線、量測、文字標註等專業看盤工具，小白幾乎不會用到）
  - Date Range 選擇、目前時間、auto 即時更新開關
- 下半：三個子分頁 **Txns / Top Traders / Holders（含總持有人數，如 93,191）**
  - Txns 表格欄位：TXN（買/賣圖示+時間）/ USD（金額）/ PRICE / TRADER（錢包地址縮寫），每欄都有篩選圖示

#### 子分頁 3：Chart
純圖表視圖（未逐一展開驗證，推測為 Chart+Txns 拿掉下方交易表的精簡版）

#### 子分頁 4：Txns
純交易紀錄列表視圖（未逐一展開驗證，推測為 Chart+Txns 下方表格的全螢幕版）

---

## Tab 2：Search（快速掃描）

### 頁面概覽
搜尋任意代幣，含「熱門推薦」卡片牆。

### 功能清單

| # | 功能名稱 | 類型 | 說明 | 互動方式 | 備註 |
|---|---------|------|------|---------|------|
| 1 | 搜尋框 | 輸入框 | 進頁面自動彈出鍵盤 | 打字搜尋 | |
| 2 | Spotlight / History | 分段按鈕 | 熱門推薦 vs 自己的搜尋歷史 | 點擊切換 | |
| 3 | 推薦代幣卡片牆 | 雙欄網格卡片 | 每張卡：圖示、名稱、（Boosted 加速標記如「⚡10」）、鏈別 | 點擊進入詳情頁 | 可上下滑動載入更多 |

---

## Tab 3：Watchlist（快速掃描）

### 頁面概覽
自選清單，支援多個獨立清單（目前為「Main list」）。

### 功能清單

| # | 功能名稱 | 類型 | 說明 | 互動方式 | 備註 |
|---|---------|------|------|---------|------|
| 1 | Edit / + New | 導覽列按鈕 | 編輯目前清單 / 新增另一個清單 | 點擊 | 代表可以建立多個主題自選清單 |
| 2 | Set watchlist alert / Share | 功能按鈕 | 對整個清單設提醒 / 分享清單 | 點擊 | |
| 3 | 統計列 | 靜態資訊 | 24H VOLUME / 24H TXNS 加總 | 純顯示 | |
| 4 | 代幣列表 | 列表 | 結構同 Screener 列表項目 | 點擊進入詳情頁 | 本次裝置上已有 1 筆既有紀錄（他人測試留下） |
| 5 | 篩選列 | chip 列 | 24H / All Chains / Sort / Rank / Profile | 點擊 | 比 Screener 篩選列精簡（少了 DEX/漲跌欄位排序） |

---

## Tab 4：Alerts（快速掃描）

### 頁面概覽
價格提醒功能，**需要先開通知權限**（本次未實際開啟，僅記錄狀態）。

### 功能清單

| # | 功能名稱 | 類型 | 說明 | 互動方式 | 備註 |
|---|---------|------|------|---------|------|
| 1 | 空狀態提示 | 文字 | "To use price alerts please enable notifications first" | — | 需要系統通知權限，本次未嘗試開啟 |
| 2 | Enable notifications | 按鈕 | 觸發 iOS 系統通知授權彈窗 | 點擊 | [需授權，未測試] |

---

## Tab 5：Menu（設定/個人頁面，完整掃描）

### 頁面概覽
帳號、外觀、應用設定、社群連結、法律文件、除錯資訊。

### 功能清單

| # | 功能名稱 | 類型 | 說明 | 互動方式 | 備註 |
|---|---------|------|------|---------|------|
| 1 | THEME | 三段選擇器 | Light / Dark / System | 點擊切換 | |
| 2 | MY ACCOUNT | 區塊 | 目前為 anon（匿名），提供 Sign in | 點擊登入 | [需登入，未測試] |
| 3 | Screener Display | 設定項 | 目前值：List（推測還有 Grid 等選項） | 點擊進入子頁 | 未展開驗證選項全貌 |
| 4 | Default Home Screen | 設定項 | 目前值：Screener（可改成別的分頁當開場頁） | 點擊進入子頁 | 未展開驗證選項全貌 |
| 5 | Default Pair Details Tab | 設定項 | 目前值：Info（可改成進代幣詳情頁時預設看哪個子分頁） | 點擊進入子頁 | 未展開驗證選項全貌 |
| 6 | Pair Display | 設定項 | 交易對顯示方式設定 | 點擊進入子頁 | 未展開驗證 |
| 7 | Show Hidden Pairs | 設定項 | 顯示被隱藏的交易對（可能是低品質/詐騙幣過濾） | 點擊切換 | 未展開驗證 |
| 8 | Rate us on App Store | 連結 | 跳轉 App Store 評分 | 點擊 | [外部跳轉，未測試] |
| 9 | Discord | 連結 | 官方 Discord 社群 | 點擊 | [外部跳轉，未測試] |
| 10 | FAQ / Trending / API Reference | 連結（3個） | MORE INFO 分類下的官方文件連結 | 點擊 | [外部跳轉，未測試] |
| 11 | Disclaimer / Terms & Conditions / Privacy Policy / App Privacy Policy | 連結（4個） | LEGAL 分類下的法律文件 | 點擊 | [外部跳轉，未測試] |
| 12 | Application Version / User ID | 靜態資訊 | 版本 2.9.34.13 (23G71)；匿名 User ID | 純顯示（可能可複製） | DEBUG 分類 |

---

## 付費 / Pro 功能

**本次掃描未發現明顯的付費牆或 [PRO] 標記。** DEX Screener 這款 App 目前看起來核心看盤功能全部免費開放，付費功能（如官方網站版有的進階篩選器/API）在 App 內未出現，或深藏在未展開的子設定頁中，需要更細的驗證才能下結論。

## 外部跳轉整合

- **Trade 按鈕**（代幣詳情頁）→ 跳轉外部 DEX 進行實際換幣交易
- **Website / Twitter / Telegram**（代幣詳情頁）→ 跳轉外部瀏覽器或對應 App
- **Rate us on App Store** → App Store
- **Discord** → Discord App/網頁
- **FAQ / Trending / API Reference / 4份法律文件** → 官方網站對應頁面

---

## 掃描過程附記（給下一手接手的人）

- **座標操作要用 accessibility tree，不要用截圖像素猜座標**：`GET /session/:id/source` 抓 XCUIElement XML，直接讀 `label` 文字＋`x/y/width/height` 算出正確 tap 座標（390×844 point 座標系，非 1170×2532 截圖像素）。已寫好 `/tmp/claude/scratchpad/parse_source.py` + `dump.sh` 兩個小工具，可以重複用（在 A 機的暫存區，非專案內）。
- **`wda.sh find-click` 常常失效**：它用 `link text` 策略比對 accessibility label，這款 App 很多元素是 RN/自訂渲染，label 抓不到會直接 `IndexError`。改用算好座標的 `tap` 更穩。
- **K 線圖表區塊是 WebView**，accessibility tree 讀不到內容，只能靠截圖人工判讀。
- **有兩次操作意外把 iPhone 切到 Chrome**（原因不明確，懷疑是連續下指令時某次 tap 座標落在會觸發外部連結/系統手勢的元素上），需要 `wda.sh home` 重新導航回 App。另外操作中途 WDA 連線斷過一次（exit code 56），跑 `wda.sh up` 幂等重啟即解決。
- **All DEXes 篩選、Sort 排序選單、Screener Display/Default Home Screen/Pair Display 等設定子頁**因裝置操作意外中斷，**未完整展開驗證**，上表已標注。如果要做到 100% 精確，這幾項需要再花一輪跑。
