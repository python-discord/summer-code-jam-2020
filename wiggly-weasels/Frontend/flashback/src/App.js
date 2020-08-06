import React, {useState} from 'react';
import { createGlobalStyle, ThemeProvider } from 'styled-components';

import { styleReset, List, ListItem, Divider, AppBar, Toolbar, Button, TextField, Hourglass, Tabs, Tab, TabBody} from 'react95';
// pick a theme of your choice
import original from "react95/dist/themes/original";
// original Windows95 font (optionally)
import ms_sans_serif from "react95/dist/fonts/ms_sans_serif.woff2";
import ms_sans_serif_bold from "react95/dist/fonts/ms_sans_serif_bold.woff2";

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
  fetch(url, {
    method: 'post',
    body: JSON.stringify(opts),
    Headers: {'Content-Type': 'application/json',
            'Accept': '*/*'}
  }).then(function(response) {
    return response.json();
  }).then(function(data) {
  });
}


const App = () => {
  const [state, setState] = useState({
    value: '',
    email_value: '',
    user_value: '',
    activeTab: 0
  });
  const handleChange = e => setState({ email_value: e.target.value });
  const tabChange = (e, value) => setState({ activeTab: value });

  const { activeTab } = state;
  return (
    <div
    style={{
      padding: '5rem',
      background: 'teal'
    }}>

    <div>
    <GlobalStyles />
    <ThemeProvider theme={original}>
      
      <AppBar>
        <Toolbar style={{ justifyContent: 'space-between' }}>

        <div style={{ position: 'relative', display: 'inline-block' }}>

        <Button
        onClick={() => {
            console.log(state.email_value)
            postRequest('http://127.0.0.1:8000/account/', {'email': state.email_value})
         }}
          style={{ marginLeft: '2px' }}>Login</Button>

        </div>

        <Hourglass size={32} />

        </Toolbar>
      </AppBar>

      <Tabs value={activeTab} onChange={tabChange}>
          <Tab value={0}>Email</Tab>
          <Tab value={1}>Username</Tab>
          <Tab value={2}>Password</Tab>
      </Tabs>
      
      <TabBody style={{ height: 300 }}>
        
        {activeTab == 0 &&(
          <div>
            <TextField
        value={state.email_value}
        placeholder='Your Email'
        onChange={handleChange}
        ></TextField>
          </div>
        )}

        {activeTab == 1 &&(
        <TextField
        value={state.email_value}
        placeholder='Your Username'
        onChange={handleChange}
        >
      </TextField>)}

      {activeTab == 2 &&(
        <TextField
        value={state.email_value}
        placeholder='Your Password'
        onChange={handleChange}
        >
      </TextField>
      )}

      </TabBody>

    </ThemeProvider>
  </div>
  </div>
  )
};

export default App;

/*
<div>
<GlobalStyles />
<ThemeProvider theme={original}>
  <div>
  <AppBar>
    <Toolbar style={{ justifyContent: 'space-between' }}> </Toolbar>
      <div style={{ position: 'relative', display: 'inline-block' }}>
  <Button
        onClick={() => {
          console.log(state.email_value)
          postRequest('http://127.0.0.1:8000/account/', {'email': state.email_value})
         }}
          style={{ marginLeft: '2px' }}>Login</Button>
      </div>
</AppBar>
</div>
<div>
<TextField
        value={state.email_value}
        placeholder='Your Email'
        onChange={handleChange}
        >
      </TextField>
      
</div>
</ThemeProvider>


</div>
*/

