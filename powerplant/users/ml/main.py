# Utils
from utils import Utils

# Models
from models import Models


if __name__=='__main__':
    utils = Utils()
    models = Models()
    
    data = utils.load_from_csv('./in/clean_dataset.csv')
    
    X, y = utils.features_target(data, ['AT', 'V', 'AP', 'RH'], ['PE'])
    models.grid_training(X,y)