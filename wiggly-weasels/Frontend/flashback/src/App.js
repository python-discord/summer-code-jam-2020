//    ______ _           _     _                _    
//   |  ____| |         | |   | |              | |   
//   | |__  | | __ _ ___| |__ | |__   __ _  ___| | __
//   |  __| | |/ _` / __| '_ \| '_ \ / _` |/ __| |/ /
//   | |    | | (_| \__ \ | | | |_) | (_| | (__|   < 
//   |_|    |_|\__,_|___/_| |_|_.__/ \__,_|\___|_|\_\
//                                                   
// 
import React, {useState} from 'react';
import { createGlobalStyle, ThemeProvider } from 'styled-components';

import { styleReset, List, ListItem, Divider, AppBar, Toolbar, Button, TextField, Hourglass, Tabs, Tab, TabBody} from 'react95';
// pick a theme of your choice
import original from "react95/dist/themes/original";
// original Windows95 font (optionally)
import ms_sans_serif from "react95/dist/fonts/ms_sans_serif.woff2";
import ms_sans_serif_bold from "react95/dist/fonts/ms_sans_serif_bold.woff2";

import Terminal from 'terminal-in-react'

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
  .then((response) => {
    console.log(response)
    if(!response.ok){
      alert('Something went wrong, try again...')
      throw 'Bad Request'
    }
  return response
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
  const [group, setGroup] = useState('')

  const email_Change = e => setEmail(e.target.value);
  const user_change = e => setUser(e.target.value);
  const password_change = e => setPassword(e.target.value);
  const tabChange = (e, value) => setActiveTab(value);
  const session_id = Cookies.get('session_id');

  console.log(group)
  
  return (
    <div
    style={{
      height: '103vh',
      background: 'teal'
    }}>

    <div style={{padding:'5rem'}}>
    <GlobalStyles />
    <ThemeProvider theme={original}>
      
      <AppBar>
        <Toolbar style={{ justifyContent: 'space-between' }}>

        <div style={{ position: 'relative', display: 'inline-block'}}>
        { session_id ? (
          <Button
          onClick={() => {
            Cookies.remove('session_id')
            window.location.reload()
           }}
            style={{ marginLeft: '2px' }}>Logout</Button>
        ) : (
        <Button
        onClick={() => {
          if(activeTab === 0){
            const response = postRequest('http://127.0.0.1:8000/account/check-login/', {'password': sha256(password), 'username': user})
            response.then((data) => {
              Cookies.set('session_id', data.username)
              window.location.reload()
            })
          }else{
            const response = postRequest('http://127.0.0.1:8000/account/', {'email': email, 'hashed_pass': sha256(password), 'nickname': user})
            response.then((data) => {
                Cookies.set('session_id', data.nickname)
                window.location.reload()
              }
            )
          }
         }}
          style={{ marginLeft: '2px' }}>Begin</Button>
        )}
        
        </div>
      {!session_id && (
        <Hourglass size={32} />
      )}

        </Toolbar>
      </AppBar>
  {session_id ? (
    <div style = {{display:"flex", justifyContent: "center"}}>
      <Terminal hideTopBar
      color = 'green'
      msg = 'Welcome to the FlashBack IRC Client.&#10;Type "help", "credits" for more information.'
        commands={{
          join: {
            method: (args, print, runCommand) => {
              print(`Attempting to join ${args._[0]}`);
              const response = postRequest('http://127.0.0.1:8000/group/join-group/', {'group_name': args._[0]})
              response.then( (data) => {
                window.hack_group = args._[0]
                window.hack_messages = data.messages.length
                data.messages.forEach((message) => {
                  print(`${message.sender}: ${message.content}`)
                })
              })
            },
            options: [
              {
                name: 'color',
                description: 'The color the output should be',
                defaultValue: 'white',

              },
            ],
          },
          create:{
            method: (args, print, runCommand) => {
              print(`Creating Group ${args._[0]}`)
              postRequest('http://127.0.0.1:8000/group/', {'messages': [{'sender': 'flashback', 'content': `Welcome to ${args._[0]}`}], 'name': args._[0], 'creator': session_id})

          }
        },
          send:{
            method:(args, print, runCommand) => {
              const read_response = postRequest('http://127.0.0.1:8000/group/read-message/', {'group_name': window.hack_group, 'index': window.hack_messages})
              read_response.then((data) => {
                data.messages.forEach((message) => {
                  print(`${message.sender}: ${message.content}`)
                  window.hack_messages += 1})
                })
              print('Sending message')
              console.log(group)
              const response = postRequest('http://127.0.0.1:8000/group/new-message/', {'sender': session_id, 'content': args._.join(' '), 'group_name': window.hack_group})
              response.then(() => {
                print(`${session_id}: ${args._.join(' ')}`)
                window.hack_messages += 1
              })
            }
          },
        exit:{
          method:(args, print, runCommand) => {
            print('Leaving group')
            window.hack_group = ''
          }
        },
        read:{
          method: (args, print, runCommand) => {
            print('New Messages')
            const response = postRequest('http://127.0.0.1:8000/group/read-message/', {'group_name': window.hack_group, 'index': window.hack_messages})
            response.then((data) => {
              data.messages.forEach((message) => {
                print(`${message.sender}: ${message.content}`)
                window.hack_messages += 1
              })
            })
          }
        },
        help:{
          method: (args, print, runCommand)=> {
            print('These are common Flashback IRC commands used in various situations:\n\njoin [group-name]\t\
- Join an active Group\n\ncreate [group-name]\t- Create a group\n\nsend [message]\t- Send a message to the group\n\nread\t- Read all new messages\n\nclear\t- Clear the screen\n\nexit\t- Exit current group\n')
          }
        },
        credits:{
          method: (args, print, runCommand) => {
            print('Wiggly Weasels:\nMVP:JetDeveloping#4308\nUnloadingGnat#8067\nt11s#6825\nAashay03#8907')
          }
        }
        }}
      />
    </div>
  ) : (
    <>
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
</>
    ) }

    </ThemeProvider>
  </div>
  </div>
  )
};

export default App;

