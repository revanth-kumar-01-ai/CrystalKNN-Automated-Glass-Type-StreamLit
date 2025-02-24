import pandas as pd
import joblib

try:
    preprocess_transformation_Pipeline = joblib.load('./models/preprocess_transformation_pipe')
    preprocess_pipeline = joblib.load('./models/preprocess_scaleTransform')
except Exception as e:
    print(e)

def DataPreProcessing(df):
    
    if preprocess_transformation_Pipeline:
        df[['Ca', 'Mg']] = preprocess_transformation_Pipeline.transform(df[['Ca', 'Mg']])

    if preprocess_pipeline:
        transformed_df = pd.DataFrame(preprocess_pipeline.transform(df), columns=preprocess_pipeline.get_feature_names_out())
   
    return transformed_df

