# mars-rover
The Mars Colonization Program

Web App URL: https://jagadeeshramd.github.io/mars-rover/
# Jagadeeshram Mars Rover

The project has been developed using Python in the back end and the Flask web framework with the front end developed in HTML, CSS, Javascript, ReactJS. The back end is deployed as an API on Heroku cloud. The web app has an interactable grid that lets you choose a start and end point and add obstacles in the cells of the grid. Breadth First Search, Dijkstra’s algorithm, A\* algorithm – Manhattan heuristic have been implemented. The user can choose any of the above algorithms to find the shortest path and its length between the start and end cells on the grid while avoiding obstacles on the way.

## Deployed endpoint:

API: https://jagadeeshram-mars-rover.herokuapp.com/getPath

```
curl -X POST \
  https://jagadeeshram-mars-rover.herokuapp.com/getPath \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"boardHeight": "100",
	"boardWidth": "100",
	"wallsList": [[2, 0], [7, 0]],
	"startPoint": [0, 0],
	"endPoint": [4, 5],
	"algorithm": "a"
}'
```

## To run locally
## To run UI

`npm install`

`npm start`

## To run backend

`cd API`

`set FLASK_APP=app`

`flask run`


