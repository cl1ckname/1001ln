import pandas as pd
from sklearn.tree import DecisionTreeRegressor
dino_data = pd.read_csv('./static/db.csv')
features = ['firstq','secondq','thirdq']
X = dino_data[features]
y = dino_data.answe

model = DecisionTreeRegressor(random_state=1)
model.fit(X,y)

def solve(f,s,t):
    return model.predict([(f,s,t)])