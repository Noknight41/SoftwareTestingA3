# 1.a Set Up Local

## Install Selenium
```
pip install selenium
```

## Install Pylightxl
```
pip install pylightxl
```

## Download Chrome Driver and Add PATH

Downloaded chromedriver.exe and change PATH to the current position 
(Already did this)

# 1.b Access Virtual ENV (Alternative to 1.a)

## Activate VENV
```
source .\myenv\Scripts\activate (Bash)
source .\myenv\Scripts\activate.fish (Fish shell)
.\myenv\Scripts\activate.bat (Command Prompt)
.\myenv\Scripts\Activate.ps1 (Powershell)
```

## Install Python Package 
```
pip install -r .\requirement.txt
```

## Deactivate VENV
```
deactivate
```

# Run Testing Script with Level 0 (No Assertion, just Action)

## Function Testing Part using Equivelance Class Testing 
```
python testing.py
```

# Run Testing Script with Level 1

## Run Function Testing Part using Decision Table Testing 
```
python testing.py DTT
```

## Run Function Testing Part using Boundary Value Testing 
```
python testing.py BVT
```

## Run Function Testing Part using Equivelance Class Testing 
```
python testing.py ECT
```

## Run Function Testing Part using Use Case Testing 
```
python testing.py UCT
```

## Run Non-Functional Testing Part
```
python testing.py NF
```
