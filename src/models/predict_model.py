import pickle
import os
import src.data.make_dataset as data
import streamlit as st
from sklearn.metrics import (plot_confusion_matrix,
                             plot_precision_recall_curve, plot_roc_curve,
                             precision_score, recall_score)
from src.features.build_features import Encode
from src.shared.config import loadConfig

from .algo.logistic_regression import LogisticRegressionModel
from .algo.svm import SupportVectorMachineModel

# from pandas_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report


st.set_option('deprecation.showPyplotGlobalUse', False)


def Predict():
    config = loadConfig()
    st.sidebar.title(config['contents']['heading'])
    st.markdown(config['contents']['sub-heading'])
    class_names = ['Negative', 'Positive']
    roundOff = 6        

    def plot_metrics(metrics_list):
        """[summary]

        Args:
            metrics_list ([type]): [description]
        """
        if 'Confusion Matrix' in metrics_list:
            st.subheader("Confusion Matrix")
            plot_confusion_matrix(
                model, df['X'], df['Y'], display_labels=class_names)
            st.pyplot()

        if 'ROC Curve' in metrics_list:
            st.subheader("ROC Curve")
            plot_roc_curve(model, df['X'], df['Y'])
            st.pyplot()

        if 'Precision-Recall Curve' in metrics_list:
            st.subheader('Precision-Recall Curve')
            plot_precision_recall_curve(model, df['X'], df['Y'])
            st.pyplot()

    @st.cache(persist=True)
    def load_data():
        df = data.make_datasets('test-dataset-path')
        encode = Encode()
        df['X'] = encode.encodeColumns(df['X'])
        return df

    df = load_data()
    if st.sidebar.checkbox("Show data", False):
        st.subheader(config['contents']['sub-heading2'])
        st.write(df['X'])
        st.markdown(config['contents']['dataset-desc'])

    # if st.sidebar.checkbox("Profile data", False):
    #     pr = ProfileReport(df['X'], explorative=False)
    #     st.title("Pandas Profiling in Streamlit")
    #     st.write(df['X'])
    #     st_profile_report(pr)

    st.sidebar.subheader("Choose Classifier")
    classifier = st.sidebar.selectbox(
        "Classifier", ("Support Vector Machine (SVM)", "Logistic Regression"))

    if classifier == 'Logistic Regression':
        metrics = st.sidebar.multiselect(
            "What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'))

        if st.sidebar.button("Classify", key='classify'):
            st.subheader("Logistic Regression Results")
            model = pickle.load(
                open(os.getcwd() + config['data']['save-model'] + '/LogisticRegression.pkl', 'rb'))
            accuracy = model.score(df['X'], df['Y'])
            y_pred = model.predict(df['X'])
            st.write("Accuracy: ", accuracy.round(roundOff))
            st.write("Precision: ", precision_score(
                df['Y'], y_pred, labels=class_names).round(roundOff))
            st.write("Recall: ", recall_score(
                df['Y'], y_pred, labels=class_names).round(roundOff))
            plot_metrics(metrics)

    if classifier == 'Support Vector Machine (SVM)':
        metrics = st.sidebar.multiselect(
            "What metrics to plot??", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'))

        if st.sidebar.button("Classify", key='classify'):
            st.subheader("Support Vector Machine Results")
            model = pickle.load(
                open(os.getcwd() + config['data']['save-model'] + '/SupportVectorMachine.pkl', 'rb'))
            accuracy = model.score(df['X'], df['Y'])
            y_pred = model.predict(df['X'])
            st.write("Accuracy: ", accuracy.round(roundOff))
            st.write("Precision: ", precision_score(
                df['Y'], y_pred, labels=class_names).round(roundOff))
            st.write("Recall: ", recall_score(
                df['Y'], y_pred, labels=class_names).round(roundOff))
            plot_metrics(metrics)

# def Predict():
#     Predictor()
