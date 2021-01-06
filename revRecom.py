# Lakukan kembali me-rename kolom jadi reviewsRecommend
rating.rename(columns={"reviews.doRecommend":"reviewsRecommend"},inplace=True)

# Cari nilai dari kolom
rev_rec = rating['reviewsRecommend'].value_counts()
rev_rec

# Visualisasikan dari hasil nilai
dims = (10, 8)
fig, ax = plt.subplots(figsize=dims)
ax = sns.countplot(x="reviewsRecommend", data=rating)