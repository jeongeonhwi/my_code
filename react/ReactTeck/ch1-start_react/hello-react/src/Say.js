import React, { useState } from "react";

const Say = () => {
  const [message, setMessage] = useState("");
  const onClickEnter = () => setMessage("nice to meet you");
  const onClickEvent = () => setMessage("good bye~");

  const [color, setColor] = useState("black");

  return (
    <div>
      <button onClick={onClickEnter}>enter</button>
      <button onClick={onClickEvent}>exit</button>
      <h1 style={{ color }}>{message}</h1>
      <button style={{ color: "red" }} onClick={() => setColor("red")}>
        red
      </button>
      <button style={{ color: "green" }} onClick={() => setColor("green")}>
        green
      </button>
      <button style={{ color: "blue" }} onClick={() => setColor("blue")}>
        blue
      </button>
    </div>
  );
};

export default Say;
