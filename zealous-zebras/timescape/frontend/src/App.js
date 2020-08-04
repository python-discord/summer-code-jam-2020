import React from 'react';
import MenuBar from "./components/menubar.js"

function App() {
  return (
    <div className="App">


      {/* The menu bar should be present on all pages. Change the used values below. */}
      <MenuBar
        valueSpan={[1998, 2020]}
        initialValue={2004}
        labelValues={[{ value: 2000 }, { value: 2004 }, { value: 2007 }, { value: 2015 }]}
      />
    </div>
  );
}

export default App;
