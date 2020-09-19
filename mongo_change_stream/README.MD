After dealing to configure mongo with replicaset in a local machine, I finally figure out. Why use mongo with replicaset, because I want test change_stream in python.

## How To use it
docker-compose run app change_stream
And in another terminal 
docker-compose run app load_resource