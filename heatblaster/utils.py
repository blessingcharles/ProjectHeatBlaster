import matplotlib.pyplot as plt

def plot_feature_distribution(features):
    
    print('Properties of feature: ' + features.name)
    print(features.describe())
    f, ax = plt.subplots(1, figsize=(10, 6))
    ax.hist(features, bins=100)
    ax.set_xlabel('value')
    ax.set_ylabel('fraction')
    
    plt.show()    