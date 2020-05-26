import pandas as pd
from sklearn.tree import DecisionTreeRegressor
dino_data = pd.read_csv('./static/db.csv')
features = ['firstq','secondq','thirdq','fourthq','fifthq','sixthq']
X = dino_data[features]
y = dino_data.answer

model = DecisionTreeRegressor(random_state=1)
model.fit(X,y)

def solve(f,s,t,fr,fv,sx):
    return model.predict([(f,s,t,fr,fv,sx)])