# Stage Gate Tracker

The Stage Gate Tracker is a Python script that reads submittal data from an Excel file and creates a plot to visualize the due date against the actual submission date. The script highlights the area where the points represent late submissions in red.

## Prerequisites

Before running the script, make sure you have the following installed on your machine:

- Python (3.11.4 & up recommended)
- `pandas` library
- `plotly.graph_objects` library
- `webbrowser` library

You can install the required libraries using pip:

```bash
pip install pandas plotly webbrowser
```

## Installation

1. Clone this repository to your local machine using Git or download the ZIP file.
```bash
cd StageGateTracker
```
## Usage

1. Place the Excel file containing the submittal data in the same directory as the script.

2. Open the `script.py` file in a text editor or an Integrated Development Environment (IDE).

3. Modify the file path to the Excel file & generated HTML file (if needed) by changing the value of `filename` variable and the `df` variable:

```python
df = pd.read_excel("path/to/your/Stage gates cleaned data.xlsx")
filename = "path/to/your/StageGateTracker.html"
```
4. Run the script:

```python
python stageGateTracker.py
```

## Output

The script will generate an HTML file named `StageGateTracker.html` that visualizes the submittal data. The plot displays the due date against the actual submission date, with late submissions highlighted in red.

![](https://github.com/Sadkoi/Stage-Gate_Tracker/blob/main/SGTPreview.PNG)
