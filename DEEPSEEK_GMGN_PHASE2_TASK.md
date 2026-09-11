# DeepSeek 任務書：GMGN App Phase 2 內容策略分析

## 任務

以「內容策略顧問」身份，分析 `gmgn-app-full-manual.md`（GMGN 手機 App 全功能實機探索手冊，1281行）對照網站現有的 GMGN 網頁版教學內容，找出「App 有、網站還沒講清楚」的缺口，產出一份網站內容規劃方案 `gmgn-website-plan.md`。

**這不是寫程式任務，不用碰任何 code，只需要讀資料、分析、寫一份新的 Markdown 報告。**

## 背景

`meme-lol` 是一個面向中文用戶的迷因幣（meme coin）交易教學網站。首頁定位：「用手機把 GMGN、Axiom、fomo、DEX Screener 四個幣圈工具串成一條『發現→驗證→下單→追蹤→出場』流程的小白教學站，內建小白／進階雙模式與詞彙查詢。非投資建議，僅供工具操作教學。」

`index.html` 裡已經有一份成熟的 GMGN **網頁版**教學（`id="tool-gmgn"`，約在第 428~720 行），結構是 🚀上手／🟣進階／📖詞彙／⚠️風險 四個分頁。現在要補的是 GMGN **手機 App** 特有、網頁版沒講過的內容，方法是實機操作 iPhone 逐分頁探索，探索結果就是 `gmgn-app-full-manual.md`。

**必讀參考範本**：昨天做過同一套流程分析 DEX Screener（`dex-screener-website-plan.md`，17KB，已存在於這個 worktree 根目錄），格式和分析深度都要**照著這份範本的風格做**，不要另外發明新格式。重點抓住範本的精神：
- 先講結論（哪些是真缺口、哪些其實網站已經覆蓋不用重做）
- 用 🟢強烈建議／🟡建議／🔴不建議 三級標記逐項評估，附一句話理由
- 每個要做的模組寫清楚：對應 App 哪個功能、建議用什麼形式呈現（示意圖/條列/懶人包等）、放進網站哪個分頁的哪個位置、目標用戶是誰、具體內容草稿或大綱
- 網站架構建議是「在既有架構內插入」，不是重建整個網站
- 結尾附「給下一手的提醒」——之後真的要動手把內容寫進 index.html 的人（可能是另一個 agent）需要知道的注意事項

## 範圍

1. 讀完整份 `gmgn-app-full-manual.md`（0～9 章 + 附錄A/B，共1281行）
2. 讀 `index.html` 第 428~720 行左右的現有 GMGN 網頁版教學內容（用 `grep -n 'id="tool-gmgn"'` 或搜尋 `data-tool="gmgn"` 定位），搞清楚哪些內容已經講過
3. 也可以參考 `raw/B_gmgn_fragment.html`（GMGN 教學原始碼片段）跟 `raw/B_gmgn_glossary.json`（現有詞彙表）加速比對
4. 逐一比對兩邊內容，找出真正的缺口（App 有、網站沒講或講不清楚的）
5. 產出 `gmgn-website-plan.md`，內容至少包含：
   - 先講結論（200字內摘要）
   - 功能分類評估表（🟢🟡🔴 三級 + 理由）——**至少涵蓋這幾個本次手冊裡標記教學價值★★★的重點**：
     - 退租（關閉空帳戶回收SOL，網頁版完全沒提過）
     - 釣魚偵測 + 利潤分佈（對應網站現有「風險」分頁）
     - 多錢包合併顯示 + 持倉篩選預設值（新手「幣不見了」誤會來源）
     - 官方數據解釋（22條術語定義，可能可以直接補進網站詞彙表）
     - Copy Trade 完整設定表單（跟買/賣出/過濾/費用）
     - 持有者分析（Top Holders/Dev Wallet/Insiders/Snipers）
     - 戰壕篩選器的反 rug 條件（X改名次數/Dev遷移比例/隱藏開發者地址）
     - 監控分頁的 KOL Callouts 統計卡（拆穿 KOL 話術）
   - 內容模組規劃（每個要做的模組：對應功能/實作形式/目標用戶/放置位置/內容大綱）
   - 網站架構建議（在現有架構內插入的位置）
   - 一個簡短的優先級排序（用🟢🟡🔴對應P0/P1/P2即可，不用另外發明新的優先級系統）
   - 一小段「懶人包/速查表建議」（哪些內容適合做成一頁式圖卡）
   - 一小段「SEO關鍵字建議」（中文為主，抓幾個「GMGN App 教學」「GMGN 跟單設定」這類長尾詞）
   - 給下一手的提醒

## 白名單（允許改動）

- `gmgn-website-plan.md`（新建這一個檔案，寫在 worktree 根目錄）

## 黑名單（絕對不准碰）

> 這一段是隔離真正生效的關鍵。

- `index.html`（只准讀，絕對不准修改）
- `gmgn-app-full-manual.md`（只准讀，這是 Phase 1 的產出，不是你的任務範圍）
- `dex-screener-website-plan.md`、`dex-screener-features.md`、`dex-screener-screener-tab-walkthrough.md`、`dex-screener-token-detail-walkthrough.md`（只准讀當範本參考，不准修改）
- `raw/` 整個目錄（只准讀）
- `HANDOFF.md`、`幣圈四大工具懶人包_UIUX規劃書.md`、`collapse_stamps.py`、`integrate_10field.py`、`verify_figs.py`、`wrangler.jsonc`、`.gitignore`、`.assetsignore`
- 不要跑 `git commit`（這次任務書會由 CC 在驗收後幫你 commit，你只需要把檔案寫好存檔）

## 驗收條件

- [ ] `gmgn-website-plan.md` 存在，格式比照 `dex-screener-website-plan.md` 的風格（先講結論/分級評估表/內容模組規劃/架構建議/懶人包/SEO/給下一手的提醒）
- [ ] 涵蓋任務書列出的 8 個★★★重點功能，每項都有明確的🟢🟡🔴分級跟理由
- [ ] 有清楚指出「網站已經覆蓋、不用重做」的部分（避免重複造輪子），不是全部東西都判🟢
- [ ] 除了 `gmgn-website-plan.md`，其他檔案零改動（用 `/usr/bin/git status --short` 確認）

## 環境備註

這台機器的 bash 環境套了輸出壓縮工具（rtk），`git diff` 等指令有時只會顯示摘要、沒有逐行 +/- 內容——這是正常現象。需要完整輸出時直接呼叫 `/usr/bin/git` 繞過這層包裝即可。

---

## 完工前自查清單

完成 `gmgn-website-plan.md` 之後，回報完工之前依序自己做完下列檢查：

1. 重讀一遍自己寫的內容，確認每個判斷都有具體理由支撐，不是空泛的「這個不錯」。
2. 檢查有沒有內容重複或結構混亂的地方，順手整理。
3. 用挑剔的眼光重讀一次（當作在 review 別人交的報告），抓得到問題就自己修。
4. 用 `/usr/bin/git status --short` 確認除了 `gmgn-website-plan.md` 沒有動到任何其他檔案。
5. 在報告最前面加一段簡短摘要（200字內）。
6. 上面任何一步發現問題，自己修完再回報，不用等對方確認。

完工後在回報裡簡短說明：涵蓋了哪些重點、有沒有發現「網站已經覆蓋不用做」的項目、自查清單過了沒有。
