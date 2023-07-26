import pandas as pd
import plotly.graph_objects as go
from datetime import timedelta
import plotly.graph_objects as go

import webbrowser
# Read the Excel file into a DataFrame
#df = pd.read_excel("C:\\Users\\pbesser\\Downloads\\Stage gates cleaned data.xlsx")
df = pd.read_excel("C:\\Users\\mdas\\Documents\\PythonProject\\StageGateTracker\\Stage gates cleaned data.xlsx")

dft = pd.DataFrame({
    'x': pd.to_datetime(['2021-01-01','2026-07-10']),
    'y': pd.to_datetime(['2021-01-01','2026-07-12'])
})

# create data
x = pd.to_datetime(df['Proposed Sub Date '])
y = pd.to_datetime(df['Submittal Date'])
xlin = pd.to_datetime(dft['x'])
ylin = pd.to_datetime(dft['y'])

# # modify the line attribute of the trace to have a slope of 1 and an intercept of 0

# create figure
scatter_data = go.Scatter(x=y, y=x, text=df["Submittal Number"], mode='markers', marker=dict(color='#ffffff'), hovertext= df['Title'] + "<br>" + df['Submittal Number'],hovertemplate='<b>%{hovertext}</b>')

line_trace = go.Scatter(x=ylin, y=xlin, fill='tozeroy', fillcolor='rgba(128, 25, 25, 0.2)', line_color='rgba(128, 25, 25, 0.6)',  hovertemplate='')

# Calculate the width of the plot div in pixels
div_width_vw = 70  # This value should match the width set in the CSS style for #plot
div_width_px = div_width_vw * 10  # Convert vw to pixels

fig = go.Figure(data=[line_trace, scatter_data],layout=go.Layout(height=div_width_px))

fig.update_layout(
    xaxis_title="Proposed Submission Date",
    yaxis_title="Submission Date",
    template="plotly_dark",
    showlegend=False,
    xaxis=dict(range=[min(x) - timedelta(days = 10), max(x) + timedelta(days = 10)]),
    yaxis=dict(range=[min(y) -  timedelta(days = 10), max(y) + timedelta(days = 10)]),
    uirevision='graph',
)

def count_within_n_days(x, y, n):
    count = sum((x - y <= timedelta(days=n)) & (x <= y))
    return count

percentComplete = float(sum(x > y)) / float(sum(x > y) + sum(y > x))
if percentComplete > 0.6:
    msgIndex = 0
elif percentComplete > 0.3:
    msgIndex = 1
else:
    msgIndex = 2
headerMessage = ["Good Work, You're Right On Track!", "You're Almost there", "You're Behind Schedule"]
onTimeSub = "<h1>" + str(sum(x > y)) + "</h1> Submittals were made on time"
lateSub = "<h1>" + str(sum(y > x)) + "</h1> Submittals were late"
furtherSub = "You have <h1>" + str(count_within_n_days(y, x, 30)) + "</h1> submittals submitted within 30 days"
#custom html
custom_html_start = """
<!DOCTYPE html>
<html>
<head>
    <title>Stage Gate Tracker</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@200&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@40,200,0,0" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>
<script>
    $(document).ready(function(){
        console.log("through");
        window.onresize = responsiveDisp;
        if(window.innerWidth <= 1200){
            cellResponse();
            console.log("sound");
        }else{
            computerResponse();
        }
    
        function responsiveDisp(){
            if (window.innerWidth <= 850) {
                cellResponse();
            }else{
                computerResponse();
            }
        }

        function cellResponse(){
            $("#plot").css("width","96vw");
            $("#infoPanel").css({"top":"800px","left":"2vw","width":"96vw","font-size":"20px"});
            $("h1").css("font-size","30px");
            $("#headerText").css("font-size","7vw");
        }

        function computerResponse(){
            $("#plot").css("width","65vw");
            $("#infoPanel").css({"top":"11vw","left":"65vw","width":"30vw","font-size":"0.9vw"});
            $("h1").css("font-size","1.5vw");
            $("#headerText").css("font-size","3.2vw");
        }
    });
</script>
<style>
    h1{
        display: inline;
        font-size: 1.5vw;
    }
    body{
        background-color: #111111;
        color: white;
        font-family: 'DM Sans', sans-serif;
        letter-spacing: .07vw;
    }

    #plot{
        position: absolute;
        top: 5.5vw;
        left: 2vw;
        width: 65vw;
        min-width: 
        height: 70vh;
        border-radius: 3vw;
        overflow: hidden;
    }

    @keyframes fadeAndMove {
        0% {
            opacity: 0;
            transform: translateY(-1vw); /* Move up 10vw */
        }
        100% {
            opacity: 1;
            transform: translateY(0); /* Move down to original position */
        }
    }

    #headerText{
        position: absolute;
        top: 3vw;
        left: 4vw;
        text-align: left; 
        font-size: 3.2vw;
        z-index: 2;
        opacity: 0; /* Start with opacity 0 */
        animation: fadeAndMove 0.75s forwards;
    }

    #infoPanel{
        position: absolute;
        top: 11vw;
        left: 65vw;
        width: 30vw;
        font-size: 0.9vw;
        min-font-size: 25px;
        line-height: 2.5vw;
        display: flex; 
        align-items: top;
        z-index: 2;
    }
    #lateholder{
        position: absolute;
        top: 7vw;
        left: 60vw;
        width: 30vw;
        background: red;
    }

    #text{
        line-height: 40px;
    }
    
    .scatterlayer path.point {
        cursor: pointer;
    }

    #test{
        position: absolute;
        width: 35vw;
        left: 60%;
        height: 20vw;
        background-color: blue;
    }
</style>
<body>

<div id = "headerText">
    """ + headerMessage[msgIndex] + """
</div>
<div id = "lateholder">
</div>
<div id = "infoPanel">
    <div id = "icons" style="flex: 0.2;text-align: center;padding-top:0.1vw;line-height: 45px;">
        <span class="material-symbols-outlined" style = "color:#00d100;">done_all</span><br>
        <span class="material-symbols-outlined" style = "color:#e80000;">clock_loader_90</span><br>
        <span class="material-symbols-outlined" style = "color:#e8e800;">warning</span>
    </div>
    <div id = "text" style="flex: 2;">
        """ + onTimeSub + """<br>
        """ + lateSub + """<br>
        """ + furtherSub + """
    </div>
</div>
<div id="plot">
    <!-- Plotly chart will be inserted here -->
"""

custom_html_end = """
</div>

</body>
</html>
"""

#pio.write_html(fig, file="StageGateTracker.html", auto_open=True, include_plotlyjs=False, config={"displayModeBar": False, "scrollZoom": False})
filename = "C:\\Users\\mdas\\Documents\\PythonProject\\StageGateTracker\\StageGateTracker.html"  # Modify the filename as needed
#filename = "C:\\Users\\pbesser\\Downloads\\StageGateTracker.html"
with open(filename, "w", encoding="utf-8") as file:
    file.write(custom_html_start)
    file.write(fig.to_html(full_html=False, include_plotlyjs=True))
    file.write(custom_html_end)

# Open the HTML file in a web browser
webbrowser.open_new_tab(filename)
