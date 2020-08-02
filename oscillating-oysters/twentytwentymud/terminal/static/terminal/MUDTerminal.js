/* MUDTerminal
 *
 * creates an xterm.js terminal and connects it to the
 * back-end.
 * 
 * depends on: 
 *    xterm.js
 *    xterm.css
 */

class MUDTerminal {
  
  constructor(elementId) {
    this.terminal = new Terminal();
    this.terminal.open(document.getElementById(elementId));
    this.terminal.onData( e => { this.onInputEvent(e) } );

    this.buffer = [];

    /* TODO change this to sockets once its running */
    this.sender = this.sendByPOST;

    this.printWelcome();
  }

  onInputEvent(event) {
    switch (event) {
      case '\r': // Enter
        this.sendBuffer();
        break;
      case '\u007F': // Backspace
        if (this.terminal._core.buffer.x > 2) {
          this.terminal.write('\b \b');
        }
        break;
      default:
        this.buffer.push(event);
        this.terminal.write(event);
    }
  }

  sendBuffer() {
    this.sender(this.buffer.join(''));
    this.buffer = []
  }

  printReply(reply) {
    this.terminal.write('\r\n');
    this.terminal.write(reply);
    this.terminal.write('\r\n');
    this.printPrompt();
  }

  printWelcome() {
    this.sendByPOST('welcome');
  }
  
  printPrompt() {
    this.terminal.write('\r\n$ ');
  }

  sendByPOST(message) {
    /* callback for the onreadystatechange in the Http request */
    var t = this;
    this.callback  = function () {
      if (this.readyState == 4) {
        if (this.status == 200) {
          t.printReply(this.responseText);
        }
      }
    };

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = this.callback;
    xhttp.open("POST", "command/" + message +"/");
    xhttp.send("");
  }

}

terminal = new MUDTerminal('terminal');
