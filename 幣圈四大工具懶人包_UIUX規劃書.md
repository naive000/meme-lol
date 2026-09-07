# 幣圈工具懶人包網站 — UI/UX、資訊架構與內容規劃

> 由 fable 模型研究並規劃（2026/9），目標：把 GMGN.ai、Axiom.trade、fomo.family、DEX Screener 四個幣圈交易工具的用法，做成手機優先、給市場小白也能看懂的懶人包網站，同時保留進階內容。此文件可直接丟給 Claude Code 或其他執行環境，作為建站的完整規格書使用。

---

## 0. 查證結論摘要（給所有執行者的共同事實基礎）

**「robinhood」不是 Robinhood 公司 App，而是「Robinhood Chain」**：Robinhood 公司推出的 Ethereum Layer-2，用 Arbitrum Orbit 技術，主網 2026-07-01 上線，gas 用 ETH、EVM 相容（地址是 0x 開頭）。原本定位是股票代幣化（RWA），結果 79% 以上的 DEX 成交量都是迷因幣。代表幣 CASHCAT；主要發射台 Noxa（7/13 已關閉）與 Pons.family。Axiom 於 7/11 接入（鏈選單顯示 HOOD，URL 參數 `chain=robinhood`），fomo 支援（入金用 USDC/USDG），GMGN API 也列有 `robinhood` 鏈，Dexscreener 可看圖。**Robinhood 公司不審核、不背書鏈上任何代幣**，同名仿冒幣極多。

| 工具 | 一句話 | 支援鏈 | 手機形式 | 費率（查證時） | 小白友善度 |
|---|---|---|---|---|---|
| GMGN.ai | 迷因幣「安全檢查＋聰明錢跟單」終端機 | SOL/BSC/ETH/Base/Monad/TRON(+robinhood) | Web＋App＋Telegram Bot | 每筆約 1%（買賣各收） | ★★★ |
| Axiom.trade | 專業級多鏈交易終端（Pulse 新幣雷達） | SOL/BNB/ETH/Robinhood Chain | 無官方 App，手機瀏覽器 PWA（商店的「Axiom App」是假的） | 基礎 1%，等級返現最低 0.75%，推薦碼 −10% | ★★ |
| fomo.family | 像社群 App 的「社交交易」（Apple Pay 入金、免助記詞） | SOL/Base/BNB/Monad/ETH/Robinhood Chain | iOS/Android/Web | 現貨約 0.5%（推薦碼 0.45%），gas 由平台代付 | ★★★★★ |
| DEX Screener | 免費、免登入的多鏈圖表/交易對聚合器 | 幾乎所有主流鏈 | iOS/Android/Web | 免費（看盤） | ★★★★ |

---

## 1. 網站定位與命名

**一句話定位**：用手機 10 分鐘看懂 GMGN、Axiom、fomo、DEX Screener 四個工具，從「發現新幣 → 驗證安全 → 下單 → 追蹤出場」串成一套小白也能照做的流程。

**名稱候選**（繁中為主）：
1. **鏈上四寶**（主推：短、好記、直接點題「4 個工具」）
2. **迷因幣工具箱 MemeKit**
3. **土狗生存手冊**（幣圈黑話「土狗」＝高風險迷因幣，較有社群感，但對純小白略陌生）

**免責聲明位置（4 處）**：
1. **首次進站底部彈窗（bottom sheet）**：需按「我知道了」才關閉，用 `localStorage` 記住，之後不再出現。
2. **每頁頁尾**：固定一行小字。
3. **每個工具頁「上手」分頁最上方**：一行黃色提示條。
4. **底部導覽「風險」分頁**：完整版。

**文案草稿（完整版）**：
> 本站僅為工具操作教學與公開資訊整理，**不構成任何投資建議**。迷因幣屬極高風險資產，多數最終歸零；所有操作請自行研究（DYOR），只投入可承受全部損失的金額。本站與 GMGN、Axiom、fomo、DEX Screener 及 Robinhood 均無隸屬關係；各平台介面、費率與功能可能隨時變動，請以官方公告為準。本站部分連結含推薦碼。

**短版（頁尾/提示條）**：「非投資建議｜迷因幣極高風險，多數歸零｜介面與費率以官方為準」

---

## 2. 資訊架構 / Sitemap（手機優先）

**導覽結構：底部固定 Tab Bar（5 個）＋ 頂部 sticky 標題列（含「小白/進階」切換）**。不用漢堡選單（隱藏導覽對小白不友善）。單一 HTML 用 hash 路由（`#/home`、`#/tools/gmgn`）切換 `<section>` 顯示。

```
底部 Tab Bar
├─ 🏠 首頁 (#/home)
│   ├─ Hero：一句話定位 + 「我是小白，從這裡開始」大按鈕 → #/flow
│   ├─ 4 工具卡片（一句話介紹 + 小白友善度星等 + 進入按鈕）
│   ├─ 「robinhood 是什麼？」提示卡（因為 3 個工具都會看到這個字）
│   └─ 3 條開始前必知（先小額、先看流動性、先設停損）
├─ 🧰 工具 (#/tools)
│   ├─ 工具切換 chip：GMGN｜Axiom｜fomo｜DEX Screener（橫向可滑、sticky）
│   └─ 每個工具頁內 4 個子分頁（sticky）：上手｜進階｜詞彙｜風險
│       (#/tools/gmgn/start、#/tools/gmgn/pro …)
├─ 🔗 流程 (#/flow)   ← 4 工具串接：發現→驗證→下單→追蹤→出場
│   └─ 直式時間軸；每一步標明「用哪個工具、做什麼、看什麼數字」
├─ 📖 詞典 (#/glossary)
│   ├─ 頂部搜尋框 + 分類 chip（基礎／安全指標／下單／鏈與錢包）
│   └─ 每個詞：一句白話 + 一句「小白怎麼看」
└─ ⚠️ 風險 (#/risk)
    ├─ 完整免責聲明
    ├─ 五大常見被割方式（仿冒幣、蜜罐、拉地毯、狙擊/捆綁、假 Bot/釣魚）
    └─ 安全清單（可勾選 checklist，localStorage 記住）
```

頂部標題列：左＝站名／返回，中＝目前頁名，右＝「小白 ⇄ 進階」切換開關。

---

## 3. 「小白模式」與「進階模式」的呈現

**採用「全站模式開關 ＋ 內容區塊分級」雙機制**，而非兩套獨立頁面（避免內容重複與維護成本）。

**互動規格**：
- 頂部開關 `<button class="mode-toggle" aria-pressed>`，兩個狀態：`小白`（預設）／`進階`。狀態存 `localStorage.mode`，`<html data-mode="beginner|advanced">`。
- 所有內容區塊加 `data-level="beginner" | "advanced" | "both"`。
- **小白模式**：`advanced` 區塊不隱藏，而是收合成 `<details>` 手風琴，標題顯示「🟣 進階：XXX ▸」——讓小白知道有更多，但不被淹沒。
- **進階模式**：`beginner` 的步驟教學縮成「精簡清單」（CSS 把 `.step p.detail` 隱藏，只留步驟標題），`advanced` 區塊自動展開。
- 每張卡片左上有難度標籤：🟢 小白／🟣 進階／🔴 高風險。
- 工具頁內的子分頁「上手」預設給小白、「進階」預設給進階，切換模式時自動跳到對應子分頁（可手動切回）。
- 詞典：小白模式顯示「一句白話」；進階模式多顯示「進階補充」（例如滑點在小白是「願意多付幾 %」，進階補充「Auto/Turbo/Anti-MEV 三種模式差異」）。
- 內文術語用 `<span class="term" data-term="滑點">` 包起來，點擊彈出底部小卡解釋（不跳頁），資料來自詞典同一份 JSON。

---

## 4. 視覺設計系統

### 4.1 排版原則
- **單欄**、內容區 `max-width: 640px` 置中（桌機也好看）。
- **卡片式**：所有內容單位都是卡片，圓角 16px、內距 16px。
- **拇指熱區**：主要 CTA 與 Tab Bar 在螢幕下半部；Tab Bar 高 56px ＋ `env(safe-area-inset-bottom)`。
- **點擊目標 ≥ 44×44px**；按鈕全寬或至少 48px 高。
- **字級**：正文 16px（絕不小於 14px）、行高 1.6；標題 H1 24/H2 20/H3 17，字重 600–700。
- 步驟教學每步一張卡，含「步驟號大圓點＋標題＋一句話＋（可選）截圖占位框」。
- 橫向內容（表格、費率比較）包在 `overflow-x:auto` 容器，body 不橫向捲動。
- 尊重 `prefers-reduced-motion`；動畫只用 opacity/transform。

### 4.2 配色（深色為主，亮色為輔，用 CSS 變數）
```css
:root{                    /* 亮色 fallback */
  --bg:#F5F7FA; --surface:#FFFFFF; --card:#FFFFFF; --border:#E2E8F0;
  --text:#0F172A; --text-2:#475569; --text-3:#94A3B8;
  --accent:#7C3AED;       /* 主色：紫（Solana 感） */
  --accent-2:#06B6D4;     /* 次色：青 */
  --up:#16A34A; --down:#DC2626; --warn:#D97706; --gold:#CA8A04;
  --beginner:#16A34A; --advanced:#7C3AED; --danger:#DC2626;
}
/* 深色主題：套用在 prefers-color-scheme:dark 與 [data-theme=dark] */
:root{
  --bg:#0B0E14; --surface:#12161F; --card:#181D28; --border:#262D3B;
  --text:#F1F5F9; --text-2:#A3ADBD; --text-3:#6B7484;
  --accent:#A78BFA; --accent-2:#22D3EE;
  --up:#22C55E; --down:#EF4444; --warn:#F59E0B; --gold:#FBBF24;
  --beginner:#22C55E; --advanced:#A78BFA; --danger:#EF4444;
}
```
對比：深色下 `#F1F5F9` on `#181D28` ≈ 14:1；次要文字 `#A3ADBD` ≈ 7:1，均符合 WCAG AA。漲綠跌紅（台灣使用者習慣是紅漲綠跌，但幣圈工具全是綠漲紅跌，為了跟工具介面一致採綠漲紅跌，並在詞典註明）。

### 4.3 字體
`font-family: -apple-system, BlinkMacSystemFont, "PingFang TC", "Noto Sans TC", "Microsoft JhengHei", "Segoe UI", Roboto, sans-serif;` 數字/地址用 `ui-monospace, "SF Mono", Menlo, monospace`。不載入外部字體（單檔、離線可用、省流量）。

### 4.4 間距系統
4pt 基準：`--s1:4px --s2:8px --s3:12px --s4:16px --s6:24px --s8:32px`。卡片間距 12px，區塊間距 24px，頁面左右內距 16px。

### 4.5 元件清單（固定 class 名，方便分工）
| 元件 | class | 用途 |
|---|---|---|
| 卡片 | `.card` `.card--tool` `.card--risk` | 內容容器 |
| 難度標籤 | `.badge .badge--beginner/--advanced/--danger` | 卡片左上 |
| 步驟條 | `.steps > .step`（含 `.step__num .step__title .step__body .step__shot`） | 上手教學 |
| 截圖占位 | `.shot`（虛線框＋文字「此處為 XXX 畫面示意」）| 不放真實截圖，避免版權與過時 |
| 提示框 | `.callout .callout--tip/--warn/--danger` | 小訣竅／注意／高風險 |
| CTA 按鈕 | `.btn .btn--primary/--ghost`（全寬 48px） | 前往工具、下一步 |
| 手風琴 | `<details class="acc">` | 進階區塊收合 |
| 子分頁 | `.tabs > .tab[aria-selected]` | 上手/進階/詞彙/風險 |
| Chip | `.chip` `.chip--active` | 工具切換、詞典分類 |
| 術語 | `.term[data-term]` | 點擊彈詞典小卡 |
| 底部彈窗 | `.sheet` | 免責、術語解釋 |
| 檢核清單 | `.checklist > label > input[type=checkbox]` | 下單前檢查 |
| 指標卡 | `.metric`（名稱＋安全值＋危險值） | 安全指標速查 |
| 時間軸 | `.timeline > .tl-item` | 流程頁 |
| 外部連結 | `.ext`（含 ↗ 圖示，`rel="noopener"`）| 官方連結 |
| 圖示 | 內嵌 SVG 或 emoji（🏠🧰🔗📖⚠️），不載入 icon 字體 |

---

## 5. 內容大綱（每個工具一份）

> 格式統一：**一句話介紹 → 小白上手（3–5 步）→ 進階功能 → 詞彙 → 風險提醒**。以下事實均已查證（2026/9）。

### 5.1 GMGN.ai

**一句話**：迷因幣「體檢報告＋聰明錢跟單」終端機——每個幣自動檢查安全性，還能一鍵複製厲害錢包的買賣。

**小白上手（5 步）**
1. **開啟並選鏈**：進 `gmgn.ai/?chain=sol`，頂部選 SOL（Solana）。有 Web、手機 App、Telegram Bot 三種形式；小白用 Web 或 App。
2. **建立/連接錢包**：可用 Email/社群登入自動生成「熱錢包」（可匯出私鑰），或連接 Phantom。**只放要交易的小額**，獲利定期轉出。
3. **看懂三個主頁**：「Trenches 戰壕」＝剛發射的幣（三欄：新建立 New Creation → 快畢業 Completing → 已畢業 Completed）；「Trending 熱門」＝依 1m/5m/1h/6h/24h 成交排行；「Copy Trade 跟單」。
4. **點進代幣頁看「安全面板」**：紅綠燈式檢查——Honeypot（蜜罐）、Mint/Freeze 權限是否放棄、LP 是否燒毀、Rug 機率、Top 10 持倉 %、Dev 持倉 %、Insiders/Bundlers/Snipers %。**小白規則：任何一項紅燈就不碰**。
5. **下單**：輸入 SOL 數量 → 設定滑點（新幣 10–15%、老幣 3–5%）→ 優先費（0.01–0.03 SOL）→ MEV 保護選「Secure」→ 買入。賣出可先設好 TP/SL（止盈/止損）。

**進階功能**
- **Smart Money / 錢包追蹤（Monitor/Follow）**：錢包標籤：Smart Money、KOL、Fresh Wallet、Sniper、Dev、Insider、Bundler；看 7d/30d PnL、勝率；加入追蹤後左下角紅點＋聲音提醒。
- **Copy Trade 跟單設定**：最多 10 個任務（建議 5–7）；買入模式 Fixed Buy（固定金額）／Max Buy（跟隨上限）／Fixed Ratio（比例）；篩選：市值、流動性、幣齡、LP 燒毀比、單幣上限、只跟 Pump.fun/Raydium、黑名單 20 個；賣出自動跟隨。**跟單落後原錢包至少 1 個區塊**，無法消除。選擇標準：30 筆以上、勝率 ≥60%、1d/7d/30d 皆正。
- **Auto Sell / 限價單**：止損 −30~−40%，止盈分批（2x 賣 50%、5x 賣 30%、留 20%）。
- **Sniper Bot**：新幣自動偵測與買入。
- **滑點三模式**：Auto／Turbo（搶新幣）／Anti-MEV；**MEV 三檔**：Off／Reduced／Secure。
- **Telegram Alert Bot**：官方 `@GMGN_sol_bot`，假 Bot 極多，務必核對。
- **Data API / gmgn-skills**：開放 API 給機器人與 AI agent（Claude/GPT）；欄位如 `rug_ratio`（>0.3 高風險）、`top_10_holder_rate`、`bundler_rate`、`dev_team_hold_rate`。
- 推薦制：30% 返佣。多鏈：SOL/BSC/ETH/Base/Monad/TRON（API 亦含 robinhood）。

**詞彙**：Trenches/戰壕、Bonding Curve/聯合曲線、畢業(Migrate)、Honeypot/蜜罐、Mint 權限、Freeze 權限、LP 燒毀、Rug 機率、Top 10 持倉、Dev 持倉、Bundler/捆綁、Sniper/狙擊、Insider/內部人、Smart Money/聰明錢、KOL、Fresh Wallet、跟單、TP/SL、優先費(Jito Tip)、MEV/三明治攻擊、滑點。

**風險重點**：1% 買＋1% 賣＝來回 2%；優先費永遠不可大於交易額；聰明錢也常亂買（官方原話）；假 Telegram Bot 釣魚；熱錢包只放小額；單筆倉位 ≤ 錢包 2–5%。

---

### 5.2 Axiom.trade

**一句話**：Solana 老手最愛的專業交易終端，現在也能交易 BNB、ETH 與 Robinhood Chain（HOOD）——「Pulse」新幣雷達＋錢包/推特追蹤＋一鍵快買。

**小白上手（5 步）**
1. **註冊與錢包**：`axiom.trade` 用 Email/Google/Phantom 登入。Email 登入會自動建立 Turnkey 託管錢包 → **立刻到 Settings › Account & Security › Manage Wallets 匯出 12 字助記詞備份**。用推薦碼手續費 −10%。
2. **入金**：從 Phantom/交易所轉 SOL，或用內建 Coinbase 法幣入金。要玩 Robinhood Chain：Deposit → Convert，把 SOL/BNB/USDC 直接換成 Robinhood Chain 上的 ETH（gas 幾美分）。
3. **選鏈**：右上角鏈選單，選 SOL 或 HOOD（＝Robinhood Chain）。Pulse/Tracker/Discover 可各自勾多條鏈（URL 的 `pulseChains=sol,robinhood,bnb` 就是這個）。
4. **看 Pulse 三欄**：New Pairs（剛發、市值常 <$40K）→ Final Stretch（快畢業）→ Migrated（已進開放市場，流動性較深）。每張卡：幣齡、MC、Vol、Holders、Dev%、Top10%、Snipers%、Insiders%、Bundle%。**小白只看 Migrated 欄**。
5. **點代幣 → 檢查 → 買**：先看 token info 彈窗（審計圖示），再用「閃電⚡Quick Buy」或右側面板；預設 P1/P2/P3 三組（滑點／優先費／Bribe／MEV 模式）；MEV 選 Secure。賣出有 25/50/100% 快捷鍵。

**進階功能**
- **Pulse 14 個篩選**：幣齡、Top10%、Dev%、Snipers、Insiders、Bundle%、持有人數、Pro Traders、流動性、成交量、市值、交易數、買/賣數；可選發射台、關鍵字含/排除。
- **Discover 探索**：熱門幣＋篩選（例：市值 <$1M、流動性 >$20K）、1m/5m/30m/1h 時間窗、含蜜罐風險與審計。
- **Trackers 追蹤**：錢包追蹤（手動或 JSON 批次匯入、從交易頁一鍵加入、買入即時通知）；**推特追蹤**（最多 1,500 帳號，需達交易量門檻）；可拖曳浮動視窗。
- **訂單**：限價單、TP/SL、Sniper Buy（畢業瞬間自動買）／Sniper Sell。
- **Perps 永續合約**（Hyperliquid）、**Yield**（閒置資金生息）、**Portfolio**、**Rewards**（6 等級 wood→champion 返現、費率 1%→0.75%、積分可能空投）。
- **費用**：基礎 1% + Solana gas + 優先費/Jito tip（預設 0.001 SOL）。
- 手機：無官方 App，用瀏覽器「加到主畫面」當 PWA。

**詞彙**：Pulse、New Pairs/Final Stretch/Migrated、Quick Buy、Preset/預設組、Bribe/賄賂費、Jito Tip、Turnkey、PWA、Perps/永續、Yield、HOOD/Robinhood Chain、Bonding Curve、Sniper Buy、Tracker。

**風險重點**：New Pairs 裡多數幣幾小時內歸零（原文）；助記詞不備份＝平台出事錢就沒了；App Store 的「Axiom App」都是假的；Robinhood Chain 仿冒幣多，合約地址要用兩個來源核對；Perps 有槓桿爆倉風險。

---

### 5.3 fomo.family

**一句話**：把迷因幣交易做成「社群 App」——Apple Pay 入金、免助記詞、免 gas，看別人買什麼跟著看，最適合完全沒碰過鏈上的人。

**小白上手（4 步）**
1. **下載與註冊**：App Store/Google Play 搜「fomo」(開發者 FOMO Labs；仿冒 App 多，核對開發者名)，或 `fomo.family` 網頁版。Email/Apple 帳號註冊 <1 分鐘，**沒有助記詞**（Privy 嵌入式錢包，金鑰分片，可匯出）。
2. **入金**：Apple Pay／Google Pay／金融卡（Coinbase 通道）或 USDC 轉入。一個帳戶一個現金餘額，跨 6 條鏈通用（Solana/Base/BNB/Monad/ETH/Robinhood Chain；Robinhood Chain 用 USDG）。
3. **找幣**：首頁「動態牆 Feed」看交易員即時買賣（附已實現損益）；「排行榜」看 30 天績效；點代幣進「代幣頁」：圖表、市值、流動性、持有人分布、安全警告、頂尖交易員、誰剛買。
4. **買/賣**：輸入美元金額 → 確認（費用顯示在確認頁）→ 幾秒完成；滑點與 gas 平台處理。賣出選部位、數量、確認。

**進階功能**
- **關注交易員**：對方開倉即通知；可對交易附「論點 thesis」、在圖表下留言。
- **跟單 ≠ 自動複製**：fomo 沒有自動跟單，只有社交發現，需手動下單。
- **Perps**（Hyperliquid/TradeXYZ）：加密、美股(NVDA)、指數、原物料、pre-IPO；逐倉、TP/SL；**美國用戶不可用**。
- **費率**：現貨約 0.5%（推薦碼 0.45%，部分主流幣 0.05%），Perps 0.05%/邊＋Hyperliquid 費；gas 由 ERC-4337 代付。
- 推薦：被推薦人 −10%，推薦人拿 25% 手續費分潤。無平台幣、無空投承諾。
- 背景：舊金山 FOMO Labs，三位 ex-dYdX 創辦人，2025/5 上線；2026/6 Index Ventures 領投 $75M B 輪，估值 $5.5 億；50 萬+ 用戶。
- FaceID 才能提款／匯出金鑰。

**詞彙**：社交交易、動態牆、已實現損益、排行榜、關注 vs 跟單、嵌入式錢包(Privy)、金鑰分片、gas 代付、USDG、Perps、逐倉、論點(thesis)。

**風險重點**：好買難賣（有評測回報賣出失敗）；沒有存款保險，手機丟了且沒備份＝錢沒了；Feed/排行榜設計就是要你衝動下單（FOMO）；排行榜看不出對方有沒有加減本金；仿冒 App。

---

### 5.4 DEX Screener (dexscreener.com)

**一句話**：業界標準、免費免登入的「鏈上看盤機」——任何幣只要有流動性池就自動上架，用它核對價格、流動性與真假。

**小白上手（5 步）**
1. **搜尋要用合約地址（CA）**：頂部搜尋框貼上 CA 最安全；同名同代號的假幣很多。左側/底部選鏈（Solana、Ethereum、Robinhood Chain…）。
2. **看首頁四區**：Trending（5m/1h/6h/24h 熱度）、New Pairs（新配對）、Gainers & Losers、Top Boosted（**付費推廣，不是推薦**）。
3. **讀懂交易對頁面 8 個數字**：價格、5m/1h/6h/24h 漲跌、Txns（買/賣筆數）、Volume、Makers（獨立交易者數）、**Liquidity 流動性**、FDV/Market Cap、Pair age（配對年齡）、Pooled tokens。
4. **三個安全判斷**：①流動性 vs 市值（市值 $90M 但流動性 $4M＝出不了場）；②買賣筆數是否失衡；③配對年齡與 makers 是否過少。加上手機 App 內的審計旗標。
5. **加自選＋設警示**：星號加入 Watchlist；Alerts 設價格通知（App 推播 / Telegram Bot）。

**進階功能**
- **Multicharts**：同時看最多 16 張 TradingView 圖；圖表可加 RSI/MA/MACD/BB。
- **New Pairs 篩選**：最低流動性、最低成交量、幣齡。
- **Boosts / Enhanced Token Info**：專案付費（約 $100–$1,500）換金色圖示、搜尋優先與資料卡；**不影響 Trending 演算法**，也不代表安全。GMGN 甚至把 `dexscr_boost_fee`、`dexscr_ad` 當風險欄位看。
- **Community Takeover (CTO)**：開發者跑路後社群接管的標記。
- **FDV 算法**：(總供給 − 燒毀) × 價格；MC 用自報/CoinGecko 流通量。
- **Moonshot**：官方合作的公平發射/交易 App。
- **Portfolio**、**公開 API**（配對資料、搜尋、代幣所有池子）。
- iOS/Android App 有完整圖表與推播。

**詞彙**：CA/合約地址、交易對(Pair)、流動性(Liquidity)、FDV、市值、Makers、Txns、Pooled、Boost、Enhanced Token Info、CTO、Multicharts、TradingView、K 線、Watchlist。

**風險重點**：DEX Screener **沒有自己的代幣**，任何「DEXScreener 幣/預售」都是詐騙；上榜／Boost／金色勾＝付錢，不＝安全；搜名字會搜到假幣；只看圖不代表能賣出（流動性才是關鍵）。

---

### 5.5 四工具串接總覽（流程頁核心內容）

| 階段 | 用什麼 | 做什麼 | 看哪些數字 | 小白版建議 |
|---|---|---|---|---|
| ① 發現 | Axiom Pulse（Migrated 欄）／GMGN Trending／fomo 動態牆 | 找到候選幣，**複製 CA** | 幣齡、市值、持有人數、成交量 | 只看已畢業/上榜超過 1 小時的幣 |
| ② 驗證 | GMGN 安全面板 ＋ DEX Screener 交易對頁 | 用 CA 交叉核對 | Honeypot/Mint/Freeze/LP 燒毀、Rug 機率、Top10%、Dev%、Bundler%；流動性 vs 市值、買賣比、Makers | 任何紅燈不碰；流動性 < 市值 5% 不碰 |
| ③ 下單 | fomo（最簡單）／Axiom（專業、多鏈）／GMGN（要跟單或自動止盈止損） | 小額買入，同時設 TP/SL | 滑點、優先費、MEV 模式、手續費 | 首單 ≤ 錢包 2–5%；MEV 選 Secure |
| ④ 追蹤 | DEX Screener Watchlist＋Alerts；Axiom/GMGN 錢包追蹤；fomo 關注交易員 | 設價格警示、看聰明錢動向 | 聰明錢是否出貨、持有人變化 | 只設警示，不加倉 |
| ⑤ 出場 | 原下單工具 | 分批賣：2x 賣一半、到停損就走 | 已實現損益 | 先賣回本金，剩下的才是「免費籌碼」 |

**工具定位一句話**：fomo＝最像一般 App 的入口；DEX Screener＝免費第二意見；GMGN＝體檢＋跟單；Axiom＝專業駕駛艙。

**共用「CA 貼來貼去」教學**：在任何工具點代幣名旁的複製圖示 → 到另一工具搜尋框貼上 → 確認名稱、圖示、鏈都一致。

---

## 6. 執行分工建議（給任何要動手刻站的執行者，含 Claude Code）

**建議拆分成 5 個工作單元（可分給 5 個 agent，或自己依序做）**：

| 單元 | 任務 | 產出 | 需要的素材 |
|---|---|---|---|
| **A 設計系統＋骨架** | `index.html` 全站殼：CSS 變數（§4.2 色碼）、§4.5 全部元件樣式、hash 路由、底部 Tab Bar、頂部模式切換（§3 規格）、`<details>` 收合邏輯、術語底部彈窗、免責首次彈窗、深/亮主題、首頁、風險頁、詞典頁殼。留 4 個空的工具區塊。 | `index.html` ＋一段「元件範例 HTML」cookbook | §1、§2、§3、§4 全文；§0 表格；robinhood 說明段落；§5.x 風險重點 |
| **B GMGN 內容** | 寫 GMGN 的 4 個子分頁（上手/進階/詞彙/風險），用 §4.5 class | HTML 片段＋詞彙 JSON | §0、§5.1、§4.5、§3 |
| **C Axiom 內容** | 同上，Axiom；額外寫「Robinhood Chain 是什麼」卡片 | HTML 片段＋詞彙 JSON | §0、§5.2、§4.5、§3 |
| **D fomo＋DEX Screener 內容** | 同上，兩個工具 | 兩個 HTML 片段＋詞彙 JSON | §0、§5.3、§5.4、§4.5、§3 |
| **E 整合＋流程頁＋QA** | 把 B/C/D 片段塞進 A 的骨架；寫「流程」頁（§5.5）；合併去重詞彙 JSON；QA：375px 寬無橫向捲動、Tab 切換、模式切換、`localStorage` try/catch、深/亮主題、外連 `rel="noopener"`、免責 4 處到位 | 最終 `index.html` | §5.5、§2、§4.5、其他四人產出 |

**共同約定**：
1. 只用 §4.5 的固定 class 與 `data-level`，不自創樣式。
2. 不放真實截圖，用 `.shot` 佔位框寫「畫面示意：XXX」。
3. 所有數字、費率後面加「（2026/9 查證，請以官方公告為準）」。
4. 每個工具頁上手分頁第一行必放免責短版 `.callout--warn`。
5. 外部連結：`gmgn.ai/?chain=sol&ref=KzpFUrXI`（含推薦碼，需在免責聲明註明）、`axiom.trade`、`fomo.family`、`dexscreener.com`。
6. 詞彙 JSON 格式固定：`{ "term":"滑點", "en":"Slippage", "cat":"下單", "simple":"你願意接受的成交價偏差上限，新幣通常設 10–15%。", "pro":"GMGN 有 Auto/Turbo/Anti-MEV 三模式…" }`。

---

## Sources（查證依據）

- [GMGN 官方教學索引](https://docs.gmgn.ai/index)、[GMGN Track Smart Money](https://docs.gmgn.ai/index/track-smart-money)、[GMGN 官網](https://gmgn.ai/?chain=sol)、[GMGNAI/gmgn-skills SKILL.md](https://github.com/GMGNAI/gmgn-skills/blob/main/skills/gmgn-market/SKILL.md)、[CoinCodeCap GMGN 設定與費率](https://coincodecap.com/best-settings-for-gmgn-bot)
- [Axiom 官方 Pulse 文件](https://docs.axiom.trade/axiom/finding-tokens/pulse)、[Axiompedia 註冊指南](https://axiompedia.com/guides/getting-started/how-to-sign-up-for-axiom)、[Axiompedia Pulse 篩選](https://axiompedia.com/guides/trading/axiom-pulse-explained)、[PANews Axiom 完全指南](https://panews.io/articles/4qhagi68)、[Solana-trading：Axiom 交易 Robinhood Chain](https://solana-trading.com/blog/how-to-trade-memecoins-on-robinhood-chain-axiom)、[Axiom × Robinhood Chain 整合](https://solana-trading.com/blog/axiom-integrates-robinhood-chain-hood-trading-100k)
- [Datawallet FOMO App 解析](https://www.datawallet.com/crypto/fomo-app-explained)、[Token Metrics fomo 評測](https://tokenmetrics.com/blog/fomo-social-trading-review/)、[Medium FOMO App Guide](https://medium.com/coinmonks/fomo-app-guide-social-trading-rewards-and-how-to-start-02b15b8d05a8)、[CrowInvesting fomo.family 教學](https://crowinvesting.com/crypto-trading/fomo-family-tutorial/)
- [DEX Screener Token Listing 文件](https://docs.dexscreener.com/token-listing)、[DEX Screener FAQ](https://docs.dexscreener.com/)、[BingX DEX Screener 指南](https://bingx.com/en/learn/article/what-is-dex-screener-and-how-to-use-it-for-crypto-trading)、[OpenLiquid Boost 解析](https://openliquid.io/blog/dexscreener-boost-feature-explained/)、[Bitcoin Foundation Dexscreener 新手指南](https://bitcoinfoundation.org/news/defi/how-to-use-dexscreener-beginners-guide/)、[CryptoAdventure DEX Screener 評測](https://cryptoadventure.com/dex-screener-review-2026-real-time-dex-pair-tracking-alerts-and-api/)
- [CoinGecko：Robinhood Chain built for RWA loved for memes](https://www.coingecko.com/learn/robinhood-chain-built-for-rwa-loved-for-memes)、[CryptoTicker：Robinhood Chain 迷因幣完全指南](https://cryptoticker.io/en/robinhood-chain-memecoins-explained/)
