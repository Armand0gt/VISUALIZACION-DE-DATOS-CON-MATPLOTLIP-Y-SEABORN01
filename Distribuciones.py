import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
tips
tips.head

sns.histplot(data=tips, x="tip")
plt.show()

sns.histplot(data=tips, x="tip", cumulative=False,hue="sex")
plt.show()

sns.histplot(data=tips, x="tip", cumulative=False,hue="sex", stat="frequency")
plt.show()

sns.histplot(data=tips, x="tip", cumulative=False,hue="sex", stat="probability")
plt.show()

sns.histplot(data=tips, x="tip", cumulative=False,hue="sex", stat="percent")
plt.show()

sns.histplot(data=tips, x="tip", cumulative=False,hue="sex", stat="density")
plt.show()


sns.histplot(data=tips, x="tip", cumulative=False,hue="sex", stat="count", multiple="layer")
plt.show()


sns.kdeplot(data=tips, x="tip",hue="sex", shade=True)
plt.show()

sns.ecdfplot(data=tips, x="tip",hue="sex", stat="percent")
plt.show()


sns.displot(data=tips, x="tip",hue="sex", kind="hist", multiple= "stack")
plt.show()