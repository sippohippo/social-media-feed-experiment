# Social Media Feed Experiment Web App

## Project description

The purpose of this app is two-fold. First, it works as a game that demonstrate how difficult it is to detect bot profiles on a social media feed. Second, it allows running experiments and collecting data on how well people playing the game can distinguish real and fake profiles. 

For the user, the app is like a game where they can log in and play. When they begin to play, they are presented a simulated social media feed (e.g. like on Twitter), with multiple posts visible at once. These posts will be drawn randomly from a large sample of genuine and fake ones. Thus each game will be unique and each user will see a different instance of the simulated social media feed. The user can then vote for each of these posts if they believe it is written by a bot or a real human. Once they are done labeling each post, they then in the end see how many accounts they labeled correctly and what a typical score is.

For the administrator, the app allows setting up the posts that the users see and viewing statistics on how well the users of the app have performed in the game. 

The fake profiles and general setup of this type of an experiment is described in more detail and demonstrated in the paper *Are Deep Learning-Generated Social Media Profiles Indistinguishable from Real Profiles?* [[1]](#1). This previous implementation was done with a Qualtrics survey, and the goal of this project is to allow hosting the experiment on a webpage in the future. A demo of what the simulated feed looks like can be seen [here](https://drive.google.com/file/d/1HxljYvi2OsAD_e6Pi92Gd-w_Y8eZzWi_/view?usp=share_link).

### Tentative database tables

* users (contains credentials for users and admins)
* real_posts (contains the real posts and profile information of the creator of the post. The data in these has been collected earlier via the Twitter API)
* fake_posts (the generated texts used to populate a post, generated using GPT-3)
* fake_profiles (the profile information of fake profiles generated with a basic python script and profile images created with StyleGAN)
* userdata (each row contains the results of a game played by the participant)

The real_posts and fake_posts and fake_profiles are split into three separate tables although technically all could put into one table if adding a column that indicates if the profile is real or fake. I decided to split them into three, so that the real profiles will always stay the same, while the posts and fake profiles can be mixed easily to add variety to each time the game is played.

## Installation and setup

To be added...

## References
<a id="1">[1]</a> 
Rossi, S., Kwon, Y., Auglend, O., Mukkamala, R., Rossi, M., & Thatcher, J. (2023). 
Are Deep Learning-Generated Social Media Profiles Indistinguishable from Real Profiles?
Proceedings of the 56th Hawaii International Conference on System Sciences. https://hdl.handle.net/10125/102645.


## What is this?

This is a repository for my submissions in the University of Helsinki course Tietokanta-sovellus 2023 (Database application).

You can find the course materials [here](https://hy-tsoha.github.io/materiaali/) (in Finnish only).