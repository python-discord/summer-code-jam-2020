import React from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { getYear, setYear } from './actions/year'
import MenuBar from "./components/menubar.js"

function App() {
  const test = useSelector(state => state.year);
  const dispatch = useDispatch();
  return (
    <div className="App">
      <p>Current Year: {test}</p>
      <input type="text" id="test" />
      <button onClick={() => { dispatch(setYear(document.getElementById('test').value)) }}>Set Year</button>

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
