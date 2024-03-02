# How to evaluate WatsonX models with Rougue, Bert and Bleu metrics for Customer Support Ticket Dataset

Hello today we are going to build a simple application to evaluate our LLM generations in 
WatsonX.AI to solve Customer Support Ticket Dataset by Using RAG.

In this demo we are going to use a Customer Support Ticket Dataset which is a dataset that includes customer support tickets for various tech products. It consists of customer inquiries related to hardware issues, software bugs, network problems, account access, data loss, and other support topics. The dataset provides information about the customer, the product purchased, the ticket type, the ticket channel, the ticket status, and other relevant details.

In particular we are going to use the following information.

- Ticket Description: The description of the customer's issue or inquiry.
- Resolution: The resolution or solution provided for closed tickets.

We will create a chatbot that  Solve the Ticket  by using  RAG  and test the different models to get the best. 


## Environment Creation
For this repository we are going to use Python 3.10.11

```
python -m venv .venv
```
we activate our environment

```
.\.venv\Scripts\activate
```
the we install our packages

```
python m pip install --upgrade pip
```
and
```
pip install -r requirements.txt
```

```
python -m ipykernel install --user --name MetricX --display-name "Python (MetricX)"
```


## Run pur Web Application

```
python  src/manage.py runserver localhost:7860
```




