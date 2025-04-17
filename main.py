import streamlit as st
import base64

# ------------------ CONFIG ------------------
st.set_page_config(page_title="PhD Toolkit Dashboard", page_icon="🎓", layout="wide")
st.title("🎓 PhD Toolkit Dashboard")

# ------------------ SIDEBAR ------------------
st.sidebar.title("📂 Categories")
search_term = st.sidebar.text_input("🔍 Search Tool")
selected_category = st.sidebar.radio("Jump to Section", [
    "📚 Research Management",
    "🗓 Project & Time Management",
    "📝 Writing & Drafting",
    "🔍 Research & Analysis",
    "📊 Visualization",
    "🤝 Collaboration",
    "💡 Productivity & Wellness"
])

# ------------------ TOOL DATA ------------------
tools = {
    "📚 Research Management": [
        {"name": "EndNote", "desc": "Reference management software.", "url": "https://endnote.com", "emoji": "📘", "tags": ["reference", "citations"], "rating": 4.5},
        {"name": "Research Rabbit", "desc": "Visual tool to explore academic papers.", "url": "https://www.researchrabbit.ai", "emoji": "🐇", "tags": ["visual", "papers"], "rating": 5},
        {"name": "Notion", "desc": "Organize notes, tasks, and references.", "url": "https://notion.so", "emoji": "🗃️", "tags": ["notes", "dashboard"], "rating": 5},
        {"name": "Paperpile", "desc": "Reference tool integrated with Google Docs.", "url": "https://paperpile.com", "emoji": "📎", "tags": ["google docs", "citations"], "rating": 4},
        {"name": "Connected Papers", "desc": "Visual explorer for literature networks.", "url": "https://connectedpapers.com", "emoji": "🧠", "tags": ["visual", "mapping"], "rating": 4.5},
        {"name": "Zotero", "desc": "PDF and reference manager.", "url": "https://zotero.org", "emoji": "📂", "tags": ["pdf", "annotations"], "rating": 4.5},
        {"name": "Rayyan", "desc": "Systematic review screening tool.", "url": "https://rayyan.ai", "emoji": "📝", "tags": ["review", "collaboration"], "rating": 4}
    ],
    "🗓 Project & Time Management": [
        {"name": "Trello", "desc": "Kanban-style project tracker.", "url": "https://trello.com", "emoji": "🗂️", "tags": ["task", "workflow"], "rating": 4.5},
        {"name": "ClickUp", "desc": "All-in-one project and time manager.", "url": "https://clickup.com", "emoji": "🛠️", "tags": ["productivity"], "rating": 4.5},
        {"name": "Pomofocus", "desc": "Custom Pomodoro timer.", "url": "https://pomofocus.io", "emoji": "⏱️", "tags": ["focus", "pomodoro"], "rating": 4.5},
        {"name": "Google Calendar", "desc": "Time blocking and reminders.", "url": "https://calendar.google.com", "emoji": "📆", "tags": ["calendar", "reminders"], "rating": 4},
        {"name": "Toggl Track", "desc": "Simple time tracking.", "url": "https://toggl.com/track", "emoji": "⏳", "tags": ["tracking", "analytics"], "rating": 4},
        {"name": "Gantt Charts", "desc": "Visualize your long-term project timeline.", "url": "https://teamgantt.com", "emoji": "📈", "tags": ["timeline", "gantt"], "rating": 4}
    ],
    "📝 Writing & Drafting": [
        {"name": "Overleaf", "desc": "LaTeX-based collaborative writing platform.", "url": "https://overleaf.com", "emoji": "📄", "tags": ["latex", "collaboration"], "rating": 5},
        {"name": "Scrivener", "desc": "Powerful writing tool for long documents.", "url": "https://literatureandlatte.com/scrivener", "emoji": "🖋️", "tags": ["writing", "draft"], "rating": 4.5},
        {"name": "Grammarly", "desc": "Grammar and style suggestions for writing.", "url": "https://grammarly.com", "emoji": "✍️", "tags": ["proofreading", "grammar"], "rating": 4.5}
    ],
    "🔍 Research & Analysis": [
        {"name": "Google Colab", "desc": "Cloud-based Jupyter notebook environment.", "url": "https://colab.research.google.com", "emoji": "💻", "tags": ["python", "notebooks"], "rating": 5},
        {"name": "Zotero+Zotfile", "desc": "Enhanced PDF and citation organization.", "url": "https://zotfile.com", "emoji": "📁", "tags": ["sync", "pdfs"], "rating": 4.5},
        {"name": "Scite.ai", "desc": "Smart citations with context.", "url": "https://scite.ai", "emoji": "🔬", "tags": ["citations", "metrics"], "rating": 4.5},
        {"name": "Semantic Scholar", "desc": "AI-powered academic search engine.", "url": "https://semanticscholar.org", "emoji": "📑", "tags": ["search", "papers"], "rating": 4.5}
    ],
    "📊 Visualization": [
        {"name": "Canva", "desc": "Design graphics and posters easily.", "url": "https://canva.com", "emoji": "🎨", "tags": ["design", "slides"], "rating": 5},
        {"name": "Figma", "desc": "Collaborative UI and wireframe design.", "url": "https://figma.com", "emoji": "📐", "tags": ["interface", "prototyping"], "rating": 4.5},
        {"name": "Prezi", "desc": "Non-linear presentation tool.", "url": "https://prezi.com", "emoji": "📽️", "tags": ["presentation", "animated"], "rating": 4},
        {"name": "Beautiful.ai", "desc": "Smart templates for professional slides.", "url": "https://www.beautiful.ai", "emoji": "🖼️", "tags": ["slides", "automation"], "rating": 4.5}
    ],
    "🤝 Collaboration": [
        {"name": "Google Docs", "desc": "Collaborative document editing.", "url": "https://docs.google.com", "emoji": "📃", "tags": ["editing", "comments"], "rating": 5},
        {"name": "Slack", "desc": "Team communication workspace.", "url": "https://slack.com", "emoji": "💬", "tags": ["chat", "team"], "rating": 4.5},
        {"name": "Microsoft Teams", "desc": "Meetings, chat, and document collaboration.", "url": "https://teams.microsoft.com", "emoji": "🧑‍💼", "tags": ["microsoft", "teams"], "rating": 4},
        {"name": "GitHub", "desc": "Version control and code sharing platform.", "url": "https://github.com", "emoji": "🐙", "tags": ["code", "collaboration"], "rating": 5}
    ],
    "💡 Productivity & Wellness": [
        {"name": "Notion Templates", "desc": "PhD-specific dashboards and planners.", "url": "https://notion.so", "emoji": "📋", "tags": ["templates", "tracking"], "rating": 5},
        {"name": "Forest App", "desc": "Stay focused by growing trees.", "url": "https://forestapp.cc", "emoji": "🌳", "tags": ["focus", "pomodoro"], "rating": 4.5},
        {"name": "Cold Turkey", "desc": "Block distractions effectively.", "url": "https://getcoldturkey.com", "emoji": "🦃", "tags": ["blocker", "focus"], "rating": 4},
        {"name": "Freedom", "desc": "Block websites and apps across devices.", "url": "https://freedom.to", "emoji": "🔒", "tags": ["block", "focus"], "rating": 4.5},
        {"name": "Headspace", "desc": "Guided meditation for stress relief.", "url": "https://headspace.com", "emoji": "🧘", "tags": ["meditation", "mental health"], "rating": 4.5},
        {"name": "Insight Timer", "desc": "Free meditation and mindfulness app.", "url": "https://insighttimer.com", "emoji": "⏰", "tags": ["mindfulness", "sleep"], "rating": 4.5},
        {"name": "Calm", "desc": "Meditation, sleep stories, and focus music.", "url": "https://calm.com", "emoji": "🌙", "tags": ["sleep", "relaxation"], "rating": 4.5}
    ]
}

# ------------------ FILTER FUNCTION ------------------
def display_tools(category, tools_list):
    for tool in tools_list:
        if search_term and search_term.lower() not in tool["name"].lower():
            continue
        st.markdown(f"{tool['emoji']} **[{tool['name']}]({tool['url']})**")
        st.markdown(f"- {tool['desc']}")
        st.markdown(f"- ⭐ Rating: {tool['rating']} / 5")
        st.markdown(f"- 🏷️ Tags: {', '.join(tool['tags'])}")
        st.markdown("---")

# ------------------ MAIN CONTENT ------------------
if selected_category in tools:
    display_tools(selected_category, tools[selected_category])
else:
    st.write("No tools found.")
