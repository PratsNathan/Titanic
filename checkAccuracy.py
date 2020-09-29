import pandas as pd

test = pd.read_csv('test.csv')
solution = pd.read_csv('solution.csv')
predictions = pd.read_csv('submission.csv')

test = pd.merge(test, solution, on = 'Name')
df = pd.merge(test, predictions, on = 'PassengerId')

df['Sum'] = df['Survived_x']+df['Survived_y']
df.loc[df['Sum'] == 0, 'Points'] = 1
df.loc[df['Sum'] == 2, 'Points'] = 1
df.loc[df['Sum'] == 1, 'Points'] = 0

score = df['Points'].sum()
numberOfRows = df['Points'].count()
accuracy = score/numberOfRows

print(accuracy)