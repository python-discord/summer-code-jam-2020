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
    this.terminal.onData((e) => {
      this.onInputEvent(e);
    });

    const ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    const ws_path =
      ws_scheme + "://" + window.location.host + "/dungeon/stream/";

    this.terminal.writeln("Connecting to " + ws_path);
    this.socket = new ReconnectingWebSocket(ws_path);

    /* Set up a message handler */
    var t = this;
    this.socket.onmessage = function (message) {
      var data = JSON.parse(message.data);

      // todo: have a better parsing system, maybe a service
      if (data.leave) {
        t.printReply("Leaving: " + data.leave);
      } else if (data.msg_type == "ENTER") {
        t.printReply(
          "Server: " + data.username + " has entered the DuNgEoN!!!"
        );
      }
      t.printReply("Server: " + data.message);
    };

    this.sender = this.sendByWebSocket;

    this.buffer = [];
  }

  onInputEvent(event) {
    switch (event) {
      case "\r": // Enter
        this.sendBuffer();
        break;
      case "\u007F": // Backspace
        if (this.terminal._core.buffer.x > 2) {
          this.terminal.write("\b \b");
        }
        break;
      default:
        this.buffer.push(event);
        this.terminal.write(event);
    }
  }

  sendBuffer() {
    this.sender(this.buffer);
    this.buffer = [];
  }

  printReply(reply) {
    this.terminal.write("\r\n");
    this.terminal.write(reply);
    this.printPrompt();
  }

  printPrompt() {
    this.terminal.write("\r\n$ ");
  }

  sendByWebSocket(message) {
    var cmd;
    message = message.join("");
    var split = message.split(" ");
    if (split.length > 1) {
      cmd = split[0];
      message = split.slice(1);
    } else {
      cmd = message;
      message = null;
    }
    const msg = JSON.stringify({ command: cmd, message: message });
    this.socket.send(msg);
  }

  sendByPOST(message) {
    /* callback for the onreadystatechange in the Http request */
    var t = this;
    this.callback = function () {
      if (this.readyState == 4) {
        if (this.status == 200) {
          t.printReply(this.responseText);
        }
      }
    };

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = this.callback;
    xhttp.open("POST", "command/" + message.join("") + "/");
    xhttp.send("");
  }
}

terminal = new MUDTerminal("terminal");
