# FSDS_GENAI_Assignment
This repository is for practising python projects. :)


## How to run:

1. Create a new virtual environment

```bash
conda create -n assistant python=3.10

```

# Note:
# Uploading visual documentation/screenshot - Just copy paste

# Right way vs wrong way to create virtual environment
![alt text](<right vs wrong way to create virtual environment.png>)



1. Checkout the created virtual environment

```bash
conda env list

```

3. Activate the virtual environment

```bash
conda activate assistant 

```

4. Install all the packages present in the requirements file


```bash
pip install -r requirements.txt

```

```bash
streamlit run app.py

```



## Required Github Commands

```bash
git add .

git commit -m "message"

git push origin main
```

# take 2 numbers -> do addition, do subtraction, do multiplication, do division
# take any numbers -> do the above
# take any numbers, but when 0 is there then ignore the number

1. in console + using Class + try except + logging
2. as API (only result in API) FastApi
3. as API (only result in API) flask
4. as API flask (Numbers entered are shown, Result is also shown)
5. as API FastApi and streamlit


# main.py is used for performing console based calculation
# app.py is used for performing api based calculation
# calculator.py contains the classes 