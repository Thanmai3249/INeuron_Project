# INeuron_Project
Implemented Supervised and Unsupervised Machine Learning Algorithms with Regularization Techniques, HyperParameter Tuning and Evaluation Metrics.

# Supervised Machine Learning Algorithms

## Linear Regression

Linear Regression is a machine learning algorithm based on supervised learning. It performs a regression task. Regression models a target prediction value based on independent variables. It is mostly used for finding out the relationship between variables and forecasting. Different regression models differ based on – the kind of relationship between dependent and independent variables they are considering, and the number of independent variables getting used.

![image](https://user-images.githubusercontent.com/102719065/200178503-4e71060f-086e-4745-ba54-908ded3a9c9b.png)

![image](https://user-images.githubusercontent.com/102719065/200178588-21d929bf-68e4-4ce6-b8d1-0d2065d60b38.png)

## Support Vector Regrssion

Support Vector Machines (SVMs) are well known in classification problems. The use of SVMs in regression is not as well documented, however. These types of models are known as Support Vector Regression (SVR).
SVR gives us the flexibility to define how much error is acceptable in our model and will find an appropriate line (or hyperplane in higher dimensions) to fit the data.

Minimize: ![image](https://user-images.githubusercontent.com/102719065/200178838-62fb8286-51dc-4d86-bb91-5a763fb2c0ac.png)

Constraints: ![image](https://user-images.githubusercontent.com/102719065/200178844-5d7953ab-8e07-474b-a27d-195af7874202.png)

![image](https://user-images.githubusercontent.com/102719065/200178877-b3eea5f0-653e-4797-a562-9d47af3c7779.png)

The concept of slack variables is simple: for any value that falls outside of ϵ, we can denote its deviation from the margin as ξ.
We know that these deviations have the potential to exist, but we would still like to minimize them as much as possible. Thus, we can add these deviations to the objective function.

Minimize: ![image](https://user-images.githubusercontent.com/102719065/200178976-666a10ba-a5ab-49d4-a06e-c43e18a4db83.png)

Constraints: ![image](https://user-images.githubusercontent.com/102719065/200178997-b51276ee-b5e9-4e05-99ae-ded4c0cee6f3.png)

![image](https://user-images.githubusercontent.com/102719065/200179011-e61a0a43-5ee9-4271-b9fc-26db23372466.png)

We now have an additional hyperparameter, C, that we can tune. As C increases, our tolerance for points outside of ϵ also increases. As C approaches 0, the tolerance approaches 0 and the equation collapses into the simplified (although sometimes infeasible) one.



