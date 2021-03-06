# FAKE - FAcebook big data marKEt
Created by Seyoung Park(seyoung.park@aalto.fi) @ 2015.Dec.24.:tada:
<br>Deployed at http://fake-seyoung.herokuapp.com/

## What is FAKE?
FAKE stands for “Facebook big data marKet” and it's a web store for nominal Facebook user data. Facebook has billions of users and many people can’t survive a day without using it. That enables Facebook to collect and parse tremendously huge amount of private data about their customers' every-second life. Facebook is “free” but we all know where they get the cash from: their user data. For example they sell the data they collected to relevant advertisers. We all know that these things happen but still we don’t really know how this kind of business works and what kind of data is available and sold. It’s very sensitive but undeniably interesting as well. On FAKE, you can register either as a seller who can register user data products or a buyer who can buy those.


## Is it real?
The application is called **FAKE**. Indeed it is. This is just for fun :)


## Screenshots
### Store
[![Fake thumbnail](/readme_images/fake_thumbnail.png)](http://fake-seyoung.herokuapp.com/)
### Different user types
[![Fake thumbnail](/readme_images/authority.png)](http://fake-seyoung.herokuapp.com/)
### "Layered" Comments
[![Fake thumbnail](/readme_images/comments.png)](http://fake-seyoung.herokuapp.com/)
### Upload images. Unique url for images with randomized file names.
https://fake-seyoung-ireland.s3.amazonaws.com/media/images/6b796e76-27e0-42f9-8c7b-46769436d048-sox_sat22_bb_22blog.jpg

[![Fake thumbnail](/readme_images/unique_url3.png)](https://fake-seyoung-ireland.s3.amazonaws.com/media/images/6b796e76-27e0-42f9-8c7b-46769436d048-sox_sat22_bb_22blog.jpg)

## Functions
* Register objects
* Two types of users
* Authentication
* Authorization
* Upload files/images
* Unique url for every file/image using Amazon S3
* Share images
* Pagination
* Ajax
* Basic Search
* Change password
* Add to Cart
* Order

## Environment
* Mac OS X 10.10.4 (Actually this shouldn't matter in anycase.)
* Python 2.7.9
* Django 1.8.2
* Bootstrap 3.3.5
* jQuery 1.11.3

## Technologies
* Heroku
* Amazon S3
* Postgres

## Test environment
Google Chrome 47 64-bit

## Tips
When you edit views.py or some Python scripts, the local server might not be able to update it quick enough. In such case, restart the server.

## License
MIT
