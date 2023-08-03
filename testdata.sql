
/* NOTE! CHANGE THE ADDRESS OF THE IMAGE-FILES. CTRL-F, /Users/sippo and replace all with your location */

/* inserting test images */
insert into images values (1, 'img1', TRUE, pg_read_binary_file('/Users/sippo/social-media-feed-experiment/test_images/Fake1.jpg')::bytea);
insert into images values (2, 'img2', TRUE, pg_read_binary_file('/Users/sippo/social-media-feed-experiment/test_images/Fake2.jpg')::bytea);
insert into images values (3, 'img3', TRUE, pg_read_binary_file('/Users/sippo/social-media-feed-experiment/test_images/Fake3.jpg')::bytea);
insert into images values (4, 'img4', FALSE, pg_read_binary_file('/Users/sippo/social-media-feed-experiment/test_images/Real1.jpg')::bytea);
insert into images values (5, 'img5', FALSE, pg_read_binary_file('/Users/sippo/social-media-feed-experiment/test_images/Real2.jpg')::bytea);
insert into images values (6, 'img6', FALSE, pg_read_binary_file('/Users/sippo/social-media-feed-experiment/test_images/Real3.jpg')::bytea);

/* inserting test real posts */

insert into real_posts values (1, 'Phil Madden', '@philmadden', 'Happinesss comes from WHAT we do. Fulfillment comes from WHY we do it.', 4);
insert into real_posts values (2, 'William Bennett', '@williamb', 'When things do not work out as we wish, it may be that we have not been 100% clear in our request.', 5);
insert into real_posts values (3, 'Matthew Gibson', '@MatthewGibson', 'Do not discount yourself no matter what you are doing. Everyone has a unique perspective that they can bring to the world.', 6);

/* inserting test fake posts */

insert into fake_posts values (1, 'Believe in yourself and all that you are – for within you lies a power greater than you could ever imagine. The path to success may be riddled with setbacks, but never let them deter you');
insert into fake_posts values (2, 'Every journey to success begins with a SINGLE step, take that leap of confidence NOW.');
insert into fake_posts values (3, 'Barbie, an iconic figure that has inspired generations, is more than just a doll. With over 200 careers, Barbie has encouraged kids to dream big and break boundaries.');

/* inserting test fake profiles */

insert into fake_profiles values (1, 'Daniel Batista', '@danielbatista', 1);
insert into fake_profiles values (2, 'Ralp Raynor', '@ralphraynor412', 2);
insert into fake_profiles values (3, 'Eugene Pohlman', '@Pohlman', 3);
