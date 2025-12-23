from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.data_normalization import normalize_scores
from src.visualization import *

def main():
    df = load_data("data/student_performance.csv")
    df = clean_data(df)
    df = normalize_scores(df)

    plot_g3_distribution(df)
    plot_gender_avg_score(df)
    plot_score_boxplot(df)
    plot_g2_g3_relation(df)

if __name__ == "__main__":
    main()