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
    this.terminal.attachCustomKeyEventHandler(this.keyEventFilter);

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
          data.username + " enters room."
        );
      } else if (data.msg_type == "EXIT") {
        t.printReply(
          data.username + " leaves."
        );
      } else {
        t.printReply(data.message);
      }
    };

    this.sender = this.sendByWebSocket;

    this.buffer = [];
  }

  keyEventFilter(event) {
    /* Block xterm.js from using the arrow keys to move the cursor. */
    switch(event.key) {
      case "ArrowUp":
      case "ArrowDown":
      case "ArrowLeft":
      case "ArrowRight":
        return false;
      default:
        return true;
    }
  }

  onInputEvent(event) {
    switch (event) {
      case "\r": // Enter
      case "\n": // Ctrl-J
        this.sendBuffer();
        this.terminal.write("\r\n");
        this.printPrompt();
        break;
      case "\u007F": // Backspace
        if (this.buffer.length > 0) {
          this.terminal.write("\b \b");
          this.buffer.pop();
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
     /* \x9B1M deletes current line (the prompt) which we overwrite, and then
      * print a new prompt */
    this.terminal.write("\x9B1M" + reply);
    this.terminal.write("\r\n");
    this.printPrompt();
  }

  printPrompt() {
    this.terminal.write("$ " + this.buffer.join(""));
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
