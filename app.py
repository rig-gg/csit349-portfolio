import streamlit as st
import pandas as pd

st.set_page_config(page_title="GYLE AMIHAN | Portfolio", page_icon="👋", layout="wide")

with st.sidebar:
    st.markdown(
        """
        <div style="padding:4px 0 2px 0;">
            <div style="font-size:1.12rem;font-weight:700;line-height:1.25;">
                Gyle M. Amihan
            </div>
            <div style="font-size:0.78rem;color:#8a8f98;margin-top:3px;">
                BSIT 4 &middot; Section G01
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown(
        """
        <style>
        .side-nav a {
            display:block;
            padding:6px 10px;
            margin:2px 0;
            border-radius:8px;
            text-decoration:none;
            color:inherit;
            font-size:0.9rem;
        }
        .side-nav a:hover { background:rgba(37,99,235,0.12); }
        </style>
        <div class="side-nav">
            <a href="#about">About</a>
            <a href="#autobiography">Autobiography</a>
            <a href="#skills">Skills</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()
    st.link_button("📧 Email me", "mailto:amihangyle@gmail.com", width="stretch")
    st.link_button("💻 GitHub", "https://github.com/rig-gg", width="stretch")

    st.divider()
    st.caption("CSIT 349 · Applied AI")

st.title("Gyle Mangpang Amihan")
st.subheader("Applied AI Student · CSIT 349")
st.caption("📍 Cebu, Philippines · 🎓 BSIT 4 · CIT University")

st.markdown('<div id="about"></div>', unsafe_allow_html=True)

left, right = st.columns([1, 2], gap="large")

with left:
    st.image("photo.png",
             caption="Gyle M. Amihan", width=260)

with right:
    st.markdown("### About me")
    st.write("Hello! I am Gyle Amihan, a fourth-year BSIT student. I built this site to showcase my projects and skills.")
    st.info("Program: BSIT  |  Year: Fourth Year  |  Section: G01")

m1, m2, m3 = st.columns(3)
m1.metric("Projects", "3")
m2.metric("Skills", "6")
m3.metric("Year", "4th")

st.divider()

st.header("Autobiography", anchor="autobiography")
tab_bg, tab_edu, tab_int, tab_mile = st.tabs(
    ["🌱 Background", "🎓 Education", "💡 Interests", "🏁 Milestones"]
)

with tab_bg:
    st.markdown("#### Where I started")
    st.write("I grew up on Sitio Pusoan, 105 Buhisan Road, Cebu City. I lived with my mom and dad until college, when I moved to Tisa to stay with my grandparents. Growing up in Buhisan taught me to be compassionate and to appreciate the hard work our family has done, and it's still instilled in me today — hopefully it stays that way.")

with tab_edu:
    st.markdown("#### Education")
    st.write("I started at a religious school, then a private medical school for senior high, and now I'm at CIT studying IT!")
    st.markdown("- **2010-2020** (Elementary to Junior High) — Started at Evangelical Theological College of the Philippines (ETCP)")
    st.markdown("- **2020-2023** (Senior High School) — Transferred to Southwestern University (SWU)")
    st.markdown("- **2023-Present** (College) — Cebu Institute of Technology University (CIT)")

with tab_int:
    st.markdown("#### Interests")
    st.write("I enjoy building systems focused on automation and making software that helps simplify existing apps or games. Outside of coding, I enjoy playing video games, lifting weights as a lifestyle, and walking outside as a way to appreciate life and nature.")

with tab_mile:
    with st.expander("2024 — A website of the One Piece Anime", expanded=True):
        st.write("I made my first bare-bones website project by myself! Sadly, the file got lost because I saved it on a local computer shop — I didn't have a personal gadget back then.")
    with st.expander("2024 — First Programming Language"):
        st.write("I know this might sound like a little thing, but learning C piqued my interest in software development, programming, and understanding the systems that have been around us for quite some time now.")
    with st.expander("2024 — Dota Intramurals Champion"):
        st.write("It mattered most to me because it helped me become confident that I can do anything with determination and hard work.")
    with st.expander("2025 — Dota Intramurals Champion"):
        st.write("Further achievements shaped who I am as a person. I felt more connected with myself — not just as a player but also as a student!")

st.divider()

st.header("Skills", anchor="skills")
st.write("Skills I've built through coursework and personal projects, rated honestly from 1 to 10.")

skills = pd.DataFrame({
    "Skill": ["Python", "Java", "C", "HTML/CSS", "Streamlit", "SQL"],
    "Category": ["Programming", "Programming", "Programming", "Web", "Data Apps", "Database"],
    "Rating (1-10)": [5, 8, 6, 5, 5, 6],
    "Years of practice": [1, 3, 2, 2, 1, 2],
})

col_table, col_chart = st.columns(2, gap="large")

with col_table:
    st.markdown("#### Skill table")
    st.dataframe(
        skills,
        hide_index=True,
        width="stretch",
        column_config={
            "Rating (1-10)": st.column_config.ProgressColumn(
                "Rating (1-10)", min_value=0, max_value=10, format="%d"
            )
        },
    )

with col_chart:
    st.markdown("#### Skills chart")
    metric = st.selectbox(
        "Chart metric",
        ["Rating (1-10)", "Years of practice"],
        label_visibility="collapsed",
    )
    st.bar_chart(skills, x="Skill", y=metric, height=330, width="stretch")

st.divider()

st.header("Projects", anchor="projects")
st.write("A few things I've built, what I did on each, and how they turned out.")

projects = [
    {
        "title": "One Piece Fan Website",
        "role": "Solo developer and designer",
        "tools": ["HTML", "CSS Tailwind"],
        "outcome": "Built my first website from scratch to practice layout and styling. The files were lost on a shared shop PC, but it proved I could ship a page alone.",
        "link": "",
    },
    {
        "title": "OOP 2 Game",
        "role": "Game Developer and designer",
        "tools": ["Java", "Tiled"],
        "outcome": "A game inspired by Soul Knight–like mechanics, set in a post-apocalyptic Philippines after a deadly political war. **(NOTE: CHARACTERS ARE MADE FOR FUN ONLY)**",
        "link": "https://github.com/Murgwell/Capstone",
    },
    {
        "title": "MediBook",
        "role": "Lead Developer",
        "tools": ["Java Spring Boot", "Supabase", "Kotlin", "React"],
        "outcome": "An online medical appointment booking app that lets patients book from their phones while doctors use the website to approve, deny, and accept bookings.",
        "link": "https://github.com/rig-gg/MediBook",
    },
]

for col, p in zip(st.columns(3, gap="medium"), projects):
    with col:
        with st.container(border=True):
            st.subheader(p["title"])
            st.caption(f"Role: {p['role']}")
            st.write(p["outcome"])
            st.write("**Tools:** " + ", ".join(p["tools"]))
            if p["link"]:
                st.link_button("View project", p["link"], width="stretch")

st.divider()

st.header("Contact & Feedback", anchor="contact")
st.write("Have a question, comment, or project idea? Send me a note below.")

c1, c2, c3 = st.columns(3)
c1.link_button("📧 Email me", "mailto:amihangyle@gmail.com", width="stretch")
c2.link_button("💻 GitHub", "https://github.com/rig-gg", width="stretch")
c3.link_button("📍 Cebu, Philippines", "https://maps.google.com/?q=Cebu+City", width="stretch")

if "feedback" not in st.session_state:
    st.session_state.feedback = []

with st.form("contact_form", clear_on_submit=True):
    a, b = st.columns(2)
    name = a.text_input("Your name")
    email = b.text_input("Your email")
    topic = st.radio(
        "Topic",
        ["General feedback", "Project question", "Collaboration"],
        horizontal=True,
    )
    rating = st.slider("How useful was this portfolio?", 1, 5, 4)
    message = st.text_area("Message", height=120)
    wants_reply = st.checkbox("I'd like a reply")
    submitted = st.form_submit_button("Send feedback")

if submitted:
    if not name.strip() or not message.strip():
        st.error("Please add your name and a message.")
    else:
        st.session_state.feedback.append(
            {
                "Name": name,
                "Email": email,
                "Topic": topic,
                "Rating": rating,
                "Reply?": "Yes" if wants_reply else "No",
                "Message": message,
            }
        )
        st.success(f"Thanks, {name}! Your feedback was received.")
        st.toast("Feedback saved for this session", icon="✅")
        st.balloons()

if st.session_state.feedback:
    st.markdown("#### Feedback received this session")
    fb = pd.DataFrame(st.session_state.feedback)
    st.dataframe(fb, hide_index=True, width="stretch")
    st.download_button(
        "Download feedback (CSV)",
        fb.to_csv(index=False).encode("utf-8"),
        "feedback.csv",
        "text/csv",
    )

st.divider()
st.caption("© 2026 Gyle M. Amihan · BSIT 4 · Section G01 · CSIT 349 Applied AI")