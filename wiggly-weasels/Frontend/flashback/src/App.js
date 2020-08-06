import React, {useState} from 'react';
import { createGlobalStyle, ThemeProvider } from 'styled-components';

import { styleReset, List, ListItem, Divider, AppBar, Toolbar, Button, TextField} from 'react95';
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
    Headers: {'Accept': 'application/json'}
  }).then(function(response) {
    return response.json();
  }).then(function(data) {
  });
}


const App = () => {
  const [state, setState] = useState({
    value: '',
    email_value: '',
    user_value: ''
  });
  const handleChange = e => setState({ email_value: e.target.value });

  return (
  <div>
    <GlobalStyles />
    <ThemeProvider theme={original}>
    <AppBar>
    <Toolbar style={{ justifyContent: 'space-between' }}> </Toolbar>
    <Button
            onClick={() => {
              console.log(state.email_value)
              postRequest('http://127.0.0.1:8000/account/', {'email': state.email_value})
            }}
            style={{ fontWeight: 'bold' }}
          >Button</Button>
          <TextField
            value={state.email_value}
            placeholder='Your Email'
            onChange={handleChange}
            >
          </TextField>
    </AppBar>
    </ThemeProvider>
  </div>
)
};

export default App;