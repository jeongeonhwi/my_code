import React from "react";

const test = () => {
  const name = "리액트";
  return (
    <div>
      {name === "리액트" ? <h1>리액트입니다.</h1> : <h1>리액트아닙니다.</h1>}
    </div>
  );
};

export default test;
