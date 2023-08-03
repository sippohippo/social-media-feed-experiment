# Social Media Feed Experiment Web App

## Status report (Välipalautus 2, 6.8.2023)

* Currently the registration and login system is implemented
* There is a very rough draft of the actual game / experiment where you get to see genuine and generated profiles

### Note on data and GDPR compliance

The three "real" test profiles in the test data of this public Github repository do not contain genuine names or post content and are generated as are the fake profiles. All data in this repository is purely for testing that the app works.

## Installation and setup

This repository has been tested with a Mac (M1, Ventura). PostgreSQL should be installed.

1. Clone this repository
2. 

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
* real_posts (contains the real posts and profile information of the creator of the post. The data has been collected earlier via the Twitter API)
* fake_posts (the generated texts used to populate a post, generated using GPT-3)
* fake_profiles (the profile information of fake profiles generated with a basic python script)
* results (each row contains the results of a game played by the participant)
* images (profile images created with StyleGAN as well as real profile images)

The real_posts and fake_posts and fake_profiles are split into three separate tables although technically all could be put into one table if adding a column that indicates if the profile is real or fake. I decided to split them into three, so that the real profiles will always stay the same, while the posts and fake profiles can be mixed easily to add variety to each time the game is played.

All profile and post data has already been generated / collected already. 


## References
<a id="1">[1]</a> 
Rossi, S., Kwon, Y., Auglend, O., Mukkamala, R., Rossi, M., & Thatcher, J. (2023). 
Are Deep Learning-Generated Social Media Profiles Indistinguishable from Real Profiles?
Proceedings of the 56th Hawaii International Conference on System Sciences. https://hdl.handle.net/10125/102645.


## What is this?

This is a repository for my submissions in the University of Helsinki course Tietokanta-sovellus 2023 (Database application).

You can find the course materials [here](https://hy-tsoha.github.io/materiaali/) (in Finnish only).