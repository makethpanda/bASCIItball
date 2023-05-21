import tensorflow as tf
import numpy as np

# Define the AI agent class
class AIAgent:
    def __init__(self):
        self.state_size = 5  # Player coordinates (x, y), Ball coordinates (x, y), Score
        self.action_size = 3  # Move left, Move right, Hold space

        # Define the model
        self.model = self.build_model()

        # Define hyperparameters
        self.learning_rate = 0.001
        self.discount_factor = 0.99
        self.optimizer = tf.keras.optimizers.Adam(learning_rate=self.learning_rate)

    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(24, activation='relu', input_shape=(self.state_size,)),
            tf.keras.layers.Dense(24, activation='relu'),
            tf.keras.layers.Dense(self.action_size, activation='linear')
        ])
        return model

    def get_action(self, state):
        state = np.reshape(state, [1, self.state_size])
        q_values = self.model.predict(state)[0]
        return np.argmax(q_values)

    def train(self, state, action, reward, next_state, done):
        state = np.reshape(state, [1, self.state_size])
        next_state = np.reshape(next_state, [1, self.state_size])

        target = self.model.predict(state)
        if done:
            target[0][action] = reward
        else:
            target[0][action] = reward + self.discount_factor * np.max(self.model.predict(next_state))

        # Optimize the model
        with tf.GradientTape() as tape:
            q_values = self.model(state)
            loss = tf.keras.losses.MeanSquaredError()(target, q_values)
        grads = tape.gradient(loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(grads, self.model.trainable_variables))
