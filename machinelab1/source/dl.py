import pandas as pd
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Load iris data from sklearn then use pandas data frame to prepare the data
data = load_iris()
df = pd.DataFrame(data.data, columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
df["target"] = pd.Series(data.target)

# Extract features and labels from pandas data frame
features = df.loc[:, ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
labels = df.loc[:, ['target']]

# Push both features and labels into OneHotEncoder then transform into array
one_hot_encoder = OneHotEncoder()
one_hot_encoder.fit(features)
features = one_hot_encoder.transform(features).toarray()
one_hot_encoder.fit(labels)
labels = one_hot_encoder.transform(labels).toarray()

# Split the data into 80% train data and 20% test data
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

# Declare variables for logistic regression formula
x = tf.placeholder(tf.float32, [None, 15])
y = tf.placeholder(tf.float32, [None, 3])
w = tf.Variable(tf.zeros([15, 3]))
b = tf.Variable(tf.zeros([3]))

# Declare variable for predicted value
y_predicted = tf.nn.softmax(tf.add(tf.matmul(x, w), b))

# Create loss function for logistic regression
loss = tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_predicted)

# Create optimizer with gradient descent to minimize the loss with 0.00 learning rate
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.003).minimize(loss)

total_row = df.shape[0]

# Run TensorFlow session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./graphs/output', sess.graph)
    # Training Logistic Regression model against training data
    for _ in range(total_row):
        __, current_loss = sess.run([optimizer, loss], feed_dict={x: x_train, y: y_train})
        print("(Iteration,Loss):({},{})".format(_ + 1, sum(current_loss) / total_row))
    # Test accuracy against testing data
    prediction = tf.equal(tf.argmax(y_predicted, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(prediction, tf.float32))
    print("Model accuracy:", accuracy.eval({x: x_test, y: y_test}))
    writer.close()