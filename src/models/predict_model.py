
import configparser
import os
import pickle

import src.data.make_dataset as data
import streamlit as st
from sklearn.metrics import (plot_confusion_matrix,
                             plot_precision_recall_curve, plot_roc_curve,
                             precision_score, recall_score)
from src.features.build_features import Encode

from .algo.logistic_regression import LogisticRegressionModel

st.set_option('deprecation.showPyplotGlobalUse', False)



class Predict:

    def __init__(self):
        """[summary]
        """
        self.config = configparser.ConfigParser()
        self.config.read(os.getcwd() + '/tox.ini')
        self.model_path = self.config['data']['save-model'] + \
            'LogisticRegression.pkl'
        st.title(self.config['contents']['heading'])
        st.sidebar.title(self.config['contents']['heading'])
        st.markdown(self.config['contents']['sub-heading'])
        self.class_names = ['Negative', 'Positive']

    def plot_metrics(self, metrics_list):
        """[summary]

        Args:
            metrics_list ([type]): [description]
        """
        if 'Confusion Matrix' in metrics_list:
            st.subheader("Confusion Matrix")
            plot_confusion_matrix(self.model, self.df['X'], self.df['Y'], display_labels=self.class_names)
            st.pyplot()

        if 'ROC Curve' in metrics_list:
            st.subheader("ROC Curve")
            plot_roc_curve(self.model, self.df['X'], self.df['Y'])
            st.pyplot()

        if 'Precision-Recall Curve' in metrics_list:
            st.subheader('Precision-Recall Curve')
            plot_precision_recall_curve(self.model, self.df['X'], self.df['Y'])
            st.pyplot()

    @st.cache(persist=True)
    def load_data(self):
        df = data.make_datasets()
        encode = Encode()
        df['X'] = encode.encodeColumns(df['X'])
        return df

    def predictModel(self):
        """[to predict the model]
        """
        self.df = self.load_data()
        if st.sidebar.checkbox("Show data", False):
            st.subheader("Heart Disease Data Set (Classification)")
            st.write(self.df['X'])
            st.markdown(self.config['contents']['dataset-desc'])

        st.sidebar.subheader("Choose Classifier")
        classifier = st.sidebar.selectbox(
            "Classifier", ("Support Vector Machine (SVM)", "Logistic Regression"))

        if classifier == 'Logistic Regression':
            st.sidebar.subheader("Model Hyperparameters")
            metrics = st.sidebar.multiselect(
                "What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'))

            if st.sidebar.button("Classify", key='classify'):
                st.subheader("Logistic Regression Results")
                self.model = pickle.load(open(self.model_path, 'rb'))
                accuracy = self.model.score(self.df['X'], self.df['Y'])
                y_pred = self.model.predict(self.df['X'])
                st.write("Accuracy: ", accuracy.round(2))
                st.write("Precision: ", precision_score(
                    self.df['Y'], y_pred, labels=self.class_names).round(2))
                st.write("Recall: ", recall_score(
                    self.df['Y'], y_pred, labels=self.class_names).round(2))
                self.plot_metrics(metrics)
