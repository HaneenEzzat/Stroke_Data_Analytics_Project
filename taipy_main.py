import taipy as tp
import taipy.gui.builder as tgb
from taipy.gui import Gui, Icon, navigate
import plotly.graph_objs as go
import pandas as pd
import sqlite3

# Load Data
connection = sqlite3.connect("enriche_data.db")
query = "SELECT * FROM clean_stroke"
df = pd.read_sql(query, connection)

# Figures for General Stroke Data
fig1 = go.Figure()
for status in df['smoking_status'].unique():
    subset = df[(df['smoking_status'] == status) & (df['stroke'] == 'Yes')]
    count = len(subset)
    fig1.add_trace(go.Bar(x=[status], y=[count], name=status, text=[count], textposition='outside'))
fig1.update_layout(title="Stroke Cases by Smoking Status", xaxis_title="Smoking Status", yaxis_title="Stroke Count", template="plotly_white")

# Figures for Non-Smoker Stroke Patients
never_smoked_stroke_df = df[(df['smoking_status'] == 'never smoked') & (df['stroke'] == 'Yes')]
work_type_count = never_smoked_stroke_df['work_type'].value_counts()
fig_non_smokers = go.Figure(data=[go.Bar(x=work_type_count.index, y=work_type_count.values, text=work_type_count.values, textposition='outside')])
fig_non_smokers.update_layout(title="Work Type Distribution for Non-Smokers with Stroke", xaxis_title="Work Type", yaxis_title="Count", template="plotly_white")

# Function to handle menu navigation
def menu_option_selected(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

# Root Page (Navigation Menu)
with tgb.Page() as root_page:
    tgb.menu(
        label="Menu",
        lov=[
            ("general", Icon("images/stroke.png", "General Stroke Data")),
            ("non_smoker", Icon("images/no_smoke.png", "Non-Smoker Stroke Data")),
        ],
        on_action=menu_option_selected,
    )

# Page 1: General Stroke Data
with tgb.Page() as general_stroke_page:
    tgb.text("# General Stroke Data", mode="md")

    tgb.html("br")  # Adds spacing

    # Row 1
    with tgb.layout(columns="2 3"):
        tgb.chart(figure="{fig1}")
        tgb.chart(figure="{fig6}")

    tgb.html("br")

    # Row 2
    with tgb.layout(columns="2 3"):
        tgb.chart(figure="{fig7}")
        tgb.chart(figure="{fig8}")

    tgb.html("br")

    # Row 3
    with tgb.layout(columns="2 3"):
        tgb.chart(figure="{fig9}")
        tgb.chart(figure="{fig10}")

    tgb.html("br")

    # Row 4
    with tgb.layout(columns="2 3"):
        tgb.chart(figure="{fig11}")
        tgb.chart(figure="{fig12}")

    tgb.html("br")

    # Row 5
    with tgb.layout(columns="2 3"):
        tgb.chart(figure="{fig13}")
        tgb.chart(figure="{fig14}")

    tgb.html("br")



# Page 2: Non-Smoker Stroke Data
with tgb.Page() as non_smoker_stroke_page:
    tgb.text("# Non-Smoker Stroke Patients", mode="md")
    tgb.chart(figure="{fig6}")
    tgb.chart(figure="{fig6}")
    tgb.chart(figure="{fig6}")
    tgb.chart(figure="{fig6}")
# Define Pages
pages = {
    "/": root_page,
    "general": general_stroke_page,
    "non_smoker": non_smoker_stroke_page,
}

# Run GUI
if __name__ == "__main__":
    gui=tp.Gui(pages)
    gui.run(title='Brain Stroke Analysis Dashboard', use_reloader=True)
    