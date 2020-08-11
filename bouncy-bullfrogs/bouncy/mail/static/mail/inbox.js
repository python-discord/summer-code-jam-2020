window.onpopstate = function (event) {
    if (event.state.view === 'mailbox')
        load_mailbox(event.state.mailbox);
    if (event.state.view === 'compose')
        compose_email();
    if (event.state.view === 'read')
        read_email(event.state.email_id);
}

document.addEventListener('DOMContentLoaded', function () {

    // enable switching  views
    document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
    document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
    document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
    document.querySelector('#compose').addEventListener('click', () => compose_email());
    document.querySelector('#reply-btn').addEventListener('click', () => compose_email(window.history.state.email_id))
    load_mailbox('inbox');

    // Compose mail
    document.querySelector('#compose-form').onsubmit = function () {
        const recipients = document.querySelector('#compose-recipients').value;
        const subject = document.querySelector('#compose-subject').value;
        const body = document.querySelector('#compose-body').value;
        fetch('/emails', {
            method: 'POST',
            body: JSON.stringify({
                recipients: recipients,
                subject: subject,
                body: body,
            })
        })
            .then(response => response.json())
            .then(result => {
                if (result["message"] !== undefined) {
                    show_message('success', result.message);
                    load_mailbox('sent');
                } else {
                    show_message('danger', result.error);
                }
            })
            .catch(error => {
                console.log(error);
            });
        return false;
    }
});

function show_message(type, message) {
    document.querySelector('#message-box').innerHTML += `<div class="alert alert-${type} alert-dismissible fade show" role="alert">
                            ${message}
                            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>`;
    document.querySelector('.close').onclick = () => {
        document.querySelector('.alert').remove();
    }
    setTimeout(() => {
        if (document.querySelector(".alert")) document.querySelector(".alert").remove();
    }, 5000);
}

function compose_email(reply_email_id = null) {

    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#read-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';

    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
    if (reply_email_id !== null) {
        fetch(`/emails/${reply_email_id}`)
            .then(response => response.json())
            .then(email => {
                document.querySelector('#compose-view h3').innerHTML = 'Replying Email';
                document.querySelector('#compose-recipients').value = `${email.sender}`;
                document.querySelector('#compose-subject').value = email.subject.startsWith("Re:") ? `${email.subject}` : `Re: ${email.subject}`;
                document.querySelector('#compose-body').value = `On ${email.timestamp}, ${email.sender} wrote:\n${email.body}\n\n\t`;
            })
            .catch(error => {
                console.log(error);
            });
    }
    history.pushState({ view: 'compose' }, "", 'write');
}

function read_email(email_id) {
    // Get the email.
    fetch(`/emails/${email_id}`)
        .then(response => response.json())
        .then(email => {
            document.querySelector('#read-from').innerHTML = `<h5>${email.sender}</h5>`;
            if (email.recipients.length > 1) {
                document.querySelector('#read-to').innerHTML = "";
                email.recipients.forEach(recipient => {
                    document.querySelector('#read-to').innerHTML += `<h5>${recipient}</h5>`;
                });
            }
            else {
                document.querySelector('#read-to').innerHTML = `<h5>${email.recipients}</h5>`;
            }
            document.querySelector('#read-subject').innerHTML = `<h5>${email.subject}</h5>`;
            document.querySelector('#read-timestamp').innerHTML = `<i><b>${email.timestamp}</b></i>`;
            document.querySelector('#read-body').innerHTML = `<hr><pre>${email.body}</pre>`;
            const archive_btn = document.querySelector('#archive-btn');
            if (email.archived) {
                archive_btn.className = "unarchive";
                archive_btn.setAttribute("title", "Remove from Archive");
                archive_btn.removeEventListener('click', archive);
                archive_btn.addEventListener('click', unarchive);
            }
            else {
                archive_btn.className = "archive";
                archive_btn.setAttribute("title", "Send to Archive");
                archive_btn.removeEventListener('click', unarchive);
                archive_btn.addEventListener('click', archive);
            }
            // Show read view and hide other views
            document.querySelector('#read-view').style.display = 'block';
            document.querySelector('#emails-view').style.display = 'none';
            document.querySelector('#compose-view').style.display = 'none';
            history.pushState({ view: 'read', email_id: email_id }, "", 'read');

        })
        .catch(error => {
            console.log(error);
        });
}
function archive() {
    fetch(`/emails/${window.history.state.email_id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: true
        })
    })
        .then(response => {
            if (response.status === 204) {
                document.querySelector('#read-view').style.animationPlayState = 'running';
                show_message('success', 'Your email was sent to the Archive');
                setTimeout(() => { load_mailbox('inbox'); }, 400);
            }
        })
        .catch(error => {
            console.log(error);
        });
}
function unarchive() {
    fetch(`/emails/${window.history.state.email_id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: false
        })
    })
        .then(response => {
            if (response.status === 204) {
                document.querySelector('#read-view').style.animationPlayState = 'running';
                show_message('success', 'Your email was sent back to the Inbox');
                setTimeout(() => { load_mailbox('inbox'); }, 400);
            }
        })
        .catch(error => {
            console.log(error);
        });
}
function load_mailbox(mailbox) {

    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#read-view').style.display = 'none';

    if (mailbox === 'sent') {
        document.querySelector('#read-view').className = "container";
        document.querySelector('#archive-btn').style.display = 'none';
    }
    else {
        document.querySelector('#read-view').className = "container archive-animation";
        document.querySelector('#read-view').style.animationPlayState = 'paused';
        document.querySelector('#archive-btn').style.display = 'block';
    }
    // Show the mailbox name
    document.querySelector('#emails-view h3').innerHTML = `${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}`;
    // Reset the list
    document.querySelector('#emails-list').innerHTML = '';
    // Get mails
    fetch(`/emails/${mailbox}`)
        .then(response => response.json())
        .then(result => {
            if (result.length > 0) {
                result.forEach(email => {
                    document.querySelector('#emails-list').append(render_email_li(email));
                });
            }
            else {
                document.querySelector('#emails-list').innerHTML = "<li> No emails on this mailbox </li>";
            }
        })
        .catch(error => {
            console.log(error);
        });
    history.pushState({ view: 'mailbox', mailbox: mailbox }, "", `${mailbox}`);
}

function render_email_li(email) {
    // Create and add HTML email.
    const html_email = document.createElement('li');
    html_email.id = `email-${email.id}`;
    let img;
    if (email.read) {
        img = "../static/mail/read.png";
        html_email.className = "media read-email";
    }
    else {
        img = "../static/mail/unread.png";
        html_email.className = "media unread-email";
    }
    html_email.innerHTML = `<img class="mr-2" src=${img} alt="email icon">
                            <div class="media-body">
                              <h5 class="mt-0 mb-2">${email.sender}  <small style="float:right">${email.timestamp}</small></h5>
                              <b>Subject:</b> ${email.subject}
                            </div>`;
    // Add response to clicking an unread email.
    html_email.addEventListener('click', () => {
        if (!email.read) {
            fetch(`/emails/${email.id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    read: true
                })
            })
                .then(response => {
                    if (response.status === 204) {
                        html_email.className = "media read-email";
                        html_email.querySelector("img").setAttribute("src", "../static/mail/read.png");
                        setTimeout(() => { read_email(email.id); }, 500);
                    }
                })
                .catch(error => {
                    console.log(error);
                });
        }
        else {
            read_email(email.id);
        }
    });
    return html_email;
}
