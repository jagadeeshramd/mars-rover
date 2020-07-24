import React, { useState, useEffect } from "react";
import Two from "two.js";
import "./App.css";

function App() {
  const board = [30, 30];
  const defaultStartPoint = [Math.floor(Math.random() * board[0]) + 1, Math.floor(Math.random() * board[1]) + 1];
  const defaultEndPoint = [Math.floor(Math.random() * board[0]) + 1, Math.floor(Math.random() * board[1]) + 1];
  const [response, setResponse] = useState([]);
  const [startPoint, setStartPoint] = useState(defaultStartPoint);
  const [endPoint, setEndPoint] = useState(defaultEndPoint);
  const [settings, setSettings] = useState({
    boardHeight: "30",
    boardWidth: "30",
    wallsList: [
      [2, 2],
      [7, 0],
    ],
    startPoint,
    endPoint,
    algorithm: "a",
  });

  useEffect(() => {
    document.getElementById(startPoint.join("-")).style.backgroundColor = "green";
    document.getElementById(endPoint.join("-")).style.backgroundColor = "red";
  });

  const handleGridClick = (e) => {
    console.log(e.target.id);
  };

  const fetchData = async () => {
    const response = await fetch("https://jagadeeshram-mars-rover.herokuapp.com/getPath", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(settings),
    });

    const jsonResponse = await response.json();
    return jsonResponse[1].map((el) => [el[0] * 30, el[1] * 30]);
  };

  const drawLine = (twojs, c1, c2) => {
    const line = twojs.makeLine(...c1, ...c2);
    line.linewidth = 6;
    line.stroke = "rgba(255, 0, 0, 0.5)";
    twojs.update();
  };

  const drawHandler = async () => {
    const response = await fetchData();
    setResponse(response);

    const el = document.getElementById("board");
    const twojs = new Two({
      height: board[0] * 30,
      width: board[1] * 30,
    });
    twojs.appendTo(el);

    response.forEach((el, i) => {
      if (i < response.length - 1) drawLine(twojs, el, response[i + 1]);
    });
  };

  const handleSelectChange = (e) => {
    setSettings({ ...settings, algorithm: e.target.value });
  };

  const reload = () => {
    window.location.reload();
  };

  const algos = [
    {
      value: "bfs",
      label: "Breadth First Search",
    },
    {
      value: "d",
      label: "Dijkstra's Algorithm",
    },
    {
      value: "a",
      label: "A* Algorithm",
    },
  ];
  return (
    <>
      <h1>Jagadeeshram Mars Rover</h1>
      <div id="board" style={{ height: board[0] * 30, width: board[1] * 30, backgroundColor: "" }}>
        {[...Array(board[0] * board[1]).fill("")].map((el, i) => {
          const x = i % 30;
          const y = Math.floor((i + 1) / 30) === 30 ? 29 : Math.floor((i + 1) / 30);
          const generatedCoordinate = x + "-" + y;
          return (
            <div id={generatedCoordinate} className="grid" onClick={handleGridClick} key={generatedCoordinate}></div>
          );
        })}
      </div>
      <div id="toolbar">
        <h3>Select Algorithm</h3>
        <select onChange={handleSelectChange}>
          {algos.map((algo) => (
            <option key={algo.value} value={algo.value}>
              {algo.label}
            </option>
          ))}
        </select>
        <button onClick={reload}>Randomize Start & End Points</button>
        <button onClick={drawHandler}>Draw Path</button>
      </div>
    </>
  );
}

export default App;
