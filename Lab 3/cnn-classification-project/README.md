# CNN Classification Project

This project implements, trains, and evaluates various Convolutional Neural Network (CNN) architectures on benchmark datasets. The goal is to analyze the impact of network depth and dataset complexity on classification accuracy and computational efficiency.

## Architectures Implemented

The following CNN architectures are included in this project:

- **LeNet-5**: A pioneering architecture for handwritten digit recognition.
- **AlexNet**: A deep CNN that won the ImageNet competition in 2012.
- **VGGNet**: Known for its simplicity and depth, using small convolutional filters.
- **ResNet-50**: Introduces residual connections to enable training of very deep networks.
- **ResNet-100**: A deeper version of ResNet with more layers.
- **EfficientNet**: Optimizes accuracy and efficiency through a compound scaling method.
- **InceptionV3**: Utilizes inception modules to capture multi-scale features.
- **MobileNet**: Designed for mobile and edge devices, focusing on efficiency.

## Datasets

The project supports the following benchmark datasets:

- **MNIST**: Handwritten digits dataset.
- **Fashion-MNIST**: A dataset of clothing items, serving as a drop-in replacement for MNIST.
- **CIFAR-10**: A dataset containing 10 classes of images, commonly used for image classification tasks.

## Project Structure

```
cnn-classification-project
├── src
│   ├── models
│   │   ├── lenet5.py
│   │   ├── alexnet.py
│   │   ├── vggnet.py
│   │   ├── resnet50.py
│   │   ├── resnet100.py
│   │   ├── efficientnet.py
│   │   ├── inceptionv3.py
│   │   └── mobilenet.py
│   ├── train.py
│   ├── evaluate.py
│   └── utils.py
├── data
│   └── datasets.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd cnn-classification-project
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To train a model, run the following command:
```
python src/train.py --model <model_name> --dataset <dataset_name>
```

To evaluate a trained model, use:
```
python src/evaluate.py --model <model_name> --weights <path_to_weights>
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.