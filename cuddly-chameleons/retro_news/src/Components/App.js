import React from 'react';
import '../css/App.css';
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Header from './Header';
import Login from './Login';

function App() {
  return (
      <BrowserRouter>
          <Header />
          <Switch>
              <Route path="/login" children={<Login />} />
          </Switch>
      </BrowserRouter>
  );
}

export default App;
