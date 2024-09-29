import pandas as pd, plotly.express as px, umap

from pathlib import Path
from sklearn.datasets import load_breast_cancer
#|%%--%%| <oY19PTkA5E|8C9r88WE4J>

data, meta_data = load_breast_cancer(return_X_y = True, as_frame = True)

data.columns

#|%%--%%| <8C9r88WE4J|m2Y7QcY6OD>

meta_data

#|%%--%%| <m2Y7QcY6OD|mGe34s0GDH>

meta_data = pd.DataFrame(meta_data)
#Let's add another bit of metadata just for the heck of it.
meta_data['big_radius'] = data['mean radius'] > data['mean radius'].mean()

#|%%--%%| <mGe34s0GDH|eY6JJ8QnVA>

reducer_2d = umap.UMAP(n_components = 2)
results_2d = pd.DataFrame(data = reducer_2d.fit_transform(data), columns = ['2d1','2d2'])

# Let's do it all at once, because we can
results_3d = pd.DataFrame(data = umap.UMAP(n_components = 3).fit_transform(data), columns = ['3d1','3d2','3d3'])

# WWCA means "What We Care About"
wwca = meta_data.join(results_2d).join(results_3d)
wwca

#|%%--%%| <eY6JJ8QnVA|RC2Z0gahgY>
r"""°°°
# Initial plotting with plotly
°°°"""
#|%%--%%| <RC2Z0gahgY|0foch0zS43>

fig = px.scatter(wwca, x='2d1',y='2d1')
fig.show()

#|%%--%%| <0foch0zS43|4U3G93u08T>
r"""°°°
# Clean up the label to something people like
°°°"""
#|%%--%%| <4U3G93u08T|LI20dW1L0N>

new_data['text label'] = labels.map(lambda x: ['Benign','Malignant'][x])
new_data

#|%%--%%| <LI20dW1L0N|5sSbn2D9QS>

new_data

