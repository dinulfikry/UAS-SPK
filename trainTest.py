reader = Reader()
data = Dataset.load_from_df(rating[['reviews.username','id','reviewsRating']], reader)

# Train & Test
trainset, testset = train_test_split(data, test_size=0.20, random_state=50)