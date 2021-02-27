import pickle

import src.data.make_dataset as data
import streamlit as st
from pandas_profiling import ProfileReport
from sklearn.metrics import (plot_confusion_matrix,
                             plot_precision_recall_curve, plot_roc_curve,
                             precision_score, recall_score)
from src.features.build_features import Encode
from src.shared.config import loadConfig
from streamlit_pandas_profiling import st_profile_report

from .algo.logistic_regression import LogisticRegressionModel
from .algo.svm import SupportVectorMachineModel

st.set_option('deprecation.showPyplotGlobalUse', False)


class Predict:

    def __init__(self):
        """[summary]
        """
        self.config = loadConfig()
        st.title(self.config['contents']['heading'])
        st.sidebar.title(self.config['contents']['heading'])
        st.markdown(self.config['contents']['sub-heading'])
        self.class_names = ['Negative', 'Positive']
        self.roundOff = 6

    def plot_metrics(self, metrics_list):
        """[summary]

        Args:
            metrics_list ([type]): [description]
        """
        if 'Confusion Matrix' in metrics_list:
            st.subheader("Confusion Matrix")
            plot_confusion_matrix(
                self.model, self.df['X'], self.df['Y'], display_labels=self.class_names)
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
        df = data.make_datasets('test-dataset-path')
        encode = Encode()
        df['X'] = encode.encodeColumns(df['X'])
        return df

    def predictModel(self):
        """[to predict the model]
        """
        self.df = self.load_data()
        if st.sidebar.checkbox("Show data", False):
            st.subheader(self.config['contents']['sub-heading2'])
            st.write(self.df['X'])
            st.markdown(self.config['contents']['dataset-desc'])

        # if st.sidebar.checkbox("Profile data", False):
        #     pr = ProfileReport(self.df['X'], explorative=False)
        #     st.title("Pandas Profiling in Streamlit")
        #     st.write(self.df['X'])
        #     st_profile_report(pr)

        st.sidebar.subheader("Choose Classifier")
        classifier = st.sidebar.selectbox(
            "Classifier", ("Support Vector Machine (SVM)", "Logistic Regression"))

        if classifier == 'Logistic Regression':
            metrics = st.sidebar.multiselect(
                "What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'))

            if st.sidebar.button("Classify", key='classify'):
                st.subheader("Logistic Regression Results")
                self.model = pickle.load(
                    open(self.config['data']['save-model'] + '/LogisticRegression.pkl', 'rb'))
                accuracy = self.model.score(self.df['X'], self.df['Y'])
                y_pred = self.model.predict(self.df['X'])
                st.write("Accuracy: ", accuracy.round(self.roundOff))
                st.write("Precision: ", precision_score(
                    self.df['Y'], y_pred, labels=self.class_names).round(self.roundOff))
                st.write("Recall: ", recall_score(
                    self.df['Y'], y_pred, labels=self.class_names).round(self.roundOff))
                self.plot_metrics(metrics)

        if classifier == 'Support Vector Machine (SVM)':
            metrics = st.sidebar.multiselect(
                "What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'))

            if st.sidebar.button("Classify", key='classify'):
                st.subheader("Support Vector Machine Results")
                self.model = pickle.load(
                    open(self.config['data']['save-model'] + '/SupportVectorMachine.pkl', 'rb'))
                accuracy = self.model.score(self.df['X'], self.df['Y'])
                y_pred = self.model.predict(self.df['X'])
                st.write("Accuracy: ", accuracy.round(self.roundOff))
                st.write("Precision: ", precision_score(
                    self.df['Y'], y_pred, labels=self.class_names).round(self.roundOff))
                st.write("Recall: ", recall_score(
                    self.df['Y'], y_pred, labels=self.class_names).round(self.roundOff))
                self.plot_metrics(metrics)
