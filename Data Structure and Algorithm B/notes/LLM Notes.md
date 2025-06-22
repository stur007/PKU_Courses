# LLM Notes

## Chapter 1 Basic Concepts

### Difference between LLM and traditional models

- NLP (natural language model)
- the wider range of application

### the position of LLM

![image-20250224183226060](https://raw.githubusercontent.com/stur007/img/main/img/202502241917937.png)

**the most important feature of deep learning:** without bring explicitly programmed and manual feature extraction

**custom-built LLMs:** performed better and more secure for company etc.

### how to build custom-built LLMs

pretraining -> finetuning

instruction finetuning: input & output

classification finetuning: Yes & No

**transformer** 

1. composition

​	encoder: input text -> (numeric) **embedding** vectors

​	decoder: numeric vectors -> output text

2. self-attention mechanism: 'combine' the relevant text

### the tasks that LLMs can do

- filling the blanks (BERT) complete the sentences (GPT)
- zero-shot task (a completely new task)
- few-shot task (a few examples ahead)

**token:** the unit for a model to read

**autoregressive model:** incorporate previous outputs as inputs for predictions

### the procedures of LLM construction

![image-20250224190711175](https://raw.githubusercontent.com/stur007/img/main/img/202502241917471.png)

## Chapter 2 working with text data

### embedding

mapping from discrete objects to continuous vector space

