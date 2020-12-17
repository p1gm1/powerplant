# Numpy
import numpy as np

# Pandas
import pandas as pd 

# Matplotlib
import matplotlib.pyplot as plt

# Seaborn
import seaborn as sns

# Scipy
from scipy import stats
from scipy.stats import norm, skew

class Data_Utils:
    """Handles utilities for
    cleaning data.
    """

    def read_csv(self, csv_path):
        """Read a csv file as dataframe"""
        return pd.read_csv(csv_path)

    def show_head_csv(self, df):
        """Show the first five rows
        of a dataframe.
        """
        print(f"The dataframe size is : {df.shape}")
        print(df.head(5))

    def draw_scatter_plot(self, df, col1, col2):
        """Draw on matplotlib a scatter_plot"""
        fig, ax = plt.subplots()
        ax.scatter(x = df[col1], y = df[col2])
        plt.ylabel(col2, fontsize=13)
        plt.xlabel(col1, fontsize=13)
        plt.show()

    def target_variable_analisis(self, df, col_t):
        """Plot target variable."""
        sns.distplot(df[col_t] , fit=norm)

        # Get the fitted parameters used by the function
        (mu, sigma) = norm.fit(df[col_t])
        print( '\n mu = {:.2f} and sigma = {:.2f}\n'.format(mu, sigma))

        #Now plot the distribution
        plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(mu, sigma)],
                    loc='best')
        plt.ylabel('Frequency')
        plt.title(col_t+' distribution')

        #Get also the QQ-plot
        fig = plt.figure()
        res = stats.probplot(df[col_t], plot=plt)
        plt.show()

    def log_transform(self, df, col):
        """Log_transform of a feature"""
        #We use the numpy fuction log1p which  applies log(1+x) to all elements of the column
        return np.log1p(df[col])

    def missing_data_analisis(self, df):
        """Analisis of missing data if any"""
        df_na = (df.isnull().sum() / len(df)) * 100
        df_na = df_na.drop(df_na[df_na == 0].index).sort_values(ascending=False)[:30]
        missing_data = pd.DataFrame({'Missing Ratio' :df_na})
        print(missing_data.head(20))

    def data_correlation(self, df):
        """Plot in a heatmap the data correlation"""
        corrmat = df.corr()
        plt.subplots(figsize=(12,9))
        sns.heatmap(corrmat, vmax=0.9, square=True)
        plt.show()

    def skew_features(self, df):
        """Check the skew of all numerical features"""
        skewed_feats = df.apply(lambda x: skew(x)).sort_values(ascending=False)
        print("\nSkew in numerical features: \n")
        skewness = pd.DataFrame({'Skew' :skewed_feats})
        print(skewness.head(10))

    def df_to_csv(self, df):
        """Send a df to a csv"""
        
        df.to_csv('../in/clean_dataset.csv',index=False)


    

    

    
