# Data utils
from data_utils import Data_Utils as du

if __name__=='__main__':
    du = du()

    train = du.read_csv('../in/Folds5x2_pp.csv')
    #du.show_head_csv(train)

    #du.draw_scatter_plot(train, 'V', 'PE')

    train['PE'] = du.log_transform(train, 'PE')
    train['RH'] = du.log_transform(train, 'RH')
    train['AP'] = du.log_transform(train, 'AP')
    train['V'] = du.log_transform(train, 'V')
    train['AT'] = du.log_transform(train, 'AT')

    du.show_head_csv(train)

    #du.target_variable_analisis(train, 'PE')

    #du.missing_data_analisis(train)

    #du.data_correlation(train)

    #du.skew_features(train)

    du.df_to_csv(train)

