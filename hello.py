from preswald import table, text, plotly, sidebar
import plotly.express as px
import pandas as pd

# 1. Enable sidebar to display logo from branding config
sidebar()

# 2. Create your in-memory dataset
df = pd.DataFrame({
    "Volunteer": ["406-0003", "406-0003", "406-0003", "406-0005", "406-0006", "406-0006"],
    "Week":      ["bsl", "wk06", "wk10", "wk10", "wk06", "wk10"],
    "group":     [0, 0, 0, 1, 1, 1],
    "Trad":      [9.0, 10.0, 9.0, 8.0, 9.0, 10.0],
    "AVG_T":     [9.0, 8.0, 10.0, 8.0, 9.0, 9.5],
    "Sed":       [6.0, 8.0, 10.0, 10.0, 7.5, 9.0],
    "AVG_S":     [9.0, 9.0, 9.0, 10.0, 8.5, 9.5]
})

# 3. Filter volunteers with AVG_T ≥ 9
filtered_df = df[df["AVG_T"] >= 9]

# 4. Build UI with text and table
text("# CyberOps Volunteer Performance Dashboard")
text("Displaying all volunteers with an average test score (AVG_T) of 9 or higher.")
table(filtered_df, title="Filtered High AVG_T Volunteers")

# 5. Create a bar chart: AVG_T by Week per Volunteer
fig = px.bar(
    filtered_df,
    x="Week",
    y="AVG_T",
    color="Volunteer",
    barmode="group",
    title="AVG_T by Week"
)
plotly(fig)