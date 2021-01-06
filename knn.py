sim_options = {'name': 'pearson_baseline','shrinkage': 0}
algo = KNNBasic(sim_options=sim_options)
algo_knn = KNNBasic(k=50, sim_options=sim_options)
prediction_knn = algo_knn.fit(trainset).test(testset)

# Prediksi
prediction_knn