# Social Media Feed Experiment Web App

## Status report (Välipalautus 2, 6.8.2023)

* Currently the registration and login system is implemented
* There is a very rough draft of the actual game / experiment where you get to see genuine and generated (only text features currently, profile pictures are still work in progress...)

### Known bugs and missing features

To be added:

* Collection of results to a database table
* Calculation of accuracy in results page
* Admin page and UI for updating / removing data
* Proper graphics 


### Note on data and GDPR compliance

The "real" test profiles in the test data of this public Github repository do not contain genuine names or post content and are generated with a similar method as the fake profiles. All data in this repository is purely for testing that the app works. In production, the real profiles would contain data collected via Twitter's API. 

## Installation and setup

This repository has been tested with both macOS Ventura and Cubbli Linux. PostgreSQL should be installed.

1. Clone this repository and go to the newly created directory

```bash
git clone https://github.com/sippohippo/social-media-feed-experiment
cd social-media-feed-experiment
```

2. Create a local .env file. Then open it and insert your local DATABASE_URL and own SECRET_KEY

```bash
touch .env
```

```
DATABASE_URL=<db-address-here>
SECRET_KEY=<secret-key-here>
```

3. Activate a virtual environment and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
```

4. Setup the database and populate it with test data. Note, you need to change the address in lines 5-10 in the test data! 

```bash
psql < schema.sql
psql < testdata.sql
```

5. Start the app

```bash
flask run
```

## User guide

1. Create a new account
2. Start the experiment
3. Vote for each profile and press submit
4. See the results
5. Return to main menu and quit or do the experiment again


## Project description

The purpose of this app is two-fold. First, it works as a game that demonstrates how difficult it is to detect bot profiles on a social media feed. Second, it allows running experiments and collecting data on how well people playing the game can distinguish real and fake profiles. 

For the user, the app is a game where they can log in and play. When they begin to play, they are presented a simulated social media feed (e.g. like on Twitter), with multiple posts visible at once. These posts will be drawn randomly from a large sample of genuine and fake ones. Thus, each game will be unique and each user will see a different instance of the simulated social media feed. The user can then vote for each of these posts if they believe it is written by a bot or a real human. Once they are done labeling each post, they see how many accounts they labeled correctly and what the average score is.

For the administrator, the app allows setting up the posts that the users see, and viewing statistics on how well the users of the app have performed in the game. 

The fake profiles and general setup of this type of an experiment is described in more detail and demonstrated in the paper *Are Deep Learning-Generated Social Media Profiles Indistinguishable from Real Profiles?* [[1]](#1). This previous implementation was done with a Qualtrics survey, and the goal of this project is to allow hosting the experiment on a webpage in the future. A demo of what the simulated feed and voting options could look like can be seen [here](https://drive.google.com/file/d/1Thu1EiI0KjJo8-HpJuNy8ZfOKenInpRG/view?usp=share_link).


### Main features

* The user can log in and out or create a new profile 
* After logging in the user sees the main menu where the options are to play the game or log out
* When choosing to play the game, the app takes the user to a new page which consists of a simulated social media feed with 3 visible posts. Each post contains text as well as the name and profile picture of the profile that posted it. The user can mark each profile as a human or a bot. 
* After completing the task the user sees how many profiles they labeled accurately and then can play again or go to the main menu.
* The administrator can add or remove profiles to the experiment
* The administrator can view statistics on how well the users have performed

### Tentative database tables

* users (contains credentials for users and admins)
* posts (contains the posts and profile information of the creator of the post. The data of real profiles has been collected earlier via the Twitter API and generated data produced with GPT-3)
* images (profile images created with StyleGAN as well as real profile images)

All profile and post data has already been generated / collected already. 


## References
<a id="1">[1]</a> 
Rossi, S., Kwon, Y., Auglend, O., Mukkamala, R., Rossi, M., & Thatcher, J. (2023). 
Are Deep Learning-Generated Social Media Profiles Indistinguishable from Real Profiles?
Proceedings of the 56th Hawaii International Conference on System Sciences. https://hdl.handle.net/10125/102645.


## What is this?

This is a repository for my submissions in the University of Helsinki course Tietokanta-sovellus 2023 (Database application).

You can find the course materials [here](https://hy-tsoha.github.io/materiaali/) (in Finnish only).