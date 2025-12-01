import streamlit as st
import datetime
import pandas as pd

# --- CONFIGURATION ---
st.set_page_config(page_title="December Challenge", page_icon="🎄", layout="centered")

# --- CUSTOM STYLES ---
st.markdown("""
    <style>
    .big-font { font-size:20px !important; font-weight: bold; }
    .stProgress > div > div > div > div { background-color: #d90429; }
    </style>
    """, unsafe_allow_html=True)

# --- QUEST DATABASE (Updated) ---
QUESTS = {
    2: "No screens for 30 mins before bed 📵",
    3: "10-min stretching session together 🧘",
    4: "Board Game or Puzzle Night (No TV) 🎲",
    5: "Dine Outside (Treat yourselves!) 🍽️",
    6: "Silly face selfie with the kids 📸",
    7: "Declutter one drawer in the house 🧹",
    8: "No added sugar today 🍬",
    9: "Read a Christmas story to the kids 📖",
    10: "Read 10 pages of a book 📚",
    11: "Don't complain about anything for 24h 🤐",
    12: "Dance to 3 Christmas songs with kids 💃",
    13: "Family Karaoke Night (1 song each) 🎤",
    14: "20 Jumping Jacks with the kids 🏃",
    15: "Organize shoe rack or coat closet 🧥",
    16: "No social media scrolling today 📵",
    17: "Cook a healthy meal together 🥗",
    18: "50 Squats (Total throughout the day) 🏋️",
    19: "Watch a Christmas movie with family 🎬",
    20: "Write down 3 goals for next year 📝",
    21: "Living Room 'Picnic' Dinner 🧺",
    22: "DIY Christmas decoration with kids 🎨",
    23: "Drive around to see Christmas Lights 🚗",
    24: "FINAL WEIGH IN & GIFT EXCHANGE 🎁"
}

# --- FUNCTIONS ---
def get_daily_quest():
    today = datetime.datetime.now().day
    return QUESTS.get(today, "Waiting for December 2nd to start!")

def calculate_score(user_role, w1, w2, w3, s_half, s_full, cal, prot, sleep_hrs, quest_done, bonus_active):
    score = 0
    
    # Water (15 JBP Max)
    if w1: score += 5
    if w2: score += 5
    if w3: score += 5
    
    # Steps (15 JBP Max)
    if s_half: score += 5
    if s_full: score += 10 
    
    # Nutrition (20 JBP)
    if cal: score += 20
    
    # Protein (10 JBP)
    if prot: score += 10
    
    # Sleep (Tiered: 6h=10pts, 7h+=25pts)
    if sleep_hrs >= 7:
        score += 25 
    elif sleep_hrs >= 6:
        score += 10 
        
    # Quest (25 JBP)
    if quest_done: score += 25
    
    # Bonus Multiplier
    if bonus_active:
        score = int(score * 1.1)
        
    return score

# --- MAIN APP ---
st.title("🎄 The December Challenge 🎅")
st.write("### 🏁 Race to Christmas Eve")

# Display Today's Quest
st.info(f"**🎅 Today's Quest (Dec {datetime.datetime.now().day}):** {get_daily_quest()}")

# Tabs
tab1, tab2, tab3 = st.tabs(["👩 Wife", "👨 Husband", "🏆 Leaderboard"])

with tab1:
    st.header("Wife's Tracker")
    st.caption("Targets: 2.2L Water | 7,500 Steps | 1,200 Cal | Sleep 7h+")
    
    with st.form("wife_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**💧 Water Intake**")
            w_w1 = st.checkbox("1.2L before 12pm")
            w_w2 = st.checkbox("0.5L before 5pm")
            w_w3 = st.checkbox("0.5L after Dinner")
            
            st.markdown("**👟 Steps**")
            s_w1 = st.checkbox("Hit 50% (3,750) by 6pm")
            s_w2 = st.checkbox("Hit Total (7,500) by Sleep")

        with col2:
            st.markdown("**🍎 Nutrition & Body**")
            n_w_cal = st.checkbox("Calories under 1,200")
            n_w_prot = st.checkbox("Hit Protein Goal")
            w_sleep = st.slider("Hours Slept Last Night", 0.0, 12.0, 7.0, 0.5)
            w_quest = st.checkbox("✅ Daily Quest Completed!")
            w_bonus = st.checkbox("Did you hit ALL targets yesterday? (1.1x Bonus)")

        submit_wife = st.form_submit_button("Calculate My Jingle Points")
        
        if submit_wife:
            final_score_w = calculate_score("Wife", w_w1, w_w2, w_w3, s_w1, s_w2, n_w_cal, n_w_prot, w_sleep, w_quest, w_bonus)
            if final_score_w >= 100:
                st.balloons()
            st.success(f"🌟 **Today's Score: {final_score_w} JBP**")

with tab2:
    st.header("Husband's Tracker")
    st.caption("Targets: 2.2L Water | 6,000 Steps | 1,500 Cal | Sleep 7h+")
    
    with st.form("husband_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**💧 Water Intake**")
            h_w1 = st.checkbox("1.2L before 12pm")
            h_w2 = st.checkbox("0.5L before 5pm")
            h_w3 = st.checkbox("0.5L after Dinner")
            
            st.markdown("**👟 Steps**")
            h_s1 = st.checkbox("Hit 50% (3,000) by 6pm")
            h_s2 = st.checkbox("Hit Total (6,000) by Sleep")

        with col2:
            st.markdown("**🍎 Nutrition & Body**")
            n_h_cal = st.checkbox("Calories under 1,500")
            n_h_prot = st.checkbox("Hit Protein Goal")
            h_sleep = st.slider("Hours Slept Last Night", 0.0, 12.0, 7.0, 0.5)
            h_quest = st.checkbox("✅ Daily Quest Completed!")
            h_bonus = st.checkbox("Did you hit ALL targets yesterday? (1.1x Bonus)")

        submit_husband = st.form_submit_button("Calculate His Jingle Points")
        
        if submit_husband:
            final_score_h = calculate_score("Husband", h_w1, h_w2, h_w3, h_s1, h_s2, n_h_cal, n_h_prot, h_sleep, h_quest, h_bonus)
            if final_score_h >= 100:
                st.snow()
            st.success(f"🌟 **Today's Score: {final_score_h} JBP**")

with tab3:
    st.write("### 📊 Current Standings")
    st.write("*(Use this tab to manually log your daily totals if you like!)*")
    col_a, col_b = st.columns(2)
    col_a.metric("Wife's Total", "0 JBP", "Target: Weight Loss")
    col_b.metric("Husband's Total", "0 JBP", "Target: Weight Loss")
