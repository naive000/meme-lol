# DEX Screener App — Screener（首頁）分頁全功能實測走查

> 掃描日期：2026-09-10（第二輪，比第一輪 `dex-screener-features.md` 更深入）
> 方式：實機操作 + 截圖（已裁掉最上方時間／WiFi／電池狀態列）+ 逐項文字說明
> 範圍：底部 5 大分頁裡的 **Screener（首頁）**，逐一點開每個欄位並截圖，包含篩選列最右邊的 Reset
> 截圖檔案位置：`/tmp/claude/scratchpad/dexscreener-shots/`（暫存區，非專案版控檔案，僅供本次規劃參考）

---

## 01 — Screener 首頁預設狀態（Trending／6H）

截圖：`01-screener-default.png`

畫面由上到下：
- 頂部 3 顆模式鈕：**Trending（目前選中，藍底）／New／Top**，Trending 鈕上還帶著目前的時間窗「6H」
- **Metas 篩選列**（本輪新發現，第一輪未記錄到）：一排可橫向捲動的「主題分類」chip，例如「🏆 Meme Hall of Fame $1.94B」「🐈 Cat」，每個 chip 右邊有市值總計
- 全域統計列：24H VOLUME／24H TXNS／BLOCK 幾秒前
- 代幣列表，每列比第一輪記錄多看到幾個細節：
  - 左側 SWAP／DEX 圖示（三橫線＝Solana 系 DEX、R 六角形＝Robinhood 鏈 DEX）
  - Boost 數字徽章旁邊**確實有閃電圖示**（⚡100／⚡10／⚡500），驗證了上一輪查證的結論：這是付費推廣標記，不是安全分數
- 底部篩選 chip 列（可橫向捲動，這裡先看到前段）：**24H／Solana（鏈別，帶 ⓧ 可清除）／All DEXes／Sort（帶 ⓧ）／…（後面還有）**
- 最底部固定 5 個分頁：Screener／Search／Watchlist／Alerts／Menu

## 02 — 點開「Metas」主題分類

截圖：`02-metas-open.png`

點「Metas」chip 會整頁跳轉到一個**主題分類總表**，不是小下拉選單。每個分類卡片顯示：
- 分類名稱 + 一句話定位（例：「Meme Hall of Fame — Established memes, enduring communities」「Cat」「Degen — Chaos, degeneracy and commitment」）
- 6 個數據：**MCAP**（該分類全部代幣市值加總）／**24H Δ**（24小時市值變化金額）／**24H %**（變化百分比）／**24H VOL**（成交量）／**LIQUIDITY**（流動性）／**TOKENS**（該分類收錄幾顆幣）

這其實是「幣圈敘事（narrative）熱度儀表板」——例如一眼看出「Cat 迷因」整體這 24 小時是漲是跌、資金有沒有在流入。對中級用戶判斷「現在市場在炒什麼題材」很有用，但概念偏進階，小白不會用到。

## 03 — Trending 時間窗下拉

截圖：`03-trending-period.png`

點 Trending 鈕上的「6H▾」會從畫面下方彈出一個小面板，4 個選項：**5 minutes／1 hour／6 hours／24 hours**。這個時間窗決定「熱門」榜單是用哪個區間的熱度在排序，跟代幣列表卡片上顯示的「1H／24H」漲跌幅是不同的兩件事（那個永遠固定顯示 1H 和 24H，不受這裡影響）。

## 04 — New（新配對）分頁

截圖：`04-new-tab.png`

依上線時間排序，最新的排最前面（4h／5h／1h／54m／6h 這種新鮮度標籤）。**這裡截到一個活生生的仿冒案例**：排前幾名的幣叫「GOOGL」「HOOD」「Claude」「HOLO」，圖示是灰色問號佔位圖（代表沒有上傳 logo，也沒有官方驗證），名字明顯是蹭 Google／Robinhood／Anthropic 等知名品牌，MCAP 卻只有幾百萬到幾千萬台幣等級——這正是網站「風險」分頁一直在講的「同名仿冒幣」，而且是 New Pairs 這個功能天生最容易冒出這種東西的地方（剛發射、還沒人審核）。這張截圖本身就是很好的教學素材。

## 05 — 意外發現：統一排序模式選單

截圖：`05-sort-mode-menu.png` / `05b-sort-mode-scrolled.png`

在 New 分頁點選單，彈出的其實不是「New 專屬設定」，而是**整個 App 的排序模式總選單**，比原本認知的「Trending／New／Top 三顆固定鈕」更完整。選單結構：
- **Newest**（＝New 分頁）
- **Trending**：5 minutes／1 hour／6 hours／24 hours
- **Top**：Most Volume／Most Txns
- **Gainers**：5 minutes／1 hour／6 hours／24 hours（漲幅排行，這是本次才發現、先前兩輪都沒記錄到的第 4 種模式！）

捲到底確認**沒有「Losers」（跌幅排行）選項**——App 只提供漲幅排行，不提供跌幅排行的專屬入口（要看跌最多的，只能靠 Screener 主列表手動依 24H% 排序）。

一句話重點：Screener 首頁其實有 **4 大排序模式**（熱門／最新／排行／漲幅），不是原本記錄的 3 種，網站教學如果要提這段建議一併更新。

## 06 — Top（排行）分頁

截圖：`06-top-tab.png`

依 Most Volume 排序後，榜首反而不是迷因幣，而是 **SOL（Wrapped SOL）、RAY（Raydium）、PUMP** 這種主流／平台代幣——因為排行是看絕對成交量，大幣的量本來就是天文數字，會把迷因幣擠到後面。這點值得提醒讀者：**Top／依量排行≠迷因幣熱門榜**，跟 Trending／New 是完全不同的用途，別搞混。

---

## 篩選 chip 列（可橫向捲動，逐一點開）

## 07 — 「24H」時間窗篩選

截圖：`07-24h-filter.png`

點開是單選清單：**Last 5 minutes／Last hour／Last 6 hours／Last 24 hours**（目前選中項目右邊打勾）。這個控制的是列表每一列右側顯示的「24H」欄位要改看哪個時間窗的漲跌幅（也會連動列表排序時抓哪個區間），跟前面 Trending／Gainers 各自的時間窗選項是分開的、互不影響的三套時間窗設定。

## 08 — 鏈別選擇器（目前顯示 Solana）

截圖：`08-chain-picker.png`

點鏈別 chip 彈出全螢幕選擇器：頂部一個搜尋框（可打字找鏈，前一輪已驗證），下面是 2 欄網格常駐鏈：**Solana（目前選中）／Robinhood／Base／BSC／Ethereum／Polygon／HyperEVM／PulseChain**，往下捲還有更多（前一輪記錄過捲軸顯示 8 頁）。網站教學如果只服務 Robinhood 鏈用戶，這裡簡單帶過即可；但如果之後要涵蓋 Solana（迷因幣最大宗鏈），這個選擇器就是入口。

## 09 — All DEXes（DEX 篩選器）

截圖：`09-all-dexes.png`

跟鏈別選擇器介面幾乎一樣（搜尋框 + 2 欄網格），差別是這裡列的是**該條鏈底下的個別 DEX／發射平台**：目前在 Solana 底下看到 **PumpSwap／Raydium／Meteora／Orca／Pump.fun／Meteora DBC／FluxBeam／MetaDAO**。這個功能對「只在特定 DEX 上找幣」（例如只看 Pump.fun 剛發射的）的中級用戶有用，小白教學可略過細節，提一句「可以篩到特定交易所」即可。

## 10 — Sort（完整排序面板）

截圖：`10-sort-picker.png`

這是目前挖到資訊量最大的一個面板，標題「Sort Pairs」，選項：
- **Most Txns／Most Volume（目前選中）／Most liquidity**
- **Pair Age - Newest／Pair Age - Oldest**
- **Market Cap - Highest／Market Cap - Lowest**
- **Price change - Up**：24 Hours／6 Hours／1 Hour／5 Minutes（綠色▲，漲幅排行）
- **Price change - Down**：24 Hours／6 Hours／1 Hour／5 Minutes（紅色▼，**跌幅排行**）
- 底部 **Clear** 按鈕（清空排序）

**重大修正前面第 05 項的結論**：先前以為 App 沒有「Losers／跌幅排行」的入口，其實有——只是不是像 Gainers 那樣掛在頂部模式選單，而是藏在這個 Sort 面板的「Price change - Down」裡。這個面板等於是全部排序邏輯的總表，前面篩選列上單獨看到的 Market Cap／FDV／Txns／Buys／Sells 幾個小 chip，本質上都是這裡面某幾個選項的捷徑按鈕。

> 附註：關掉 Sort 面板時手滑多點到「Most liquidity」，之後列表變成依流動性排序、篩選列也多了個「Liquidity ⓧ」捷徑 chip——不影響後續操作，只是說明這幾個捷徑 chip 是動態的，會隨你最後選的排序條件而變化名稱。

## 11 — Profile 開關（篩選出有填資料的代幣）

截圖：`11-chips-scrolled.png`（開啟時）／`12-profile-toggle.png`（關閉後對照）

「Profile」預設是**開啟**狀態（chip 上有 ⓧ 可清除），這時列表只顯示「有填 Website／Twitter／Telegram 等資料」的代幣。**把它關掉之後，GOOGL／HOOD／Claude 這幾顆仿冒大品牌名字的空白幣立刻冒出來**（見對照圖）——證實 Profile 開關的作用就是「先濾掉連基本資料都懶得填的幣」，是新手最簡單的第一層防呆機制。反過來說：**有填 Profile 不代表沒有問題，只是最低標準**，網站教學這裡要講清楚，避免讀者誤以為「有社群連結＝安全」。

## 12 — Boosted 開關（只看有付費推廣的代幣）

截圖：`13-boosted-toggle.png`

開啟後，列表**只留下有 ⚡ Boost 徽章的代幣**，24H VOLUME 也從 $1.10B 驟降到 $16.7M（代表大部分主流成交量其實跟「有沒有花錢推廣」無關）。這個開關本質上是「只看花錢買曝光的幣」，跟「這顆幣本身好不好」沒有任何關係——呼應網站現有內容「Top Boosted 是專案方付錢買的推廣位，不代表推薦」，這個開關剛好是最直接的反面教材：打開它＝主動只看廣告。

## 13 — Ads 開關（只看買廣告版位的代幣）

截圖：`14-ads-toggle.png`

開啟後這次篩到 **「No tokens found」（0 筆結果）**——代表 Ads（廣告／進階版位）跟 Boosted 是兩種不同的付費項目，符合度更窄。這個開關同樣是「只看誰在花錢買曝光」，跟前面 Boosted 是同類性質但不同產品層級，兩個都不是安全或品質指標。

## 14 — Rank（排名面板，跟 Sort 幾乎同款）

截圖：`15-rank-toggle.png`

點開「Rank」彈出的「Rank Pairs」面板，選項跟第 10 項的「Sort Pairs」高度重疊：Most Volume／Most Txns／Most Liquidity／Pair Age - Newest／Pair Age - Oldest／Market Cap - Highest／Trending（4 時間窗）／Price change - Up（4 時間窗）／Price change - Down（4 時間窗）。**唯一差異是這裡少了「Market Cap - Lowest」**。實測上感覺 Rank 跟 Sort 是同一套排序邏輯的兩個入口（介面上標題圖示不同：🏆 Rank Pairs vs ⇅ Sort Pairs），沒有觀察到功能上的實質差異，可能是 App 介面重複设計或有還沒摸清的細節差異，建議標注「疑似重複功能，不確定差異」，不要在網站上寫死兩者不同。

## 15 — Market Cap（其實是數值範圍篩選器，不是排序！）

截圖：`16-marketcap-sort.png`

重要修正：**篩選列上的「Market Cap／FDV／Txns／Buys／Sells」這排 chip，功能是「依數值範圍篩選」，不是排序捷徑**（跟第 10、14 項的 Sort／Rank 面板是完全不同的機制）。點開「Market Cap」彈出「Filter by Market Cap」：
- 8 個常用區間快速按鈕：**<$100K／<$250K／<$1M／<$10M／>$1M／>$10M／>$100M／>$1B**
- 自訂 **Min／Max** 輸入框（可打任意數字精確篩選）
- **Apply**（套用）／**Clear**（清空）按鈕

對小白很實用：例如想避開「市值太小、一碰就是老鼠倉」的幣，可以直接設 Min $1M 濾掉小雜魚；反過來想找「還沒被發現的早期小幣」也能設 Max。這是本次唯一挖到、**帶數字輸入框的自訂篩選功能**，比其他都更強大。

## 16 — FDV（同款範圍篩選器）

截圖：`17-fdv-filter.png`

跟 Market Cap 完全同一套介面（同樣 8 個區間快速鈕 + Min/Max + Apply/Clear），只是篩選對象換成 FDV（完全稀釋市值）。

## 17 — Txns（交易筆數範圍篩選）

截圖：`18-txns-filter.png`

同款介面，但快速選項換成筆數區間：**>10／>100／>1K／>5K／>10K**。這次 Min 欄位還留著前面操作殘留的「50」數值（代表這欄位狀態會保留、不會每次重開自動清空），可以順便提醒讀者：篩選條件設完記得檢查是不是忘記清掉。

## 18 — Buys（買單筆數範圍篩選）

截圖：`19-buys-filter.png`

同款介面，快速選項：**>1／>100／>1K／>5K／>10K**。

## 19 — Sells（賣單筆數範圍篩選）

截圖：`20-sells-filter.png`

同款介面，快速選項：**>10／>100／>1K／>5K／>10K**。至此 Market Cap／FDV／Txns／Buys／Sells 五個 chip 全部確認是**同一套「數值範圍篩選」機制**，只是篩選欄位不同，快速選項依欄位性質（金額 vs 筆數）微調。

## 20 — Reset（一鍵重設，範圍比想像中大）

截圖：`21-reset-after.png`

點下 Reset 之前，畫面已經累積了本次操作留下的一堆狀態（Profile 關閉、Txns 篩選殘留 Min=50、排序被動到 Most Liquidity……）。點下去之後**重設的範圍比「只清數值篩選」大得多**：
- 頂部模式**直接跳回 Trending（6H）**，不是停留在原本的 Top 分頁
- 鏈別從「Solana」變回「**All Chains**（全鏈）」——這時列表出現了前面沒見過的組合，例如「牛來」（中文迷因幣）、「PONS」（Robinhood 鏈粉紅獨角獸圖示）混在同一份榜單裡，證實 All Chains 是真的把所有鏈的幣混合排序
- Profile／Boosted／Ads／Market Cap／FDV／Txns／Buys／Sells 全部清空
- 但 **Sort chip 上仍留著一個 ⓧ**，看起來排序條件沒有被完全重設乾淨——這是個小小的 App 介面小瑕疵，紀錄下來供未來對照，如果之後重測發現行為不同，以重測結果為準。

一句話結論：**Reset 幾乎是「整個 Screener 分頁回到剛打開 App 的樣子」**，不只是清空篩選數字，連你切到哪個鏈、哪個模式都會一起重設，操作前如果不想失去目前設定要注意。

---

## 總結：本輪新發現 vs 第一輪記錄

- 排序模式其實有 **4 種**（Trending／New／Top／Gainers），不是 3 種；還有藏在 Sort 面板裡的 **Price change - Down（跌幅排行）**
- **Metas 主題分類**是完全獨立的一個大功能（第一輪沒發現）
- Boost 數字徽章（先前查證是付費推廣）現在**視覺上確認閃電圖示存在**
- **Market Cap／FDV／Txns／Buys／Sells 是數值範圍篩選器，不是排序**——這點第一輪完全記錄錯了
- Profile／Boosted／Ads 是三個獨立的「只看／濾掉」開關，各自代表不同的可信度訊號強度
- Rank 面板疑似跟 Sort 面板功能重複
- Reset 的重設範圍比預期大（連模式和鏈別一起重設）

本文件與 `dex-screener-features.md`（第一輪）合併閱讀即可拿到 Screener 分頁的完整、已修正的功能圖景。


