

import streamlit as st

#---------------------------------------------------

import firebase_admin
from firebase_admin import credentials, firestore
import datetime


# Firestore 認証情報を secrets.toml から読み込む
cred = credentials.Certificate({
    "type": st.secrets["firestore"]["type"],
    "project_id": st.secrets["firestore"]["project_id"],
    "private_key_id": st.secrets["firestore"]["private_key_id"],
    "private_key": st.secrets["firestore"]["private_key"],
    "client_email": st.secrets["firestore"]["client_email"],
    "client_id": st.secrets["firestore"]["client_id"],
    "auth_uri": st.secrets["firestore"]["auth_uri"],
    "token_uri": st.secrets["firestore"]["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["firestore"]["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["firestore"]["client_x509_cert_url"]
})

# Firebase 初期化（複数回初期化されないように）
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# データベース接続
db = firestore.client()

st.title("うま王メンバーズチャット")


#---------------------------------------------------

options = ["2026年うま王収支表（単勝）","2026年うま王収支表（馬連）","2026年うま王収支表（三連複）",
           "0426フローラＳ","0426マイラーズＣ",
           "0425青葉賞",
           "0419皐月賞","0419福島牝馬Ｓ",
           "0418アンタレスＳ",
           "0412桜花賞",
           "0411ニュージーランドＴ","0411阪神牝馬Ｓ",
           "0405大阪杯",
           "0404ダービー卿ＣＴ","0404チャーチルダウンズＣ",
           "0329高松宮記念","0329マーチＳ",
           "0328日経賞","0328毎日杯",
           "0322阪神大賞典","0322愛知杯",
           "0321フラワーカップ","0321ファルコンＳ",
           "0315スプリングＳ","0315金鯱賞",
           "0308弥生賞","0307中山牝馬Ｓ", "0307フィリーズレビュー",
           "0301中山記念", "0301チューリップ賞", "0228オーシャンＳ",
           "0222フェブラリーＳ", "0222小倉大賞典",
           "0221ダイヤモンドＳ", "0221阪急杯",
           "0215共同通信杯", "0215京都記念", "0214クイーンカップ", 
           "0210東京新聞杯", "0210きさらぎ賞",
           "0201シルクロードＳ", "0201根岸Ｓ",
           "0125アメリカジョッキーＣ", "0125プロキオンＳ", "0124小倉牝馬Ｓ",
           "0118京成杯", "0118日経新春杯",
           "0112シンザン記念", "0111フェアリーＳ",
           "0104中山金杯", "0104京都金杯"]

# Streamlit のコンボボックス
enemy = st.selectbox("レースを選択してください", options)

# 選択されたレースに応じて画像を表示
if enemy:
    # ファイル名を辞書で管理
    image_files = {
        "2026年うま王収支表（単勝）": "2026うま王収支表（単勝）.png",
        "2026年うま王収支表（馬連）": "2026うま王収支表（馬連）.png",
        "2026年うま王収支表（三連複）": "2026うま王収支表（三連複）.png",
        "0426フローラＳ":"0426フローラＳ.png",
        "0426マイラーズＣ":"0426マイラーズＣ.png",
        "0425青葉賞":"0425青葉賞.png",
        "0419皐月賞":"0419皐月賞.png",
        "0419福島牝馬Ｓ": "0419福島牝馬Ｓ.png",
        "0418アンタレスＳ":"0418アンタレスＳ.png",        
        "0412桜花賞":"0412桜花賞.png",
        "0411ニュージーランドＴ":"0411ニュージーランドＴ.png",
        "0411阪神牝馬Ｓ": "0411阪神牝馬Ｓ.png",
        "0405大阪杯": "0405大阪杯.png",
        "0404ダービー卿ＣＴ": "0404ダービー卿ＣＴ.png",
        "0404チャーチルダウンズＣ": "0404チャーチルダウンズＣ.png",        
        "0329高松宮記念": "0329高松宮記念.png",
        "0329マーチＳ": "0329マーチＳ.png",
        "0328日経賞": "0328日経賞.png",
        "0328毎日杯": "0328毎日杯.png",
        "0322阪神大賞典": "0322阪神大賞典.png",
        "0322愛知杯": "0322愛知杯.png",
        "0321フラワーカップ": "0321フラワーカップ.png",
        "0321ファルコンＳ": "0321ファルコンＳ.png",
        "0315スプリングＳ": "0315スプリングＳ.png",
        "0315金鯱賞": "0315金鯱賞.png",
        "0308弥生賞": "0308弥生賞.png",
        "0307中山牝馬Ｓ": "0307中山牝馬Ｓ.png",
        "0307フィリーズレビュー": "0307フィリｰズレビュー.png",        
        "0301中山記念": "0301中山記念.png",
        "0301チューリップ賞": "0301チューリップ賞.png",
        "0228オーシャンＳ": "0228オーシャンＳ.png",
        "0222フェブラリーＳ": "0222フェブラリーＳ.png",
        "0222小倉大賞典": "0222小倉大賞典.png",
        "0221ダイヤモンドＳ": "0221ダイヤモンドＳ.png",
        "0221阪急杯": "0221阪急杯.png",
        "0214クイーンカップ": "0214クイーンカップ.png",
        "0215共同通信杯": "0215共同通信杯.png",
        "0215京都記念": "0215京都記念.png",
        "0214クイーンカップ": "0214クイーンカップ.png",
        "0210東京新聞杯": "0209東京新聞杯.png",
        "0210きさらぎ賞": "0209きさらぎ賞.png",
        "0201シルクロードＳ": "0201シルクロードS.png",
        "0201根岸Ｓ": "0201根岸S.png",        
        "0125アメリカジョッキーＣ": "0125アメリカジョッキーC.png",
        "0125プロキオンＳ": "0125プロキオンS.png",
        "0124小倉牝馬Ｓ": "0124小倉牝馬S.png",
        "0118京成杯": "0118京成杯.png",
        "0118日経新春杯": "0118日経新春杯.png",
        "0112シンザン記念": "0112シンザン記念.png",
        "0111フェアリーＳ": "0111フェアリーS.png",
        "0104中山金杯": "0104中山金杯.png",
        "0104京都金杯": "0104京都金杯.png",
    }

    filename = image_files.get(enemy)

    st.write(f"選択されたレース：{enemy}")

    # 画像表示
    st.image(filename, width=800)


#---------------------------------------------------


st.header("チャットルーム")

# 名前入力
user = st.text_input("名前を入力してください")

# メッセージ入力
message = st.text_input("メッセージを入力してください")

# 送信ボタン
if st.button("送信"):
    if user and message:
        db.collection("chat").add({
            "user": user,
            "message": message,
            "timestamp": datetime.datetime.now()
        })
        st.success("送信しました！")
        st.experimental_rerun()  # ← 送信後に即時更新
    else:
        st.warning("名前とメッセージを入力してください。")

st.subheader("メッセージ一覧（最新50件）")

# Firestore からメッセージ取得（新しい順）
messages = (
    db.collection("chat")
    .order_by("timestamp", direction=firestore.Query.DESCENDING)
    .limit(50)
    .stream()
)

# 表示（新しい順 → 古い順に並べ替え）
messages = list(messages)[::-1]

for msg in messages:
    data = msg.to_dict()
    timestamp = data["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"**{data['user']}**：{data['message']}  \n _{timestamp}_")
