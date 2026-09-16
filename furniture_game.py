import time
import streamlit as st
st.markdown("<h1 style='color: purple; text-align: center;'>เกมทายศัพท์หมวดเฟอร์นิเจอร์🛋️</h1>",unsafe_allow_html=True,)

st.write("ทายคำศัพท์จากคำใบ้ให้ครบทั้ง 5 คำ !")

# 1. กำหนดค่าเริ่มต้นใน session_state
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""
if "game_started" not in st.session_state:
    st.session_state.game_started = False


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = ""  # เคลียร์ค่าช่องข้อ 3
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 4 
    st.session_state.ans5_val = ""  # เคลียร์ค่าช่องข้อ 5
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog
    st.session_state.game_started = True  # ทำการเริ่มเกม


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()
    

    # ตรวจข้อ 1
    if u_ans1 == "bed":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "television":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มตรวจข้อ 3, 4, 5 ตรงนี้
   # ตรวจข้อ 3
    if u_ans3 == "table":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    # ตรวจข้อ 4
    if u_ans4 == "sofa":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")
     
    # ตรวจข้อ 5
    if u_ans5 == "mirror":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 5:
        st.success("😍 โหดขั้นเทพระดับมาเฟีย")
    if score == 4:
        st.success("😯คนธรรมด๊าาา ธรรมดาา")
    if score == 3:
        st.success("😯คนธรรมด๊าาา ธรรมดาา")
    if score == 2:
        st.success("😯คนธรรมด๊าาา ธรรมดาา")
    if score == 1:
        st.success("😯คนธรรมด๊าาา ธรรมดาา")
    if score == 0:
        st.success("🐔 กระจอกระดับขี้ไก่")
  


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if st.session_state.get("game_started", False) and not st.session_state.get(
    "is_ended", False
):
    time_left = int(90 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.metric(label="⏳ เวลาที่เหลือ", value=f"{time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ
ans1 = st.text_input(
    "ข้อ 1: `b _ d`.It supports the mattress and your body while sleeping.😴",
    key="ans1_val",
)
ans2 = st.text_input(
    "ข้อ 2:  `t _ l _ vis _ on `.A screen in the living room used for watching movies, and shows.📺",
    key="ans2_val",
)

# ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มข้อ 3, 4, 5 ตรงนี้
ans3 = st.text_input(
    "ข้อ 3: `_ a _ _ e`.Have legs but cannot walk. You can put your food or books on me.📚",
    key="ans3_val",
)
ans4 = st.text_input(
    "ข้อ 4:  `s _ _ a`.It features soft cushions and armrests, designed for multiple people to sit on.🛋",
    key="ans4_val",
)
ans5 = st.text_input(
    "ข้อ 5: `_ i r r _ r `.A glass surface that reflects your image when you look into it.🚽 ",
    key="ans5_val",
)

# 4. ปุ่มส่งคำตอบ และระบบนับถอยหลัง Real-time
if st.session_state.get("game_started", False) and not st.session_state.get(
    "is_ended", False
):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    # หน่วงเวลา 1 วินาทีแล้วสั่งรีเฟรชหน้าเฉพาะตอนที่เกมกำลังดำเนินอยู่
    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5)
