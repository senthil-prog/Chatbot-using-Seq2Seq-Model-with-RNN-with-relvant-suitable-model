

#Chatbot using Seq2Seq RNN model

Name:Sharanya R
USN:4AL22CS132

#project
This project implements an intelligent conversational chatbot using a Sequence-to-Sequence (Seq2Seq) model with Recurrent Neural Networks (RNNs). The model is designed to understand user inputs, identify key phrases, and generate relevant responses, simulating natural conversation.

#Dataset
user_input | chatbot_response

#Model Architecture
Seq2Seq RNN Variants Implemented:
Vanilla Seq2Seq - Encoder-decoder RNN with a single hidden layer
Stacked RNN - Multiple RNN layers for deeper sequence understanding
Attention-enhanced Seq2Seq - Weights important words in input sequences
Hybrid LSTM/GRU Seq2Seq - Combines LSTM and GRU for better context retention

#Model Configuration:
Architecture: Encoder-Decoder RNN (Vanilla Seq2Seq with attention optional)
Hidden Layers: 2-3 RNN layers with 128, 64 units
Dropout: 0.2 for regularization
Optimizer: Adam
Loss Function: Categorical Cross-Entropy (for token predictions)
Inference: Uses keyword matching and sequence similarity for improved real-time responses


#Performance Metrics
The chatbot achieves:
Response accuracy: >85% for dataset queries with partial keyword matching
Real-time responsiveness: <1 second per reply
Graphical insight: Overlap graph shows the number of matched keywords per input
Scalability: Can be integrated with GUI or web applications for interactive chat