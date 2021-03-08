# AirBnB clone
This project aims to deploy on our server a simple copy of the [AirBnB website](https://airbnb.com). We won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

At the end, we will have a complete web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data
* An API that provides a communication interface between the front-end and our data

![AirBnB Clone implementation](https://lh3.googleusercontent.com/pw/ACtC-3eYaqg89XL26Y_DFvTLt4MW-w3C7u1gw9aK8c0lhiC3RYHVdLguOuWW7LZdXu5h0117WqFc9OYEYpAQOnyj6ldRz8EXusQW9_QS5IgmbBnEafXvaXsQVIQleFWUxl31_nOfc68hip5XvQjKooJzWgY=w960-h512-no?authuser=1)

## Roadmap and documentation
The application won't be built all at once, but step by step. Here it is our roadmap and each step respective documentation:

1. [The console](#1)
   1. [How to start it](#11)
   2. [How to use it](#12)
   3. [Examples](#13)
2. [Web static](#2)
3. [MySQL storage](#3)
4. [Web framework - templating](#4)
5. [RESTful API](#5)
6. [Web dynamic](#6)

### 1. The console [done] <a name="1"></a>
This is a built-in command line interpreter that provides a way to interact with the Storage-engine. The purposes of this step are:
* Data model creation
* Objects management (creation, updating, destroying, etc.) via a console / command interpreter
* Objects storage and persistency to a JSON file

    ### i. How to start it <a name="11"></a>

    **First.** Clone this repository: <https://github.com/nicolasportela/AirBnB_clone.git>

    **Second.** Go to the repo. 

    **Third.** From its root directory, run: `$ ./console.py`

    ### ii. How to use it <a name="12"></a>

    Once you run the previous command, the following prompt will emerge: `(hbnb) ` 
    
    Ready to work!

    #### Available Commands
    * `EOF`

    * `quit`

    * `create`

    * `show`

    * `destroy`

    * `all`

    * `update`

    * Run `help` for more information

    ### iii. Examples <a name="13"></a>

    #### Create an User

    ```
    (hbnb) create User  # command run
    2f9fa3f9-4de5-4d1b-863a-1d1a140d5868  # id retrieved
    ```

    #### Show a previously created object

    ```
    (hbnb) show User 2f9fa3f9-4de5-4d1b-863a-1d1a140d5868
    [User] (2f9fa3f9-4de5-4d1b-863a-1d1a140d5868) {'id': 2f9fa3f9-4de5-4d1b-863a-1d1a140d5868', 'created_at': datetime.datetime(2021, 02, 18, 13, 58, 14, 530494), 'updated_at': datetime.datetime(2021, 02, 18, 13, 58, 14, 530515)}
    ```

    #### Destroy an object

    ```
    (hbnb) destroy User 2f9fa3f9-4de5-4d1b-863a-1d1a140d5868
    (hbnb) show User 2f9fa3f9-4de5-4d1b-863a-1d1a140d5868
    *** instance not found ***
    ```

### 2. Web static [done] <a name="2"></a>

Before developing a big and complex web application, we build here the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

* Simple HTML static pages creation
* Style guide
* Fake contents
* No Javascript
* No data loaded from anything

### 3. MySQL storage [to-do] <a name="3"></a>

### 4. Web framework - templating [to-do] <a name="4"></a>

### 5. RESTful API [to-do] <a name="5"></a>

### 6. Web dynamic [to-do] <a name="6"></a>