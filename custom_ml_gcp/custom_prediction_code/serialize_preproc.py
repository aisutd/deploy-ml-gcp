# import dependencies
import pickle

from preprocess import Preprocessor

def main():
    # initialize preprocessor
    preprocessor = Preprocessor()        

    # serialize preprocessor
    with open('preprocessor.pkl', 'wb') as f:
            pickle.dump(preprocessor, f)

if __name__ == '__main__':
    main()
