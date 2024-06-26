# snake_game_ai
**Training a neural network with deep Q learning to play the snake game**

As part of **Women in AI mentorship -program** and with the support of my mentor Denis Vorotyntsev, I wanted to better understand AI, and the concept of machine learning.

In this project I explore reinforcement learning and Python by training a model to play the classic snake game. Training an AI agent to play Snake -game implementing Reinforcement Learning, coded in Python with PyGames and PyTorch. It uses feed forward neural network with input layer of 11 neurons, a hidden layer and output layer of 3 neurons.

🚀 You can run the training model code by executing **ai_agent.py**

🚀 To play the game manually you can run **snake_game.py**

The agent was able to reach a high score of 64 after 90 training games.

![Figure_7](https://github.com/rosamakinen/snake_game_ai/assets/112611789/cf1248a1-28ee-4419-9b53-c67aa8eb978b)





At the start of training the model, the agent acted very incoherently, running around in circles and often running straight into a wall, as it did not have enough data to make educated choices.

https://github.com/rosamakinen/snake_game_ai/assets/112611789/d355de2d-8f23-4915-a54d-f78ba723353c




At it's best run the agent was able to reach the high score of 64, although it was not always making the most optimal choices. On many occasions it for example first turns away from the food and goes through a longer route.


https://github.com/rosamakinen/snake_game_ai/assets/112611789/3cc3ae67-1140-4e3b-81d4-297dbdbc0d8b



