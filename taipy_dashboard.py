import taipy as tp
import taipy.gui.builder as tgb
import plotly.graph_objects as go
import pandas as pd
import sqlite3
from taipy.gui import Gui, Icon, navigate


connection = sqlite3.connect("enriche_data.db")
query = "SELECT * FROM clean_stroke"
df = pd.read_sql(query, connection)

fig1 = go.Figure()
for status in df["smoking_status"].unique():
    subset = df[(df["smoking_status"] == status) & (df["stroke"] == "Yes")]
    count = len(subset)

    fig1.add_trace(go.Bar(x=[status], y=[count], name=status, text=[count], textposition="outside"))

fig1.update_layout(
    title="Stroke Cases by Smoking Status",
    xaxis_title="Smoking Status",
    yaxis_title="Stroke Count",
    barmode="group",
    template="plotly_white"
)

def menu_option_selected(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

# Root Page (Navigation Menu)
with tgb.Page() as root_page:
    tgb.menu(
        label="Menu",
        lov=[
            ("general"),
            ("non_smoker"),
        ],
        on_action=menu_option_selected,
    )

# Page 1: General Stroke Data
with tgb.Page() as general_stroke_page:
    tgb.text("# General Stroke Data", mode="md")
    tgb.chart(figure="{fig1}")

# Page 2: Non-Smoker Stroke Data
with tgb.Page() as non_smoker_stroke_page:
    tgb.text("# Non-Smoker Stroke Patients", mode="md")
    tgb.chart(figure="{fig1}")

# Define Pages
gui = Gui()

# Add pages to the Gui
gui.add_pages({
    "general": general_stroke_page,
    "non_smoker": non_smoker_stroke_page,
    "/": root_page  
})

if __name__ == "__main__":
    gui.run(title="Simple Dashboard", use_reloader=True, dark_mode=False)
