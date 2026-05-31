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

Should no specific issue occur, one will see a picture similar to this:

<img width="1459" height="768" alt="Capture d’écran 2026-05-31 à 10 35 50" src="https://github.com/user-attachments/assets/8878103d-f44d-419f-a257-cc3672178475" />

## Perform serving

The serving is about using a pre-trained model to perform predictions in a production environment. With FastAPI, we proceed as follows:

- Fix the values for the independent variables:
  <img width="1458" height="772" alt="Capture d’écran 2026-05-31 à 10 45 10" src="https://github.com/user-attachments/assets/5781afb1-9f3e-4b39-b95c-75e32ebf5687" />
- Click on the button execute.

## Contact

For questions or feedback, contact:

- Email: your.email@example.com
- GitHub: username
