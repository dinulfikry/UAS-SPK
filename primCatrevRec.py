dims = (10, 8)
fig, ax = plt.subplots(figsize=dims)
ax = sns.countplot(x="primaryCategories",hue="reviewsRecommend", data=rating)