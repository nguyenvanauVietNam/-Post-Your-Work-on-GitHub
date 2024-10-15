# Post-Your-Work-on-GitHub

**Post Project 2**
## Bike Share Data Analysis

### Overview
In this project, you will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. You will write code to import the data and answer interesting questions about it by computing descriptive statistics. You will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

![Overview Illustration](divvy.jpg)

### Bike Share Data
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

![Bike Share Data](istockphoto-478482204-612x612.jpg)


### Project Title: Post your Work on GitHub

### Description
#### 1. Project Introduction
This project aims to guide users on how to post their work on GitHub. 
It provides the necessary steps to set up the working environment, configure Git, and connect to personal GitHub accounts.

#### 2. Required Software for Using GIT and GitHub
To use Git and GitHub, you need to install the following software:
- **Git**: A distributed version control system that helps track changes in source code.
- **GitHub Desktop** (optional): A graphical interface application for GitHub that makes it easier to manage repositories.
- **Visual Studio Code** (or any preferred code editor): A powerful code editor for software development.

#### 3. Steps to Configure and Connect from Local to GitHub
1. **Install Git**:
   - Download and install Git from the [official website](https://git-scm.com/).

2. **Set Up User Information**:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "email@example.com"
   ```
3. **Initialize a New Repository:**:
   ```bash
   git init
   ``` 

4. **Connect to GitHub:**:
   ```bash
   git remote add origin https://github.com/<your_username>/<repository_name>.git
   ```   
5. **Push Code to GitHub:**:
   ```bash
    git add .
    git commit -m "Commit message"
    git push -u origin master
   ```   
6. **Setting Up .gitignore**:
   ```bash
    touch .gitignore
   ```   
 - Add patterns for files and directories you want to ignore. For example
    ```bash
    # Ignore node_modules
    node_modules/

    # Ignore log files
    *.log

    # Ignore csv files
    *.csv
   ```   
### Files used
The following file:
Git Commands Documentation.pdf


### Credits
[Git Documents](https://git-scm.com/doc)