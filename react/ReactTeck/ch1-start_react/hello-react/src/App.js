import React, { Component } from "react";
import ScrollBox from "./ScrollBox";
import IterationSample from "./IterationSample";
import LifeCycleSample from "./LifeCycleSample";

class App extends Component {
  render() {
    return (
      <div>
        <ScrollBox ref={(ref) => (this.ScrollBox = ref)} />
        <button onClick={() => this.ScrollBox.scrollToBottom()}>
          go to bottum
        </button>
        <hr></hr>
        <IterationSample />
        <hr></hr>
        <LifeCycleSample />
      </div>
    );
  }
}

export default App;
