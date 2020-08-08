import React, {useState} from 'react';
import { createGlobalStyle, ThemeProvider } from 'styled-components';

import { styleReset, List, ListItem, Divider, AppBar, Toolbar, Button, TextField, Hourglass, Tabs, Tab, TabBody} from 'react95';
// pick a theme of your choice
import original from "react95/dist/themes/original";
// original Windows95 font (optionally)
import ms_sans_serif from "react95/dist/fonts/ms_sans_serif.woff2";
import ms_sans_serif_bold from "react95/dist/fonts/ms_sans_serif_bold.woff2";

import sha256 from 'js-sha256'
import Cookies from 'js-cookie'

const GlobalStyles = createGlobalStyle`
  @font-face {
    font-family: 'ms_sans_serif';
    src: url('${ms_sans_serif}') format('woff2');
    font-weight: 400;
    font-style: normal
  }
  @font-face {
    font-family: 'ms_sans_serif';
    src: url('${ms_sans_serif_bold}') format('woff2');
    font-weight: bold;
    font-style: normal
  }
  body {
    font-family: 'ms_sans_serif';
  }
  ${styleReset}
`;

function postRequest(url, opts) {
  return fetch(url, {
  method: 'POST', // or 'PUT'
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(opts),
  })
  .then(response => response.json())

}



const App = () => {
  const [state, setState] = useState({
    value: '',
    email_value: '',
    user_value: '',
    password_value: ''
  });

  const [activeTab, setActiveTab] = useState(0)
  const [email, setEmail] = useState('')
  const [user, setUser] = useState('')
  const [password, setPassword] = useState('')

  const email_Change = e => setEmail(e.target.value);
  const user_change = e => setUser(e.target.value);
  const password_change = e => setPassword(e.target.value);
  const tabChange = (e, value) => setActiveTab(value);

  return (
    <div
    style={{
      height: '100vh',
      background: 'teal'
    }}>

    <div style={{padding:'5rem'}}>
    <GlobalStyles />
    <ThemeProvider theme={original}>
      
      <AppBar>
        <Toolbar style={{ justifyContent: 'space-between' }}>

        <div style={{ position: 'relative', display: 'inline-block'}}>

        <Button
        onClick={() => {
          if(activeTab === 0){
            const response = postRequest('http://127.0.0.1:8000/account/check-login/', {'password': sha256(password), 'username': user})
            response.then((data) => {
              if(password !== '' && user !== ''){
              Cookies.set('session_id', data.username)}
              else{
                alert('Empty Fields...')
              }

            })
          }else{
            const response = postRequest('http://127.0.0.1:8000/account/', {'email': email, 'hashed_pass': sha256(password), 'nickname': user})
            response.then((data) => {
              if(password !== '' && user !== '' && email !== ''){
                Cookies.set('session_id', data.nickname)}
                else{
                  alert('Empty Fields...')
                }
            })
          }
         }}
          style={{ marginLeft: '2px' }}>Login</Button>

        </div>

        <Hourglass size={32} />

        </Toolbar>
      </AppBar>

      <Tabs value={activeTab} onChange={tabChange}>
          <Tab value={0}>Login</Tab>
          <Tab value={1}>Sign Up</Tab>
      </Tabs>
      
      <TabBody style={{ height: 300 }}>
        
        {activeTab === 0 &&(
          <div>
            <TextField
              value={user}
              placeholder='Your Username'
              onChange={
                user_change}>
            </TextField>

            <TextField
              value={password}
              placeholder='Your Password'
              onChange={password_change}>
            </TextField>
          </div>
        )}

        {activeTab === 1 &&(
          <div>
        <TextField
          value={user}
          placeholder='Your Username'
          onChange={user_change}>
        </TextField>
      
      <TextField
      value={email}
      placeholder='Your Email'
      onChange={email_Change}>
    </TextField>

    <TextField
      value={password}
      placeholder='Your Password'
      onChange={password_change}>
    </TextField>
      </div>
      )}

      </TabBody>

    </ThemeProvider>
  </div>
  </div>
  )
};

export default App;

