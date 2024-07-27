import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(x=["A","B","C"], y=[1,2,3])
plt.show()

sns.set(style= "ticks", palette="dark", font="Verdana", font_scale=1)
sns.barplot(x=["A","B","C"], y=[1,2,3])
plt.show()