import tkinter as tk
from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.data_normalization import normalize_scores
from src.visualization import *

def load_and_clean():
    global df
    df = load_data("student_data.csv")
    df = clean_data(df)
    df = normalize_scores(df)

def show_hist():
    plot_g3_distribution(df)

def show_bar():
    plot_gender_avg_score(df)

def show_box():
    plot_score_boxplot(df)

def show_scatter():
    plot_g2_g3_relation(df)

app = tk.Tk()
app.title("Student Performance Analysis")
app.geometry("350x300")

btn_load = tk.Button(app, text="Load & Clean Data", command=load_and_clean)
btn_load.pack(pady=5)

btn_hist = tk.Button(app, text="Histogram G3", command=show_hist)
btn_hist.pack(pady=5)

btn_bar = tk.Button(app, text="Bar Chart Gender", command=show_bar)
btn_bar.pack(pady=5)

btn_box = tk.Button(app, text="Boxplot Scores", command=show_box)
btn_box.pack(pady=5)

btn_scatter = tk.Button(app, text="Scatter G2 vs G3", command=show_scatter)
btn_scatter.pack(pady=5)

app.mainloop()