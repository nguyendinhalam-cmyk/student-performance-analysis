import matplotlib.pyplot as plt

# 1. Histogram điểm G3
def plot_g3_distribution(df):
    plt.hist(df['G3'], bins=10)
    plt.title("Phân bố điểm cuối kỳ (G3)")
    plt.xlabel("Điểm G3")
    plt.ylabel("Số sinh viên")
    plt.show()


# 2. Biểu đồ cột: giới tính vs điểm trung bình
def plot_gender_avg_score(df):
    avg_scores = df.groupby('sex')['G3'].mean()
    avg_scores.plot(kind='bar')
    plt.title("Điểm trung bình G3 theo giới tính")
    plt.xlabel("Giới tính")
    plt.ylabel("Điểm trung bình")
    plt.show()


# 3. Boxplot điểm số
def plot_score_boxplot(df):
    plt.boxplot([df['G1'], df['G2'], df['G3']], labels=['G1', 'G2', 'G3'])
    plt.title("Phân bố điểm G1, G2, G3")
    plt.ylabel("Điểm")
    plt.show()


# 4. Scatter plot G2 vs G3
def plot_g2_g3_relation(df):
    plt.scatter(df['G2'], df['G3'])
    plt.title("Mối quan hệ giữa G2 và G3")
    plt.xlabel("G2")
    plt.ylabel("G3")
    plt.show()
