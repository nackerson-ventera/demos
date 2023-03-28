# Predictive Lean Analytics on Google Analytics Datasets

**If you only need to pull data from GA Data API just focus on step 1 below. The rest of this Readme focuses on predictive lean analytics implementations:**

1. **Export Google Analytics data:** First, you need to export your Google Analytics data. You can use the[Google Analytics Reporting API](https://developers.google.com/analytics/devguides/reporting/core/v4) to fetch data, such as user sessions, page views, time on site, and other relevant metrics. Alternatively, you can use a tool like[Google Analytics Spreadsheet Add-on](https://developers.google.com/analytics/solutions/google-analytics-spreadsheet-add-on) to export the data to a spreadsheet.

    _Prerequisites:_

    1. Create a project in Google Cloud Platform.
    2. Ensure that you have a service account key that has access to the Google Analytics account you want to retrieve data from.
    3. Clone or download the repository and install any necessary dependencies.
    4. In the project, add the service account key as a JSON file and ensure that it is included in the code. 
    5. Use the provided functions in the library to retrieve data from the Google Analytics API.

2. **Preprocess the data:** Once you have the data, preprocess it by cleaning, transforming, and encoding categorical features. For example, you can one-hot encode categorical variables like browser or device type, normalize numerical features, and fill missing values. 70-30 or 80-20 split depending on the amount.
3. **Feature engineering:** Create additional features that may help the model make better predictions. For example, you can create features like the average time spent on the website, the number of pages visited, or the bounce rate. Additionally, you can use domain-specific knowledge to create more relevant features.

    _Features to consider:_

    1. _Pageviews_
    2. _Time on site_
    3. _Bounce rate_
    4. _User's device (desktop, mobile etc)_
    5. _Browser_
    6. _Geographic location_
    7. _Referral source_
4. **Model selection:** More than likely XGBoost however LR, Decision Trees/Random Forests, SVM, CNN/RNN/MLP NNs are options as well depending on our goals.
5. **Label the data:** You need to label your data based on whether users completed the task or not. You can use goals or events in Google Analytics to identify users who have completed the task, and label them as 1 (positive), while users who didn't complete the task can be labeled as 0 (negative).
6. **With event or goal tracking being collected:** We get our target variables (labels)
7. **Build a TF model:** Create a binary classification model using TensorFlow. You can start with a simple feedforward neural network or experiment with more complex architectures like LSTM or Transformer models. For example, you could use a Keras Sequential model with several dense layers.
8. **Train and eval the model:** Train the model using your training data, and then evaluate its performance on the test set. Adjust the model's architecture or hyperparameters if necessary to improve its performance.
9. **Deploy the model:** Once you're satisfied with the model's performance, you can deploy it to a web server to make predictions on new data.

With this setup, you can use the trained TensorFlow model to predict which groups of users are likely to complete the task on your website and which are not. Remember, though, that the performance of your model will depend on the quality and relevance of the input features you choose. You might need to experiment with different features and model architectures to achieve the best results.