dims = (10, 8)
fig, ax = plt.subplots(figsize=dims)
ax = sns.boxplot(x="reviewsRating", y="primaryCategories", hue="reviewsRecommend", data=rating)