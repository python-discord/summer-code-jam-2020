import React from 'react';
import { getYear, setYear } from './actions/year'
import MenuBar from "./components/menubar.js"
import DynamicHome from "./components/dynamic-home"
import { useSelector, useDispatch } from 'react-redux';

function App() {
  const dispatch = useDispatch();
  // const dispatch = useDispatch();
  return (
    <div className="App">
      <DynamicHome />
      {/* The menu bar should be present on all pages. Change the used values below. */}
      <MenuBar
        valueSpan={[1998, 2020]}
        initialValue={2020}
        labelValues={[]}
        dispatch={dispatch}
      />
    </div>
  );
}

export default App;
