# Cloud VSR Pipeline

## Step 1: Video Input
User uploads a video containing visible lip movements.

## Step 2: Frame Extraction
Video is converted into frames using OpenCV.

## Step 3: Lip Region Detection
Face detection followed by lip region cropping.

## Step 4: Feature Extraction
CNN extracts spatial features from lip frames.

## Step 5: Temporal Modeling
LSTM models temporal dynamics of lip movements.

## Step 6: Text Prediction
Fully connected layers decode features into character probabilities.

## Step 7: Cloud Inference
Model inference is exposed via a FastAPI endpoint.
