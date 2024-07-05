# 專案簡介

本專案展示了如何在 Django 應用程式中使用 Markdown 進行內容管理，參考自 Real Python 的教程：[How to Render Markdown in a Django Application](https://realpython.com/django-markdown/#how-to-use-markdown-for-content-in-a-django-application)。

## 目錄

- [專案簡介](#專案簡介)
  - [目錄](#目錄)
  - [概述](#概述)
  - [功能](#功能)
  - [安裝](#安裝)
    - [先決條件](#先決條件)
    - [步驟](#步驟)
  - [使用方法](#使用方法)
  - [授權](#授權)

## 概述

這個 Demo 希望能讓 Django 學習者瞭解如何在 Django 專案中，使用 Markdown 語法來新增和編輯內容，透過 Markdown 這種輕量級標記語言，使撰寫和閱讀文本文件變得簡單。  
專案中亦有教導學習者如何「建立與使用 template tags」、「延伸 markdown 的擴充功能」，建議學習者需具備基礎 Django 知識，會更容易理解本專案內容。  

## 功能

- 可以使用 Markdown 語法創建、編輯文章。
- 在網頁上可以以高亮色彩形式，顯示 Markdown 的 code block 程式碼區域。

## 安裝

按照以下步驟在本地端上運行此專案。

### 先決條件

- Python 3.12
- Django 3.0.6 或更高版本
- Poetry

### 步驟

1. 克隆此 Repository  

    ```bash
    git clone git@github.com:chienchuanw/django-markdown-demo.git
    cd django-markdown-demo
    ```

2. 建立虛擬環境並啟動，如果還沒有安裝 Poetry，請先安裝  

    ```bash
    pip install poetry
    ```

    使用 Poetry 進入虛擬環境  

    ```bash
    poetry shell
    ```

3. 使用 Poetry 安裝依賴套件  

    ```bash
    poetry install
    ```

4. 設定環境變數，於路徑 `/core` 內複製 `.env.example` 並重新命名為 `.env`，根據檔案內指引提示設定對應的環境變數  

    ```bash
    # .env 文件範例
    SECRET_KEY=Django-專案金鑰
    ```

5. 遷移資料庫  

    ```bash
    python manage.py migrate
    ```

6. 創建超級用戶以訪問管理介面  

    ```bash
    python manage.py createsuperuser
    ```

7. 啟動開發伺服器

    ```bash
    python manage.py runserver
    ```

8. 打開瀏覽器並於網址列輸入 `http://127.0.0.1:8000/admin/`，登入後點擊 `Posts` 新增文章，並於文章內使用 Markdown

## 使用方法

- 使用超級用戶帳戶登入管理介面。
- 使用 Markdown 語法新增文章。
- 在網站上查看渲染的 HTML 內容。

## 授權

本專案使用 MIT 授權條款。詳情請參閱 `LICENSE` 文件。  
如有其他建議，可以透過 Discord 搜尋 `chienchuan_w` 加好友並留言私訊，歡迎大家相互交流。  
這邊是我的[中文版影音解說](https://youtu.be/wul6BInftl4)  
