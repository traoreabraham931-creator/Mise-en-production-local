# Model deployment via FastAPI

The project is a simple illustration about how to deploy a pre-trained Neural Network model. The model considered is the one developed in the repository "Call_prediction".


## Installation

Clone the repository:

```bash
git clone https://github.com/traoreabraham931-creator/Mise-en-production-local.git
```

## Project Structure

```
├── app/
│   ├── library.py
│   └── main.py
├── models/
│   ├── custom_attention.weights.h5 # weights of the trained model
├── Dockerfile                      # Dockerfile
├── launch-docker.sh                # sh file to build the docker container allowing to deploy the model
├── requirements.txt                # requirement file containing the necessary libraries
└── README.md

```

## Creation of the container allowing to deploy the model
```bash
./launch-docker.sh
```
## Checking

In a browser, type: http://0.0.0.0:8000/docs

## License

This project is licensed under the MIT License.

## Contact

For questions or feedback, contact:

- Email: your.email@example.com
- GitHub: username
