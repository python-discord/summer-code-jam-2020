import React from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { getYear,setYear } from './actions/year'

function App() {
  const test = useSelector(state => state.year);
  const dispatch = useDispatch();
  return (
    <div className="App">
      <p>Current Year: {test}</p>
      <input type="text" id="test"/>
      <button onClick={()=>{dispatch(setYear(document.getElementById('test').value))}}>Set Year</button>
    </div>
  );
}

export default App;
