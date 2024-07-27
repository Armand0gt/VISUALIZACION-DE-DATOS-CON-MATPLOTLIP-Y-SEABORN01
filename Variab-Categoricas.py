import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
tips.head(2)


sns.countplot(data=tips,x="day",hue="sex")
plt.show()


sns.countplot(data=tips,y="day",hue="sex")
plt.show()

sns.stripplot(data=tips,x="day",y="total_bill",hue="sex")
plt.show()

sns.stripplot(data=tips,x="day",y="total_bill",hue="sex", dodge=True)
plt.show()

plt.figure(figsize=(6,6))
sns.stripplot(data=tips,x="day",y="total_bill",hue="sex", dodge=True)
plt.show()


plt.figure(figsize=(6,6))
sns.swarmplot(data=tips,x="day",y="total_bill",hue="sex", dodge=True)
plt.show()

#Boxplot
plt.figure(figsize=(6,6))
sns.boxplot(data=tips,x="day",y="total_bill",hue="sex", dodge=True)
plt.show()


plt.figure(figsize=(6,6))
sns.boxplot(data=tips,x="day",y="total_bill",hue="sex", dodge=True)
sns.swarmplot(data=tips,x="day",y="total_bill",hue="sex", dodge=True,color="0",marker= "<")
plt.show()

plt.figure(figsize=(6,6))
sns.violinplot(data=tips,x="day",y="total_bill",hue="sex", dodge=True, color="green")
plt.show()


plt.figure(figsize=(6,6))
sns.violinplot(data=tips,x="day",y="total_bill",hue="sex", split=True, palette="pastel")
plt.show()

plt.figure(figsize=(6,6))
sns.violinplot(data=tips,y="total_bill")
plt.show

sns.catplot(data=tips,x="day",y="total_bill",hue="sex", dodge=True, kind="box", col="time")
plt.show()