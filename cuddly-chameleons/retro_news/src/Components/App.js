import React from 'react';
import '../css/App.css';
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Header from './Header';
import Login from './Login';
import SignUp from './SignUp';

function App() {
  return (
      <BrowserRouter>
          <Header />
          <Switch>
              <Route path="/login" children={<Login />} />
              <Route path="/signup" children={<SignUp />} />
          </Switch>
      </BrowserRouter>
  );
}

export default App;
