# Gunakan fungsi svd() yang sudah disediakan pada surprise
algo_svd = SVD()
prediction_mf = algo_svd.fit(trainset).test(testset)

# Prediksi
prediction_mf