var term = new Terminal();
term.open(document.getElementById('terminal'));

function runFakeTerminal() {
  if (term._initialized) {
    return;
  }

  term._initialized = true;

  term.prompt = () => {
    term.write('\r\n$ ');
  };

  term.writeln('Welcome to == 2020 MUD ==');
  term.writeln('Where the future is now.');
  term.writeln('Type "help" for a list of commands');
  term.writeln('');
  prompt(term);

  var buffer = [];
  term.onData(e => {
    switch (e) {
      case '\r': // Enter
      case '\u0003': // Ctrl+C
        // HANDLE ALL THE COMMANDS HERE!!
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
          if (this.readyState == 4) {
            if (this.status == 200) {
              term.write('\r\n');
              term.write(this.responseText);
              term.write('\r\n');
              prompt(term);
            } else  {
              prompt(term);
            }
          }
        };
        xhttp.open("POST", "command/" + buffer.join('') +"/");
        xhttp.send("");
        buffer = []
        break;
      case '\u007F': // Backspace (DEL)
        // Do not delete the prompt
        if (term._core.buffer.x > 2) {
          term.write('\b \b');
        }
        break;
      default: // Print all other characters
        buffer.push(e);
        term.write(e);
    }
  });
}

function prompt(term) {
  term.write('\r\n$ ');
}

runFakeTerminal();
