import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
tips.corr(numeric_only=True)
sns.heatmap(tips.corr(numeric_only=True), annot=True, cmap="coolwarm", linewidths=4, linecolor="black", vmin=0.5, vmax=1)
plt.show()

sns.heatmap(tips.corr(numeric_only=True), annot=True, cmap="coolwarm", linecolor="black", vmin=0.5, vmax=1)
plt.show()

