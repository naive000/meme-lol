# 交接說明 — 鏈上四寶（幣圈4大工具懶人包網站）

> 給接下來要在 Claude Code（CC）繼續處理這個專案的你自己看的交接筆記。這份資料夾是這次任務的完整產出，可以直接丟進你的 CC 專案資料夾。

## 這個資料夾裡有什麼

```
handoff/
├─ index.html                          ← 完整可直接開啟的網站（雙擊或用瀏覽器開就能跑，手機優先）
├─ 幣圈四大工具懶人包_UIUX規劃書.md      ← fable 產出的完整規劃書（定位/資訊架構/視覺系統/內容大綱/分工建議）
├─ HANDOFF.md                           ← 這份檔案
└─ raw/                                 ← 5個opus agent各自的原始產出(尚未整合前)，只有想拆開改個別區塊時才需要用
   ├─ A_shell.html / A_cookbook.html    ← 設計系統+骨架agent的產出
   ├─ B_gmgn_fragment.html / B_gmgn_glossary.json     ← GMGN內容
   ├─ C_axiom_fragment.html / C_axiom_glossary.json   ← Axiom內容
   ├─ D_fomo_fragment.html / D_dexscreener_fragment.html / D_glossary.json  ← fomo+DEXScreener內容
   └─ E_qaNotes.txt                     ← 整合agent的QA報告全文+issues清單
```

**平常改東西只要動 `index.html` 這一個檔案就好**，`raw/` 只是留底、方便回頭對照某個工具原始內容或抓某個功能的原始寫法。

## 網站現狀

已經發布成一個可分享的線上版本（Claude Artifact）：`鏈上四寶`。`index.html` 是同一份內容，但補上了 `<!DOCTYPE html>`/`<html>`/`<head>`/`<body>` 完整標籤，可以直接當一般網頁檔案用（開瀏覽器、丟到任何靜態網站託管、或在CC裡繼續編輯都行）。

**架構**：單檔 HTML，內嵌全部 CSS/JS，無外部依賴（不用網路也能開）。手機優先，桌機也能看。底部5個Tab（首頁/工具/流程/詞典/風險），hash 路由切換（`#/home` `#/tools` `#/flow` `#/glossary` `#/risk`）。頂部有「小白⇄進階」模式切換鈕，狀態存 localStorage。深/淺色主題都做了（跟隨系統或手動切換都可以，CSS variable token 化）。

## 已知問題／可以繼續做的事（整合 agent 自己列出來的，原文在 `raw/E_qaNotes.txt`）

1. **內容偏長**：整頁約135KB、全站約1.4萬字。想瘦身可以先砍「工具頁-風險分頁」跟「風險總頁」之間重複的敘述（例如Axiom和fomo的仿冒App提醒，兩處都有講）。
2. **checklist 持久化不完整**：只有「風險頁」的安全檢查清單會存 localStorage，4個工具頁裡自己的小checklist（GMGN 6項/Axiom 6項/fomo 3+4項/DEX 5項）目前重新整理就清空。要修的話，幫每個checkbox補一個唯一的`data-ck`屬性，並把儲存邏輯改成掃全站`.checklist`（目前只掃`#safetyChecklist`）。
3. **「進階」分頁在小白模式仍看得到**：用`<details class="acc">`手風琴收合而非完全隱藏，是agent的設計取捨（避免小白模式下該分頁整片空白）。如果你想要完全隱藏，需要幫「進階」這個tab按鈕加上`data-level="advanced"`，讓整個tab在小白模式一起消失。
4. **內容事實未二次複核**：所有費率、募資金額、估值、Robinhood Chain成交量佔比、Axiom推特追蹤上限等數字都是B/C/D產出、標「2026/9查證」的二手資訊，E做整合時沒有重新連外驗證。**發布前建議至少複核一次四家的最新費率跟GMGN官方Telegram Bot帳號**（假冒Bot很多）。
5. **GMGN連結含你的推薦碼**（`ref=KzpFUrXI`），免責聲明已經寫「本站部分連結含推薦碼」，如果想更保守可以在首頁四張工具卡也各補一行小字提示。
6. **截圖全是虛線示意框**（共30處，文案「畫面示意：…」），沒放真實截圖（因為平台規則禁止外連圖片）。要放真實截圖的話，要轉成內嵌`data:` URI 圖片格式，不能用一般`<img src="外部連結">`。

## 這次任務的規劃來源

`幣圈四大工具懶人包_UIUX規劃書.md` 是最初用 fable 模型研究 gmgn.ai / axiom.trade / fomo.family / dexscreener.com 四個網站之後產出的完整規劃書，包含：網站定位與命名、資訊架構/Sitemap、小白/進階雙模式的呈現方式、視覺設計系統（配色/字體/元件class清單）、四個工具各自的教學內容大綱、以及原本給5個agent的分工建議。之後 index.html 就是照這份規劃書實際刻出來的成品，如果要大改版（例如換一套視覺風格、重新分工），可以直接從這份規劃書出發修改。

## 用量紀錄（供參考）

- 規劃階段（fable研究+規劃）：108,236 tokens，約8.5分鐘
- 建站階段（opus 4+1 agent 平行建置）：433,315 tokens，約35分鐘
- 總計：541,551 tokens，約46分鐘（原始預算是0.5M token／1小時，token部分超支約8.3%，時間在預算內）
