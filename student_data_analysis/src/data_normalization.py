from sklearn.preprocessing import MinMaxScaler

def normalize_scores(df):
    scaler = MinMaxScaler()
    df[['G1', 'G2', 'G3']] = scaler.fit_transform(df[['G1', 'G2', 'G3']])
    return df